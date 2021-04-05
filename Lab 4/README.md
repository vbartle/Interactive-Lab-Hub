# Ph-UI!!!

For lab this week, we focus on the prototyping the physical look and feel of the device. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_

 
**a. Document the design for your paper display.** (e.g. if you had to make it again from scratch, what information would you need?). Include interim iterations (or at least tell us about them).

**b. Make a video of your paper display in action.**

**c. Explain the rationale for the design.** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

### Part D
### Materiality

**Open Ended**: We are putting very few constraints on this part but we want you to get creative.

Design a system with the Pi and anything from your kit with a focus on form, and materiality. The "stuff" that enclose the system should be informed by the desired interaction. What would a computer made of rocks be like? How would an ipod made of grass behave? Would a roomba made of gold clean your floor any differently?

**a. document the material prototype.** Include candidates that were considered even if they were set aside later.

**b. explain the selection.**

### Part 2.

1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device
5. Submit these in the lab 4 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.

---
**Sketch progression:**
![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%204/sketches.JPG)

The basic idea at first was: looks like a picture frame, works like a daily planner, acts like an Alexa. To get it to look like a picture frame I would make a picture frame out of wood, to make it work like a daily planner I would connect an e-ink display, and to get it to act like an Alexa I would connect the speech to text and text to speech functionality I prototyped in Lab 3. Ultimately though I wanted to have some clear interaction with "Alexa" to be conveyed over the device, and not much was changed by this setup besides making the display e-ink instead of full color. 

The next iteration I considered taking the (remaining, working) digital servo from the last lab and using it to rotate the display. In the final video you'll see I tried making this, and in the sketches above you can see the plan for how the screen would rotate. Unfortunately though, creating a joint that would support this kind of movement is highly non-trivial, and most importantly, the servo was far too weak to support this movement without a supporting bracket. 

The final iteration I considered keeping the frame still, and the vertical orientation, and addressing the wake word problem with Alexa, where maybe a person doesn't want to or cannot speak. So maybe the display could instead be embedded into a door. Where one knocks on a door as a sort of real-life wake word. I thought this idea would be fantastic so I moved on to making the actual door and case. 

The case is made from strips of walnut wood cut on a bandsaw that were then glued together with the magical glue gun mailed to us, and then trimmed on a router. So the main problem with all of this was 1) I have no idea how woodworking works, and 2) I don't have much experience working with small pieces of wood. Two project specific problems that arose were: 1) the case/framing broke several times, as shown in the video and 2) the monitor overheated in the case design I made, also shown in the video. 

From a technical standpoint this is less complex than my last labs, everything runs on the web editor of p5.js: editor.p5js.org, a real miracle out of NYU, with the support of TheCodingTrain by Daniel Shiffman, and Google/NYU's TeachableMachine. There is a nontrivial aspect of actually getting this to run on Chromium on the pi, and it definitely is at the edge of the Pi's ability. One minor problem: supporting emoji's which was resolved with this post: https://raspberrypi.stackexchange.com/questions/104181/colored-emojis-in-chromium. And to get WebGL to work I ran chromium --enable-webgl --ignore-gpu-blacklist. 

The last important note was having the microphone work accurately -- the mic that came with the kit has a lot of noise, and I found more success with my usual mic which also just connected over USB. It is interesting that the model results did not transfer between mics: if I made the model on one mic, it would not perform as well if run on the other mic. 

**Final video:**
[![](https://github.com/vbartle/Interactive-Lab-Hub/blob/Spring2021/Lab%204/pre.png)](https://drive.google.com/file/d/1MGOn1q9r1fo0QlbezuGJtMP_xpUEFjhd/view?usp=sharing)

In case it's not clear: the three classes are: nothing, normal knock, speak-easy knock. 

**Would have liked to:**
1. Merged with progress in Lab 3 where navigating YouTube over voice was feasible. 
2. Included hand pose detection for navigation. E.g. pinch = volume down, thumb & index apart = volume up.
3. Made TeachableMachine model run on python as a keras model. This is a lot more complicated but would run without Chrome. 
4. Run this on Jetson Nano (**is this allowed?**) for smoother performance.
5. Made a cleaner case. 
