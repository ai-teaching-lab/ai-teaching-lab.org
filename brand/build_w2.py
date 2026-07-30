#!/usr/bin/env python3
"""Production build of the approved W2 lockup — colour and white.

W2: PENN CAREY LAW · PENNAI.LAW share the eyebrow line, spanning the wordmark's
ink width exactly. URL at 85% of eyebrow size, tracked 0.12em, cap-centred on the
eyebrow. Text block still fitted to the shield's ink mass (204u, y 28-232).

The white variant does NOT use Penn red for the rule. #822024 on navy is 1.75:1 —
the same colorimetry that ruled out red text on navy fields. On dark grounds the
rule goes white at reduced opacity.
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
exec(open(HERE / "build_brand.py").read().split("# ---- layout")[0])

OUT = Path.home() / "Downloads" / "PennCareyLawAIProject-brand-2026-07"
OUT.mkdir(parents=True, exist_ok=True)

EYEBROW, WORDMARK, URL = "PENN CAREY LAW", "AI PROJECT", "PENNAI.LAW"
TEXT_X, DIV_X = 336.0, 292.0
SH_Y, SH_H, CANVAS_H = 22.0, 258.0, 310
MASS_TOP, MASS_BOT = 28.0, 232.0
U_WM, U_EB, U_GAP, U_RULE_OFF, U_RULE_W = 145.0, 35.0, 144.0, 22.0, 8.0

# W2 parameters, approved 2026-07-29.
URL_SCALE, URL_TRACK_EM, GAP_EM, DOT_EM = 0.85, 0.12, 0.50, 0.15

STATIC = Path.home() / "code/ai-teaching-lab/ai-teaching-lab.org/static"


def shield_of(fname):
    return re.search(r"<image[^>]*/>", (STATIC / fname).read_text()).group()


def primary():
    def fit(k):
        wm_s, eb_s, gap = U_WM * k, U_EB * k, U_GAP * k
        wb, eb0 = measure(WORDMARK, wm_s), measure(EYEBROW, eb_s)
        ls = ((wb[2] - wb[0]) - (eb0[2] - eb0[0])) / (len(EYEBROW) - 1)
        eb_base, wm_base = 100.0, 100.0 + gap
        _, wm_b = path_of(WORDMARK, wm_s, 0.0, TEXT_X, wm_base)
        _, probe = path_of(EYEBROW, eb_s, ls, TEXT_X, eb_base)
        eb_x = TEXT_X + (wm_b[0] - probe[0])
        _, eb_b = path_of(EYEBROW, eb_s, ls, eb_x, eb_base)
        dy = (MASS_TOP + ((MASS_BOT - MASS_TOP) - (wm_b[3] - eb_b[1])) / 2) - eb_b[1]
        wm_d, wm_b = path_of(WORDMARK, wm_s, 0.0, TEXT_X, wm_base + dy)
        eb_d, eb_b = path_of(EYEBROW, eb_s, ls, eb_x, eb_base + dy)
        return dict(wm_d=wm_d, wm_b=wm_b, eb_b=eb_b, eb_size=eb_s,
                    rule_w=U_RULE_W * k, rule_y=eb_base + dy + U_RULE_OFF * k,
                    eb_base=eb_base + dy, ink_h=wm_b[3] - eb_b[1], ls=ls)
    k = (MASS_BOT - MASS_TOP) / fit(1.0)["ink_h"]
    return fit(k)


P = primary()
WM_L, WM_R = P["wm_b"][0], P["wm_b"][2]
SPAN, CANVAS_W = WM_R - WM_L, round(P["wm_b"][2] + 30)
EB_SIZE, EB_BASE = P["eb_size"], P["eb_base"]
CAP_MID = (P["eb_b"][1] + P["eb_b"][3]) / 2

u_size = EB_SIZE * URL_SCALE
u_ls = u_size * URL_TRACK_EM
gap = EB_SIZE * GAP_EM
dot_d = EB_SIZE * DOT_EM

u_nat = measure(URL, u_size)
consumed = (u_nat[2] - u_nat[0]) + u_ls * (len(URL) - 1) + gap * 2 + dot_d
eb_nat = measure(EYEBROW, EB_SIZE)
eb_ls = ((SPAN - consumed) - (eb_nat[2] - eb_nat[0])) / (len(EYEBROW) - 1)

_, p = path_of(EYEBROW, EB_SIZE, eb_ls, 0.0, EB_BASE)
EB_D, EB_B = path_of(EYEBROW, EB_SIZE, eb_ls, WM_L - p[0], EB_BASE)
_, up0 = path_of(URL, u_size, u_ls, 0.0, 0.0)
U_D, U_B = path_of(URL, u_size, u_ls, WM_R - up0[2],
                   CAP_MID + (up0[3] - up0[1]) / 2)
DOT_CX = EB_B[2] + gap + dot_d / 2

assert abs(EB_B[0] - WM_L) < 0.01, "eyebrow left edge drifted"
assert abs(U_B[2] - WM_R) < 0.01, "url right edge drifted"
assert abs((P["wm_b"][3] - P["eb_b"][1]) - (MASS_BOT - MASS_TOP)) < 0.01, "block height drifted"


def lockup(shield, ink, divider, dot, url, rule, rule_op="1"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}" '
            f'role="img" aria-label="Penn Carey Law AI Project — pennai.law">\n'
            f'  <title>Penn Carey Law AI Project — pennai.law</title>\n'
            f'  {shield}\n'
            f'  <path id="divider" stroke="{divider}" stroke-width="3" d="M {DIV_X} 46 L {DIV_X} 264"/>\n'
            f'  <path id="eyebrow" fill="{ink}" d="{EB_D}"/>\n'
            f'  <circle id="sep" cx="{DOT_CX:.2f}" cy="{CAP_MID:.2f}" r="{dot_d/2:.2f}" fill="{dot}"/>\n'
            f'  <path id="url" fill="{url}" d="{U_D}"/>\n'
            f'  <path id="rule" fill="none" stroke="{rule}" stroke-opacity="{rule_op}" '
            f'stroke-width="{P["rule_w"]:.2f}" '
            f'd="M {WM_L:.2f} {P["rule_y"]:.2f} L {WM_R:.2f} {P["rule_y"]:.2f}"/>\n'
            f'  <path id="wordmark" fill="{ink}" d="{P["wm_d"]}"/>\n</svg>\n')


# Dot takes the mark's red (#822024), matching the rule directly beneath it rather
# than the site bar's #990000 — the mark stays internally consistent.
colour = lockup(shield_of("heading-color.svg"), "#011f5b", "#c9c7c0",
                "#822024", "#5c6678", "#822024")
# On dark grounds red is 1.75:1 against navy. The rule is a long stroke and still
# reads as a shape at low contrast; a 6.4u dot does not — at a 75px header it is
# 1.6px. So the white variant keeps a light dot and a white rule.
white = lockup(shield_of("heading-white.svg"), "#ffffff", "#7f8794",
               "#8595b4", "#b3c0da", "#ffffff", rule_op="0.55")

for name, svg in (("lockup-color.svg", colour), ("lockup-white.svg", white)):
    assert "<text" not in svg, f"{name} contains live text"
    (OUT / name).write_text(svg)

print(f"W2 · canvas {CANVAS_W}x{CANVAS_H} ({CANVAS_W/CANVAS_H:.3f}:1)")
print(f"  eyebrow  {EB_SIZE:.1f}u, tracking {eb_ls:.2f}u ({eb_ls/EB_SIZE:.3f}em) "
      f"= {eb_ls/P['ls']*100:.0f}% of solo-line tracking")
print(f"  url      {u_size:.1f}u, tracking {u_ls:.2f}u ({URL_TRACK_EM}em) "
      f"-> {u_size*75/CANVAS_H:.1f}px at a 75px header")
print(f"  dot      d={dot_d:.1f}u at x={DOT_CX:.1f}, cap-centred y={CAP_MID:.1f}")
print(f"  fits     L {EB_B[0]-WM_L:+.3f}  R {U_B[2]-WM_R:+.3f}  "
      f"H {(P['wm_b'][3]-P['eb_b'][1])-(MASS_BOT-MASS_TOP):+.3f}")
for n in ("lockup-color.svg", "lockup-white.svg"):
    print(f"  {(OUT/n).stat().st_size//1024:>3}KB  {n}")
