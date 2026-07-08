import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer
from PIL import Image

def make_qr_with_logo(
    url: str,
    logo_path: str,
    output_path: str = "qr_with_logo.png",
    qr_size: int = 1024,
    logo_scale: float = 0.22,  # 22% of QR width — keeps error correction margin safe
):
    """
    Generate a QR code with a centered logo that actually scans.

    Key rules for reliable scanning:
    - Use ERROR_CORRECT_H (~30% recovery) so the logo doesn't break decoding
    - Keep the logo ≤ 25% of the QR width
    - Add a white border around the logo for contrast
    """

    # 1. Build the QR code with HIGH error correction
    qr = qrcode.QRCode(
        version=None,               # auto-fit version
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=4,                   # standard quiet zone
    )
    qr.add_data(url)
    qr.make(fit=True)

    # 2. Render as a clean, sharp image
    qr_img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=CircleModuleDrawer(),   # rounded dots — modern look, still scannable
        fill_color="black",
        back_color="white",
    ).convert("RGBA")

    qr_img = qr_img.resize((qr_size, qr_size), Image.LANCZOS)

    # 3. Load and resize the logo
    logo = Image.open(logo_path).convert("RGBA")
    logo_w = int(qr_size * logo_scale)
    logo_h = int(logo_w * logo.height / logo.width)
    logo = logo.resize((logo_w, logo_h), Image.LANCZOS)

    # 4. Add a white padding border around the logo (improves contrast)
    padding = 8
    padded_size = (logo_w + 2 * padding, logo_h + 2 * padding)
    padded_logo = Image.new("RGBA", padded_size, (255, 255, 255, 255))
    padded_logo.paste(logo, (padding, padding), logo)

    # 5. Center the padded logo on the QR code
    x = (qr_size - padded_size[0]) // 2
    y = (qr_size - padded_size[1]) // 2
    qr_img.paste(padded_logo, (x, y), padded_logo)

    qr_img.save(output_path)
    print(f"QR code saved -> {output_path}")
    print(f"   URL:        {url}")
    print(f"   QR size:    {qr_size}×{qr_size}px")
    print(f"   Logo cover: ~{logo_scale * 100:.0f}% of QR area")
    print(f"   Tip: test with multiple phones / lighting conditions!")


if __name__ == "__main__":
    make_qr_with_logo(
        url="https://www.linkedin.com/in/xueyi-wang-00ab11195/",
        logo_path="Yourphoto.png",
        output_path="qr_instagram.png",
    )
