form PIL import Image

import face_recognition

Image = face_recognition.load_image_file("../Images/Data_Types_In_Python_2.jpg")

face_locations = face_recognition.face_loactions(Image)

for face_location in face_locations:
    face_image = image[top:bottom, left:right]
    pil_image = Image.formarray(face_image)
    pil_image.show()





 