# ai-teaching-lab.org

Hugo source for the Penn Carey Law AI Project website, live at https://pennai.law.
The custom domain comes from `static/CNAME`; don't delete it.

## Develop

Needs Hugo extended (CI pins 0.161.1). Then:

```
hugo server
```

Pagefind powers the site search. It runs in CI, not in `hugo server`, so the
search overlay returns nothing locally — that is expected.

## Deploy

`.github/workflows/hugo-deploy.yml` builds with Hugo, indexes with Pagefind,
and publishes to GitHub Pages on every push to `main`. Pushes to `dev` build
but do not deploy, as a sanity check.

## Layout

- `content/` — pages and sections (projects, toolkit, events, research, build, teach)
- `layouts/` — templates; `partials/row.html` is the indexed row used across the index pages
- `assets/css/main.css` — the whole stylesheet, driven by the `:root` custom properties
- `data/clusters.toml` — the project clusters and their order
- `static/` — brand SVGs, slides, papers, `CNAME`
- `brand/` — lockup and favicon generator scripts (`build_w2.py` is the production one; see `brand/README.md`)

Type is Rajdhani (display), IBM Plex Sans (body), and IBM Plex Mono (metadata),
loaded from Google Fonts — the site's only external dependency.

Design spec: `docs/superpowers/specs/2026-07-29-site-redesign-design.md`.

## License

Site content and design are CC BY 4.0 — see `LICENSE`.
