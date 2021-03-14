#Importing Libraries
import pyttsx3
import wikipedia
import webbrowser
import speech_recognition as sr
import os
import datetime
#creating the engine and setting up the voices
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#speak function of voice assistant
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hr=int(datetime.datetime.now().hour)
    if hr>0 and hr<12:
        speak("Good Morning Sir")
    elif hr>12 and hr<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good evening sir")
    speak("I am Edith2.0 , your personal voice assistant. Please tell me how may I help you.")

if __name__ == '__main__':
    wishMe()
