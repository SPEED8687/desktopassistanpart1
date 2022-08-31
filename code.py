import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from time import strftime
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greetMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak('Good Morning Rivaan')
    elif(hour>=12 and hour<=16):
        speak('Good Afternoon Rivaan')
    elif(hour>16):
        speak('Good Evening Rivaan')
    speak("Hi I'm Your Desktop Assistant. How may I help you today?")
if(__name__=='__main__'):
    greetMe()