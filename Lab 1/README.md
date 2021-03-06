

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.



For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

1. Set up [your Github "Lab Hub" repository](../../../) by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Spring/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how](https://guides.github.com/features/mastering-markdown/) to post links to your submissions on your readme.md so we can find them easily.

### For lab, you will need:

1. Paper
1. Markers/ Pen
1. Smart Phone--Main required feature is that the phone needs to have a browser and display a webpage.
1. Computer--we will use your computer to host a webpage which also features controls
1. Found objects and materials--you’ll have to costume your phone so that it looks like some other device. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case. Be creative!
1. Scissors

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process.
1. Video sketch of the prototyped interaction.
1. Submit these in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


## Overview
For this assignment, you are going to 

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

To stage the interaction with your interactive device, think about:

_Setting:_ Where🏠 is this interaction happening? (e.g., a jungle, the kitchen) When⏰ is it happening?

_Players:_ Who🧍 is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.

_Activity:_ What📕 is happening between the actors?

_Goals:_ What are the goals of each player?🔥 (e.g., jumping to a tree, opening the fridge). 

The interactive device can be anything *except* a computer, a tablet computer or a smart phone, but the main way it interacts needs to be using light.
**Describe your setting, players, activity and goals here.**

Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 
**Include a picture of your storyboard here**

Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.
**Summarize feedback you got here.**

----
### Part A. Plan 
Alex🧍 is a caregiver assisting a client, Aaron🧍, with a passive range-of-motion exercise at home🏠 during their weekly⏰ visits: standing knee flexion, where the client stands and bends one knee so the tibia rotates as far as possible, also leaving them standing on one leg. To maximize rotation and track progress, the client needs the caregiver to cue them. In order to avoid confusion from nodding or verbal cues, the caregiver will use Tinkerbelle to indicate progression 📕relative to their farthest🔥, or past rotation. 

https://www.youtube.com/embed/YubFqnGJ5Qk

I added this class late, my apologies, so I don't have breakout room feedback. But feedback received from my brother: consider the scenario of Aaron wanting to do this exercise by themselves -- can the device be programmed in some way to notice the farthest they've gone on it's own? 

![](Screenshot%20from%202021-02-19%2009-34-42.png)


## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

**Are there things that seemed better on paper than acted out?**

**Are there new ideas that occur to you or your collaborators that come up from the acting?**

### Part B. Act out the Interaction

I pretended to exercise knee mobility myself and found my first instinct wasn't to keep my moving knee parallel with my unmoving knee, so I had to consciously keep the moving knee in place. It could be good to setup a cue via color to indicate that knees aren't parallel with each other. Like having white to blue for knee mobility and then flashing if knees aren't parallel. 

## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

**Give us feedback on Tinkerbelle.**
Cool! You could add some method of enabling interpolation between points so that wizarding can be automated to some degree, or so a wizard can more steadily control gradients rather than resorting to flipping quickly between extreme colors to make a point. Here's a quick prototype of this in JS: https://editor.p5js.org/bartle/sketches/AeD_5ZJC0. Happy to help if something like this seems useful.

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

**Include your first attempts at recording the set-up video here.**

Now, change the goal within the same setting, and update the interaction with the paper prototype. 

**Show the follow-up work here.**

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

**Include sketches of what your device might look like here.**
![](Screenshot%20from%202021-02-19%2009-53-24.png)

**What concerns or opportunitities are influencing the way you've designed the device to look?**
The main one is positioning wherever the person wants to do this exercise so the light is nearby or can be easily placed where the person would like. So a tripod is included. The aesthetic element of the device has not come up in feedback yet, it seems that the simplicty of the device is prefered.

## Part F. Record

**Take a video of your prototyped interaction.**


**Please indicate anyone you collaborated with on this Lab.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

Contributions: Wife and brothers giving me feedback on the interaction video :).
Other influences: This youtube video about standing knee flexion. https://www.youtube.com/watch?v=YubFqnGJ5Qk

# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.

## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

**Summarize feedback from your partners here.**

1. How could you position it to be eye-level for any height person and be positioned anywhere easily by a solo adult?
1. How could you indicate that the exercise is being done correctly? E.g. having knees parallel? 
1. How would you set the goal point?
1. How could you celebrate hitting a goal point?
1. How could you indicate that the session has started?
1. How could you indicate reps and progress toward reps? 

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors, 
3) We will be grading with an emphasis on creativity. 

**Document everything here.**

## Final compiled video:
1. Added tripod.
2. Added light flashing for knee's being parallel. 
3. Added 3-2-1 start.
4. Added holding. 
5. Added goal setting,
6. Added celebratory lighting.

https://drive.google.com/file/d/1shW5M__bRLnxYkbMOPYelLtpWTXn8w_w/view?usp=sharing

## Reflection:
Creating a language through the symbols that are light patterns turned into an interesting experiment with design. One example being how, before including the idea of sound, to communicate to the user that their knees weren't in-line it wasn't entirely clear what the best approach might be. There could be a red flashing light, but this miscommunicates urgency as I learned through feedback from peers. It ultimately seemed best to fade in and out of black which I felt communicated that the exercise was being done incorrectly in some way. The notion of adding in a goal and allowing the user to set a goal also seems elaborate, although for a simple exercise like knee flexion it seems like a gesture suffices. I imagine for more complex physical therapy or otherwise mobility exercises a gesture might not be ideal -- what if both hands are occupied, for instance. The use of vocalizing might be a necessary medium at that point. One big to-do feature for a future iteration is progress tracking, so that when the user starts the device they are shown the work they did in the past and what their current best is, to inform their current-day exercise.

As for costuming, there is the consideration of designing devices for the elderly such that they are easily used. Attaching the device to a tripod allows for ease of movement and placement so that the user can see it easily. One additional feature to explore for a future iteration might be to clamp a bar or chair to the tripod so that the user can use the device as a hold, although at this point the device becomes furniture and there is the liability of it not being strong enough to hold the client. 

