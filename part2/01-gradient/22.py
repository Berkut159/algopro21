# придумаем градиентную заливку

from PIL import Image

img = Image.open("./images/white.jpg")
width, height = img.size
ky = 256 / height
kx = 256 / width

for y in range(height):
    for x in range(width):
        pos = abs(n-1-(x+y)),end = "")
        r = 127 - int(pos*ky/2)
        g = 255 - int(pos*ky)
        b = int(pos*ky)
        img.putpixel((x, y), (r, g, b))

img.save('./gradients/_' + '97.jpg')
img.show()
