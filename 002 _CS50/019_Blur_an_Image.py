# # This Need Internet To Download Lip PIL IN CMD => pip install pillow
# # Fix The Path
from PIL import Image, ImageFilter

before   = Image.open("D:\Programming\learn\#006_python\#002 _CS50\Images\Data_Types_In_Python_2.jpg")
before.show()
after   =  before.filter(ImageFilter.BoxBlur(20))
after.show()
# after.save("../Images/out.tmp")
