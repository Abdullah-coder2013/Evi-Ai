import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import json
import requests
import time

engine = pyttsx3.init('sapi5')

def speak(audio):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Abdullah!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon Abdullah!")   

    else:
        speak("Good Evening Abdullah!")  


    speak("How may I help you?")
    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Didn't get it...\n")   
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'what is' in query or 'who is' in query or 'where is' in query or 'why is' in query or 'how is' in query or 'what can' in query or 'who can' in query or 'where can' in query:
            question = query
            app_id="EQV68E-JQ7VX6VKQK"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)
             
        elif 'open website' in query:
            speak("Which Website should I open?")
            
            query = takeCommand().lower()
            speak(f"Opening {query}")
            webbrowser.open(query)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'introduce yourself' in query or 'who are you' in query:
            print("""
I am E.V.I or known as Efficient Virtual Intelligence.
I am developed by Abdullah Bin Abdul Munim.
I am from ErrorPage.Net.
I may not be considered to be like Alexa, Siri or Cortana.
But I can do something that will make you happy.
                  """)
            speak("""
I am E.V.I or known as Efficient Virtual Intelligence.
I am developed by Abdullah Bin Abdul Munim.
I am from ErrorPage.Net.
I may not be considered to be like Alexa, Siri or Cortana.
But I can do something that will make you happy.
                  """)
        
        elif 'what can you do' in query:
            print("""
I can do anything by one voice command.
For example I can open any website,
the time, answer your questions and predict the weather.
                  """)
            speak("""
I can do anything by one voice command.
For example I can open any website, any app,
the time, answer your questions and predict the weather.
                  """)

        elif 'close' in query:
            speak("Starting the AI Shutdown Process!")
            speak("Fairwell Abdullah!")
            break