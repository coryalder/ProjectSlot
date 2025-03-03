import FreeCAD
#import Import
import Mesh

doc = FreeCAD.open('projectslot.FCStd')

sheet = doc.Spreadsheet
#sheet.set("pcb_width", str(20))
#sheet.set("rail_length", str(120))
#sheet.set("chamfer", str(6))
sheet.recompute()

targetObjLabels = ["projectslot", "ps-pcb-mount", "pcb-slide-in-clip"];

for obj in doc.Objects:
    print(obj.Label);
    if obj.Label in targetObjLabels:
        obj.touch();
        print(f"exporting {obj.Label}")
        Mesh.export([obj], f"stls/{obj.Label}.stl")
    else:
        print(f"skipping {obj.Label}")