#!/usr/bin/env python3
"""Full brand asset set for the Penn Carey Law AI Project (N1 fitted lockup).

Emits colour and white lockups with outlined text (no font dependency) plus a
favicon set derived from the shield.
"""
import base64
import re
import subprocess
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT = str(Path.home() / "Library/Fonts/Rajdhani-Bold.ttf")
STATIC = Path.home() / "code/ai-teaching-lab/ai-teaching-lab.org/static"
OUT = Path.home() / "Downloads" / "PennCareyLawAIProject-brand-2026-07"
OUT.mkdir(parents=True, exist_ok=True)

NAVY, WHITE, RED = "#011f5b", "#ffffff", "#822024"

with open(FONT, "rb") as fh:
    DATA = fh.read()
_tt = TTFont(FONT)
_gs = _tt.getGlyphSet()
_order = _tt.getGlyphOrder()
_face = hb.Face(DATA)
UPEM = _face.upem


def _shape(text):
    f = hb.Font(_face)
    f.scale = (UPEM, UPEM)
    hb.ot_font_set_funcs(f)
    b = hb.Buffer()
    b.add_str(text)
    b.guess_segment_properties()
    hb.shape(f, b)
    return list(zip(b.glyph_infos, b.glyph_positions))


class _Null:
    def __getattr__(self, _):
        return lambda *a, **k: None


def _run(text, size, ls, x0, base, sink):
    s = size / UPEM
    ls_fu = ls / s
    bounds = BoundsPen(_gs)
    pen = 0.0
    for info, pos in _shape(text):
        g = _order[info.codepoint]
        tr = (s, 0, 0, -s, x0 + (pen + pos.x_offset) * s, base - pos.y_offset * s)
        _gs[g].draw(TransformPen(sink, tr))
        _gs[g].draw(TransformPen(bounds, tr))
        pen += pos.x_advance + ls_fu
    return bounds.bounds


def measure(text, size, ls=0.0):
    return _run(text, size, ls, 0, 0, _Null())


