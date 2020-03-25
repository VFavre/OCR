from PIL import Image, ImageDraw, ImageFont

label = 'Hellq!' 
font = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 36)
line_height = sum(font.getmetrics())
fontimage = Image.new('L', (font.getsize(label)[0], line_height))
ImageDraw.Draw(fontimage).text((0, 0), label, fill=255, font=font)
fontimage = fontimage.rotate(7, resample=Image.BICUBIC, expand=True)

orig = Image.new('L',(fontimage.size[0],fontimage.size[1]), color = 'white')
orig.paste("black", box=(0, 0), mask=fontimage)
orig.save("test.png")