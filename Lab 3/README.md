# You're a wizard, vince!

<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.


## Text to Speech and Speech to Text

In the home directory of your Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

you can run these examples by typing 
`./espeakdeom.sh`. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts

```

You can also play audio files directly with `aplay filename`.

After looking through this folder do the same for the `speech2text` folder. In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

## Optional

There is an included [dspeech](./dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

1. Sketch ideas for what you'll work on in lab on Wednesday.
![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%203/initial_storyboard.png)

## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*
I had a medical appointment Wednesday morning and didn't make it to this sketch sharing session, but this is the feedback I got from some family members:

**Michael:** "Can you get the YouTube videos to stop and start again? It would be nice to be able to browse the videos through voice commands. Also it might be cool if the robot could watch the YouTube videos somehow and react to them."

**David:** "You can try sending song recommendations over voice maybe, like if the person is looking sad or angry maybe you can have the robot move and then have a text-only suggestion on the screen that the robot points to with it's movements."

**Kat:** "It would be cute if the robot danced to the songs! Like having the audio signal informing robot movement directions?"

*The feedback was primarily around how to make this a fun interaction for the user while enhancing Alexa. Some things I couldn't really get to but it was obvious that the robot didn't have to really be too complicated to get some interesting observations from a user. So I focused on a simple robot and YouTube video requesting.*

Iterated storyboard based on the feedback:
![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%203/end_storyboard.png)

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*
Pip install package, SpeechRecognition handles the speech to text with Google, and google TTS is handled by the pip install package gTTS, these two together act as the full speech stack. On top of this are three browser automation tools: BeautifulSoup(+RegEx) for webpage parsing, PyAutoGui to handle clicking YouTube elements, and the standard python WebBrowser package for opening and searching on a browser, these three together act as the YouTube automation medium -- in addition to wizarding to handle lag in microphone input, and internet processing. Lastly, Flask and OpenCV handle streaming a camera to sense and assist in interacting with a user -- as well as two mini digital servo's propped together as a robot that can be sent arrow key input for 2DOF movement -- one servo broke in the process. 

To get the full system running, besides installing the requirements.txt and the following apt-get packages: {chromium, swig, pkg-config libcairo2-dev gcc python3-dev libgirepository1.0-dev}; the raspberry pi is SSH'd into and the RunDemo.sh file within PCA8675 is run, then the flask server as: python pi-camera-stream-flask/main.py is run on the raspberry pi, and the voice engine is run within the Lab\ 3 folder as python main.py. With the voice engine, 2DOF robot, and camera stream running the whole system is up. 

The point of this setup was to see how an Alexa might be augmented through movement, and how a user might react to this movement. The enhancements to this Alexa are mainly in what is afforded in access to YouTube videos, the ability to watch a moving picture, and then have company in the form of a robot that might also be experiencing the same visual experience the user is experiencing. All of this to explore how a user develops an affinity to the device. 

*Include videos or screencaptures of both the system and the controller.*
![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%203/robot_control.png)
![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%203/Kat.png)


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

## Final video prototype:
[![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%203/preview.png)](https://drive.google.com/file/d/1sAyDeGDEG1PoWVENRhgvGNVL8zU8Xbw3/view?usp=sharing)
(click^!)

Answer the following:

### What worked well about the system and what didn't?
Overall the system does a 8/10 job, (Alexa being a reference for a 10, which isn't a great 10!) at surfacing search results that a user might want. TTS works very well, but SST does not. There is a question of what is it that causes people to expect excellence from a voice assistants ability to do SST, and if there are some design choices that can help in having a user understand that they might have to annunciate or that it struggles with certain words. Why do we seek excellence from SST when often we struggle with SST? How might a system be designed to encourage empathy for technical deficiency? Maybe if we could see what it interpreted we might be taught how to better communicate with some given voice assistant. Certainly the keyboard and the mouse are imperfect input mediums, and yet we have gained an empathy to be able to work with them.

One interesting artifact from this system was that after some time the user became interested in learning about what songs the robot might have a different dance to -- in effect sharing what was initially their own musical curation, with the Alexa embodiment.

### What worked well about the controller and what didn't?
The video feed works perfectly, without any lag or bandwidth restrictions along the way. It might have been nice to be able to control the camera orientation if the user moved, but there is also a lot to be learned about what it means to a system when the user is within camera proximity, and beyond camera proximity. On the other hand, controlling the mini digital servo's was very disappointing, and ultimately one servo broke and ended up erratic. The control system worked as well as it seems it could have in taking arrow key input, but it might be worth consideration in the future to instead pre-program stances or movements and ask the servos to act them out. It might be worth looking into stepper motors for their more fluid movements.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
The most difficult wizarding aspects were in handling edge cases where internet lag or hardware lag was inconsistent, and it wouldn't be sufficient to just extend wait times between action items because this might scale to be an overall lagging system. In some cases if the user didn't speak fast enough, for instance in selecting a song, the voice recognition system would assume the user was done -- so maybe some sort of backchanneling signal to indicate that the user is done would help the system calibrate it's pace in actions. 

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?
Could create a dataset of emotional reactions to a set of robotic movements, and try to extract principal components of an emotion inducing robotic movement based on a set of reactions that a user has. I think it would be interesting not to add more sensing modalities but to try to further exploit the camera feed to get data from eye movement, to try to get a sort of more intelligent version of eye tracking. It would be great to get a better microphone and get some sense of directionality in the audio signal. The single mic array doesn't facilitate this but directionality in audio signal could well be used to make the robot more autonomous. 
