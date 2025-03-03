import sys
import os

freecad_paths = [
    '/home/runner/work/lumenpnp/lumenpnp/squashfs-root/usr/lib',  # For CI when using AppImage
    '/mnt/c/Users/computer/Code/ProjectSlot/squashfs-root/usr/lib', # for my machine
    '/usr/lib/freecad/lib/',  # For CI
    '/usr/lib/freecad-daily-python3/lib/',  # For Ubuntu
    '/usr/lib64/freecad/lib64/',  # For Fedora
    '/Applications/FreeCAD.app/Contents/MacOS',  # For Mac OS X
    'c:/Program Files/FreeCAD 0.18/bin/',  # For Windows
    'c:/Program Files/FreeCAD 0.19/bin/',  # For Windows
]

for path in freecad_paths:
    if os.path.exists(path):
        print(f"Added possible FreeCAD path: {path}")
        sys.path.append(path)

import FreeCAD
import Mesh

doc = FreeCAD.open('projectslot.FCStd')
varset = doc.getObject("VarSet")

# set variables like so:
# varset.rail_length = 120
# doc.recompute()

targetObjLabels = ["projectslot", "ps-pcb-mount", "pcb-slide-in-clip"];

for obj in doc.Objects:
    if obj.Label in targetObjLabels:
        print(f"exporting {obj.Label}")
        Mesh.export([obj], f"stls/{obj.Label}.stl")
    else:
        print(f"skipping {obj.Label}")

exit();