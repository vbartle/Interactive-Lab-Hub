import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
import datetime
from suntime import Sun, SunTimeException

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

lat = 43.7128
lon = -75.006
sun = Sun(lat,lon)
today_sr = sun.get_local_sunrise_time()
today_ss = sun.get_local_sunset_time()

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline='black', fill=(0,0,0,100))

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py 
    draw.multiline_text((10,10), strftime("%m/%d/%Y")+"\n"+strftime("%I:%M:%S"), font=font, fill=(255,255,255))
    draw.text((10,60), "sunrise: "+today_sr.strftime('%I:%M'), font=font, fill=(255,255,255))
    # Display image.
    draw.text((10,80), "sunset: "+today_ss.strftime('%I:%M'), font=font, fill=(255,255,255))
    disp.image(image, rotation)
    image.show()
    time.sleep(1)
