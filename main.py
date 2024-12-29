#importing files
from typing import Mapping
import pyttsx3
import speech_recognition as sr
import os
import datetime
import wikipedia
import webbrowser
from win32com.client import WithEvents
from win32com.client.makepy import main
#voice of jarvis
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
#speak function
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)
if name== ' main ':
   def speak(audio):
     engine.say(audio)
     engine.runAndWait()
#wishing function
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
#speech recognising or taking command
def takeComand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("recongnising...")
        query=r.recognize_google(audio,language='en-in')
        print("user said:",query)
    except Exception as e :
        return "none"
    query= query. lower()
    return query
#main program calling all function
main
wishme()
speak("I am jarvis, how may I help you? ")
while True:
    query= takeComand(). lower()
    #introduction of jarvis
    if 'introduce' in query:
        speak("ok ma'am")
        wishme()
        speak("I am Just another really very intelligent system in shot J.A.R.V.I.S....... I am the first AI,artificial intelegence made by Suhani Verma..... I can do a lot of things and can make your work easier, though I need some more improvement but it seems good to see smiles on your faces while you are hearing me, aren't you smiling? hmmmmmmm")
    #telling time
    elif 'the time' in query:
        strtime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"ma'am the time is{strtime}")
    #wikipedia search
    elif 'wikipedia'in query:
        speak("searching on wikipedia...")
        query = query.replace("wikipedia", " ")
        results= wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    #opening youtube
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    #opening google
 elif 'open google' in query:
        webbrowser.open("google.com")
    #opening stakeoverflow
    elif 'open stakeoverflow' in query:
        webbrowser.open("stakeoverflow.com")
    #opening learn cbse
    elif 'open learn cbse' in query:
        webbrowser.open("learncbse.com")
    #playing movies
    elif 'play movies' in query:
        speak("ok here we go,")
        movies='D:\\MOVIE'
        picture= os.listdir(movies)
        os.startfile(os.path.join(movies,picture[0]))
    #playing music
    elif 'music' in query:
        speak("i think you will like this")
        music='D:\\music'
        mu= os.listdir(music)
        os.startfile(os.path.join(music,mu[0]))
        os.startfile(os.path.join(music,mu[1]))
        os.startfile(os.path.join(music,mu[2]))
        os.startfile(os.path.join(music,mu[3]))
    #defining ways of quiting
    elif 'quit' in query:
        speak("it was nice to have your time")
        quit()
    elif 'go to sleep' in query:
        speak("as you wish, ma'am")
        quit()
   elif 'give me a break' in query:
        speak("okay")
        quit()        
    elif'need a break' in query:
        speak("i feel the same")
        quit()
