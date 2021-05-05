import mic_vad_streaming 
import digitalio
import board
import adafruit_rgb_display.st7789 as st7789
import busio
import paho.mqtt.client as mqtt
import uuid
from PIL import Image, ImageDraw, ImageFont
import speech_recognition as sr
import pyttsx3
from time import gmtime, strftime
import re
import time

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    print(str("test"))
    engine.runAndWait()

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
height = disp.width  # we swap height/width to rotate it to landscape! 
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

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

curr_message = 'No messages yet.'
topic = "IDD/voice_app/1"
all_msgs = []
def on_connect(client, userdata, flags, rc):
    #client.subscribe("IDD/voice_app/"+str(arg2))
    client.subscribe("IDD/voice_app/2")
def on_message(client, userdata, msg):
    global curr_message
    curr_message = msg.payload.decode('UTF-8')
    all_msgs.append(curr_message)
    print(curr_message)

client.on_connect = on_connect
client.on_message = on_message
draw.rectangle((0, 0, width, height), outline='black', fill=(0,0,0,100))
#TODO: fill in here. You should be able to look in cli_clock.py and stats.py
fontsize = 20
font = ImageFont.truetype("garamond.ttf", fontsize)
draw.multiline_text((10,10), "No messages yet.", fill=(255,255,255), font=font)
disp.image(image, rotation)
image.show()
time.sleep(.25)
#client.loop_forever()

def run():
    while True:
        client.loop()
        if len(all_msgs)>0:
            #print(len(all_msgs))
            #print('@@@@')
            #draw.text((10,10), "Newest message preview:", fill=(255,255,255), font=font)
            draw.rectangle((0, 0, width, height), outline='black', fill=(0,0,0,100))
            for ind,i in enumerate(all_msgs[::-1]):
                #time = re.findall(r'\([^)]*\)', i)
                #text = re.sub(r'\([^)]*\)', '', i)
                draw.text((10,10+(ind)*fontsize), i, fill=(255,255,255), font=font)
            disp.image(image, rotation)
            image.show()
                

            
        if not buttonA.value:
            with open('output.txt', 'w') as f:
                f.write("")
            # Current bug TODO: cannot run more than once because the device is unavailable/seemingly still in use from last run.        
            mic_vad_streaming.run(100)
            with open('output.txt', 'r') as f:
                voice_data = f.read()
            client.publish(topic,"("+strftime("%I:%M:%S", gmtime())+")" + voice_data)
        if not buttonB.value:
            #client.on_message = on_message
            speakable = re.sub(r'\([^)]*\)', '', curr_message)
            speak(speakable)

# end
if __name__ == '__main__':
    
    import argparse
    parser = argparse.ArgumentParser(description="Stream from microphone to DeepSpeech using VAD")

    parser.add_argument('-p1')
    parser.add_argument('-p2')
    ARGS = parser.parse_args()
    run()
    
    #import sys
    #run(sys.argv[0],sys.argv[1])
