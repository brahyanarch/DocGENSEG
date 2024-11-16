import qrcode

# URL que deseas convertir en QR
url = "https://drive.google.com/drive/folders/1baE2XW6uUVQhxcJ8fbgSLge_h6wuxwSy?usp=drive_link"

# Genera el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Crea la imagen del QR
img = qr.make_image(fill='black', back_color='white')

# Guarda la imagen del QR
img.save("qr_code.png")
