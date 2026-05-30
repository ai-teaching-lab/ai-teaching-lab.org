# Faculty AI Resources Portal → ai-teaching-lab.org — Migration Design

**Date:** 2026-05-30
**Status:** Approved design, pre-implementation
**Source:** `~/Penn Law Dropbox/Polk Wagner/code/penn-law-ai-resources` (repo `polkwagner/penn-law-ai-resources`, served at `polkwagner.github.io/penn-law-ai-resources/`)
**Destination:** `~/code/ai-teaching-lab/ai-teaching-lab.org` (repo `ai-teaching-lab/ai-teaching-lab.org`, served at `ai-teaching-lab.org`)

## Goal

Move the Penn Carey Law faculty AI Resources portal onto the Lab site, preserving it as a self-contained interactive HTML sub-site, and surface it as a card in the Lab's Toolkit. Retire the standalone site behind redirects so existing links keep working.

## Decisions (locked)

| Decision | Choice |
|---|---|
| Migration style | Static drop-in — portal HTML served verbatim, not reauthored into Markdown |
| New canonical URL | `https://ai-teaching-lab.org/toolkit/ai-resources/` |
| Files migrated | All published pages + assets (portal, reading pages, skills page, office-hours, signage, license) |
| Toolkit card category | `audience` (faculty) |
| Toolkit card title | "Faculty AI Resources" |
| Visual design | Keep the portal's own design system (reads as a distinct sub-site — accepted) |
| Old site | Per-page redirect stubs → new URLs; repoint `pennlaw.link/ai-resources` |

## Architecture

### Component 1 — The static portal bundle

All published files move verbatim to `static/toolkit/ai-resources/` in the Lab repo:

```
static/toolkit/ai-resources/
  index.html                  # the tab-based portal (self-contained CSS/JS, Cmd+K search)
  agentic-ai-security.html    # long-form security reading page
  agentic-ai-overview.html    # redirect stub → index.html#agentic-ai
  ai-office-hours.html        # faculty AI office-hours session screen
  ai-signage.html             # auto-cycling faculty-lounge digital signage
  claude-skills.html          # 12 public AI skills listing
  license.html                # portal's own license page (CC BY 4.0 + Apache 2.0)
  assets/                     # favicons, logos/, ai-teaching-lab-stacked.svg
```

**Why this path:** Hugo copies `static/` verbatim into `public/`, so the portal's relative links (`agentic-ai-security.html`, `assets/logos/claude.png`) resolve correctly at `/toolkit/ai-resources/…`. The portal is unmodified except for the cosmetic link cleanup below.

**Hard constraint — do NOT use the repo's root `assets/`.** Hugo's top-level `assets/` is reserved for Hugo Pipes asset processing and is not served at a public URL. The portal's `assets/` must live *inside* the bundle at `static/toolkit/ai-resources/assets/`. Putting it at repo-root `assets/` would 404 every portal image.

**Not migrated** (source-repo scaffolding, not published content): `CLAUDE.md`, `docs/`, root `LICENSE`, `.git`, `.gitignore`, `.superpowers`, `docs/files.zip`.

### Component 2 — Toolkit bridge (card in the grid)

`layouts/toolkit/list.html` renders one card per Hugo content page, grouped by `toolkit_category`. A static bundle is not a Hugo page, so two small pieces bridge it into the grid:

**(a) Bridge content stub** — `content/toolkit/ai-resources.md`, front matter only:

```yaml
---
title: "Faculty AI Resources"
description: "<one-line summary of the portal>"
toolkit_category: "audience"
audience: ["faculty"]
availability: "public"
version: "<current portal version/date>"
weight: <fits the audience group ordering>
external_url: "/toolkit/ai-resources/"
_build:
  render: never      # don't generate an empty orphan Hugo page
  list: always       # but include this card in the toolkit grid
---
```

