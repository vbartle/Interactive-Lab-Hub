from p5 import *
import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
from time import ctime # get time details
import random
from time import ctime # get time details
import webbrowser # open browser
import yfinance as yf # to fetch financial data
import ssl
import certifi
import time
import os # to remove created audio files
# from audioplayer import AudioPlayer
from bs4 import BeautifulSoup
import requests
import re
from selenium.webdriver import ActionChains
from selenium import webdriver
import pyautogui
import time as t

width = 590
height = 940
h1 = 100
h2 = 50
h3 = 30

monday_morning_tasks = ['walk', 'record vitals']
monday_evening_tasks = ['exercise']
status = 'home'
spoken = False
leg_swell_image = load_image('./edema.png')
leg_swell_chart = load_image('./edema_chart.jpeg')
r = sr.Recognizer() # initialise a recogniser

def word_wrap(text, n=35):
    words = iter(text.split())
    lines, current = [], next(words)
    for word in words:
        if len(current) + 1 + len(word) > n:
            lines.append(current)
            current = word
        else:
            current += " " + word
    lines.append(current)
    return lines

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms, voice_data):
    for term in terms:
        if term in voice_data:
            return True


def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            # speak('I did not get that')
            pass
        except sr.RequestError:
            # speak('Sorry, the service is down') # error: recognizer is not connected
            pass
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    # AudioPlayer(audio_file).play(block=True)
    print(f"Ginger: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

def setup():
    size(width, height)

time.sleep(1)
person_obj=person()
def draw():
    if status == 'home':
        background(253,246,227)
        fill('black')
        text_font(create_font('garamond.ttf', size=h1))
        display_time = ctime().split(" ")[3].split(":")[0:2]
        
        if display_time[0] == '00':
            hours = '12'
        else:
            hours = display_time[0]
        minutes = display_time[1]
        
        text(f'{hours}:{minutes}', 10,10)
    
    voice_data = record_audio() # get the voice input
    if voice_data:
        respond(voice_data)
    print(status)
    
def respond(voice_data):
    global status
    global spoken
    global monday_morning_tasks
    global monday_evening_tasks
    
    if there_exists(['add to the morning'], voice_data):
        added_task = voice_data.split("morning")[-1]
        monday_morning_tasks.append(added_task)
        
    if there_exists(['add to the evening'], voice_data):
        added_task = voice_data.split("evening")[-1]
        monday_evening_tasks.append(added_task)
        
    if there_exists(['remove from the morning'], voice_data):
        removed_task = voice_data.split("morning")[-1]
        try:
            monday_morning_tasks.remove(removed_task)
        except:
            pass
    
    #if there_exists(['hey','hi','hello'], voice_data):
    #    greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
    #    greet = greetings[random.randint(0,len(greetings)-1)]
    #    speak(greet)
    
    if there_exists(["youtube"], voice_data):
        os.system("pkill chromium")
        search_term = voice_data.split("for")[-1]
        # url = f"https://www.youtube.com/results?search_query={search_term}"
        url = 'https://www.youtube.com/results'
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        response = requests.get(url, params={'search_query':search_term}, headers=headers)
        # print(url)
        soup = BeautifulSoup(response.content,'html.parser')
        expression = re.compile(r'\bwatch\b.{14}')
        found = expression.findall(str(soup))
        found = [i for i in found if '?' in list(i)]
        webbrowser.get('chromium').open('https://youtube.com/'+found[0])
        speak(f'Here is what I found for {search_term} on youtube')
        t.sleep(6)
        pyautogui.click(485,445) 
    
    if there_exists(["stop music"], voice_data):
        speak("stopping music")
        os.system("pkill chromium")

    if there_exists(["stop browser"], voice_data):
        speak("stopping chrome")
        os.system("pkill chromium")
    
    if there_exists(['home'], voice_data):
        status = 'home'
        print('set status:home')
    
    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"], voice_data):
        if person_obj.name:
            speak("my name is Ginger")
        else:
            speak("my name is Ginger. what's your name?")

    if there_exists(["my name is"], voice_data):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object
        
    # 3: greeting
    if there_exists(["how are you","how are you doing"], voice_data):
        speak(f"I'm very well, thanks for asking {person_obj.name}") 

    # 4: care structure
    if there_exists(["care plan", "airplane", "mycareplan"], voice_data):
        status = 'care plan'
        spoken = False
        print("status:care plan set")
    
    if there_exists(["leg swelling", "like swelling"], voice_data):
        status = 'leg swelling'
        spoken = False
        print('status:leg swelling set')
    
    if there_exists(['continue'], voice_data):
        status = 'continue'
        spoken = False
        print('status:continue set')
        
    if there_exists(['moderate'], voice_data):
        status = 'moderate'
        spoken = False
        print('status:moderate set')
        
    if there_exists(['yes'], voice_data):
        status = 'yes'
        spoken = False
        print('status:yes set')
        
    if there_exists(['no'], voice_data):
        status = 'no'
        spoken = False
        print('status:no set')
    
    if status == 'yes':
        background(253,246,227)
        phrase1 = "Ok, reminder set for tomorrow to measure leg swelling."
        display_phrase = word_wrap(phrase1, n=50)
        text_font(create_font('garamond.ttf', size=h2))
        text("Measurement", 10, 10)
        
        text_font(create_font('garamond.ttf', size=h3))
        incr = 0
        for i in display_phrase:
            fill('black')
            text(i, 20, 110+incr)
            incr += h3+5
        time.sleep(5)
        if not spoken:
            speak(phrase1)
            spoken = True
    
    if status == 'moderate':
        background(253,246,227)
        phrase1 = "This is a concerning reading, would you like me to alert the client's nurse?"
        display_phrase = word_wrap(phrase1, n=50)
        text_font(create_font('garamond.ttf', size=h2))
        text("Measurement", 10, 10)
        
        text_font(create_font('garamond.ttf', size=h3))
        incr = 0
        for i in display_phrase:
            fill('black')
            text(i, 20, 110+incr)
            incr += h3+5
            
        if not spoken:
            speak(phrase1)
            spoken = True    
                
                    
    if status == 'no':
        leg_swell_report = 'moderate'
        background(253,246,227)
        phrase1 = "Ok, for now I recorded the measurement on the clients careplan. I recommend checking leg swelling again soon, would you like me to set a reminder for tomorrow?"
        display_phrase = word_wrap(phrase1, n=50)
        text_font(create_font('garamond.ttf', size=h2))
        text("Measurement", 10, 10)
        
        text_font(create_font('garamond.ttf', size=h3))
        incr = 0
        for i in display_phrase:
            fill('black')
            text(i, 20, 110+incr)
            incr += h3+5

        if not spoken:
            speak(phrase1)
            spoken = True
    

    if status == 'continue':
        background(253,246,227)
        phrase1 = "Is the edema severe, moderate, mild, or not present?"
        
        display_phrase = word_wrap(phrase1, n=50)
        text_font(create_font('garamond.ttf', size=h2))
        text("Measurement", 10, 10)
        
        text_font(create_font('garamond.ttf', size=h3))
        incr = 0
        for i in display_phrase:
            fill('black')
            text(i, 20, 110+incr)
            incr += h3+5
        
        image(leg_swell_chart, 50,120+incr, 400,300)
        if not spoken:
            speak(phrase1)
            spoken = True
    
    if status == 'leg swelling':
        background(253,246,227)
        phrase1 = "Firmly press on the middle of the shin for at least two seconds. Then note how deeply the skin remains depressed. Let me know when to continue, or if you want me to repeat these instructions."
        #todo: repeating instructions not setup.
        display_phrase = word_wrap(phrase1, n=50)
        text_font(create_font('garamond.ttf', size=h2))
        text("Recording leg swelling...", 10, 10)
        
        text_font(create_font('garamond.ttf', size=h3))
        incr = 0
        for i in display_phrase:
            fill('black')
            text(i, 20, 110+incr)
            incr += h3+5
        
        image(leg_swell_image, 50,120+incr, 400,300)
        if not spoken:
            speak(phrase1)
            spoken = True
    
    if status == 'care plan':
        
        background(253,246,227)
        text_font(create_font('garamond.ttf', size=h1))
        text("Monday", 10, 10)
        text_font(create_font('garamond.ttf', size=h2))
        text("Morning", 10, 10+h1)
        
        text_font(create_font('garamond.ttf', size=h3))
        incr = 0
        for i in monday_morning_tasks:
            fill('black')
            text(i.capitalize(), 20, 190+incr)
            fill('white')
            square(10,210+incr,10)
            incr += 35    
        
        fill('black')
        text_font(create_font('garamond.ttf', size=h2))
        text("Evening", 10, 220+incr)
        
        text_font(create_font('garamond.ttf', size=h3))
        for i in monday_evening_tasks:
            fill('black')
            text(i.capitalize(), 20, 300+incr)
            fill('white')
            square(10, 320+incr, 10)
            incr += 35
            fill('black')
time.sleep(1)
person_obj = person()
run()
