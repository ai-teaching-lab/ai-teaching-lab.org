# ai-teaching-lab.org

Source for the Penn Carey Law AI Project website at https://ai-teaching-lab.org.

## Current state — splash page

`index.html` is a single-file static splash page served from this repo via GitHub Pages.

- No build step, no dependencies
- Inline CSS, system fonts (Iowan Old Style / Palatino serif headings; system sans body)
- SVG assets:
  - `logo-heading-color.svg` — main hero logo (full color)
  - `logo-heading-white.svg` — white variant for dark backgrounds (not used on splash; available for future)
  - `shield.svg` — Lab shield mark
  - `favicon.svg` — same shield, served as favicon
  - `penn-tech-shield.svg` — Penn Carey Law institutional shield (header)
- `CNAME` configures the custom domain (`ai-teaching-lab.org`)

To preview locally: open `index.html` in any browser.

## Domain setup

Polk owns:
- `ai-teaching-lab.org` (primary, configured here)
- `aiteachinglab.org` (typo-defense; should redirect to `.org`)

DNS pointing to GitHub Pages is queued — see `Box: AI Teaching Lab/HANDOFF.md` for the current status.

## Roadmap

Per `Box: AI Teaching Lab/design/2026-05-07-infrastructure.md`:

1. **Phase 1 (May 7–14):** Splash live at `ai-teaching-lab.org`. (This page.)
2. **Phase 2 (May 14–28):** Hugo skeleton + custom templates (no theme dependency); GitHub Actions deploy.
3. **Phase 3 (concurrent):** Box → Hugo content pipeline (`scripts/sync-from-box.py` on Mac Mini launchd).
4. **Phase 4 (June):** Content seeding — toolkit audit + migration, project pages, events, publications.
5. **Phase 5 (July–Aug):** RA onboarding.
6. **Phase 6 (September on):** Steady state.

When the Hugo site lands, `index.html` is replaced by the Hugo build output. Repo URL stays the same.

## Identity reference

All copy on this page draws from `Box: AI Teaching Lab/IDENTITY.md`. If positioning shifts, update there first, then propagate here.
