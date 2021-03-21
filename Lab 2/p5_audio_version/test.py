from p5 import *
import time
import datetime 
from datetime import datetime
from time import strftime, sleep
# import astropy.coordinates as coord
# from astropy.time import Time
# import astropy.units as u
from boundary import Boundary
from particle import Particle
from pysolar.solar import *
import numpy as np

lat = 43.7128
lon = -75.006

# import digitalio
# import board
# import adafruit_rgb_display.st7789 as st7789
# import busio
# # import adafruit_apds9960.apds9960
# buttonA = digitalio.DigitalInOut(board.D23)
# buttonB = digitalio.DigitalInOut(board.D24)
# buttonA.switch_to_input()
# buttonB.switch_to_input()

# loc = coord.EarthLocation(lon=lat * u.deg,
#                           lat=lon * u.deg)

r = requests.get('https://api.sunrise-sunset.org/json', params={'lat': lat, 'lng': lon}).json()['results']

walls = []
triggered = []
width = 1200
height = 650
fontSize = 30
bg = 'black'
import speech_recognition as sr
recognizer = sr.Recognizer()



def setup():
    size(width, height)
    background(0)
    text_font(create_font('handwriting.ttf', size=fontSize))
    global particle

    while len(walls)<3:
        x1 = np.random.randint(width)
        y1 = np.random.randint(height) 
        x2 = np.random.randint(width)
        y2 = np.random.randint(height)
        d = np.sqrt((x2-x1)**2+(y2-y1)**2)
        print(d, [x1,y1,x2,y2], len(walls))
        if d < 300:
            print(d, len(walls))
            walls.append(Boundary(x1, y1, x2, y2))
    # print([(i.a, i.b) for i in walls])
    # make boundaries of edges
    walls.append(Boundary(0, 0, height, 0))
    walls.append(Boundary(height, 0, height, width))
    walls.append(Boundary(height, width, 0, height))
    walls.append(Boundary(0, width, 0, 0))

    particle = Particle()
    
def draw():
    global bg
    global triggered
    global voice_data
    
    if not (buttonB.value and buttonA.value):
        triggered.append(1)
        with sr.Microphone() as source:
            print("how are the skies today?")
            audio = recognizer.listen(source)
            voice_data = recognizer.recognize_google(audio)
            print(voice_data)

        if voice_data == "overcast":
            bg = 'gray'
        elif voice_data == "clear":
            bg = 'blue'
        else:
            bg = 'black'
    elif len(triggered) == 0:
        bg = 'black'
        voice_data = "how are the skies today?"
    
    background(bg)
    date = datetime.datetime.now(datetime.timezone.utc)
    altitude = get_altitude(lat, lon, date)

    fill('white')
    text(voice_data, 0,height-fontSize*5)
    text(strftime("%I:%M:%S")+'pm', 0,height-fontSize*4)
    text("sunrise: "+str(int(r['sunrise'][:2])-5)+r['sunrise'][2:], 0, height-fontSize*3)
    text("     set: "+str(int(r['sunset'][:2])-5)+r['sunset'][2:], 0, height-fontSize*2)
    text("     altitude: "+str(round(altitude,3)), 0,height-fontSize)

    fill('orange')
    x = width/2+altitude
    y = height-altitude*10
    

    for wall in walls:
      wall.show()
    

    particle.update(x,y)
    particle.show()
    particle.look(walls)

def key_pressed(event):
    background(0)

run()

