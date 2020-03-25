import random
from PIL import Image, ImageDraw, ImageFont

#create text tilted at 7 degre

label = 'Hellq!' 
font = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 36)
line_height = sum(font.getmetrics())
fontimage = Image.new('L', (font.getsize(label)[0], line_height))
ImageDraw.Draw(fontimage).text((0, 0), label, fill=255, font=font)
fontimage = fontimage.rotate(7, resample=Image.BICUBIC, expand=True)

final = Image.new('L',(fontimage.size[0],fontimage.size[1]), color = 'white')
final.paste("black", box=(0, 0), mask=fontimage)


# add noise to the text
length = fontimage.size[1]
height = fontimage.size[0]

number_of_pixels = length * height
pixels = final.load()

noise_factor = int(0.3*(number_of_pixels))

for i in range(noise_factor):
    x= int(random.uniform(0, height))
    y= int(random.uniform(0, length))
    random.seed(int(random.uniform(0, number_of_pixels)))
    pixels[x,y] = 0


final.save("test.png")