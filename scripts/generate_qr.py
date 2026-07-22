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


def build(**kwargs):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=4,
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

    print(f"Wrote {png_path}")
    print(f"Wrote {svg_path}")
    print(f"Both encode: {URL}")


if __name__ == "__main__":
    main()
