# Grenton demo (SmartSpace)

Informational demo microsite for Grenton smart-home products, presented by
SmartSpace — the official Grenton representative in Moldova. RO/RU/EN.

Not an independent brand site: product photos belong to Grenton sp. z o.o.,
used here as an authorized dealer showcase.

## Structure

- `/ro/`, `/ru/`, `/en/` — language variants (home, system, control, sensors, contact)
- `assets/` — shared CSS + product images
- `scripts/build.py` — regenerates all HTML pages from the content dicts in the script

## Build

```
python scripts/build.py
```

Share cards (`assets/og/og-{grenton,lagmar}-{ro,ru,en}.jpg`, 1200×630) are rendered
separately and referenced by `build.py`; re-run after changing card text:

```
node scripts/og_cards.mjs   # needs Playwright (PLAYWRIGHT_PATH=<global node_modules>/playwright) + ImageMagick
```

Font: Manrope is self-hosted from `assets/fonts/` (SIL OFL 1.1, see `assets/fonts/OFL.txt`) —
no requests to Google Fonts.

## Deploy

Served via GitHub Pages from the `main` branch root.
