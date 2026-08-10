"""Generate konnected_base_magnetic from zefer's Konnected Alarm Panel Pro case base.

Run with FreeCAD (tested on 1.1.x):  freecadcmd build_remix.py

Reads original/konnected_base_original.step, adds press-fit magnet pockets,
removes the woodscrew wall-mount features, writes STEP + STL next to this script.
"""
import os
import Part
from FreeCAD import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "original", "konnected_base_original.step")

# --- parameters (magnet: 6mm x 2.6mm nominal disc, calipered 6.03 x 2.64) ---
STATIONS = [(58, 17), (58, -17), (-58, 17), (-58, -17), (0, 17), (0, -17)]
FLOOR_TOP    = 2.5
POCKET_D     = 6.20      # snug press fit for a 6.03mm disc; validate with magnet_fit_coupon
POCKET_DEPTH = 2.45      # magnet sits ~0.19mm proud
PAD_D, PAD_H = 9.0, 1.2  # inside ceiling pad -> pocket ceiling = 2.5 + 1.2 - 2.45 = 1.25
VENT_D       = 2.5       # air/glue escape + magnet eject port
WALLMOUNT    = [(-40.75, -6.0), (25.75, -6.0)]  # original woodscrew features: removed

base = Part.read(SRC)
body = base.Solids[0]
for s in base.Solids[1:]:
    body = body.fuse(s)

# delete wall-mount features: fill hole/countersink/counterbore, then shave the 15x15 boss flat
for (x, y) in WALLMOUNT:
    body = body.fuse(Part.makeCylinder(4.2, 7.5, Vector(x, y, 0)))
    body = body.cut(Part.makeBox(16, 16, 6, Vector(x - 8, y - 8, FLOOR_TOP)))

for (x, y) in STATIONS:
    body = body.fuse(Part.makeCylinder(PAD_D / 2, PAD_H, Vector(x, y, FLOOR_TOP)))
for (x, y) in STATIONS:
    body = body.cut(Part.makeCylinder(POCKET_D / 2, POCKET_DEPTH + 0.5, Vector(x, y, -0.5)))
    body = body.cut(Part.makeCylinder(VENT_D / 2, FLOOR_TOP + PAD_H + 1, Vector(x, y, -0.5)))
body = body.removeSplitter()

assert body.isValid() and len(body.Solids) == 1
print("valid:", body.isValid(), "solids:", len(body.Solids), "faces:", len(body.Faces))

body.exportStep(os.path.join(HERE, "konnected_base_magnetic.step"))
import MeshPart
mesh = MeshPart.meshFromShape(Shape=body, LinearDeflection=0.05, AngularDeflection=0.3, Relative=False)
mesh.write(os.path.join(HERE, "konnected_base_magnetic.stl"))
print("wrote step+stl,", mesh.CountFacets, "facets")
