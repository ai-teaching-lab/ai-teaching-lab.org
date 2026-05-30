# Faculty AI Resources Portal → Lab Subdomain — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the Penn Carey Law AI Resources portal a Lab project — owned by the `ai-teaching-lab` GitHub org, served at `https://ai-resources.ai-teaching-lab.org/` on its own GitHub Pages, and featured as a card in the Lab site's Toolkit — with no build coupling between the two sites.

**Architecture:** The portal stays its own repo (transferred to the org) and keeps deploying itself via GitHub Pages from `main`, root `/` (legacy "deploy from a branch" — confirmed: no Actions workflow, no CNAME file present). It serves on a Lab subdomain via a root `CNAME` file + a DNS record. The Lab site is untouched except for one new Toolkit card (a `render: never` content stub that links out via a new `external_url` front-matter field) and a one-line edit to the card partial.

**Tech Stack:** Hugo (extended, local 0.162.1 / CI 0.161.1), GitHub Pages, plain static HTML, `gh` CLI, DNS.

**Spec:** `docs/superpowers/specs/2026-05-30-faculty-ai-resources-migration-design.md`

**Repos & working copies:**
- Lab site: `~/code/ai-teaching-lab/ai-teaching-lab.org` (branch `migrate-faculty-ai-resources`, already created)
- Portal: `~/Penn Law Dropbox/Polk Wagner/code/penn-law-ai-resources` (branch `main`, clean; remote `polkwagner/penn-law-ai-resources`)

**Legend:** 🟢 = Claude executes locally · 🟠 = manual step Polk performs (GitHub/DNS/shortlink). Tasks are ordered to match the spec's **Cutover sequence** — local edits first (reversible), the irreversible/ops steps later, the shortlink last.

---

## File map

| File | Repo | Action | Responsibility |
|---|---|---|---|
| `layouts/partials/toolkit-card.html` | Lab | Modify | Let a card link to an external URL + show an outbound affordance |
| `content/toolkit/ai-resources.md` | Lab | Create | The Toolkit bridge card (front matter only; `render: never`) |
| `index.html` | Portal | Modify | Add canonical + Open Graph URL pointing at the subdomain |
| `agentic-ai-overview.html` | Portal | Modify | Repoint its canonical to the subdomain |
| `license.html` | Portal | Modify | Update the attribution URL to the subdomain |
| `CNAME` | Portal | Create | Set the GitHub Pages custom domain |

---

## Task 1 🟢 — Lab site: teach the toolkit card to link externally

**Files:**
- Modify: `layouts/partials/toolkit-card.html`

The current partial hard-codes `<a href="{{ .RelPermalink }}">`. We add an `external_url` override and an outbound-link affordance, leaving every existing card unchanged (they have no `external_url`, so they fall back to `.RelPermalink`).

- [ ] **Step 1: Add the `$url` variable.** In `layouts/partials/toolkit-card.html`, immediately after the existing first line `{{ $cat := .Params.toolkit_category | default "core" }}`, add:

```go-html-template
{{ $url := .Params.external_url | default .RelPermalink }}
```

- [ ] **Step 2: Change the anchor.** Replace this line:

```go-html-template
  <a href="{{ .RelPermalink }}">
```

with:

```go-html-template
  <a href="{{ $url }}"{{ if .Params.external_url }} target="_blank" rel="noopener"{{ end }}>
```

- [ ] **Step 3: Add the outbound glyph to the title.** Replace this line:

```go-html-template
    <h3>{{ .Title }}</h3>
```

with:

```go-html-template
    <h3>{{ .Title }}{{ if .Params.external_url }} <span class="toolkit-card-ext" aria-hidden="true">↗</span>{{ end }}</h3>
```

- [ ] **Step 4: Build and confirm existing cards are unchanged.** From `~/code/ai-teaching-lab/ai-teaching-lab.org`:

```bash
hugo --gc --minify --quiet && grep -c '<li class="toolkit-card' public/toolkit/index.html && grep -c '↗' public/toolkit/index.html
```

Expected: build succeeds with no errors; the `<li class="toolkit-card` count is `12` (the existing cards still render); the `↗` count is `0` (no card has `external_url` until Task 2).

- [ ] **Step 5: Commit.**

```bash
git add layouts/partials/toolkit-card.html
git commit -m "toolkit-card: support external_url with outbound affordance"
```

---

## Task 2 🟢 — Lab site: add the "Faculty AI Resources" bridge card

**Files:**
- Create: `content/toolkit/ai-resources.md`

