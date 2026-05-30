# Faculty AI Resources Portal → ai-teaching-lab.org — Migration Design

**Date:** 2026-05-30
**Status:** Approved design (revised for submodule + org transfer), pre-implementation
**Portal repo (source of truth):** `polkwagner/penn-law-ai-resources` → transfers to `ai-teaching-lab/penn-law-ai-resources`. Working copies at `~/code/penn-law-ai-resources` and `~/Penn Law Dropbox/Polk Wagner/code/penn-law-ai-resources`.
**Lab site (consumer):** `~/code/ai-teaching-lab/ai-teaching-lab.org` (repo `ai-teaching-lab/ai-teaching-lab.org`, served at `ai-teaching-lab.org`)

## Goal

Make the Penn Carey Law AI Resources portal a **Lab project** (owned by the `ai-teaching-lab` GitHub org, team-editable, actively developed) and serve it **under the Lab site's Toolkit** at `ai-teaching-lab.org/toolkit/ai-resources/`, while keeping the portal a self-contained interactive HTML site with its own design and dev workflow. One source of truth; no duplicated content.

## Decisions (locked)

| Decision | Choice |
|---|---|
| Source of truth | The portal repo stays its own repo; **git submodule** into the Lab site. Single source of truth. |
| Ownership | Transfer `penn-law-ai-resources` to the `ai-teaching-lab` org — it becomes a Lab project, not personal. |
| Active development | Continues in the portal repo; team works there. |
| Serving | Static drop-in — portal HTML served verbatim by the Lab site's Hugo build. |
| New canonical URL | `https://ai-teaching-lab.org/toolkit/ai-resources/` |
| Files served | All published pages + assets (portal, reading pages, skills page, office-hours, signage, license). |
| Toolkit card | Category `audience` (faculty); title "Faculty AI Resources". |
| Visual design | Keep the portal's own design system (reads as a distinct sub-site — accepted). |
| Repo visibility | Portal repo stays **public** (needed for CI submodule fetch; content is CC BY / Apache anyway). |
| Old URLs | Repoint `pennlaw.link/ai-resources` shortlink to the new URL; rely on GitHub's post-transfer redirect for the old `github.io` URL; portal repo's own Pages disabled. |

## Architecture

### Component 1 — Org transfer (portal becomes a Lab project)

Transfer `polkwagner/penn-law-ai-resources` to the `ai-teaching-lab` org (GitHub → repo Settings → Transfer ownership). Preserves history, issues, stars; GitHub auto-redirects the repo's web/git URLs. Requires Polk's admin on the repo + create rights in the org. **Manual GitHub step** (cannot be done from local git).

After transfer:
- Update the remote on both working copies: `git remote set-url origin https://github.com/ai-teaching-lab/penn-law-ai-resources.git`.
- Confirm the repo is **public** (or make it so) — required for CI submodule fetch (Component 4) and consistent with its CC BY 4.0 content / Apache 2.0 code license.
- **Disable GitHub Pages** on the portal repo so it does not serve a second live copy at `ai-teaching-lab.github.io/penn-law-ai-resources/`. The canonical live URL is the Lab Toolkit URL.

### Component 2 — Submodule into the Lab site

Add the portal repo as a submodule of `ai-teaching-lab.org` at a **non-served path**:

```
git submodule add https://github.com/ai-teaching-lab/penn-law-ai-resources.git \
  vendor/penn-law-ai-resources
```

Mounted at `vendor/` (not `static/`) so Hugo does not copy it wholesale. Records `.gitmodules` + the submodule gitlink in the Lab repo.

### Component 3 — Hugo module mount (serve only published files)

A submodule contains the whole portal repo — including `CLAUDE.md`, `docs/`, `LICENSE`, `.github/`, `.claude/`. If those reach `static/`, Hugo publishes them at `/toolkit/ai-resources/CLAUDE.md` etc. **They must not leak.** Use a Hugo module mount in `hugo.toml` to map only the published files into the served path, excluding scaffolding.

```toml
[module]
  # Re-declare the default static mount — defining ANY static-target mount
  # replaces Hugo's implicit `static → static`, so it must be restated.
  [[module.mounts]]
    source = "static"
    target = "static"

  # Mount the portal bundle into the toolkit URL space, minus scaffolding.
  [[module.mounts]]
    source = "vendor/penn-law-ai-resources"
    target = "static/toolkit/ai-resources"
    excludeFiles = [
      "/CLAUDE.md", "/LICENSE", "/.gitignore", "/.gitmodules",
      "/README.md",
      "/docs/**", "/.github/**", "/.claude/**", "/.superpowers/**",
    ]
```

Result: `static/toolkit/ai-resources/index.html`, `…/assets/logos/*.png`, the reading pages, etc. are served; scaffolding is not. The portal's relative links (`agentic-ai-security.html`, `assets/…`) resolve at the new path because the published files keep their relative layout.

> Implementation note: confirm the exact `excludeFiles` glob set against `git ls-files` of the portal repo before shipping, and verify nothing under `vendor/**` other than the mount target appears in `public/`. If `excludeFiles` proves fiddly, the fallback is to relocate the portal's published files into a `site/` subdir in the portal repo and mount `vendor/penn-law-ai-resources/site` (no excludes needed) — but that restructures the portal repo, so try the exclude approach first.

### Component 4 — CI submodule checkout

