
# Python QR Code Generator with Logo

Generate high-quality QR codes with a centered logo while maintaining reliable scanning performance.

## Features

* Creates QR codes from any URL
* Supports custom logo embedding
* Uses high error correction (`ERROR_CORRECT_H`) for better scan reliability
* Adds a white border around the logo for improved contrast
* Generates large, high-resolution QR codes
* Uses circular QR modules for a modern appearance

## Requirements

Install the required Python packages:

```bash
pip install qrcode[pil] pillow
```

## Usage

1. Place your logo image in the project folder.
2. Update the URL and logo filename in the script.
3. Run the script:

```bash
python myqr.py
```

Example:

```python
make_qr_with_logo(
    url="https://www.linkedin.com/in/your-profile",
    logo_path="logo.png",
    output_path="my_qr.png",
)
```

## Parameters

| Parameter     | Description                                    |
| ------------- | ---------------------------------------------- |
| `url`         | URL to encode in the QR code                   |
| `logo_path`   | Path to the logo image                         |
| `output_path` | Output QR code filename                        |
| `qr_size`     | QR image size in pixels (default: 1024)        |
| `logo_scale`  | Logo size relative to QR width (default: 0.22) |

## Example Output

The generated QR code:

* Uses high error correction for improved resilience
* Places the logo in the center
* Preserves QR readability across most mobile devices

## Project Structure

```text
.
├── myqr.py
├── logo.png
├── qr_with_logo.png
└── README.md
```

## Notes

For best scanning performance:

* Keep the logo size below 25% of the QR code width.
* Use high-contrast logos when possible.
* Test the generated QR code on multiple devices before production use.
