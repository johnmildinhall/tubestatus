import requests, json, inkyphat
from PIL import ImageFont

def rename(name):
	values = {"Hammersmith & City":"H'Smth & City", "Metropolitan":"M'politan"}
	# for value in values:
	# 	if 

#function to rotate text
def draw_text(position, text, font=None, colour=inkyphat.BLACK, rotation=0):
    x, y = position
    if font is None:
        font = inkyphat.ImageFont.truetype(inkyphat.fonts.FredokaOne,12)
    w, h = font.getsize(text)
    mask = inkyphat.Image.new('1', (w, h))
    draw = inkyphat.ImageDraw.Draw(mask)
    draw.text((0, 0), text, 1, font)
    mask = mask.rotate(rotation, expand=True)
    inkyphat.paste(colour, position, mask)

url = 'https://api.tfl.gov.uk/line/mode/tube/status'
response = requests.get(url)
data = json.loads(response.text)
for item in data:
	print(item['name'])
	print(item['lineStatuses'][0]['statusSeverity'])

inkyphat.set_rotation(90)

top = 0
font_file = inkyphat.fonts.FredokaOne
font_size = 10
font = inkyphat.ImageFont.truetype(font_file, font_size)
text = "hello"
for i in range(0,11):
	y = (i*15) + 20
	text = data[i]['name']
	if text == "Hammersmith & City":
		text = "H'Smth & City"
	if text == "Metropolitan":
		text = "M'politan"
	if text == "Waterloo & City":
		text = "W'loo & City"
	draw_text((y, 25), text, rotation=90)
	inkyphat.ellipse([y, 5, y+12, 17], fill=None, outline=inkyphat.BLACK)
inkyphat.show()