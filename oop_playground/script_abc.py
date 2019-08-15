
import sys
import adapters
import factory


toolkit = sys.argv[1]

#if toolkit == "MDAnalysis":
#    system = MDAnalysisAdapter("protein.pdb")
#elif toolkit == "MDTraj":
#    system = MDTrajAdapter("protein.pdb")

system = factory.trajectory_factory(toolkit,filename="protein.pdb")

print(system.compute_center_of_mass())
print(system.compute_radius_of_gyration()) 
