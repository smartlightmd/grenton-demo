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

## Deploy

Served via GitHub Pages from the `main` branch root.
