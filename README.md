# QR Code Generator

This Python script generates high-quality QR codes with optional customization, including custom colors, embedded logos, and additional text.

## Features
- Custom QR code colors (foreground and background)
- High error correction for better readability
- Option to embed a logo in the center
- Ability to add text in the center or corners
- Saves as a high-quality PNG image

## Requirements
Ensure you have Python installed along with the following dependencies:

```bash
pip install qrcode[pil] pillow
```

## Usage
Run the script with customized parameters:

```python
from qr_code_generator import generate_qr_code

generate_qr_code(
    data="https://spintegration.fi/",
    filename="spintegration_qr_with_text.png",
    fill_color="#8b43c9",  # Custom QR code color
    back_color="white",  # Background color
    logo_path=None,  # Add a logo by providing a file path (e.g., "logo.png")
    text="SPI",  # Text to display on the QR code
    position="center"  # Choose text position: "center" or "corner"
)
```

## Function Descriptions

### `generate_qr_code(data, filename, fill_color, back_color, logo_path, text, position)`
Generates a QR code with optional customization.

- `data`: The URL or text to encode.
- `filename`: Output filename (default: `qr_code.png`).
- `fill_color`: Color of the QR code (default: `#8b43c9`).
- `back_color`: Background color (default: `white`).
- `logo_path`: Path to an optional logo to embed in the center.
- `text`: Text to add to the QR code (default: `SPI`).
- `position`: Position of the text (`"center"` or `"corner"`).

### `add_logo_to_qr(qr_image, logo_path)`
Embeds a logo in the center of the QR code.

### `add_text_to_qr(qr_image, text, position)`
Adds text to the QR code in either the center or corner.

## Output
The generated QR code will be saved as a high-quality PNG file with the specified filename.

## License
This project is licensed under the MIT License.

