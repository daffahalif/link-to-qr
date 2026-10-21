"""Generate a QR code PNG that opens a given link/URL.

Usage:
    python qr.py <url> [-o OUTPUT]
"""

import argparse
import sys

import qrcode


def main():
    parser = argparse.ArgumentParser(description="Generate a QR code PNG that opens a given link/URL.")
    parser.add_argument("url", help="The URL to encode in the QR code")
    parser.add_argument("-o", "--output", default="qrcode.png", help="Output PNG file (default: qrcode.png)")
    args = parser.parse_args()

    if not args.url.strip():
        parser.error("URL must not be empty")

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(args.url)
    try:
        qr.make(fit=True)
        img = qr.make_image()
        img.save(args.output)
    except (qrcode.exceptions.DataOverflowError, ValueError) as exc:
        print(f"URL is too long to encode in a QR code (max ~2,331 bytes): {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Saved QR code to {args.output}")


if __name__ == "__main__":
    main()
