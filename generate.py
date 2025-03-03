import FreeCAD
#import Import
import Mesh

doc = FreeCAD.open('projectslot.FCStd')

sheet = doc.Spreadsheet
#sheet.set("radius", str(123))
sheet.recompute()

for objName in ["projectslot", "ps-pcb-mount", "pcb-slide-in-clip"]:
    obj = doc.getObject(objName);
    obj.touch();
    Mesh.export([obj], f"{objName}.stl")