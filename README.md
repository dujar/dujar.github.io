# dujar.github.io

Portfolio of [dujarfa](https://github.com/dujar) — typeset like a preprint, compiled with [leonui](https://github.com/dujar/leonui).

## Structure

```
components/
  head.html           <head>: meta, fonts, leonui CDN script
  body-open.html      <body> tag — all reactive state (works/papers data, q, sort, theme)
  masthead.html       top rule: avatar, site name, location, edition toggle
  titleblock.html     hero: title, role line, abstract, keywords
  works.html          § 1 — search line, sort toggle, keyed works list, empty state
  bibliography.html   § 2 — further reading, empty state
  footer.html         § 3 — correspondence, colophon, footnote
build.py              assembles index.html from the components above
404.html              erratum page (standalone, same stylesheet)
styles.css            the entire typesetting
```

## Editing

`index.html` is a **generated file** — do not edit it directly.

1. Edit the relevant component in `components/`. The works and bibliography
   data live in `components/body-open.html` (`ui:state`); avoid `;` and `'`
   inside the data strings.
2. Recompile:

   ```bash
   ./build.py
   ```

3. Commit and push to `main` — GitHub Pages redeploys automatically
   (`.nojekyll` keeps the deployment a plain file copy).

## Runtime

- [leonui 0.1.2](https://cdn.jsdelivr.net/npm/leonui@0.1.2/dist/leonui.js) from
  jsDelivr, pinned — signals, keyed `ui:each`, `sortBy`/`contains` expressions,
  effect verbs. No other JavaScript, no build tooling beyond `build.py`.
- Debug: `window.__ui.warns` should always be empty.
