from PIL import Image

image = Image.open("image.jpg")
list_of_pixels = list(image.getdata())