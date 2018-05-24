import requests, json, inkyphat
from PIL import ImageFont

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
draw_text((20, 20), text, rotation=90)
inkyphat.show()