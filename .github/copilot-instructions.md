# Copilot Instructions

This is a **Jekyll-based GitHub Pages site** for *Prog 1 – Introducción a la Programación I*, a Python introductory programming course at the Facultad de Ingeniería (Universidad Austral, Argentina). Content is in **Spanish**.

The site is served at `https://facultaddeingenieria.github.io/prog1/` (baseurl: `/prog1`).

## Architecture

There are two main content types, each with its own layout:

### Presentations (`layout: remark`)
Each topic under `presentation/<topic>/` contains **two files**:
- `presentation.html` — Jekyll page with front matter (`layout: remark`, `permalink: /<topic>`) and a single `{% include_relative presentation.md %}` tag.
- `presentation.md` — Pure [Remark.js](https://remarkjs.com/) slide content (no front matter). Slides are separated by `---`. The first slide always uses `class: center, middle, inverse` for a title slide.

To add a new presentation, create both files in a new folder under `presentation/`.

### Practice assignments (`layout: practice`)
Files under `practice/` use `layout: practice` and `permalink: /practice/<N>`. They contain the exercise instructions in Markdown and link out to GitHub Classroom for student submissions.

### Layouts
- `remark.html` — Loads Remark.js from CDN and renders the slide content inside a `<textarea id="source">`. Includes a JS hack to strip unwanted leading characters Jekyll may inject.
- `practice.html` — Standard HTML page with header/footer includes.
- `default.html` — Used for general pages (e.g., `index.md`, which just `{% include_relative README.md %}`).

## Key Conventions

- **Permalinks** for presentations use the topic folder name directly (e.g., `/variables`, `/functions`), not `/presentation/variables`.
- **`{{site.baseurl}}`** must be used for all asset URLs (images, PDFs, etc.) in Markdown and HTML files.
- Image assets for a presentation live in the same folder as the presentation (e.g., `presentation/hello-world/python-book.png`).
- The `README.md` is the course homepage — it is transcluded into `index.md` via `{% include_relative README.md %}`.
- Additional practice and resources are linked from `README.md`; PDFs go in `resources/`.
- `additional-practice/` holds supplemental exercises (parciales, finals) separate from the numbered TPs.

## Local Development

Requires Jekyll. To serve locally:

```bash
bundle exec jekyll serve
```

The site will be at `http://localhost:4000/prog1/`.