A front-matter-only stub. `render: never` means Hugo writes no page at `/toolkit/ai-resources/` (so it can't 404-shadow anything and there's no empty orphan); `list: always` keeps it in the Toolkit grid; `external_url` sends the card to the subdomain. Weight `100` places it at the top of the "Audience-specific guidance" group (existing audience weights are 110/120/130).

- [ ] **Step 1: Create the file** `content/toolkit/ai-resources.md` with exactly:

```markdown
---
title: "Faculty AI Resources"
description: "The faculty hub for AI at Penn Carey Law — tools, use cases, agentic-AI guidance, policies, and the wider Penn AI ecosystem."
toolkit_category: "audience"
audience: ["faculty"]
availability: "public"
version: "May 2026"
weight: 100
external_url: "https://ai-resources.ai-teaching-lab.org/"
_build:
  render: never
  list: always
---
```

- [ ] **Step 2: Build the site.**

```bash
hugo --gc --minify --quiet
```

Expected: succeeds, no errors, no duplicate-target warnings.

- [ ] **Step 3: Confirm the card renders and links to the subdomain.**

```bash
grep -A4 'Faculty AI Resources' public/toolkit/index.html | grep -o 'https://ai-resources.ai-teaching-lab.org/'
```

Expected: prints `https://ai-resources.ai-teaching-lab.org/` (the card exists and links out).

- [ ] **Step 4: Confirm NO orphan page was emitted at the portal's future path.**

```bash
test ! -e public/toolkit/ai-resources/index.html && echo "OK: no orphan page"
```

