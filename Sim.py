import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import time
import youtube_dl
import re
from gtts import gTTS
import playsound
# de instalat si pyaudio
import requests
import wolframalpha
from tkinter import *
from tkinter import ttk
from youtubesearchpython import SearchVideos
import subprocess


#print(search.result())



# INTERFATA GRAFICA :
app = Tk()
app.title('Răzvi bot')
app.geometry('900x500')
app.resizable(False,False)


# Search
ttk.Label(app,text="Căutare după termeni:").place(x=10,y=5)
search = ttk.Entry(app)
search.place(x=150,y=5,width=300,height=23)

# Buttons
check_button = ttk.Button(app,text="Caută")
check_button.place(x=470,y=4)
save_button = ttk.Button(app,text="Salvare")
save_button.place(x=570,y=4)

# Progress TODO
progress = 0
progress_bar = ttk.Progressbar(app,orient=HORIZONTAL,length=185,mode='determinate',)
progress_bar.place(x=711,y=477)


app.mainloop()

def load_progress():
    global progress
    progress += 20;

def speak(text):
    tts = gTTS(text=text, Lang="en")
    filename= "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


    def get_audio():
        r= sr.Recognizer()
        with sr.Microphone() as source:
            audio= r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                print("Exception: "+ str(e))

                return said



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.getProperty('volume')
# print(voices[1].id)
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)



def spune(audio):
    engine.say(audio,)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        spune("Good Morning!")

    elif hour>=12 and hour<18:
        spune("Good Afternoon!")

    else:
        spune("Good Evening!")

    spune("I am Sim")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='ro')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('cosmin@gmail.com', '123425')
    server.sendmail('cosmin@gmail.com', to, content)
    server.close()




if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query


        if query.count("wikipedia") >= 1:
            load_progress()
            spune('Searching Wikipedia...')
            load_progress()
            load_progress()
            query = query.replace("wikipedia", "")
            try:
                load_progress()
                results = wikipedia.summary(query, sentences=2)
                spune("According to Wikipedia")
                #results = [i for i in results]
                results = results.replace('.', '.\n')
                print(results)
                spune(results)
                load_progress()
            except Exception:
                print("Page not found")
            finally:
                query = ''

        if query.count("youtube") >= 1:
            search = SearchVideos(query, 1, "json", 1).links[0]
            webbrowser.open(search)
            query = ''

        if 'google' in query:
            webbrowser.open("google.com")
            query = ''

        if 'stack' in query:
            webbrowser.open("stackoverflow.com")
            query = ''
        if 'redit' in query:
            webbrowser.open("reddit.com")
            query = ''
        if 'proiect' in query:
            webbrowser.open("https://github.com/arolariu/2NHACK2020")
            query = ''

        if 'meteo' in query:
            webbrowser.open("http://www.meteoromania.ro/")
            query = ''

        if 'spotify' in query:
            webbrowser.open("spotify.com")
            query = ''
        if 'melodie'  in query:
            music_dir = 'C:\\MUZICA'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            query = ''
        if 'ceasul' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            spune(f"Sir, the time is {strTime}")
            query = ''

        if query.count("xl") >= 1 or query.count("excel")>=1:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath)
            query = ''

        if query.count("prezentare") >= 1:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)
            query = ''

        if query.count("word") >= 1:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)
            query = ''







