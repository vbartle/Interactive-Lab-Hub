# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.


**Describe and detail the interaction, as well as your experimentation.**
1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

The goal I had in mind for this lab was to use hand tracking for some arbitrary percentage control, e.g. selecting some percent of a list or changing the volume to be some percent. In the spirit of this lab I thought I should try something I hadn't before, so instead of Teachable Machine I used MediaPipe. Although it is possible to do hand tracking using the image model from Teachable Machine, it takes an enormous amount of data to accomodate lighting conditions, and have it work invariant to the infinity of possible backgrounds. There is a pose model but it is not yet setup for hand poses. MediaPipe however, has a rich volume of models for this. The main problem is, none are yet natively built to accomodate the Pi, so there's a lot of hacking around. Building Bazel: [(1)](https://github.com/google/mediapipe/issues/1346#issuecomment-825002094), and [(2)](https://github.com/bazelbuild/bazel/issues/13393), [(3)](https://github.com/google/mediapipe/issues/1917) and getting the media pipe build wheel to configure [attributes](https://github.com/jiuqiant/mediapipe_python_aarch64/issues/5).

Ultimately I did get it partially running for this demo, and the main constraint is that it fails by running at low FPS. This means the model has to have an increased certainty threshold to classify a pose, to beat jitter, and multi-hand detection has to be removed, because the Pi is incapable to handling the requisite compute. 

**Think about someone using the system. Describe how you think this will work.**
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

Given a video feed of what the camera sees, it is directly clear what the system is uncertain of, in some cases it is overly uncertain, jittery, and as some [studies](https://infosci.cornell.edu/~apc75/files/Self_Repair_CSCW_2021.pdf) may call this uncertainty: anxious. So there is a downside in this level of transparency of the system, although it does communicate what the system is capable. The worst case scenario for a miss classification, in the volume example, is probably first volume being too high, and second, volume being too low. This is mostly addressed by the fact that it is actually fairly hard to reach these extremes in the current mapping of the gesture, although it is possible to make the mapping increasingly logarithmic. The main optimizations I explored were in removing multi hand detection and in increasing tracking threshold, these help reduce the jittery feel of the system.

* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

In many cases a simple knob is much better than hand pose detection for percentage manipulation. However, hand pose detection allows for applications such as selection of an area, and most importantly, for dynamic signaling akin to what is found in sign language, for example. One application I explored in this, was mimicing the 'quiet coyote' from Soul, which you can see in the video. This is a clear applicaiton where a hand gesture invites some level of approachability and interactivity with the system. This is also opposed to voice control, where again, a user might just not want to speak, and is able to use their hand at some suspended distance to communicate instead. 

**Include a short video demonstrating the finished result.**
[![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%205/preview.png)](https://drive.google.com/file/d/1KWRs36-6kO7ZtHH7dLRZyWDuW3Zfa1Q5/view?usp=sharing)
