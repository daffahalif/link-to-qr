# Changelog

## [1.0.0] - 2026-10-21
### Added
- CLI QR generator: `python qr.py <url> [-o output.png]` encodes any URL/link into a PNG QR code (qrcode 8.2).
### Fixed
- Catch `ValueError` from qrcode 8.2 for overlong URLs; friendly error instead of traceback.
