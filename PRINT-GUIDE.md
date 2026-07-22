# Roll-up banner — QR print & placement guide

For a standard vertical **roll-up / retractable banner (85 × 200 cm)**.
The placement rules hold for other roll-up widths (80/100/120 cm) too.

## Files to hand the printer

- **`qr/iceberg-qr.svg`** — the master. Vector, scales with zero quality loss.
  This is what the designer should place.
- **`qr/iceberg-qr-print-15cm-300dpi.png`** — 15 cm @ 300 DPI fallback for
  raster-only workflows. Do **not** scale it up beyond 15 cm.

All files encode: **https://iceberg-refrigeration.com**

## Size on the banner

- **Make the QR ~12–15 cm square.** People scan a roll-up from ~1–1.5 m, so
  10 cm is the floor; 15 cm gives comfortable margin. The 15 cm print file is
  sized for exactly this.

## Placement (the roll-up-specific part)

A roll-up is tall and its ends are unusable — plan around that:

```
 top of banner
 ┌───────────────┐   ← top ~15 cm: hard to scan (too high), keep for logo/headline
 │   LOGO / H1   │
 │               │
 │   product     │
 │   imagery     │
 │               │
 │  ┌─────────┐  │   ← QR sits here: roughly 100–140 cm from the floor
 │  │   QR    │  │      (comfortable eye-to-waist height to scan)
 │  │ 12-15cm │  │
 │  └─────────┘  │
 │ iceberg-      │   ← print the URL as text under the QR (fallback + branding)
 │ refrigeration │
 │  .com         │
 └───────────────┘
 ↑ bottom ~15–20 cm rolls into the base cassette — put NOTHING important here
```

- **Vertical position:** center the QR around **100–140 cm from the floor** —
  the natural height to raise a phone to. Never in the bottom 15–20 cm.
- **Side margins:** keep the QR (and its white border) **≥ 3 cm** from the
  banner edges.

## Non-negotiables for a scannable code

- **Keep the white quiet zone** around the code — don't crop it or let
  artwork/text run into it.
- **Pure black on white/light:** CMYK **0/0/0/100** for the dark modules
  (not "rich black"). No gradients, no photo behind the code, no logo dropped
  in the center unless we regenerate it for that.
- **Strong contrast:** dark code on a light patch. If the banner is dark,
  place the QR on a white rounded panel.
- **Matte finish, not gloss** — gloss glare under lights defeats scanning.

## Before the full run

Print (or tape the SVG at final size) and **scan with 2–3 different phones**.
Confirm it opens https://iceberg-refrigeration.com, then approve the run.

## Regenerating (e.g. if the URL changes)

```bash
pip install "qrcode[pil]"
python scripts/generate_qr.py
```

Edit `URL` in `scripts/generate_qr.py` first if the destination changes.
