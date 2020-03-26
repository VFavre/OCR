import random
from PIL import Image, ImageDraw, ImageFont

#change the value of the next variable to cgange the maximum value of the backgroudn noise (from 0 to 255 with 
# 255 = white and 0 = black)

backgound_noise = 215

#change the next variable to change the amount of black noise (from 0 to 1 correspond to a % of the amount of
# pixel in the image that will be noise )

text_noise = 0.1





#create text tilted at between 7 and -7 degre
label = 'Hellq!' 
font = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 36)
line_height = sum(font.getmetrics())
fontimage = Image.new('L', (font.getsize(label)[0], line_height))
ImageDraw.Draw(fontimage).text((0, 0), label, fill=255, font=font)
fontimage = fontimage.rotate(random.uniform(-7, 7), resample=Image.BICUBIC, expand=True)


final = Image.new('L',(fontimage.size[0],fontimage.size[1]), color = 'white')

pixels = final.load()
length = fontimage.size[1]
height = fontimage.size[0]


for i in range(height):
    for j in range(length):
        pixels[i,j] = random.randint(backgound_noise, 255)
        

final.paste("black", box=(0, 0), mask=fontimage)


# add noise to the text

number_of_pixels = length * height
pixels = final.load()


noise_factor = int(text_noise*(number_of_pixels))

for i in range(noise_factor):
    x= int(random.uniform(0, height))
    y= int(random.uniform(0, length))
    random.seed(int(random.uniform(0, number_of_pixels)))
    pixels[x,y] = 0


final.save("test.png")