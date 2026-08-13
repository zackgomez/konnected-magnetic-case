# Printables upload package

Everything below is paste-ready. Files to upload are listed at the bottom.

**Publish as a remix** of zefer's model
(https://www.printables.com/model/680613-konnected-alarm-panel-pro-case) so
attribution links automatically.

## Title

Konnected Alarm Panel Pro Case — Magnetic Mount (press-fit magnets)

## Category / tags

Category: Hobby & Makers → Electronics (same as the original)
Tags: `konnected`, `alarm`, `alarm-panel`, `home-assistant`, `case`,
`magnetic`, `magnet`, `esphome`, `smart-home`, `freecad`, `asa`, `remix`

## Summary (120-char limit)

Remixed Konnected Alarm Panel Pro case replacing screw mounting with six
press-fit 6×3 mm magnets.

## Description

A remix of zefer's Konnected Alarm Panel Pro Case that mounts magnetically
inside a steel alarm enclosure: six 6×3 mm neodymium discs press-fit into
pockets in the base — no screws, no drilling. Assemble the board into the
case on the bench, snap it onto the enclosure wall, pull it off by hand for
service with every zone wire still landed.

**Changes from the original:**

- Six magnet pockets (Ø6.20 × 2.45 mm) in the base underside; magnets sit
  ~0.2 mm proud, so the case stands on the magnet faces
- Each pocket: low ceiling pad inside, Ø2.5 mm vent hole (air escape on
  insertion, eject port for removal)
- Woodscrew wall-mount holes and their bosses removed — use the original if
  you want screws
- Lid and board mounting unchanged; print the lid from the original model

**Fit coupon included.** Press fit depends on your printer, so print
`magnet_fit_coupon.stl` first: four pockets at Ø6.10–6.40, dot-marked 1–4
(1 = tightest). Pick the snug-but-seatable one. Ø6.20 is the shipped STL;
other diameters are a one-line change in the FreeCAD script.

**Raised features on the enclosure wall** (screw joints, rivets) keeping the
magnets off flat steel? Stack a second disc on each magnet — self-aligning,
~2.6 mm more standoff per disc, full grip. The pictured install clears its
screw joints this way.

STEP files, parametric FreeCAD build scripts, and design notes:
https://github.com/zackgomez/konnected-magnetic-case

Designed and scripted in collaboration with Claude (Fable 5, via Claude
Code) — geometry analysis, build scripts, and the coupon workflow were
Claude's.

## Print settings

- Both parts print flat as exported, no supports (pocket ceilings are short
  bridges)
- As pictured: ASA, 0.4 mm nozzle, 0.3 mm layers, ~30 g for base + lid.
  PLA at 0.2 mm works too, per the original
- Coupon prints as imported: pockets and dot marks face up

## Assembly / hardware

- 6× neodymium disc magnets, 6×3 mm (mine calipered 6.03 × 2.64; no polarity
  concerns against steel)
- CA glue optional — press fit alone holds mine; add a drop per pocket if
  magnets stay on the wall when you pull the case off
- Board mounting per the original: 4× M3 nuts, standoffs (e.g. M3 6+6),
  M3 screws; lid screws M3×6

## Files to upload

STLs:
- `konnected_base_magnetic.stl` — the remixed base
- `magnet_fit_coupon.stl` — fit-test coupon (print first)

STEPs (upload as "other files" for remixers):
- `konnected_base_magnetic.step`
- `magnet_fit_coupon.step`

(Lid: unchanged — printed from zefer's original model page.)

Photos (from `photos/`):
- `pulled-off-for-service.jpg` — **cover image** (wired panel held mid-air:
  the whole point in one frame)
- `wired-with-lid.jpg` — finished install in the enclosure
- `wired-no-lid.jpg` — lid off, zones landed
- `mounted-in-panel.jpg` — first install, pre-wiring
- `underside-magnets.jpg` — magnets seated, bench
- `fit-coupon.jpg` — coupon with a magnet seated
- `stacked-magnets.jpg` — stacked pair for extra standoff
- `printed-base-interior.jpg` — ceiling pads and vent holes

Renders (from `previews/`, optional):
- `preview_bottom.png` — pocket layout
- `preview_top.png` — interior

License: **CC BY-SA 4.0** — required, inherited from the original
(ShareAlike). Publishing as a remix on Printables sets attribution up
automatically.
