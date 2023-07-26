from PIL import Image


def image_to_symbols(image_name):
    def separate(pixel):
        global separator
        for i in range(len(separator)):
            if separator[i] <= pixel[0] <= separator[i + 1]:
                return list_of_symbols[i]
    image = Image.open(image_name)
    list_of_pixels = list(image.getdata())
    list_of_symbols = [".", ",", "'", "+", "*", "~", "=", "!", "/", "?", "%", "$", "#", "&", "@"]
    symbol_image = [[]]

    separator = [int(i * (256 / len(list_of_symbols))) for i in range(len(list_of_symbols) + 1)]

    cur_line = 0

    for pixel in list_of_pixels:
        if len(symbol_image[cur_line]) == image.width:
            cur_line += 1
            symbol_image.append([])
        symbol_image[cur_line].append(separate(pixel))

    for line in symbol_image:
        for pixel in line:
            print(pixel, end="")
        print()


def rotate_90_to_left(image_name):
    image = Image.open(image_name)
    image = image.rotate(90)
    image.show()


rotate_90_to_left("image.jpg")