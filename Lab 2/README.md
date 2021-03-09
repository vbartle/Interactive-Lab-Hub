# The Clock of Pi

Does it feel like time is moving strangely during the pandemic?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

## Prep

[Lab prep](prep.md) is extra long this week! Make sure you read it over in time to prepare for lab on Wednesday.

### Get your kit
If you are overseas, you should have already ordered your parts.

If you are remote but in the US, the teaching team mailed parts last week.

If you are in New York, you can pick up your parts. If you have not picked up your parts by class you should come to Tata 351.

### Set up your Lab 2

1. [Pull changes from the Interactive Lab Hub](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Spring/readings/Submitting%20Labs.md#to-pull-lab-updates) so that you have your own copy of Lab 2 on your own lab hub. (This may have to be done again at the start of lab on Wednesday.)

In terminal cd into your Interactive-Lab-Hub folder and run 

```
Interactive-Lab-Hub $ git remote add upstream https://github.com/FAR-Lab/Interactive-Lab-Hub.git
Interactive-Lab-Hub $ git pull upstream Spring2021
Interactive-Lab-Hub $ git add .
Interactive-Lab-Hub $ git commit -m'merge'
Interactive-Lab-Hub $ git push
```

Your local and remote should now be up to date with the most recent files.

2. Go to the [lab prep page](prep.md) to inventory your parts and set up your Pi.


## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. 
## Connect to your Pi
Just like you did in the lab prep, ssh on to your pi. Once there create a python environment.

```
ssh pi@ixe00
pi@ixe00:~ $ virtualenv circuitpython
pi@ixe00:~ $ source circuitpython/bin/activate
(circuitpython) pi@ixe00:~ $ 

```

## Part B. 
### Try out the Command Line Clock
Clone the repo for this assignment

```
(circuitpython) pi@ixe00:~$ git clone https://github.com/YOURGITID/Interactive-Lab-Hub.git
(circuitpython) pi@ixe00:~$ cd Interactive-Lab-Hub/Lab\ 2/
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub $ 
```

Install the packages from the requirements.txt and run the example

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub $ pip install -r requirements.txt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python cli_clock.py 
02/24/2021 11:20:49
```
you can press `ctrl-c` to exit.
If you're unfamiliar with the code in `cli_clock.py` have a look at [this refresher](https://hackernoon.com/intermediate-python-refresher-tutorial-project-ideas-and-tips-i28s320p). If you're still concerned please reach out to the teaching staff!


## Part C. 
## Set up your RGB Display
We will introduce you to the [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) and Python on the Pi.

<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" />

The Raspberry Pi 4 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.

<img src="https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png" height="400" />

To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

### Hardware

From your kit take out the display and the [Raspberry Pi 4](https://www.adafruit.com/product/4296 | width=200)

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

#### Testing your Screen

The display uses a communication protocol called [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to speak with the raspberry pi. We won't go in depth in this course over how SPI works. The port on the bottom of the display connects to the SDA and SCL pins used for the I2C communication protocol which we will cover later. GPIO (General Purpose Input/Output) pins 23 and 24 are connected to the two buttons on the left. GPIO 22 controls the display backlight.

We can test it by typing 
```
python screen_test.py
```

You can type the name of a color then press either of the buttons to see what happens on the display. take a look at the code with
```
cat screen_test.py
```

#### Displaying Info
You can look in `stats.py` for how to display text on the screen

#### Displaying an image

You can look in `image.py` for an example of how to display an image on the screen. Can you make it switch to another image when you push one of the buttons?



## Part D. 
## Set up the Display Clock Demo

In `screen_clock.py`. Show the time by filling in the while loop. You can use the code in `cli_clock.py` and `stats.py` to figure this out.


## Part E.
## Modify the barebones clock to make it your own

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)

Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.

**A copy of your code should be in your Lab 2 Github repo.**

you can push to your personal github repo by adding the files here, commiting and pushing.

```
git add .
git commit -m'your message here'
git push
```

After that git will ask you to login to your github account to upload.

## Part F. 
## Make a short video of your modified barebones PiClock

**Take a video of your PiClock.**

https://drive.google.com/file/d/1OxxkoBzNOUxzVK5MoC25QWlJwqEdWCIN/view?usp=sharing

## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.

Todo: Add button clicks to flip between sunrise and sunset info.


Final version I forgot to rename but is all in https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%202/p5_audio_version/test.py .

Feedback received:
The feedback I received from Rui Maki, Min Tae Lee, Erin Gong, Jacob Rauch, and Ritika Poddar was complimentary of the sunrise and set API usage, and im summary asked to include adding button presses to display more data like time to next sunset/sunrise, and enabling color or background image differences/animations overtime based on sunrise/sunset are ideal best next steps. I also shared thoughts of using a projector to display this over the day in a room.

The final result takes most of this into account, except for adding more information, instead I wanted to make it as clear as possible where the sun was so there is the inclusion of the altitude of the sun, although the data point is not as explicitly visible as the simulation of the sun made. The implementation consists of taking a python version of p5.js, a graphics library, importing solar data from a solar location API and a sun times library. Rather than squeezing this into the OLED display I did end up playing with a projector. Still, the buttons from the display are used to interface with the microphone and trigger it to listen. The background of the simulation changes based on microphone input, so if the user says it's an overcast day, the background changes to something that will make the image more favorable given the lighting conditions, and vice versa for a clear day. Part of this was also to make up for the difficulty in predicting weather and to include the user in informing the device as to the weather conditions rather than trying to do too much. I found this involvement to be enjoyable, the only possibly missing step is allowing the user to fine tune the background colors, perhaps with an additional controller like the rotoary encoder. This was already very feature packed by the time I considered this though.

Final video here (full screen please):
https://drive.google.com/file/d/1DqFRE6Ixp48aHpFxk33oakS56_45TEZw/view?usp=sharing

And because I couldn't get the shutter on the projector to match what my camera could capture, there's a rolling shutter artifact. Below is a screenshot of a more accurate representation of the display. Also it's hard to see in the video but the first screen says "how are the skies today?" followed by "overcast" and "clear" when the user said overcast or clear. 

![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%202/2021-03-08-193055_1280x720_scrot.png)

The solar simulation comes from a ray casting tutorial produced by Daniel Shiffman from NYU (https://twitter.com/shiffman/status/1126134538353152000?lang=en); it's pretty remarkable how far the RPI4 could be pushed given the complexity of this script to calculate particle positions. One slow down to make it more runnable is that the display only refreshes every 3 seconds instead of every second or half second as it would or a typical rig. The artifacts of swirl seen in the display are illusory from straight 360 straight lines emanating from the simulated position. I made some additional changes to the code to make the obstacles a certain length and orientation that represented buildings outside of my apartment, the way the sun might actually shine through the real life objects. As mentioned above the functional final code is in test.py in the p5_audio_version; I did not update the requirements file but one would need to also pip install: p5, pysolar, pyaudio, and sudo apt-get install {libglfw3, freeglut3-dev} -- some graphics libraries. 

The audio at the end if Nights by Frank Ocean, to show the display going into night, and the sun simulation is condensed from a 2.5h recording to <5 seconds.
