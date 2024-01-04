# Creating QR code using module
import qrcode as qr  # Acessing QRCode function from qrcode module 
Qr = qr.QRCode(version = 1, error_correction = qr.constants.ERROR_CORRECT_H, box_size = 10, border = 4)


Qr.add_data("https://chat.openai.com/") # link behind the code 
Qr.make(fit = True)

view = Qr.make_image(fill_color = "blue", back_color = "yellow") # setting color to the qrcode

view.save("ChatGPT.png") # save the file in png format

import inspect 
import fraction

source = inspect.getsource(fraction)
print(source)
