# Brand pipeline

Generates the Penn Carey Law AI Project lockup (W2: PENN CAREY LAW · PENNAI.LAW eyebrow line,
text block fitted to the shield's ink mass). Spec: docs/superpowers/specs/2026-07-29-site-redesign-design.md §7.

- `build_brand.py` — base pipeline: HarfBuzz shaping + fontTools outlining. Historical: emits the
  pre-URL mark. Kept because build_w2.py execs its helper functions.
- `build_w2.py` — the production mark. Emits lockup-color.svg / lockup-white.svg to
  ~/Downloads/PennCareyLawAIProject-brand-2026-07/; copy into static/ as heading-color.svg /
  heading-white.svg.

Requirements: `pip install uharfbuzz fonttools`, plus `~/Library/Fonts/Rajdhani-Bold.ttf`.
Note: build_w2.py execs the helper block of build_brand.py from its own directory — keep them together.
This directory is not published (Hugo publishes only content/, static/, assets/).
