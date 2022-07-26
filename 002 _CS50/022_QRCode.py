import os 
import qrcode

img = qrcode.make("https://hamzoooz.wordpress.com")

img.save("qr-png", "PNG")

os.system("qr.png")

