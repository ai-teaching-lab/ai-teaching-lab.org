# Faculty AI Resources Portal → Lab subdomain — Migration Design

**Date:** 2026-05-30
**Status:** Approved design (subdomain architecture), pre-implementation
**Portal repo:** `polkwagner/penn-law-ai-resources` → transfers to `ai-teaching-lab/penn-law-ai-resources`. Working copies at `~/code/penn-law-ai-resources` and `~/Penn Law Dropbox/Polk Wagner/code/penn-law-ai-resources`.
**Lab site:** `~/code/ai-teaching-lab/ai-teaching-lab.org` (repo `ai-teaching-lab/ai-teaching-lab.org`, served at `ai-teaching-lab.org`)

## Goal

Make the Penn Carey Law AI Resources portal a **Lab project**: owned by the `ai-teaching-lab` GitHub org so any org member can access and update it, served at the **Lab subdomain `ai-resources.ai-teaching-lab.org`** on its own GitHub Pages, and **featured as a card in the Lab site's Toolkit**. The portal keeps its own design, its own repo, and a normal push-to-deploy workflow. The two sites stay fully decoupled — neither build can break the other.

## Why subdomain, not a path under the main site

An earlier draft served the portal at `ai-teaching-lab.org/toolkit/ai-resources/` by pulling the portal repo into the Lab site as a git submodule. A senior review (Rex) found that coupling caused: a blocker (the Hugo module mount needed to serve the submodule also republishes the Lab site's `CNAME`, risking the live custom domain), a whole-site build dependency (any portal-repo breakage fails the entire Lab deploy), and a manual submodule-pointer bump on every portal edit (defeating "actively developed"). The subdomain removes all of these — the portal deploys itself, the Lab site is untouched, and edits go live on push. See the "How this resolves the Rex findings" appendix.

## Decisions (locked)

| Decision | Choice |
|---|---|
| Ownership | Transfer `penn-law-ai-resources` to the `ai-teaching-lab` org. Org members can access + update it. |
| Serving | Portal keeps its **own GitHub Pages**, served at the Lab subdomain **`ai-resources.ai-teaching-lab.org`** (locked). |
| Coupling | **None.** Lab site and portal are independent Pages deployments. |
| Active development | Push to the portal repo `main` → live instantly via its own Pages. |
| Repo visibility | Public (consistent with its CC BY 4.0 content / Apache 2.0 code; no private-CI concerns). |
| Toolkit presence | A bridge card in the Lab site's Toolkit links to the subdomain. Category `audience` (faculty); title "Faculty AI Resources". |
| Visual design | Portal keeps its own design system (it is a distinct site, and the URL now says so). |
| Old URLs | Repoint `pennlaw.link/ai-resources` → subdomain; custom-domain auto-redirect covers the `github.io` deep links; canonical tags point at the subdomain. |

> **Subdomain locked:** `ai-resources.ai-teaching-lab.org`.

## Architecture

### Component 1 — Org transfer + team access

Transfer `polkwagner/penn-law-ai-resources` to the `ai-teaching-lab` org (GitHub → repo Settings → Transfer ownership). Preserves history, issues, stars; GitHub auto-redirects the repo's web/git URLs. **Manual GitHub step.** Requires Polk's admin on the repo + create rights in the org.

After transfer:
- **Grant team write access — via a team, not org base permission.** Create or reuse a Lab team (e.g. `@ai-teaching-lab/portal-maintainers` or the existing team that owns the Lab site) and grant it **write** on `penn-law-ai-resources` (repo Settings → Collaborators and teams → Add team). **Do not raise the org base permission to `write`** — that would grant every org member write to *every* repo in the org, not just this one. If the genuine intent is "all org members can edit," do it as a deliberate decision by adding the all-members team, not as a side effect of base permission.
- Confirm the repo is **public**.
- Update the remote on both working copies: `git remote set-url origin https://github.com/ai-teaching-lab/penn-law-ai-resources.git`.

### Component 2 — Portal served at the Lab subdomain (its own Pages)

The portal already deploys via GitHub Pages from `main`, root `/`. Point that Pages site at the subdomain (sequencing matters — see the Cutover section; do not point DNS until the org Pages site is confirmed serving):

- **First, confirm the Pages deploy mechanism.** Check the portal repo's Settings → Pages source. If it is **"Deploy from a branch" (`main`, root `/`)** — which the portal's own CLAUDE.md implies — a root `CNAME` file is the correct, durable way to set the custom domain. If it is instead a **GitHub Actions workflow**, the custom domain must be set in Settings (and, for some community deploy actions, passed as a `cname:` input) or each deploy can wipe it. Handle per the actual mechanism before relying on the `CNAME` file.
- Add a `CNAME` file at the portal repo root containing exactly `ai-resources.ai-teaching-lab.org`, and confirm it matches Settings → Pages → Custom domain.
- **DNS:** add a CNAME record `ai-resources.ai-teaching-lab.org` → `ai-teaching-lab.github.io`. (Independent of the apex `ai-teaching-lab.org`, which already points at GitHub Pages for the Lab site. Two repos, two custom domains, same org — fully supported.) **Manual DNS step.**
- Wait for GitHub to provision the TLS cert (can take minutes to ~24h; **"Enforce HTTPS" stays greyed out until it issues**), then enable **Enforce HTTPS**.

Result: the portal serves at `https://ai-resources.ai-teaching-lab.org/`, deploying on every push to the portal repo — no dependency on the Lab site.

> Pre-existing note (not introduced here): the portal's Pages serves its repo root, so dev files (`CLAUDE.md`, `docs/`) are already web-reachable as they are today. Optional hardening: add a Jekyll `_config.yml` with an `exclude:` list, or a `.gitignore`-style Pages exclusion, so only published files serve. Minor; out of the critical path.

### Component 3 — Toolkit bridge card (Lab site)

The Lab site changes are small and touch nothing in the build pipeline (no `static/`, no `hugo.toml` mounts, no `CNAME` risk).

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
external_url: "https://ai-resources.ai-teaching-lab.org/"
_build:
  render: never      # no empty orphan page at /toolkit/ai-resources/
  list: always       # but keep the card in the toolkit grid
---
```

**(b) Card template edit** — `layouts/partials/toolkit-card.html`, honor `external_url`:

```go-html-template
{{ $url := .Params.external_url | default .RelPermalink }}
```

…used in the card's `<a href>`. Backward-compatible: existing cards have no `external_url` and fall back to `.RelPermalink`. The card should signal it's an outbound link (e.g. a `↗` glyph or `target`/`rel` — decide in the plan) so users know they're leaving the main site.

**Naming:** the Toolkit already has `ai-resources-at-penn.md` ("AI Resources at Penn", a link directory) — distinct from this portal. Both coexist.

### Component 4 — Canonical + self-reference cleanup (portal repo)

Committed in the portal repo (the source of truth). Not cosmetic — canonical tags control duplicate-content/SEO between the old `github.io` copy and the subdomain.

- `index.html` — set `<link rel="canonical">` and `og:url` to `https://ai-resources.ai-teaching-lab.org/`. **Add them if absent** (don't skip when missing).
- `agentic-ai-overview.html` — update its canonical (currently `…penn-law-ai-resources/#agentic-ai`) to the subdomain.
- `license.html` — update the attribution blockquote `Source: … polkwagner.github.io/penn-law-ai-resources` to the subdomain.
- Any other page-level canonical/`og:url` tags → subdomain.

### Component 5 — Old-URL preservation

- **Shortlink (primary):** repoint `pennlaw.link/ai-resources` → `https://ai-resources.ai-teaching-lab.org/`. **Manual.**
- **`ai-teaching-lab.github.io/penn-law-ai-resources/*`:** GitHub Pages auto-redirects the `github.io` path to the repo's custom domain once the `CNAME` is set — so deep links land on the subdomain. Real, not best-effort.
- **`polkwagner.github.io/penn-law-ai-resources/*`:** GitHub's post-transfer redirect forwards to the new owner's `github.io` path, which then redirects to the subdomain (best-effort for the transfer hop, reliable for the custom-domain hop).

## Data flow

Two **independent** pipelines:
1. **Portal:** push to `ai-teaching-lab/penn-law-ai-resources` `main` → its GitHub Pages rebuilds → live at the subdomain. Seconds. No other repo involved.
2. **Lab site:** push to `ai-teaching-lab/ai-teaching-lab.org` `main` → Hugo + Pagefind → Pages. The bridge card links out to the subdomain.

The portal is a separate site, so the Lab's Pagefind does **not** index it (the portal keeps its own Cmd+K search). This avoids the SPA-tab search confusion of the path approach. If Lab-wide search over portal content is wanted later, add it deliberately — it is not a silent side effect here.

## Verification

**Portal / subdomain**
1. `https://ai-resources.ai-teaching-lab.org/` resolves and serves the portal over HTTPS (valid cert, Enforce HTTPS on).
2. `https://ai-teaching-lab.github.io/penn-law-ai-resources/` redirects to the subdomain.
3. Portal internal nav, Cmd+K search, reading pages, and assets all resolve under the subdomain.
4. Org members (not just Polk) can push to the portal repo — confirm a test member or the team permission setting.

**Lab site**
5. Build on the `dev` branch first (the workflow builds `dev` without deploying). Confirm: the Toolkit list shows a "Faculty AI Resources" card under "Audience-specific guidance" linking to the subdomain; **all pre-existing toolkit cards and pages still render**; `public/CNAME` is unchanged (sanity check that the bridge change touched nothing in the pipeline). Then merge to `main`.

**Links**
6. `pennlaw.link/ai-resources` lands on the subdomain after repointing.

## Cutover sequence

Order matters: the repo transfer briefly takes the old `github.io` URL offline, and the TLS cert for the subdomain isn't instant. Sequencing the shortlink **last** keeps the advertised entry point pointing at something that works until the new URL is fully live. Steps marked **[manual]** can't be done from local git.

1. **Prep (harmless, do anytime, reversible).** Add the toolkit bridge card + `toolkit-card.html` edit on the Lab site's `dev` branch (Component 3); prepare the canonical/self-reference edits in the portal repo (Component 4). Don't merge/ship yet.
2. **[manual] Transfer** `penn-law-ai-resources` to the `ai-teaching-lab` org; confirm **public**; grant the **team** write access (Component 1). *Expect the old `polkwagner.github.io/penn-law-ai-resources/` URL to 404 or redirect during propagation — this is the brief downtime window.*
3. **Confirm the org Pages site rebuilt:** `https://ai-teaching-lab.github.io/penn-law-ai-resources/` serves the portal. Do **not** proceed to DNS until this is green.
4. **[manual] Custom domain + DNS:** set the portal Pages custom domain to `ai-resources.ai-teaching-lab.org` (per the verified deploy mechanism), commit the `CNAME` file, add the DNS CNAME record → `ai-teaching-lab.github.io` (Component 2).
5. **[manual] Wait for the TLS cert**, then enable **Enforce HTTPS**. Verify `https://ai-resources.ai-teaching-lab.org/` serves with a valid cert, and that `…github.io/penn-law-ai-resources/` now redirects to it.
6. **Ship the canonical edits** in the portal repo (Component 4) so the live site advertises the new URL.
7. **Merge the Lab-site bridge card** `dev` → `main` after the `dev` build checks out (Component 3 / Verification step 5).
8. **[manual] Repoint the shortlink** `pennlaw.link/ai-resources` → `https://ai-resources.ai-teaching-lab.org/`. **Last**, so it only ever points at a fully-live HTTPS URL.

## Out of scope

- Reauthoring portal content into Hugo Markdown.
- Merging overlap with `toolkit/ai-resources-at-penn.md` (separate link directory) — both coexist.
- Restyling the portal to match the Hugo theme.
- Lab-wide search indexing of portal content.
- Rotating credentials or editing portal substance.

**Known follow-up (flagged, not silently ignored):** the portal links to the personal-account sibling `polkwagner.github.io/penn-law-pedagogy-resources/` in ~7 places. After this migration, a Lab-org, Lab-subdomain site repeatedly hands users to a site on Polk's personal account. Not this migration's job, but it's now a visible inconsistency — decide separately whether to migrate the pedagogy sibling into the org the same way or leave it. Tracked here so it's a decision, not an oversight.

## Open items for implementation

- Pull the exact portal "version"/last-updated string and a one-line description for the bridge card.
- Confirm `weight` places the card sensibly in the audience group.
- Decide the outbound-link affordance on the toolkit card (glyph / new tab).
- Optional: a Hugo alias redirecting `ai-teaching-lab.org/toolkit/ai-resources/` → the subdomain, so the "obvious" path isn't a 404.

## Appendix — how this resolves the Rex findings

| Rex finding (path/submodule design) | Status under subdomain design |
|---|---|
| **Blocker** — module mount endangers Lab `CNAME` / static assets | **Gone.** No mount; Lab `static/` untouched. |
| **Major** — `excludeFiles` denylist leaks new scaffolding | **Gone.** No submodule mount. (Portal-Pages dev-file serving is pre-existing; optional Jekyll exclude noted.) |
| **Major** — submodule makes portal a build dependency of the whole Lab site | **Gone.** Fully decoupled pipelines. |
| **Major** — "actively developed" vs manual submodule bump | **Gone.** Portal push deploys instantly via its own Pages. |
| **Major** — Component 7 redirect contradiction / downgraded requirement | **Resolved.** Custom-domain auto-redirect + shortlink = real preservation. |
| **Minor** — Pagefind "net positive" unearned | **Resolved.** Portal not in Lab Pagefind; decision is explicit. |
| **Minor** — canonical mislabeled cosmetic / "if present" gap | **Resolved.** Component 4: canonical is SEO, add if absent. |
