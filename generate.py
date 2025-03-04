import sys
import os
import argparse

freecad_paths = [
    '/home/runner/work/ProjectSlot/ProjectSlot/squashfs-root/usr/lib',  # For CI when using AppImage
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

parser = argparse.ArgumentParser(description='Generate STLs dynamically from a FreeCAD file')
parser.add_argument('action', help='the stl to generate: all | rail | pcb-mount | pcb-clip')
parser.add_argument('--length', help='the length of the rail or width of pcb-clip, does nothing with pcb-holder')

args = parser.parse_args()

targetObjLabels = [];

if args.action == "all":
    targetObjLabels = ["projectslot", "ps-pcb-mount", "pcb-slide-in-clip"]
elif args.action == "rail":
    targetObjLabels = ["projectslot"]
    varset.rail_length = args.length or varset.rail_length
elif args.action == "pcb-mount":
    targetObjLabels = ["ps-pcb-mount"]
elif args.action == "pcb-clip":
    targetObjLabels = ["pcb-slide-in-clip"]
    varset.pcb_width = args.length or varset.pcb_width

doc.recompute()

for obj in doc.Objects:
    if obj.Label in targetObjLabels:
        print(f"exporting {obj.Label}")
        Mesh.export([obj], f"stls/{obj.Label}.stl")
    else:
        print(f"skipping {obj.Label}")

exit();