`_build.render: never` + `list: always` means Hugo lists the card but does not build a `/toolkit/ai-resources/` Hugo page — leaving that URL free for the static `index.html` to occupy. (The content file is named `ai-resources.md`, matching the bundle path, but because it never renders there is no collision with the static directory.)

**(b) Card template edit** — `layouts/partials/toolkit-card.html`, honor `external_url` when present:

```go-html-template
{{ $url := .Params.external_url | default .RelPermalink }}
```

…and use `{{ $url }}` in the card's `<a href>`. Backward-compatible: every existing card lacks `external_url`, so it falls back to `.RelPermalink` unchanged.

### Component 3 — Old-site redirects

In the **old** repo (`polkwagner/penn-law-ai-resources`), replace each published `.html` with a redirect stub (meta-refresh + `<link rel=canonical>` + a visible fallback link) pointing to the corresponding new URL:

| Old file | → New URL |
|---|---|
| `index.html` | `https://ai-teaching-lab.org/toolkit/ai-resources/` |
| `agentic-ai-security.html` | `…/toolkit/ai-resources/agentic-ai-security.html` |
| `agentic-ai-overview.html` | `…/toolkit/ai-resources/agentic-ai-overview.html` |
| `ai-office-hours.html` | `…/toolkit/ai-resources/ai-office-hours.html` |
| `ai-signage.html` | `…/toolkit/ai-resources/ai-signage.html` |
| `claude-skills.html` | `…/toolkit/ai-resources/claude-skills.html` |
| `license.html` | `…/toolkit/ai-resources/license.html` |

Assets stay in place (harmless). Commit + push → GitHub Pages serves the redirects.

**Manual step (flagged, not silently skipped):** repoint the `pennlaw.link/ai-resources` shortlink to the new URL in whatever service manages it. Cannot be done from the repo.

### Component 4 — Link cleanup in migrated copies (cosmetic)

Update the few self-references to the old URL so canonical/attribution data is correct. Functional links already work as-is.

- `index.html` — `og:url` / `<link rel=canonical>` (if present) → new URL
- `agentic-ai-overview.html` — `<link rel=canonical href="…penn-law-ai-resources/#agentic-ai">` → new URL
- `license.html` — attribution blockquote text `Source: … polkwagner.github.io/penn-law-ai-resources` → new URL

External links (pedagogy sibling site, `ai-teaching-lab.org/toolkit/...`, "Visit the Lab") are unchanged and correct.

## Data flow

Push to `main` → GitHub Actions (`hugo-deploy.yml`) builds Hugo (`--gc --minify`), Pagefind indexes `public/`, deploy to GitHub Pages. The static portal bundle is carried through verbatim under `public/toolkit/ai-resources/`.

**Known side effect:** Pagefind indexes the portal's HTML, so portal content becomes searchable in the Lab's site-wide search — in addition to the portal's own internal Cmd+K search. Net positive; no conflict.

## Verification

1. `hugo --gc --minify` builds with no errors.
2. `public/toolkit/ai-resources/index.html` exists; `public/toolkit/ai-resources/assets/logos/claude.png` exists.
3. No `public/toolkit/ai-resources/index.html` *Hugo page* collision (the bridge stub did not render there).
4. The Toolkit list page shows a "Faculty AI Resources" card under "Audience-specific guidance" linking to `/toolkit/ai-resources/`.
5. Spot-check portal internal nav + asset references resolve under `public/`.
6. Old-repo redirect stubs meta-refresh to the new URLs.

## Out of scope

- Reauthoring portal content into Hugo Markdown.
- Reconciling/merging overlap with the existing `toolkit/ai-resources-at-penn.md` (a separate link directory) — both coexist.
- Restyling the portal to match the Hugo theme.
- Rotating any credentials or editing portal substance.

## Open items for implementation

- Pull the exact "version"/last-updated string and a one-line description from the live portal for the bridge stub's front matter.
- Confirm the `weight` value places the card sensibly within the audience group.
