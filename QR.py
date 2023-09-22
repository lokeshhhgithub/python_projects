import qrcode
from PIL import Image

qr = qrcode.QRCode( version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 15, border = 4,
                   )

qr.add_data('https://www.facebook.com/lokesh.dhakal.969')
qr.make(fit = True)
image = qr.make_image(fill_color = 'red', back_color = 'white')
image.save('LokeshFacebook.png')



