from pyzbar.pyzbar import decode
from PIL import Image

image = Image.open('qrcode.png')

result = decode(image)

print(f"Data in QR Code is: {result[0].data}")

