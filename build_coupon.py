"""Generate magnet_fit_coupon: a fit-test plate for the magnet pockets.

Run with FreeCAD (tested on 1.1.x):  freecadcmd build_coupon.py

Four pockets stepping through diameters, dot-marked 1..4 (1 = tightest).
Prints as imported: pockets and dot marks face up. Pick the diameter that gives
a snug, fully-seatable press fit and set POCKET_D in build_remix.py to match.
"""
import os
import Part
from FreeCAD import Vector

HERE = os.path.dirname(os.path.abspath(__file__))

# --- parameters (magnet: 6mm x 2.6mm nominal disc) ---
DIAMETERS = [6.10, 6.20, 6.30, 6.40]   # pocket 1 (tightest) .. 4 (loosest)
POCKET_DEPTH = 2.45                     # magnet sits ~0.19mm proud
CEILING = 1.25
VENT_D = 2.5
PITCH = 12.0
W, T = 14.0, POCKET_DEPTH + CEILING     # plate width, thickness

L = PITCH * len(DIAMETERS) + 4
plate = Part.makeBox(L, W, T, Vector(0, -W / 2, 0))
for i, dia in enumerate(DIAMETERS):
    x = PITCH / 2 + 2 + i * PITCH
    plate = plate.cut(Part.makeCylinder(dia / 2, POCKET_DEPTH + 0.5, Vector(x, 0, T - POCKET_DEPTH)))  # pocket (opens up)
    plate = plate.cut(Part.makeCylinder(VENT_D / 2, T + 1, Vector(x, 0, -0.5)))            # vent/eject
    for k in range(i + 1):                                                                 # dot marks on top: 1..4
        plate = plate.cut(Part.makeCylinder(0.6, 0.6, Vector(x - 3 + k * 2, W / 2 - 2.2, T - 0.5)))
plate = plate.removeSplitter()

assert plate.isValid() and len(plate.Solids) == 1
print("coupon valid:", plate.isValid())

plate.exportStep(os.path.join(HERE, "magnet_fit_coupon.step"))
import MeshPart
mesh = MeshPart.meshFromShape(Shape=plate, LinearDeflection=0.03, AngularDeflection=0.25, Relative=False)
mesh.write(os.path.join(HERE, "magnet_fit_coupon.stl"))
print("wrote step+stl,", mesh.CountFacets, "facets")
