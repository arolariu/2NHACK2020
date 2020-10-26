import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
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

    spune("I am Mircea")

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('birligeacosmin@gmail.com', 'morisette1')
    server.sendmail('birligeacosmin@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            spune('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            spune("According to Wikipedia")
            print(results)
            spune(results)

        if 'youtube' in query:
            webbrowser.open("youtube.com")


        if 'google' in query:
            webbrowser.open("google.com")

        if 'plagiat' in query:
            webbrowser.open("stackoverflow.com")   
        if 'ceva' in query:
            webbrowser.open("reddit.com")
        if 'proiect' in query:
            webbrowser.open("https://github.com/arolariu/2NHACK2020")
        if 'meteo' in query:
            webbrowser.open("http://www.meteoromania.ro/")

        if 'spotify' in query:
            webbrowser.open("spotify.com")

        if 'melodie'  in query:
            music_dir = 'C:\\MUZICA'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        if 'ceasul' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            spune(f"Sir, the time is {strTime}")

        if 'fila' in query:
            codePath = "C:\\Users\\Cosmin\\PycharmProjects\\pythonProject1\\josh.py"
            spune("Felicitari, ai deschis fisierul")

        elif 'mesaj' in query:
            try:
                spune("Ce sa ii scriu")
                content = takeCommand()
                to = "birligeacosmin@yahoo.com"
                sendEmail(to, content)
                spune("Email has been sent!")
            except Exception as e:
                print(e)
                spune("E BUN")

        if 'glumă'or 'gluma' in query:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept": "application/json"}
            )
            if res.status_code == requests.codes.ok:
                spune(str(res.json()['joke']))
            else:
                spune('oops!I ran out of jokes')


            os.startfile(codePath)



