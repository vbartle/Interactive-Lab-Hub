# m[Q](https://en.wikipedia.org/wiki/QAnon)tt[Anon](https://en.wikipedia.org/wiki/QAnon): Where We Go One, We Go All

## Prep

1. Pull the new changes
2. Install [MQTT Explorer](http://mqtt-explorer.com/)
3. Readings 
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Introduction

The point of this lab is to introduce you to distributed interaction. We've included a some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects. However we want to emphasize the grading will focus on your ability to develop interesting uses for messaging across distributed devices. 
----
**1. Explain your design** 

The overall goal was to build something that could act as more casual than email but more formal than text; a messaging medium that lies somewhere between these two, like a picture frame that sits on a table and is updated from time to time with some semi-important message. Often times text is too fleeting to let the importance of a message sink in, and email seems to miss a level of freedom and play. So we created a messaging system on RPi + TFT, with MQTT and Mozilla DeepSpeech.

There are several features not fully implemented in the following storyboard, such as score keeping, but the principal idea was helpful for guiding the build of the project and conveying the purpose of the device.

![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%206/Screenshot%20from%202021-05-04%2023-04-57.png)
![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%206/Screenshot%20from%202021-05-04%2023-05-08.png)
![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%206/Screenshot%20from%202021-05-04%2023-05-17.png)

This overall interaction is shown in the first half of the video.

**2. Diagram the architecture of the system.** 

The architecture starts with Mozilla DeepSpeech for SST, this is then linked to a button on the RPi TFT so that a button triggers the stream and the stream ends after some set amount of time. The text is then stored in a text file, and the content of that text file are sent to Topic 1 in MQTT by Client 1. Client 2 running a duplicate system is subscribed to Topic 1, and receives the message that Cleint 1 sent. Client 2 plays this message using button 2 on the TFT. Inversely, Client 1 is subscribed to Topic 2, and they can read messages sent with button 2. The TFT displays these messages in descending order of time received, with the time received followed by the message. These text messages are shown as a preview on the TFT and when selected to be played, are run through pyttsx3.

**3. Build a working prototype of the system.** 
**4. Document the working prototype in use.** 

Capturing the speech to text stream through Deep Speech required an understanding of how the stream worked, where microphone stream data is treated in time frames. An [example script](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%206/mic_vad_streaming.py) provided by Mozilla was modified and imported in the [script that handles mqtt and tft control](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%206/tester.py), and set to run for ~10 seconds.

There is an un-implemented feature for clearing the DeepSpeech cache -- as it is, the memory cache only allows for 5 speech to text iterations before it cannot write to memory. This limitation is an example of some of the unweildy features of connecting DeepSpeech with MQTT, where we are essentially funneling a large SST task into a MQTT logs that are optimized for quick data tranfer. 

There was also a lot of messing with the display text so that it would show as a clean log on the TFT. Adding EB Garamond as a font really helped with legibility and spacing between messages. Also, because showing timestamps for messages seemed like an important feature for the multiple users, and because mqtt does not inherently provide log data, there was the need to manually log time at the mqtt publish stage. This manually logged time then needs to be regex'ed out so that the message is speakable by pyttsx3.

There is an additional incomplete feature of not hardcoding client 1 and 2 and topic 1 and 2, but allowing a user to set these as arguments at command line via parser. e.g. python3.7 tester.py -client Vince -topic Rui; meaning I publish to the topic Vince and subscribe to the topic Rui. This would make it so many people could for example subscribe to a single topic, creating a network of mqtt messaging clients. This was partially implemented but is left incomplete for the purposes of this lab.

One of the most interesting results of this prototype system was finding how much microphone quality impacts transcription. The included mic was almost entirely noise to dspeech, a little bit of tuning may have improved results, but this tuning is not realistic for scaling to many devices and clients, unless the devices are uniform. So for this lab no parameter tuning was done. An earbud microphone worked better than the default rpi mic, picking up longer messages, and a stage microphone worked far better than the rest. The suggests that native audio isolation found in a high quality mic might be key to off-line speech to text. 

**Final video:**

[![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%206/Screenshot%20from%202021-05-04%2022-57-37.png)](https://drive.google.com/file/d/1LrZzyW5d5auMs_47vhyaIRIryTkDqJ-P/view?usp=sharing)

**5. BONUS (Wendy didn't approve this so you should probably ignore it)** 
