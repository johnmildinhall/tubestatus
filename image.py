from PIL import ImageFont, Image, ImageDraw
update = Image.new('RGBA', (131, 210))
draw = ImageDraw.Draw(update)
draw.ellipse([0, 0,20,20], fill='blue', outline='red')
update.save('test.png')
