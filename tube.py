import requests, json, inkyphat, time, pytz, threading
from datetime import datetime, timedelta
from PIL import ImageFont
from pytz import timezone

# to do - finish this function
def rename(name):
	values = {"Hammersmith & City":"H'Smth & City", "Metropolitan":"M'politan", "Waterloo & City":"W'loo & City"}
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

#main update routine
def updateTube():
  threading.Timer(90, updateTube).start()
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

  top = 0

  #loop through each tube line
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
    if data[i]['lineStatuses'][0]['statusSeverity'] < 8 :
      inkyphat.ellipse([y, 5, y+10, 15], fill=inkyphat.RED, outline=inkyphat.BLACK)
    if data[i]['lineStatuses'][0]['statusSeverity'] > 7 and data[i]['lineStatuses'][0]['statusSeverity'] < 10:
      inkyphat.ellipse([y, 5, y+10, 15], fill=None, outline=inkyphat.BLACK)
      inkyphat.ellipse([y+3, 8, y+7, 13], fill=inkyphat.BLACK, outline=inkyphat.BLACK)
    if data[i]['lineStatuses'][0]['statusSeverity'] == 10:
      inkyphat.ellipse([y, 5, y+10, 15], fill=None, outline=inkyphat.BLACK)

   

  utc = datetime.now() + timedelta(hours=1)
  bst = pytz.timezone('Europe/London')
  fmt = '%H:%M %d/%m/%y'
  time = bst.localize(utc).strftime(fmt)

  # timestamp
  print(time)
  inkyphat.rectangle([191,0,213,131], fill=inkyphat.BLACK, outline=inkyphat.BLACK)
  draw_text((196, 6), time, colour=inkyphat.WHITE, rotation=90, size=16)
  	
  # write to inkyphat 
  inkyphat.show()

updateTube()