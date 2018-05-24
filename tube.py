import requests, json, inkyphat
from PIL import ImageFont

url = 'https://api.tfl.gov.uk/line/mode/tube/status'
response = requests.get(url)
data = json.loads(response.text)
for item in data:
	print(item['name'])
	print(item['lineStatuses'][0]['statusSeverity'])

top = 0
font_file = inkyphat.fonts.FredokaOne
font_size = 10
font = inkyphat.ImageFont.truetype(font_file, font_size)
text = "hello"
inkyphat.text((0, top), text, 2, font=font)
inkyphat.show()