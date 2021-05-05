import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)
    try:
        voice_data = r.recognize_google(audio, key=None, language='en-US', show_all=True)
    except sr.UnknownValueError:
        print("uve")
    print("uve")
