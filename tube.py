import requests, json, inkyphat, datetime, time
from PIL import ImageFont, Image, ImageDraw

def rename(name):
	values = {"Hammersmith & City":"H'Smth & City", "Metropolitan":"M'politan"}
	# for value in values:
	# 	if 

#function to rotate text
def draw_text(position, text, font=1, colour=inkyphat.BLACK, rotation=0, size=16):
    x, y = position
    if font == 1:
      font = ImageFont.truetype("/home/pi/tubestatus/BetterPixels.ttf", size)
    else:
      font = ImageFont.truetype("/home/pi/tubestatus/Extrude.ttf", size)
      # font = inkyphat.ImageFont.truetype(inkyphat.fonts.FredokaOne,size)
    w, h = font.getsize(text)
    mask = inkyphat.Image.new('1', (w, h))
    draw = inkyphat.ImageDraw.Draw(mask)
    draw.text((0, 0), text, 1, font)
    mask = mask.rotate(rotation, expand=True)
    inkyphat.paste(colour, position, mask)


# Get tube data
url = 'https://api.tfl.gov.uk/line/mode/tube/status'
response = requests.get(url)
data = json.loads(response.text)
for item in data:
	print(item['name'])
	print(item['lineStatuses'][0]['statusSeverity'])

# draw header
inkyphat.rectangle([0,0,19,131], fill=inkyphat.BLACK, outline=inkyphat.BLACK)
draw_text((2, 9), "tubetron", font=2, colour=inkyphat.WHITE, rotation=90, size=18)

# draw footer
inkyphat.rectangle([191,0,213,131], fill=inkyphat.BLACK, outline=inkyphat.BLACK)

top = 0
font_file = inkyphat.fonts.FredokaOne
font_size = 10
font = inkyphat.ImageFont.truetype(font_file, font_size)
for i in range(0,11):
	y = (i*15) + 25
	text = data[i]['name']
	if text == "Hammersmith & City":
		text = "H'Smth & City"
	if text == "Metropolitan":
		text = "M'politan"
	if text == "Waterloo & City":
		text = "W'loo & City"
	draw_text((y, 23), text, rotation=90)

inkyphat.show()

#repeating steps
update = Image.new('RGBA', (inkyphat.WIDTH, inkyphat.HEIGHT))
draw = ImageDraw.Draw(update)
print(inkyphat.WIDTH, inkyphat.HEIGHT)
draw.ellipse([0, 0,20,20], fill='red', outline='black')
for i in range(0,11):
  if data[i]['lineStatuses'][0]['statusSeverity'] < 10:
    draw.ellipse([y, 5, y+10, 15], fill='red', outline='black')
  else:
    draw.ellipse([y, 5, y+10, 15], fill='white', outline='black')
inkyphat.paste(update, mask=1)
# # timestamp
# st = datetime.datetime.now().strftime('%H:%M:%S %d/%m')
# 
# draw_text((197, 6), st, colour=inkyphat.WHITE, rotation=90, size=16)
	