def path_of(text, size, ls, x0, base):
    sink = SVGPathPen(_gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    b = _run(text, size, ls, x0, base, sink)
    return sink.getCommands(), b


# ---- layout ----------------------------------------------------------------
EYEBROW, WORDMARK = "PENN CAREY LAW", "AI PROJECT"
TEXT_X, DIV_X = 336.0, 292.0
CANVAS_H = 310

# The shield tapers to a point: its box is 258u tall (y 22-280), but the central
# 90% of its ink mass spans only y 28-232 — 204u, measured off the alpha channel
# of the embedded PNG. Text is a solid rectangular mass, so the block is fitted to
# that mass, not the box. Fitting the box makes the wordmark read as larger than
# the shield (rejected 2026-07-29 after side-by-side comparison).
MASS_TOP, MASS_BOT = 28.0, 232.0

# Proportions inside the text block, held at their shipped ratios and scaled as a
# single unit to reach the target height.
U_WM, U_EB, U_GAP, U_RULE_OFF, U_RULE_W = 145.0, 35.0, 144.0, 22.0, 8.0


def fit(k):
    """Lay the text block out at scale k, centred on the shield's ink mass."""
    wm_size, eb_size = U_WM * k, U_EB * k
    gap, rule_off, rule_w = U_GAP * k, U_RULE_OFF * k, U_RULE_W * k

    # Track the eyebrow so its ink width equals the wordmark's exactly.
    wb, eb0 = measure(WORDMARK, wm_size), measure(EYEBROW, eb_size)
    ls = ((wb[2] - wb[0]) - (eb0[2] - eb0[0])) / (len(EYEBROW) - 1)

    # Provisional baselines, then shift the whole block onto the shield's mass.
    eb_base, wm_base = 100.0, 100.0 + gap
    _, wm_b = path_of(WORDMARK, wm_size, 0.0, TEXT_X, wm_base)
    _, probe = path_of(EYEBROW, eb_size, ls, TEXT_X, eb_base)
    eb_x = TEXT_X + (wm_b[0] - probe[0])
    _, eb_b = path_of(EYEBROW, eb_size, ls, eb_x, eb_base)
    dy = (MASS_TOP + ((MASS_BOT - MASS_TOP) - (wm_b[3] - eb_b[1])) / 2) - eb_b[1]

    wm_d, wm_b = path_of(WORDMARK, wm_size, 0.0, TEXT_X, wm_base + dy)
    eb_d, eb_b = path_of(EYEBROW, eb_size, ls, eb_x, eb_base + dy)
    return dict(wm_d=wm_d, wm_b=wm_b, eb_d=eb_d, eb_b=eb_b, ls=ls,
                wm_size=wm_size, eb_size=eb_size, rule_w=rule_w,
                rule_y=eb_base + dy + rule_off, ink_h=wm_b[3] - eb_b[1])


# Ink height scales linearly with k, so a single probe solves the fit exactly.
K = (MASS_BOT - MASS_TOP) / fit(1.0)["ink_h"]
L = fit(K)
assert abs(L["ink_h"] - (MASS_BOT - MASS_TOP)) < 0.01, "height fit drifted"
assert abs(L["eb_b"][0] - L["wm_b"][0]) < 0.01 and abs(L["eb_b"][2] - L["wm_b"][2]) < 0.01, \
    "width fit drifted"
CANVAS_W = round(L["wm_b"][2] + 30)


def shield_from(fname):
    src = (STATIC / fname).read_text()
    m = re.search(r"<image[^>]*/>", src) or re.search(r"<image[^>]*></image>", src)
    return m.group()


def lockup(shield_el, ink, divider):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" \
width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}" \
role="img" aria-label="Penn Carey Law AI Project">
  <title>Penn Carey Law AI Project</title>
  {shield_el}
  <path id="divider" stroke="{divider}" stroke-width="3" d="M {DIV_X} 46 L {DIV_X} 264"/>
  <path id="eyebrow" fill="{ink}" d="{L['eb_d']}"/>
  <path id="rule" fill="none" stroke="{RED}" stroke-width="{L['rule_w']:.2f}" \
d="M {L['wm_b'][0]:.2f} {L['rule_y']:.2f} L {L['wm_b'][2]:.2f} {L['rule_y']:.2f}"/>
  <path id="wordmark" fill="{ink}" d="{L['wm_d']}"/>
</svg>
'''


colour = lockup(shield_from("heading-color.svg"), NAVY, "#c9c7c0")
white = lockup(shield_from("heading-white.svg"), WHITE, "#7f8794")

(OUT / "lockup-color.svg").write_text(colour)
(OUT / "lockup-white.svg").write_text(white)

# ---- favicons, from the shield raster --------------------------------------
src = re.search(r'(?:xlink:)?href="data:image/(png|jpeg);base64,([^"]+)"',
                (STATIC / "heading-color.svg").read_text())
tmp = OUT / "_shield_full.png"
tmp.write_bytes(base64.b64decode(src.group(2)))

sizes = {"favicon-16.png": 16, "favicon-32.png": 32, "apple-touch-icon-180.png": 180,
         "icon-192.png": 192, "icon-512.png": 512}
for name, px in sizes.items():
    subprocess.run(["sips", "-Z", str(px), str(tmp), "--out", str(OUT / name)],
                   check=True, capture_output=True)

# an SVG favicon: shield only, cropped to its own box
shield_only = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" \
width="228" height="258" viewBox="30 22 228 258" role="img" aria-label="Penn shield">
  {shield_from("heading-color.svg")}
</svg>
'''
(OUT / "favicon.svg").write_text(shield_only)

print(f"scale {K:.4f} | type {L['wm_size']:.1f}/{L['eb_size']:.1f}pt "
      f"| tracking {L['ls']:.2f}u ({L['ls']/L['eb_size']:.3f}em)")
print(f"canvas {CANVAS_W}x{CANVAS_H} ({CANVAS_W/CANVAS_H:.3f}:1) "
      f"| text ink {L['ink_h']:.1f}u, y {L['eb_b'][1]:.1f}-{L['wm_b'][3]:.1f}")
print(f"fit: L {L['eb_b'][0]-L['wm_b'][0]:+.3f}  R {L['eb_b'][2]-L['wm_b'][2]:+.3f}  "
      f"H {L['ink_h']-(MASS_BOT-MASS_TOP):+.3f}")
for p in sorted(OUT.iterdir()):
    if not p.name.startswith("_"):
        print(f"  {p.stat().st_size//1024:>4}KB  {p.name}")
print("text elements in lockups:", colour.count("<text") + white.count("<text"))
