import qrcode

class QRCodeGenerator:
    """Generates QR codes from URLs."""

    def __init__(self, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, fill_color="black", back_color="white"):
        """
        Initializes the QRCodeGenerator object with default or custom parameters.

        Args:
            version (int, optional): Controls the size of the QR code (1-40). Defaults to 1.
            error_correction (int, optional): Sets the error correction level. Defaults to qrcode.constants.ERROR_CORRECT_L.
            box_size (int, optional): Controls the size of each box in the QR code. Defaults to 10.
            border (int, optional): Sets the width of the border around the QR code. Defaults to 4.
            fill_color (str, optional): Color of the QR code modules. Defaults to "black".
            back_color (str, optional): Background color of the QR code. Defaults to "white".
        """
        self.version = version
        self.error_correction = error_correction
        self.box_size = box_size
        self.border = border
        self.fill_color = fill_color
        self.back_color = back_color
        self.qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border,
        )

    def generate(self, url, filename="qrcode.png"):
        """
        Generates a QR code for the given URL and saves it as a PNG image.

        Args:
            url (str): The URL to encode in the QR code.
            filename (str, optional): The name of the file to save the QR code image to. Defaults to "qrcode.png".
        """
        self.qr.clear()  # Clear previous data if any
        self.qr.add_data(url)
        self.qr.make(fit=True)

        img = self.qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
        img.save(filename)

        print(f"QR code saved as {filename}")

# Example usage:
url_to_encode = "https://www.deeplearning.ai/courses/"
qr_generator = QRCodeGenerator()
qr_generator.generate(url_to_encode, filename="deeplearning_ai_qr.png")

# You can also create a generator with custom parameters:
custom_qr_generator = QRCodeGenerator(version=5, box_size=12, fill_color="darkblue", back_color="lightyellow")
custom_qr_generator.generate("https://www.python.org/", filename="python_qr_custom.png")