The deploy workflow (`.github/workflows/hugo-deploy.yml`) already does `actions/checkout@v4` with `submodules: recursive`. Constraint: the default `GITHUB_TOKEN` is scoped to the Lab repo only. Because the portal repo is **public**, the submodule fetches over HTTPS without extra credentials — no workflow change needed. (If the portal repo were ever made private, this breaks; would require a deploy key or PAT. Keeping it public avoids that.)

### Component 5 — Toolkit bridge (card in the grid)

`layouts/toolkit/list.html` renders one card per Hugo content page, grouped by `toolkit_category`. The submodule-served portal is static, not a Hugo page, so two small pieces bridge it into the grid:

**(a) Bridge content stub** — `content/toolkit/ai-resources.md`, front matter only:

```yaml
---
title: "Faculty AI Resources"
description: "<one-line summary pulled from the live portal>"
toolkit_category: "audience"
audience: ["faculty"]
availability: "public"
version: "<current portal version/date string>"
weight: <fits the audience-group ordering>
external_url: "/toolkit/ai-resources/"
_build:
  render: never      # don't generate an empty orphan Hugo page
  list: always       # but include this card in the toolkit grid
---
```

`render: never` keeps Hugo from writing a page at `/toolkit/ai-resources/`, leaving that URL free for the submodule-mounted static `index.html`. `list: always` keeps the card in the grid.

**(b) Card template edit** — `layouts/partials/toolkit-card.html`, honor `external_url`:

```go-html-template
{{ $url := .Params.external_url | default .RelPermalink }}
```

…used in the card's `<a href>`. Backward-compatible: existing cards have no `external_url` and fall back to `.RelPermalink`.

**Naming:** the Toolkit already has `ai-resources-at-penn.md` ("AI Resources at Penn", a link directory) — distinct from this portal. Card title "Faculty AI Resources", URL `/toolkit/ai-resources/`. Both coexist.

### Component 6 — Link cleanup in the portal repo (cosmetic)

In the portal repo, update self-references to the new canonical URL (committed in the portal repo, since that's the source of truth):

- `index.html` — `og:url` / `<link rel=canonical>` (if present) → new URL.
- `agentic-ai-overview.html` — `<link rel=canonical href="…penn-law-ai-resources/#agentic-ai">` → new URL.
- `license.html` — attribution blockquote `Source: … polkwagner.github.io/penn-law-ai-resources` → new URL.

Functional links (relative internal links; external links to the pedagogy sibling and `ai-teaching-lab.org/...`) already work.

### Component 7 — Old-URL preservation

- **Shortlink (primary):** repoint `pennlaw.link/ai-resources` → `https://ai-teaching-lab.org/toolkit/ai-resources/`. Manual, in whatever runs the shortlink. This is the advertised entry point.
- **Old `polkwagner.github.io/penn-law-ai-resources/`:** relies on GitHub's automatic redirect after repo transfer (best-effort for Pages). Portal repo Pages is disabled, so no competing live copy.
- Accepted tradeoff: because the portal repo is now the live content source, it can't simultaneously host per-page redirect stubs (the earlier plan). Direct deep links to the old `github.io` `.html` pages are best-effort. If guaranteed redirects become necessary, a separate tiny redirect-only repo/Pages can be added later — out of scope now.

## Data flow

Push to Lab repo `main` → GitHub Actions: `actions/checkout` (recursive submodules) pulls the portal repo into `vendor/penn-law-ai-resources` → Hugo builds with the module mount, emitting the portal under `public/toolkit/ai-resources/` → Pagefind indexes `public/` → deploy to Pages. Updating the portal: commit in the portal repo, then bump the submodule pointer in the Lab repo (`git submodule update --remote`, commit) to publish the new version.

**Known side effect:** Pagefind indexes the portal HTML, so portal content is searchable in the Lab's site-wide search in addition to the portal's own Cmd+K. Net positive.

## Verification

1. `hugo --gc --minify` builds with no errors and no duplicate-target warnings for `/toolkit/ai-resources/`.
2. `public/toolkit/ai-resources/index.html` and `public/toolkit/ai-resources/assets/logos/claude.png` exist.
3. **No scaffolding leak:** `public/toolkit/ai-resources/CLAUDE.md`, `/docs/`, `/LICENSE` do NOT exist; nothing from `vendor/**` appears in `public/` except the mount target.
4. Toolkit list page shows a "Faculty AI Resources" card under "Audience-specific guidance" linking to `/toolkit/ai-resources/`.
5. Portal internal nav, Cmd+K search, and asset references resolve under `public/`.
6. Submodule fetches cleanly in a fresh clone (`git clone --recurse-submodules`) — proxy for CI behavior.

## Manual / ops steps (cannot be done from local git)

1. Transfer repo to the `ai-teaching-lab` org; confirm public; disable its Pages.
2. Repoint `pennlaw.link/ai-resources` shortlink.
3. (Org admin) confirm Lab team members have write access to the transferred repo.

## Out of scope

- Reauthoring portal content into Hugo Markdown.
- Merging overlap with `toolkit/ai-resources-at-penn.md` (separate link directory) — both coexist.
- Restyling the portal to match the Hugo theme.
- Rotating credentials or editing portal substance.
- Guaranteed per-page redirects from the old `github.io` URL.

## Open items for implementation

- Pull the exact portal "version"/last-updated string and a one-line description for the bridge stub.
- Confirm `weight` places the card sensibly in the audience group.
- Validate the `excludeFiles` glob set against the portal repo's actual file list.
