import os
import subprocess as sp
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import requests
import pywhatkit as kit
from email.message import EmailMessage
from decouple import config


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190) #set rate
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voice')
engine.setProperty('voice', voices[1].id)
paths ={
    'calculator':"C:||windows\\syatem32\\calc.exe"
    
    }
def speak(audio):
    engine.say(audio)
    engine.runAndwait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
        
    elif hour >= 12 and hour <18:
        speak('Good Afternoon')
        
    else:
        speak('Good Evening')
                
    speak('I am jarvis sir. Please tell me how i may hel[p you')
 
def takeCommand():
     
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
        print("Say that again please...")  
        return "None"
      return query 

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator']) 

def open_camera():
    sp.run('start microsoft.windows.camera:, shell=True')
    
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentenced=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)
    
def search_on_google(query):
    kit.search(query)
    
def send_whatsapp_message(number, message):
    kit.sendingmsg_instantly(f"+254{number}", message)
                       
if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences =2)
            speak('According to wikipedia')
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir, the time is {strTime}")
                           
        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
        
        elif 'open camera' in query:
            open_camera()
        
        elif 'open calculator' in query:
            open_calculator()
        
        elif 'youtube' in query: 
            speak('what do yoy want to play on youtube, sir?')
            video = take_user_input().loer()
            play_on_youtube(video)
        
        elif 'search on google' in query:
            speak('what do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)
        
        elif 'send whatsapp message' in query:
            speak('on what number should i send the message sir? please enter in the console:')
            number = input("Enter the number:")
            speak("what is the messsage sir?")
            message = take_user_input().lower()
            send_whatsapp_mesaage(number, message)
            speak("i have sent the message sir") 
              
                           