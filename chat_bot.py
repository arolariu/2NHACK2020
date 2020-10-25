#Descriere: Programul este un asistent virtual care ofera data, ceasul, raspunde inapoi cu un
#           salut la intamplare si returneaza informatii despre o persoana
#Librarii folosite (Python 3.6)

#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTS
#pip install wikipedia

#Librarii Folosite
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

# Ignora orice mesaj de avertizare
warnings.filterwarnings('ignore')


# Inregistreaza audioul si il returneaza ca un string
def recordAudio():
    # Inregistreaza sunetul
    r = sr.Recognizer()  #Creaza un obiect de recunoastere

    #Deschide microfonul si inregistreaza
    with sr.Microphone() as source:
        print('Spune ceva: ')
        audio = r.listen(source)
    # Foloseste recunoasterea vocala Google
    data = ''
    try:
        data = r.recognize_google(audio,None,language="ro-RO")
        print('Ai spus : ' + data)
    except sr.UnknownValueError:
        print('Nu te inteleg, mai repeta o data ')
    except sr.RequestError as e:
        print('Ups, reconfiguram ' + e)

    return data


recordAudio()


# O funcite pentru a obtine raspunsul asistentului
def assistantResponse(text):
    print(text)

    #Converteste textul in voce
    myobj = gTTS(text=text, lang='ro', slow=False)

    # Salveaza audioul converit intr-o fila
    myobj.save('assistant_response.mp3')

    #Deschide fila convertita
    os.system('start assistant_response.mp3')


# # O funcite pentru cuvintele/propozitiile ce pun in functiune robotul
def cuvantTrezire(text):
    cuvantTrezire = {'ok','hi','pip','cosmin','dani','razvan','chris','tu'}  # O lista cu cuvinte de trezire

    text = text.lower()  #Transformam textul in litere mici

    #Verificam daca comanda/textul utilizatorul contine un cuvant/propozitie de trezire
    for phrase in cuvantTrezire:
        if phrase in text:
            return True

    # Daca cuvantul de trezire nu este gasit in textul din loop, returneaza False
    return False


# Functia pentru obtinerii datii calendaristice corecte
def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]  # Sambata
    monthNum = now.month
    dayNum = now.day

   # O lista cu numele lunilor
    month_names = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie', 'iulie', 'august',
                   'septembrie', 'octombrie', 'noiembrie', 'decembrie']

    # O lista cu numele zilelor
    ordinalNumbers = ['1', '2', '3', ' 4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                      '14', '15', '16',
                      '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                      '29', '30', '31']

    return 'Astazi suntem pe '+ ordinalNumbers[dayNum - 1] +' '  + month_names[monthNum - 1] + ' .'


# O funcite care returneaza un salut la intamplare
def greeting(text):
    # Intrari pentru salut
    GREETING_INPUTS = ['salut', 'bună', 'hei', 'hey', 'ceau', 'ciao', 'sal', 'bună ziua', 'bună seara', 'neața',
                     'bună dimineața']

    #Raspunsuri pentru salut
    GREETING_RESPONSES = ['salut cumpănașule', 'salut boss!', 'bună să-ți fie ziua', 'să traiești', 'te pup barosane']

    # Daca intrarea utilizatorului este un salut, returneaza un salut aleator
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    # Daca niciun salut nu a fost detectat atunci returneaza un mesaj gol
    return ''


# # O functie care ia numele si prenumele unei persoane din text
def getPerson(text):
    wordList = text.split()  # Imparte textul intr-o lista de cuvinte

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'cine' and wordList[i + 1].lower() == 'este':
            return wordList[i + 2] + ' ' + wordList[i + 3]


while True:

    # inregistreaza audio-ul
    text = recordAudio()
    response = ''

    # Verificam pentru cuvantul/ propozitia de trezire
    if (cuvantTrezire(text) == True):

        #Verificam daca utilizatorul a salutat
        response = response + greeting(text)

        # Verificam daca utilizatorul a spus ceva legat de data
        if ('dată' in text):
            get_date = getDate()
            response = response + ' ' + get_date

        #Verificam daca utilizatorul a spus "cine este"
        if ('cine este' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        # assistant respond back using audio and text from response
        assistantResponse(response)