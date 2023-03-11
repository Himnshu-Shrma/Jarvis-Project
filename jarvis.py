from datetime import datetime
from unittest import result
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')#used to collect voioces (by microsoft)
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")
    speak("Jarvis is available at your service !! , How can I help you ")

def takeCommand():
    #It takes microphones input from user and returns string output 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm all ears...")
        r.pause_threshold = 1 #ctrl to get more options
        audio = r.listen(source)#ctrl to get more info/options
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User said:",query)
    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query



wishMe()


# while True:
if 1:
    query = takeCommand().lower()

    #logic for executing tasks based on query
    if 'wikipedia' in  query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia","")
        result= wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(result)
        speak(result)


    elif 'open youtube' in query:
        webbrowser.open("youtube.com",new = 1)


    elif 'open google ' in query:
        webbrowser.open("google.com",new = 1)


    elif 'open class ' in query:
        webbrowser.open("myclass.lpu.in",new = 1)
    elif 'open github' in query:
        webbrowser.open("github.com",new=1)

    elif 'play music ' in query:
        music_dir = 'F:\\A'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'the time' in query:
        strTime = datetime.now().strftime("%H:%M:%S")
        speak("Sir, the time is ",(strTime))
    elif 'open code' in query:
        codePath = "C:\\Users\\himan\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
        os.startfile(codePath)
    elif 'open game' in query:
        codePath = "D:\Grand Theft Auto V"
        os.startfile(codePath)
    # elif 'email to dad' in query:
    #     try:
    #         speak("What should I say?")
    #         content = takeCommand()
    #         to = "mksharma710d@gmail.com"
    #         sendEmail(to,content)
    #         speak("Email has been sent")
    #     except Exception as e:
    #         print(e)
    #         speak("Email cannot be sent")
