
import mdtraj as md
import MDAnalysis as mda
import numpy as np
import sys
from abc import ABC, abstractmethodC

toolkit = sys.argv[1]

if toolkit == "MDTraj":

    print("MDTraj")
    trajectory = md.load_pdb("protein.pdb")
    
    print(md.compute_center_of_mass(trajectory)*10)
    print(md.compute_rg(trajectory)*10)

elif toolkit == "MDAnalysis":

    print("MDAnalysis")
    universe = mda.Universe("protein.pdb")
    mass_by_frame = np.ndarray(shape=(len(universe.trajectory), 3))
    rg_by_frame = np.empty(len(universe.trajectory))
    for ts in universe.trajectory:
        mass_by_frame[ts.frame] = universe.atoms.center_of_mass(compound="segments")
        rg_by_frame[ts.frame] = universe.atoms.radius_of_gyration()
    
    print(mass_by_frame)
    print(rg_by_frame)

