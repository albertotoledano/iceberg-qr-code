# iceberg-qr-code

QR code assets for **Iceberg Refrigeration**, linking to
[https://iceberg-refrigeration.com](https://iceberg-refrigeration.com).

This repo is intentionally separate from the marketing site / landing-page
repos so QR and print assets stay cleanly tracked on their own.

## Contents

| Path | What it is |
|------|------------|
| `qr/iceberg-qr.png` | Raster QR code (444×444 px) — use for screens, email, slides |
| `qr/iceberg-qr.svg` | Vector QR code — use for print / large format (scales with no quality loss) |
| `scripts/generate_qr.py` | Regenerates the QR codes from a single source URL |

## The URL

The QR code points to: `https://iceberg-refrigeration.com`

To change the destination, edit `URL` in `scripts/generate_qr.py` and rerun it.

## Regenerating the QR code

```bash
pip install "qrcode[pil]"
python scripts/generate_qr.py
```

This rewrites both `qr/iceberg-qr.png` and `qr/iceberg-qr.svg`.

## Usage tips

- **Print:** always use the SVG so it stays sharp at any size.
- **Minimum size:** keep it at least ~2 cm × 2 cm on print so phones scan reliably.
- **Quiet zone:** don't crop the white border — scanners need it.
- **Test before you print** a batch: scan it with a couple of phones first.
