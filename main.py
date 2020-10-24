#Descriere: Programul este un asistent virtual care ofera data, ceasul, raspunde inapoi cu un 
#           salut la intamplare si returneaza informatii despre o persoana

#Librarii folosite ce trebuie instalate (Folosind Python 3.6 !!!)
#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTS
#pip install wikipedia  

#Librarii folosite
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
def inregistreazaAudio():

    # Inregistreaza sunetul
    r = sr.Recognizer() #Creaza un obiect de recunoastere

    #Deschide microfonul si inregistreaza
    with sr.Microphone() as source:
        print('Spune ceva!')
        audio = r.listen(source)

    # Foloseste recunoasterea vocala Google
    data = ''
    try:
        data = r.recognize_google(audio, None, 'ro-RO')
        print('Ai spus: ' + data)
    except sr.UnknownValueError: #Verifica pentru erori necunoscute
        print('Google Speech Recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error ' + e)

    return data

# O funcite pentru a obtine raspunsul asistentului
def raspunsAsistent(text):

    print(text)

    #Converteste textul in voce
    rasAsist = gTTS(text= text, lang='ro', slow=False) 

    #Salveaza audioul converit intr-o fila
    rasAsist.save('raspuns_asistent.mp3')

    #Deschide fila convertita
    os.system('start raspuns_asistent.mp3')

# O funcite pentru cuvintele/propozitiile de trezire 
def cuvantTrezire(text):
    CUVINTE_TREZIRE = ['hey spaghete', 'ok'] # O lista cu cuvinte de trezire

    text = text.lower() #Transformam textul in litere mici 

    #Verificam daca comanda/textul utilizatorul contine un cuvant/propozitie de trezire 
    for propozitie in CUVINTE_TREZIRE:
        if propozitie in text:
            return True

    # Daca cuvantul de trezire nu este gasit in textul din loop, returneaza False
    return False

# O functie pentru a obtine data calendaristica curenta
def obtineData():

    timp_acum = datetime.datetime.now()
    data_azi = datetime.datetime.today()
    numeZi = data_azi.weekday() #ex: Sambata
    numarLuna = timp_acum.month
    numarZi = timp_acum.day #ziua de azi, ex:24

    # O lista cu numele lunilor
    nume_luni = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie', 'iulie', 'august',
                   'septembrie', 'octombrie', 'noiembrie', 'decembrie']

    # O lista cu numele zilelor
    nume_zile = ['luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica']

    return 'Astazi suntem pe ' + str(numarZi) + ' ' + nume_luni[numarLuna - 1] + ', ' + nume_zile[numeZi] + '.'

# O funcite care returneaza un salut la intamplare
def salut(text):

    #Intrari pentru salut
    INTRARI_SALUT = ['salut', 'buna', 'hei', 'hey', 'ceau', 'sal', 'buna ziua', 'buna seara', 'neata',
                     'buna dimineata']

    #Raspunsuri pentru salut
    RASPUNS_SALUT = ['salut cumpanasule', 'salut!', 'buna sa-ti fie ziua', 'sa traiesti']

    # Daca intrarea utilizatorului este un salut, returneaza un salut aleator
    for cuvant in text.split():
        if cuvant.lower() in INTRARI_SALUT:
            return random.choice(RASPUNS_SALUT) + '.'

    # Daca niciun salut nu a fost detectat atunci returneaza un string gol
    return ''

# O functie care ia numele si prenumele unei persoane din text
def gasestePersoana(text):

    listaCuvinte = text.split() #Divizam textul intr-o lista de cuvinte

    for i in range(0, len(listaCuvinte)):
        if i + 3 <= len(listaCuvinte) - 1 and listaCuvinte[i].lower() == 'cine' and listaCuvinte[i+1].lower() == 'este':
            return listaCuvinte[i+2] + ' ' + listaCuvinte[i+3]


while True:

    #Inregistreaza audioul
    text = inregistreazaAudio()
    raspuns = ''

    # Verificam pentru cuvantul/propozitia de trezire
    if cuvantTrezire(text) == True:

        #Verificam daca utilizatorul a salutat
        raspuns = raspuns + salut(text)

        #Verificam daca utilizatorul a spus ceva legat de data
        if('data' in text):
            obtine_data = obtineData()
            raspuns = raspuns + ' ' + obtine_data


        #Verificam daca utilizatorul a spus ceva legat de timp
        if('timp' in text):
            ora = datetime.datime.now()

            #Convertim minutele in string
            if ora.minute < 10:
                minute = '0' + str(ora.minute)
            else:
                minute = str(ora.minute)

            raspuns = raspuns + ' ' + 'Este ora: ' + str(ora) + ":" +minute + '.'

        #Verificam daca utilizatorul a spus "cine este"
        if ('cine este' in text):
            persoana = gasestePersoana(text)
            wiki = wikipedia.summary(persoana, sentences=2)
            raspuns = raspuns + ' ' + wiki
        


        #Punem asistentul sa raspunda inapoi folosind audio si textul din raspuns
        raspunsAsistent(raspuns)  # AICI SE PRODUCE EROAREA, DACA SCRIETI pe linia 124 raspuns = 'ceva' o sa mearga 
        # (de ex: spuneti "ok, cine este lebron james", o sa va dea eroare ca cica nu a gasit text