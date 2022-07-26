# from  PIL import Image

# # # Open The Image 
# myImage = Image.open("D:\Programming\learn\#006_python\#001_Osama_Elzero\Buga.jpg")

# # # Show The Image  
# # myImage.show()
# # #############################################
# # Cropped Image 
# myNewImage = myImage.crop((400, 200, 420, 400 ))

# # # Show The Image  After Croped 
# # myNewImage.show()

# # #############################################
# # Converted Image 
# myConverted = myImage.converted("L")

# # # Show The Image  After Converted 
# myConverted.show()

# # #############################################
# Rotate Image 
from PIL import Image
with Image.open("D:\Programming\learn\#006_python\#001_Osama_Elzero\Buga.jpg") as im:
    im.rotate(45).show()


from PIL import Image, ImageFilter

before   = Image.open("D:\Programming\learn\#006_python\#002 _CS50\Images\Data_Types_In_Python_2.jpg")
before.show()
after   =  before.filter(ImageFilter.BoxBlur(20))
after.show()
# after.save("../Images/out.tmp")
