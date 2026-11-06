# campaha.org

Static site for CAMP AHA, served by Netlify (project `campaha`). Every push to `main` deploys to production.

## Layout

- `site/` is exactly what visitors get. Netlify publishes this folder only.
- `tools/prep.py` turns a raw Claude Design export into a launch-ready build.
- `tools/og.py` renders the 1200x630 share image (`site/img/og-image.jpg`).

## Updating the site

1. Edit in Claude Design and export the zip to Downloads.
2. Unzip it, then run the prep step on the export:
   `npm i @fontsource/be-vietnam-pro @fontsource/permanent-marker` in a scratch folder, then
   `python3 -I tools/prep.py <export_dir> <scratch>/node_modules`
3. Copy `site/img/og-image.jpg` back in (the prep step makes a plain placeholder; the branded card comes from `tools/og.py`).
4. Replace the contents of `site/` with the prepped export, commit, and push to `main`.

## What the prep step adds

Design exports always link Google Fonts and leave out the launch layer, so prep must run on every export:

- Fonts self-hosted in `site/fonts/` (no third-party loads before a click)
- Per-page titles, descriptions, canonical URLs, Open Graph and Twitter tags
- `privacy-policy.html` and a footer link to it on every page
- A branded `404.html` with noindex
- `robots.txt`, `sitemap.xml`
- `_redirects`: www to apex, the two old WordPress feedback pages to `/impact`, real 404s

## DNS

campaha.org DNS lives at Nexcess. Only the A record (75.2.60.5) and `www` CNAME (campaha.netlify.app) point at Netlify. MX, SPF, DKIM, MailerLite and Brevo records stay as they are.
