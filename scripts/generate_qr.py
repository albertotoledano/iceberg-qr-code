#!/usr/bin/env python3
"""Regenerate the Iceberg Refrigeration QR codes (PNG + SVG) from one source URL.

Usage:
    pip install "qrcode[pil]"
    python scripts/generate_qr.py
"""
import os
import qrcode
import qrcode.image.svg

URL = "https://iceberg-refrigeration.com"

# Write into ../qr relative to this script, so it works from any cwd.
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "qr")


def build(box_size=12, border=4, **kwargs):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
        **kwargs,
    )
    qr.add_data(URL)
    qr.make(fit=True)
    return qr


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    png = build().make_image(fill_color="black", back_color="white")
    png_path = os.path.join(OUT_DIR, "iceberg-qr.png")
    png.save(png_path)

    svg = build(image_factory=qrcode.image.svg.SvgPathImage).make_image()
    svg_path = os.path.join(OUT_DIR, "iceberg-qr.svg")
    svg.save(svg_path)

    # Print-ready raster: ~15 cm at 300 DPI, DPI metadata embedded so it
    # drops into a layout at the correct physical size. Vector SVG is still
    # the preferred master; this is a fallback for raster-only workflows.
    print_png = build(box_size=48, border=4).make_image(
        fill_color="black", back_color="white"
    )
    print_path = os.path.join(OUT_DIR, "iceberg-qr-print-15cm-300dpi.png")
    print_png.save(print_path, dpi=(300, 300))

    print(f"Wrote {png_path}")
    print(f"Wrote {svg_path}")
    print(f"Wrote {print_path} ({print_png.size[0]}px @ 300 DPI)")
    print(f"All encode: {URL}")


if __name__ == "__main__":
    main()
