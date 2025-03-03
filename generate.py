import FreeCAD
import Mesh

doc = FreeCAD.open('projectslot.FCStd')
params = doc.getObject("VarSet")
params.rail_length = 120

doc.recompute()

targetObjLabels = ["projectslot", "ps-pcb-mount", "pcb-slide-in-clip"];

for obj in doc.Objects:
    if obj.Label in targetObjLabels:
        print(f"exporting {obj.Label}")
        Mesh.export([obj], f"stls/{obj.Label}.stl")
    else:
        print(f"skipping {obj.Label}")
