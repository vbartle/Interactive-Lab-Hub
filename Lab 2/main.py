import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = recognizer.listen(source)
    voice_data = recognizer.recognize_google(audio)
    print(voice_data)
