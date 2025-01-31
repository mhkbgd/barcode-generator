import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_qr_code(data, filename="qr_code.png", fill_color="#8b43c9", back_color="white", logo_path=None, text="SPI", position="center"):
    """
    Generates a high-quality QR code with optional logo, custom colors, and text in the corners or center.

    :param data: The URL or text to encode
    :param filename: Output filename (default: "qr_code.png")
    :param fill_color: QR code color (default: "#8b43c9")
    :param back_color: Background color (default: "white")
    :param logo_path: Path to an optional logo to embed in the center of the QR code
    :param text: Text to add to the QR code (default: "SPI")
    :param position: Position of the text ("center" or "corner")
    """
    try:
        # Create a QR Code instance with better quality
        qr = qrcode.QRCode(
            version=6,  # Higher version for larger QR code (higher = bigger)
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for better readability
            box_size=15,  # Larger box size for better resolution
            border=6,  # Larger border
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create a high-quality QR code image
        qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)

        # If a logo is provided, embed it in the QR code
        if logo_path:
            qr_image = add_logo_to_qr(qr_image, logo_path)

        # Add text (SPI) to the QR code
        # qr_image = add_text_to_qr(qr_image, text, position)

        # Save the QR code image
        qr_image.save(filename, quality=95)  # Save with high quality
        print(f"✅ QR code successfully saved as '{filename}'. Scan it with your phone!")

    except Exception as e:
        print(f"❌ Error generating QR code: {e}")

def add_logo_to_qr(qr_image, logo_path):
    """
    Embeds a logo in the center of the QR code.

    :param qr_image: The generated QR code image
    :param logo_path: Path to the logo image
    :return: QR code with embedded logo
    """
    try:
        logo = Image.open(logo_path)
        
        # Resize the logo dynamically based on the QR code size
        qr_width, qr_height = qr_image.size
        logo_size = qr_width // 5  # The logo will take up 1/5 of the QR code
        logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

        # Calculate position for centering the logo
        pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        qr_image.paste(logo, pos, mask=logo.convert("RGBA"))  # Paste logo with transparency

        return qr_image

    except Exception as e:
        print(f"❌ Error adding logo: {e}")
        return qr_image  # Return original QR code if logo fails

def add_text_to_qr(qr_image, text, position="center"):
    """
    Adds text (e.g., "SPI") to the QR code.

    :param qr_image: The generated QR code image
    :param text: The text to add (default: "SPI")
    :param position: Position of the text ("center" or "corner")
    :return: QR code with embedded text
    """
    try:
        # Get QR code size
        qr_width, qr_height = qr_image.size

        # Prepare text
        draw = ImageDraw.Draw(qr_image)

        # Try loading a larger font if available
        try:
            font = ImageFont.truetype("arial.ttf", size=200)  # Use a larger font (size 200)
        except IOError:
            font = ImageFont.load_default()  # Fall back to default font if the custom font is not available

        # Calculate the size of the text using textbbox
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Positioning text
        if position == "center":
            position = ((qr_width - text_width) // 2, (qr_height - text_height) // 2)
        elif position == "corner":
            # Position the text in the top-left corner
            position = (5, 5)

        # Add text to the QR code
        draw.text(position, text, font=font, fill="black")

        return qr_image

    except Exception as e:
        print(f"❌ Error adding text: {e}")
        return qr_image

# Example usage:
generate_qr_code(
    data="https://spintegration.fi/",
    filename="spintegration_qr_with_text.png",
    fill_color="#8b43c9",  # Custom color for QR code
    back_color="white",  # Change background color
    logo_path=None,  # Add a logo by providing a file path (e.g., "logo.png")
    text="SPI",  # Text to display on the QR code
    position="center"  # Choose text position: "center" or "corner"
)
