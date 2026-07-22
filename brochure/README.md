# Booth brochure

A print-ready **A4** one-page brochure for the Iceberg booth, in Spanish, with the
QR code linking to **iceberg-refrigeration.com** ("Escanea el código y visita
nuestro sitio web").

## Files

| File | Use |
|------|-----|
| `iceberg-brochure.pdf` | **Print this.** True A4 (210 × 297 mm), vector text + QR, brand fonts embedded |
| `iceberg-brochure.png` | 2479 × 3508 px @ 300 DPI — for email, screens, or printers that want an image |
| `brochure.html` | The editable source (fully self-contained: fonts, logo, and QR are embedded) |

## What's on it

- Iceberg logo + `iceberg-refrigeration.com`
- Headline: refrigeración comercial e industrial para Latinoamérica y el Caribe
- Trust line: exclusivos de Keeprite · +32 países · +500 proyectos
- Product lines (with specs): unidades condensadoras (1–100 H.P), evaporadores
  (bajo/medio/alto perfil), chillers, compresores (1/3–150 H.P, nuevos
  semiherméticos y scroll + repuestos), máquinas de hielo (60–40,000 lb/24 h)
- QR panel: "Escanea el código y visita nuestro sitio web" + value props
- Footer: WhatsApp, teléfono, email

## Editing the text

Open `brochure.html`, edit the copy, then re-export the PDF:

```bash
chromium --headless --print-to-pdf=iceberg-brochure.pdf --no-pdf-header-footer brochure.html
```

(Any Chromium/Chrome works. The file is self-contained, so it prints identically
on any machine — no internet or fonts needed.)

## Printing notes

- Print at **100% / actual size** (do not "fit to page").
- White paper, color. Matte or gloss both fine for a handout.
- The footer bar reaches the bottom edge; if a commercial printer trims to the
  edge, ask for a 3 mm bleed or print with a small border.
