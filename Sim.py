import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from tkinter import *
from youtubesearchpython import SearchVideos

#INTERFATA GRAFICA:

app = Tk()
app.title('Soft Squad - School Assistant')
app.geometry('800x900')
app.resizable(False, False)
app.configure(bg='#000000')
frameCnt = 60
frames = [PhotoImage(file='Sufletul.gif', format = 'gif -index %i' %(i)) for i in range(frameCnt)]

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


def vorbit():
    global box
    query = takeCommand().lower()

    if query.count("wikipedia") >= 1:
        spune('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            spune("According to Wikipedia")
            results = results.replace('.', '.\n')
            box.insert('1.0', str(results))
            spune(results)
        except Exception as e:
            print(e)
            print("Page not found")
        finally:
            query = ''

    if query.count("youtube") >= 1:
        search = SearchVideos(query, 1, "json", 1).links[0]
        webbrowser.open(search)
        query = ''

    if query.count('stack') >= 1:
        webbrowser.open("stackoverflow.com")
        query = ''

    if query.count('traducere') >= 1:
        webbrowser.open("https://translate.google.com/")
        query = ''

    if query.count('vremea') >= 1:
        webbrowser.open("https://weather.com/weather/today/l/d47adb5123610c56b41dcb43c498eb3c8df0591918ce1d678bb6cbac3f50e386")
        query = ''

    if 'spotify' in query:
        webbrowser.open("spotify.com")
        query = ''

    if 'ceasul' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        spune(f"Sir, the time is {strTime}")
        query = ''

    if query.count("xl") >= 1 or query.count("excel") >= 1:
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


def update(ind):

    frame = frames[ind]
    ind += 3
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    app.after(100, update, ind)



label = Label(app)
label.pack()
Button(master = app, text="Push to talk!", command = vorbit, width=10, height=3).place(x=400, y=820)
box = Text(master=app, width=96, height=10, padx=3, pady=3)
box.place(x=10, y=610)
box1 = Text(master=app, width=100, height=0.5, bg='#000000', borderwidth=0)
box1.place(x=0, y=590)
app.after(0, update, 0)



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.getProperty('volume')
# print(voices[1].id)
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


if __name__ == "__main__":
    wishMe()
    app.mainloop()