Expected: `OK: no orphan page` (proves `render: never` worked — the subdomain owns that URL space, the Lab site doesn't shadow it).

- [ ] **Step 5: Confirm the Lab site's own custom domain is untouched.**

```bash
cat public/CNAME
```

Expected: `ai-teaching-lab.org` (unchanged — this whole change touched nothing in the publish pipeline).

- [ ] **Step 6: Commit.**

```bash
git add content/toolkit/ai-resources.md
git commit -m "toolkit: add Faculty AI Resources card linking to ai-resources subdomain"
```

---

## Task 3 🟢 — Portal repo: branch + canonical/attribution edits

**Files (in `~/Penn Law Dropbox/Polk Wagner/code/penn-law-ai-resources`):**
- Modify: `index.html`, `agentic-ai-overview.html`, `license.html`

These edits are prepared on a branch now and pushed to `main` only at the cutover point (Task 7), so the live old site doesn't advertise the new URL before it exists. `index.html` currently has **no** canonical/OG tags, so we add them; the other two have exact strings to change.

- [ ] **Step 1: Create a branch in the portal repo.**

```bash
cd ~/Penn\ Law\ Dropbox/Polk\ Wagner/code/penn-law-ai-resources
git checkout -b lab-migration
```

- [ ] **Step 2: Add canonical + Open Graph to `index.html`.** Insert this block immediately after line 6 (`<title>AI Resources — Penn Carey Law</title>`):

```html
<link rel="canonical" href="https://ai-resources.ai-teaching-lab.org/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://ai-resources.ai-teaching-lab.org/">
<meta property="og:title" content="AI Resources — Penn Carey Law">
<meta property="og:description" content="The faculty hub for AI at Penn Carey Law — tools, use cases, agentic-AI guidance, policies, and the wider Penn AI ecosystem.">
```

- [ ] **Step 3: Repoint the canonical in `agentic-ai-overview.html`.** Replace the line:

```html
<link rel="canonical" href="https://polkwagner.github.io/penn-law-ai-resources/#agentic-ai">
```

with:

```html
<link rel="canonical" href="https://ai-resources.ai-teaching-lab.org/#agentic-ai">
```

(Leave the meta-refresh and `window.location.replace("index.html#agentic-ai")` untouched — they're relative and still correct.)

- [ ] **Step 4: Update the attribution in `license.html`.** Replace the line:

```html
  <blockquote>Source: Penn Carey Law AI Resources, polkwagner.github.io/penn-law-ai-resources, CC BY 4.0</blockquote>
```

with:

```html
  <blockquote>Source: Penn Carey Law AI Resources, ai-resources.ai-teaching-lab.org, CC BY 4.0</blockquote>
```

- [ ] **Step 5: Verify all three edits.**

```bash
grep -c 'ai-resources.ai-teaching-lab.org' index.html agentic-ai-overview.html license.html
grep -rn 'polkwagner.github.io/penn-law-ai-resources' *.html
```

Expected: first command shows `index.html:2` (canonical + og:url lines), `agentic-ai-overview.html:1`, `license.html:1`. Second command prints **nothing** (no stale self-references remain).

- [ ] **Step 6: Commit (do not push yet — pushed at Task 7).**

```bash
git add index.html agentic-ai-overview.html license.html
git commit -m "Point canonical + attribution at ai-resources.ai-teaching-lab.org"
```

---

## Task 4 🟢 — Portal repo: add the CNAME file

**Files:**
- Create: `CNAME` (portal repo root)

The `CNAME` file is what sets the GitHub Pages custom domain for a deploy-from-branch site. It's committed on the `lab-migration` branch now and reaches `main` at cutover (Task 7), after the repo is in the org — so it takes effect at the right moment.

- [ ] **Step 1: Create the `CNAME` file** containing exactly one line, no trailing content:

```
ai-resources.ai-teaching-lab.org
```

- [ ] **Step 2: Verify.**

```bash
cat CNAME
```

Expected: `ai-resources.ai-teaching-lab.org`

- [ ] **Step 3: Commit.**

```bash
git add CNAME
git commit -m "Add CNAME for ai-resources.ai-teaching-lab.org custom domain"
```

> **Checkpoint.** All local edits are done and committed on branches (`migrate-faculty-ai-resources` in the Lab repo; `lab-migration` in the portal repo). Nothing is live yet. The remaining tasks are the cutover — stop here and confirm with Polk before proceeding, since Task 5 onward is irreversible-ish and outward-facing.

---

## Task 5 🟠 — MANUAL: Transfer the repo to the org + grant team access

Polk performs these (admin on the repo + org create rights required). The transfer briefly takes `polkwagner.github.io/penn-law-ai-resources/` offline while Pages moves — expected.

- [ ] **Step 1: Transfer ownership.** Either via the web UI (repo Settings → General → Danger Zone → Transfer ownership → `ai-teaching-lab`), or via CLI:

```bash
gh api -X POST repos/polkwagner/penn-law-ai-resources/transfer -f new_owner=ai-teaching-lab
```

- [ ] **Step 2: Confirm the transfer.**

```bash
gh repo view ai-teaching-lab/penn-law-ai-resources --json name,visibility,isPrivate
```

Expected: the repo resolves under `ai-teaching-lab`; `visibility` is `PUBLIC`. If it's private, make it public (Settings → Danger Zone → Change visibility) — required for org Pages and for the public site.

- [ ] **Step 3: Grant a TEAM write access (NOT org base permission).** Pick the Lab team that should maintain the portal (confirm the team slug with `gh api orgs/ai-teaching-lab/teams --jq '.[].slug'`), then:

```bash
gh api -X PUT orgs/ai-teaching-lab/teams/<TEAM_SLUG>/repos/ai-teaching-lab/penn-law-ai-resources -f permission=push
```

(`push` = write.) **Do not** change the org's base permission to write. Verify in repo Settings → Collaborators and teams that the team shows **Write**.

- [ ] **Step 4: Update local remotes** on both working copies (paths per CLAUDE.md):

```bash
cd ~/Penn\ Law\ Dropbox/Polk\ Wagner/code/penn-law-ai-resources && git remote set-url origin https://github.com/ai-teaching-lab/penn-law-ai-resources.git
git remote -v
```

Expected: `origin` now points at `ai-teaching-lab/penn-law-ai-resources`.

---

## Task 6 🟠 — MANUAL: Confirm org Pages is live (gate before DNS)

Do **not** touch DNS until the portal serves under the org's `github.io`. Pointing DNS at a Pages site that hasn't rebuilt yet causes an avoidable 404 window.

- [ ] **Step 1: Confirm Pages source.** In the transferred repo: Settings → Pages → "Deploy from a branch", `main` / `/ (root)`. (This is the current config — no Actions workflow exists.)

- [ ] **Step 2: Confirm the org Pages URL serves the portal.** In a browser or:

```bash
curl -sI https://ai-teaching-lab.github.io/penn-law-ai-resources/ | head -1
```

Expected: `HTTP/2 200`. If 404, wait for the Pages build to finish (Actions/Pages tab shows build status) before continuing.

---

## Task 7 🟢→🟠 — Ship the portal edits + set the custom domain

This publishes the `lab-migration` branch (canonical edits + `CNAME`) to `main` so the org Pages picks them up, then sets the custom domain.

- [ ] **Step 1: 🟢 Merge and push the portal edits to `main`.**

```bash
cd ~/Penn\ Law\ Dropbox/Polk\ Wagner/code/penn-law-ai-resources
git checkout main && git merge --no-ff lab-migration -m "Migrate portal to ai-resources.ai-teaching-lab.org (canonical + CNAME)"
git push origin main
```

- [ ] **Step 2: 🟠 Set the custom domain.** In repo Settings → Pages → Custom domain, enter `ai-resources.ai-teaching-lab.org` and Save. (The pushed `CNAME` file should already populate this; confirm they agree.)

- [ ] **Step 3: 🟠 Add the DNS record.** At the `ai-teaching-lab.org` DNS host, add:

```
Type:  CNAME
Name:  ai-resources
Value: ai-teaching-lab.github.io
TTL:   default
```

- [ ] **Step 4: 🟠 Wait for the TLS cert, then enforce HTTPS.** GitHub provisions a Let's Encrypt cert once DNS resolves (minutes to ~24h; the **Enforce HTTPS** checkbox stays greyed out until it issues). When available, check **Enforce HTTPS**.

- [ ] **Step 5: Verify the subdomain serves over HTTPS and the old path redirects.**

```bash
curl -sI https://ai-resources.ai-teaching-lab.org/ | head -1
curl -sI https://ai-teaching-lab.github.io/penn-law-ai-resources/ | grep -i location
```

Expected: first prints `HTTP/2 200`; second shows a `location:` header pointing at `https://ai-resources.ai-teaching-lab.org/`.

---

## Task 8 🟢 — Lab site: merge the bridge card to `main`

Now that the subdomain is live, publish the Toolkit card so it links to a working URL.

- [ ] **Step 1: (Optional CI sanity) push the feature branch to `dev`** to get a no-deploy CI build, if desired:

```bash
cd ~/code/ai-teaching-lab/ai-teaching-lab.org
git push origin migrate-faculty-ai-resources:dev
```

(The workflow builds `dev` without deploying — a free sanity check.)

- [ ] **Step 2: Merge to `main` and push** (this deploys the Lab site):

```bash
git checkout main && git merge --no-ff migrate-faculty-ai-resources -m "Add Faculty AI Resources toolkit card (ai-resources subdomain); migration spec + plan"
git push origin main
```

- [ ] **Step 3: Verify on the live Lab site** after the deploy completes:

```bash
curl -s https://ai-teaching-lab.org/toolkit/ | grep -o 'https://ai-resources.ai-teaching-lab.org/'
```

Expected: prints the subdomain URL (the card is live in the Toolkit).

---

## Task 9 🟠 — MANUAL: Repoint the shortlink (LAST)

Done last, so the advertised entry point only ever points at a fully-live HTTPS URL.

- [ ] **Step 1:** In whatever runs `pennlaw.link`, repoint `pennlaw.link/ai-resources` → `https://ai-resources.ai-teaching-lab.org/`.

- [ ] **Step 2: Verify.**

```bash
curl -sI https://pennlaw.link/ai-resources | grep -i location
```

Expected: `location:` resolves (possibly via one hop) to `https://ai-resources.ai-teaching-lab.org/`.

---

## Final verification checklist (maps to spec §Verification)

- [ ] `https://ai-resources.ai-teaching-lab.org/` serves the portal over HTTPS, valid cert, Enforce HTTPS on. *(Task 7.5)*
- [ ] `https://ai-teaching-lab.github.io/penn-law-ai-resources/` redirects to the subdomain. *(Task 7.5)*
- [ ] Portal internal nav, Cmd+K search, reading pages, and `assets/` all resolve on the subdomain. *(spot-check in browser)*
- [ ] A non-Polk org team member can push to the portal repo (team Write confirmed). *(Task 5.3)*
- [ ] Lab Toolkit shows "Faculty AI Resources" under "Audience-specific guidance," linking out with the `↗` affordance; all pre-existing cards/pages still render; `public/CNAME` unchanged. *(Tasks 1–2, 8.3)*
- [ ] `pennlaw.link/ai-resources` lands on the subdomain. *(Task 9.2)*

---

## Notes / known follow-ups (from the spec)

- **Pedagogy sibling:** the portal links to `polkwagner.github.io/penn-law-pedagogy-resources/` (~7 places) — a personal-account site now referenced from a Lab-branded one. Decide separately whether to migrate it the same way. Not in this plan.
- **Portal Pages serves dev files** (`CLAUDE.md`, `docs/`) — pre-existing behavior, not introduced here. Optional later hardening: a Jekyll `_config.yml` `exclude:` list.
- **Optional nicety:** a Hugo alias redirecting `ai-teaching-lab.org/toolkit/ai-resources/` → the subdomain, so the "obvious" path isn't a 404. Skipped by default (not advertised).
