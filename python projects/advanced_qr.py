import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=50, border=4)

qr.add_data("https://www.youtube.com")
qr.make(fit=True)
img=qr.make_image(fill_color="#fad02c", back_color="#333652")
img.save("youtube.png")