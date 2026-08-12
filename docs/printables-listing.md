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

Six press-fit magnets snap this case into a steel alarm box — no screws, no
drilling, pulls off by hand for service.

## Description

A remix of zefer's Konnected Alarm Panel Pro Case that mounts magnetically
inside a steel alarm panel enclosure — no screws, no standoff hardware, no
drilling. Six cheap 6×2.6 mm neodymium disc magnets press-fit and glue into
pockets in the base; the case snaps onto the enclosure wall and pulls off by
hand. A printed-in-place alternative to Konnected's own magnetic standoffs
that keeps the full protection of an enclosed case.

The payoff: every zone wire stays landed while the whole panel lifts off its
enclosure wall by hand — no screwdriver, no fishing for standoffs. Assemble
the board into the case on the bench, then snap it in.

**What changed from the original:**

- Six magnet pockets in the underside of the base floor (Ø6.20 × 2.45 mm) —
  the magnets sit ~0.2 mm proud, so the case stands on the magnet faces
- Each pocket has a low ceiling pad inside the case and a Ø2.5 mm vent hole:
  air/glue escape during insertion, and an eject port if you ever need to
  poke a magnet back out
- The two woodscrew wall-mount holes and their interior bosses are removed —
  this base mounts magnetically only (use the original if you want screws)
- Lid and board mounting are unchanged: print zefer's lid from the original
  model and use his M3 nut/standoff/screw scheme

**Fit coupon included.** Press-fit depends on your printer's hole shrinkage,
so print `magnet_fit_coupon.stl` first (a few minutes): four pockets at
Ø6.10 / 6.20 / 6.30 / 6.40, dot-marked 1–4 (1 = tightest). Press a magnet
into each and pick the snug-but-fully-seatable one — the vent hole lets you
poke it back out and reuse it. Ø6.20 is the shipped STL; other diameters are
a one-line change in the FreeCAD script and a regenerate.

**If your enclosure wall has raised obstructions** (screw joints, weld nubs,
rivets) that keep the magnets from reaching flat steel: stack a second disc
onto each installed magnet — they self-align magnetically, add a drop of CA
between. Each extra disc buys ~2.6 mm of standoff and grip stays
full-strength. That's how the pictured install clears its enclosure's raised
screw joints.

STEP files, the parametric FreeCAD build scripts, and full design notes:
https://github.com/zackgomez/konnected-magnetic-case

Remix designed and scripted by Claude (Fable 5, via Claude Code) working
with me — geometry analysis, FreeCAD build scripts, and the fit-coupon
workflow were Claude's; magnets, calipers, printer, and judgment were mine.

*Note Konnected's own caveat: a steel enclosure attenuates WiFi — fine if
you use the Pro's Ethernet, otherwise check signal strength.*

## Print settings

- Both parts print flat as exported, no supports (the pocket ceilings are
  short bridges — they print fine)
- As printed (the units in the photos): ASA, 0.4 mm nozzle, 0.3 mm layers,
  ~30 g for base + lid. PLA at 0.2 mm works too, per the original
- Coupon prints as imported: pockets and dot marks face up

## Assembly / hardware

- 6× neodymium disc magnets, 6 mm Ø × 2.6 mm thick (common "6×2" packs often
  measure ~6.03 × 2.64 — caliper yours). No polarity concerns against steel
- CA glue, a drop per pocket — the glue is what resists pull-off when you
  remove the case from the wall; don't skip it
- Board mounting per the original: 4× M3 nuts, standoffs (e.g. M3 6+6),
  M3 screws; lid screws M3×6
- Press magnets in until seated, mount the board on the bench, snap the case
  into the enclosure

## Files to upload

STLs:
- `konnected_base_magnetic.stl` — the remixed base
- `magnet_fit_coupon.stl` — fit-test coupon (print first)

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
