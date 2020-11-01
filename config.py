import os
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
from youtubesearchpython import SearchVideos


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.getProperty('volume', 1.0)
engine.setProperty('rate', 178)
engine.setProperty('voice', voices[0].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        spune("Good morning to ya ladies!")

    elif hour>=12 and hour<18:
        spune("Good day ol' chaps!")

    else:
        spune("Bonne nuit, am I right?")

    spune("I'm SIM by the way!")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ro')
    except Exception:
        return "None"
    
    return query
def spune(audio):
    engine.say(audio,)
    engine.runAndWait()
def vorbit():
    query = takeCommand().lower()

    if query.find("wikipedia") != -1:
        spune('Searching Wikipedia...')
        try:
            results = wikipedia.summary(query, sentences=2)
            spune("According to Wikipedia:")
            results = results.replace('.', '.\n')
            spune(results)
        except Exception as e:
            spune("I couldn't understand you!")
    
    elif query.find("xl") != -1 or query.find("excel") != -1:
        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(codePath)

    elif query.find("prezentare") != -1 or query.find("powerpoint") != -1:
        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(codePath)

    elif query.find("word") != -1 or query.find("docs") != -1:
        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(codePath)

    elif query.find("youtube") != -1:
        search = SearchVideos(query, 1, "json", 1).links[0]
        webbrowser.open(search)

    elif query.find('traducere') != -1:
        webbrowser.open("https://translate.google.com/")

    elif query.find('vremea') != -1:
        webbrowser.open("https://weather.com/weather/today/l/d47adb5123610c56b41dcb43c498eb3c8df0591918ce1d678bb6cbac3f50e386")

    elif query.find('ceasul') != -1:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        spune(f"Sir, the time is {strTime}")

    elif query.find('stack') != -1:
        webbrowser.open("stackoverflow.com")

    elif query.find('spotify') != 1:
        webbrowser.open("spotify.com")
    
    else:
        spune("I did not understand that..")
