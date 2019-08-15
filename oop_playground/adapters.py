
import mdtraj as md
import MDAnalysis as mda
import numpy as np
import factory
from interface import TrajectoryAdapter


# We made an abstract class,that both packages can be handled in the same way. Each package exported information from pdb files in different ways so we will have those be private variables.

class MDTrajAdapter(TrajectoryAdapter):

    def __init__(self, filename):
        self.filename = filename
        self._trajectory = md.load_pdb(filename)
        print("MDTraj")

    def compute_center_of_mass(self):
        return md.compute_center_of_mass(self._trajectory)*10

    def compute_radius_of_gyration(self):
        return md.compute_rg(self._trajectory)*10

class MDAnalysisAdapter(TrajectoryAdapter):

    def __init__(self, filename):
        print("MDAnalysis")
        self.filename = filename
        self._universe = mda.Universe(filename)

    def compute_center_of_mass(self):
        mass_by_frame = np.ndarray(shape=(len(self._universe.trajectory), 3))
        for ts in self._universe.trajectory:
            mass_by_frame[ts.frame] = self._universe.atoms.center_of_mass(compound="segments")
        return mass_by_frame

    def compute_radius_of_gyration(self):
        rg_by_frame = np.empty(len(self._universe.trajectory))
        for ts in self._universe.trajectory:
            rg_by_frame[ts.frame] = self._universe.atoms.radius_of_gyration()
        return rg_by_frame


factory.register("MDTraj",MDTrajAdapter)
factory.register("MDAnalysis",MDAnalysisAdapter)

