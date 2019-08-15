
from interface import TrajectoryAdapter

# Python "runs" the lowest indentation when you import a file
_toolkits = {}

def register(toolkit_name, toolkit_class):
    if not issubclass(toolkit_class,TrajectoryAdapter):
        raise TypeError("{0} is not a Trajectory Adapter".format(toolkit_class))
    _toolkits[toolkit_name] = toolkit_class

def trajectory_factory(trajectory_toolkit, **kwargs):
    #dictionary = {"MDTraj":MDTrajAdapter, "MDAnalysis":MDAnalysisAdapter}
    #if trajectory_toolkit not in dictionary.keys():
    #    raise TypeError("The package "+trajectory_toolkit+" is not supported")
    #cls = dictionary[trajectory_toolkit]

    if trajectory_toolkit not in _toolkits.keys():
        raise TypeError("The package "+trajectory_toolkit+" is not supported")
    cls = _toolkits[trajectory_toolkit]

    instance = cls(kwargs["filename"])
    return instance

