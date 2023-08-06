# -*- coding: utf-8 -*-

import os
import shutil
import logger
from subprocess import PIPE, Popen
from os.path import join, isfile
import platform


_name = "FoldX"
if platform.system() == "Windows":
    _bin_name = "foldx.exe"
else:
    _bin_name = "foldx"
# TODO once this is working again re-write given the fact that command line rather than files can be now used
# TODO maybe exploit the new foldx options for a cleaner pipeline of the pdb files etc


class FoldxWrap:
    """
    Expects a path to folder with FoldX binary and rotabase.txt files and a script dir with repairPDB.txt file
    If the file is not present in scripts dir, the class will attempt to create it
    This class can be used to run energy minimization and mutant creation with foldx
    """
    def __init__(self, foldx_dir="", script_dir="", work_dir="", skip_minimization=False):
        self.bin_dir = foldx_dir
        self.script_dir = script_dir
        self.fold_config = join(self.script_dir, "repairPDB.txt")
        self.mut_fold_config = join(self.script_dir, "buildModel.txt")
        self.agg_work_dir = work_dir
        self.skip = skip_minimization
        try:
            self._check_files()
        except logger.FoldXError:
            raise

    def minimize_energy(self, working_dir="", cleanup=True, skip_min=False):
        try:
            os.chdir(working_dir)
        except OSError:
            raise logger.FoldXError("FoldX run in a non-existing directory %s" % working_dir)
        if not isfile(join(working_dir, "input.pdb")):
            raise logger.FoldXError("input.pdb file not present if FoldX working directory %s" % working_dir)
        if not isfile(join(working_dir, "rotabase.txt")):
            # In case of multiple minimizations te code below could raise a same file error
            try:
                os.symlink(join(self.bin_dir, "rotabase.txt"), join(working_dir, "rotabase.txt"))
                os.symlink(join(self.script_dir, "repairPDB.txt"), join(working_dir, "repairPDB.txt"))
            except (OSError, AttributeError):   # Windows will not necessarily allow symlink creation
                shutil.copyfile(join(self.bin_dir, "rotabase.txt"), join(working_dir, "rotabase.txt"))
                shutil.copyfile(join(self.script_dir, "repairPDB.txt"), join(working_dir, "repairPDB.txt"))
        fold_cmd = [join(self.bin_dir, _bin_name), "-f", "repairPDB.txt"]
        if not skip_min:
            self._run_foldx(cmd=fold_cmd, msg="Starting FoldX energy minimalization", outfile="finalRepair.out")
        else:
            # since the job is ran on output from parent this "input" should be the output of the parent process
            shutil.move("input.pdb", "input_Repair.pdb")    # Pretend it was ran
        if cleanup:
            try:
                shutil.move("input_Repair.fxout", "RepairPDB.fxout")
                shutil.move("input_Repair.pdb", "folded.pdb")
            except IOError:
                raise logger.FoldXError("FoldX didn't produce expected repair files. "
                                        "Can't continue without it. This is unexpected and could indicate FoldX issues.")

    def build_mutant(self, working_dir="", mutation_list=""):
        os.chdir(working_dir)
        logger.to_file(filename="individual_list.txt", content=mutation_list)
        self.minimize_energy(working_dir=working_dir, cleanup=False, skip_min=self.skip)
        _cmd = [join(self.bin_dir, _bin_name), "-f", self.mut_fold_config]
        self._run_foldx(cmd=_cmd, msg="Building mutant model", outfile="buildMutant.out")
        try:
            shutil.move("input_Repair_1.pdb", "input.pdb")
        except IOError:
            raise logger.FoldXError("FoldX didn't produce expected mutant file. "
                                    "Can't continue without it. This is unexpected and could indicate FoldX issues.")
        self._cleanup()

    @staticmethod
    def _run_foldx(cmd, msg='', outfile=''):
        """Assumes the directory it's run from contains """
        logger.info(module_name="FoldX", msg=msg)
        logger.debug(module_name="FoldX", msg="Starting FoldX with %s" % " ".join(cmd))
        out, err = Popen(cmd, stdout=PIPE, stderr=PIPE).communicate()
        if err:
            logger.warning(module_name="FoldX", msg=err)
        logger.to_file(filename=outfile, content=out, allow_err=False)

# TODO proper cleanup handling this is a mess + is this even necessary?
    def _cleanup(self):
        with open("Dif_input_Repair.fxout", 'r') as enelog:
            d = enelog.readlines()[-1]
            d = d.split()[1] + " kcal/mol"
            logger.to_file(filename=join(self.agg_work_dir, "MutantEnergyDiff"), content=d)

        try:
            os.mkdir(join(self.agg_work_dir, "foldxOutput"))
        except OSError:
            logger.log_file(module_name=_name, msg="Couldn't create foldxOutput folder (probably already exists)")
        shutil.move("Raw_input_Repair.fxout",
                    join(self.agg_work_dir, "foldxOutput/Stability_RepairPDB_input.fxout"))
        shutil.move("Dif_input_Repair.fxout",
                    join(self.agg_work_dir, "foldxOutput/Dif_BuildModel_RepairPDB_input.fxout"))

    def _check_files(self):
        if not isfile(join(self.bin_dir,"rotabase.txt")) or not isfile(join(self.bin_dir,_bin_name)):
            raise logger.FoldXError("Provided FoldX directory (%s) misses either %s or %s " %
                                    (self.bin_dir, "rotabase.txt", _bin_name) +
                                    "files which are required for the program to run.")
        if not isfile(self.fold_config):
            try:
                self._recover_script()
            except logger.FoldXError:
                raise

        if not isfile(self.mut_fold_config):
            try:
                self._recover_mut_script()
            except logger.FoldXError:
                raise

    def _recover_script(self):
        """
        Re-write the repairPDB file in case something goes wrong
        For more info on FoldX commands and parameters see http://foldxsuite.crg.eu/documentation#manual
        Default FoldX parameters include:
        ph=7
        temperature=298
        ionStrength=0.05
        vdwDesign=2
        pdbHydrogens=false
        """
        fold_script = (
            "pdb=input.pdb\n"
            "command=RepairPDB\n"
            "water=-CRYSTAL\n"
            )
        try:
            with open(self.fold_config, "w") as f:
                f.write(fold_script)
        except IOError:
            raise logger.FoldXError("FoldX requires %s file to be present." % self.fold_config +
                                    "If default settings are used it should be in data folder inside aggrescan directory." +
                                    "Attempted to re-write the file %s to %s but failed" % (self.fold_config, self.script_dir))

    def _recover_mut_script(self):
        """
        Re-write the buildModel file in case something goes wrong
        For more info on FoldX commands and parameters see http://foldxsuite.crg.eu/documentation#manual
        Default FoldX parameters include:
        ph=7
        temperature=298
        ionStrength=0.05
        vdwDesign=2
        pdbHydrogens=false
        """
        fold_mut_script = (
            "pdb=input_Repair.pdb\n"
            "command=RepairPDB\n"
            "water=-CRYSTAL\n")
        try:
            with open(self.mut_fold_config, "w") as f:
                f.write(fold_mut_script)
        except IOError:
            raise logger.FoldXError("FoldX mutation requires %s file to be present." % self.mut_fold_config +
                                    "If default settings are used it should be in data folder inside aggrescan directory." +
                                    "Attempted to re-write the file %s to %s but failed" % (self.mut_fold_config, self.script_dir))

