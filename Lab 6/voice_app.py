import digitalio
import board
import adafruit_rgb_display.st7789 as st7789
import busio
import paho.mqtt.client as mqtt
import uuid
from PIL import Image, ImageDraw, ImageFont
import time
client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd','device@theFarm')

client.connect('farlab.infosci.cornell.edu', port = 8883)

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
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
height = disp.height  # we swap height/width to rotate it to landscape!
width = disp.width
image = Image.new("RGB", (width, height))
rotation = 0

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
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

while True:
    draw.rectangle((0, 0, width, height), outline='black', fill=(0,0,0,100))

    #TODO: fill in here. You should be able to look in cli_clock.py and stats.py 
    draw.multiline_text((10,10), "hello"+"\n"+"test", fill=(255,255,255))
    disp.image(image, rotation)
    image.show()
    time.sleep(1)
    topic = "IDD/voice"
    def on_connect(client, userdata, flags, rc):
        client.subscribe(topic)
    def on_message(client, userdata, msg):
        print(msg.payload.decode('UTF-8'))
    client = mqtt.Client(str(uuid.uuid1()))
    client.tls_set()
    client.username_pw_set
    if not buttonA.value:
        val = "button"
        client.publish(topic,val)
    if not buttonB.value:
        

# end
