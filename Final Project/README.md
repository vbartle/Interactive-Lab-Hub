# Final Project

Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Project Github page set up - May 3

Functional check-off - May 10
 
Final Project Presentations (video watch party) - May 12



## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.

1. Documentation of design process
The contents of my [Lab 2](https://github.com/vbartle/Interactive-Lab-Hub/tree/Spring2021/Lab%202) and [Lab 4](https://github.com/vbartle/Interactive-Lab-Hub/tree/Spring2021/Lab%204) setup the stage for how this design process unfolded, and the note about font choice in my [Lab 6](https://github.com/vbartle/Interactive-Lab-Hub/tree/Spring2021/Lab%206) is also relevant. 

The gist of the idea was to make something resembling a doctor's bag, for when they used to visit their patients at their homes, but now for modern day caregivers who have since substituted that role of at-home care.

From a technical stand point, the device is running in essence with google app engine handling STT and TTS, p5.py handling all visual components, python packages: webbrowser and os handling browser control, a wood device framing providing contextual grounding, and EB Garamond facilitating text legibility. As with my Lab 4, configuring all the components such that the device wouldn't overheat and shutdown was a slight hurdle. All power gets funneled first through the screen chip, so I had to separate that from everything else, and I found placing it against one of the walls worked well. 

Two new components used here were the microphone and speaker, since I found in my past labs that microphone quality drastically helped with STT, I found and am using a portable condenser mic. The screen and the mic are hot glued to the lid, I had never used a hot glue gun before this class and I am forever sold. The RPI4, speakers, and cabling are all tucked underneath and mostly held in place with hot glue as well. This was rather tricky because it meant the box had to be designed with essentially a false bottom. It turned out this still wasn't enough space so I propped the speakers such that they acted as legs and added wood feet tot hem for stability so the cables would have more space.

I initially thought having an e-ink display might be appropriate but then decided that browser and video access was important, so instead rotated the screen portrait-wise and made the color beige to inspire that paper-like feeling. Using a serif'd font also helped with this.

2. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)

To get this running make a virtual environment and recursive install the from the requirements file, then just run ginger_2. I.e. ```python -m venv venv;source venv/bin/activate;python3.7 ginger_2.py```. The ginger_2 file has been commented to explain what is happening but there's a lot packed into that one file. In summary: there are two core features dancing with each other: voice and the DOM (what's shown on the screen). Audio is streamed constantly and checks are run on that audio stream, based on the stream the status of the DOM is changed. So if 'some phrase' is found in the ```voice_data```, then some action happens on the DOM. The first feature shown of moving items across lists in the morning and evening are handled by such checks, e.g. ```if add then morning_list.append(); if remove then morning_list.remove()```. The second feature shown of navigating a task assistant is partially hard coded for a single branch of conversation, but works on the same if statements principle.

3. Video of someone using your project (or as safe a version of that as can be managed given social distancing)

[![](https://raw.githubusercontent.com/vbartle/Interactive-Lab-Hub/Spring2021/Final%20Project/final_preview.png)](https://drive.google.com/file/d/19nhoX-Td7e8_7Ot75MmUqb2jkSIoIUW3/view?usp=sharing)

4. Reflections on process (What have you learned or wish you knew at the start?)
5. 
I initially intended to include some of the machine learning components from past labs, but found that as it was the system had all the features it needed to convey the story to the device. Moreover, the machine learning components would have slowed down and heat up the system significantly, and necessitated a switch to the Jetson Nano, which I decided to hold off on for another day. I think there are still some great applications of ML to be included, such as hand pose detection for navigating the care plan list, and the various other medical CV applications. 

Overall I was surprised with how effectively if-elif-else statements worked for simple app navigation. I was afraid I might have had to incorporate some sort of state-handling system with flask, but it just barely worked smoothly enough to not need this.  



