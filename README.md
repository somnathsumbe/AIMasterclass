# AI Masterclass

A personal AI learning library built with HTML5, Tailwind CSS, custom CSS, JavaScript ES6 and independent JSON files.

## Features

- Dashboard with tool cards and list view
- Search by tool name, class title and category
- Lecture-date filter and ascending/descending sorting
- Independent JSON file for every AI tool
- Tool detail view with information, usage and practical examples
- One-question-at-a-time Q&A navigation
- Completed class tracking with browser LocalStorage
- Light and dark themes
- Responsive desktop and mobile layout

## Included sample data

The starter library contains 5 AI tools and 20 general Q&A items per tool (100 questions total):
1. ChatGPT
2. Google Gemini
3. Perplexity
4. Claude
5. Microsoft Copilot

## Run locally

The app works both from a local server and by opening `index.html` directly. Direct `file://` use reads a generated offline data bundle, because browsers block fetching JSON files from local pages.

When you change `data/manifest.json` or any file in `data/tools/`, regenerate the bundle:

```bash
python scripts/build_offline_data.py
```

### VS Code
1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Install the **Live Server** extension.
4. Right-click `index.html` and choose **Open with Live Server**.

Alternatively, run a local static server from the project root:

```bash
python -m http.server 5500
```

Then open http://localhost:5500.

## Add a new tool

1. Create a new JSON file inside `data/tools/`.
2. Follow the schema used by the existing tool JSON files.
3. Add its metadata and relative JSON path to `data/manifest.json`.
4. Refresh the dashboard.

## Data and privacy

- Learning completion and theme preference are stored in the current browser's LocalStorage.
- Tool content is stored as static JSON files in this repository.
- No login, backend, analytics or remote database is included.

## Tailwind CSS note

This starter uses the Tailwind Play CDN for quick setup and easy local testing. The Play CDN is intended for development/prototyping. Before a production release, migrate to Tailwind CLI or a standard build pipeline and generate a minimized CSS file.

## Current scope

Certificate PDF links are supported by the JSON schema but are empty in the sample records until actual certificates are provided.
