#stage 3 commandes vocale
import speech_recognition as rv #pip install SpeechRecongnition == installation de la reconnaissance vocale rv
import pyttsx3 #pip install pyttsx3 == installer texte to speech
#pip install PyAudio est aussi necessaire
import datetime
engine = pyttsx3.init()
# prendre des commande à partir du microphone
rate = engine.getProperty('rate')   # spécifier le rate
def heure():
    Heure = datetime.datetime.now().strftime("%I:%M:%S")
    parler("l'heure actuelle est :\n")
    parler(Heure)

def date():
    annee =int(datetime.datetime.now().year)
    mois =int(datetime.datetime.now().month)
    jour=int(datetime.datetime.now().day)
    parler("la date actuelle est :\n")
    parler(jour)
    parler(mois)
    parler(annee)
def deb_politesse():
    h=datetime.datetime.now().hour
    if h>= 6 and h<12:
        parler("Bon début de journée Monsieur!")
    elif h>= 12 and h<18:
        parler("Bonne aprés-midi Monsieur!")
    elif h>= 18 and h<24:
        parler("Bon soir Monsieur!")
    else :
        parler("Bonne nuit Monsieur!")
def priseCMD():
    req=input("Comment puis-je vous aider?")
    return req

def politesse():
    heure()
    date()
    parler("Meriam à votre service. Comment puis-je vous aider?")
def parler (speech):
    engine.say(speech)
    engine.runAndWait()
def getvoices(voice):
    voices=engine.getProperty('voices')
   
    if voice == 1:
        print(voices[0].id)
        print(voices[0].languages)
        engine.setProperty('voice',voices[0].id)
    if voice == 2:
        print(voices[1].id)
        engine.setProperty('voice',voices[1].id)
    if voice == 3:
        print(voices[2].id)
        engine.setProperty('voice',voices[2].id)

def priseCMDmicro():
    r=rv.Recognizer()
    with rv.Microphone() as source:
        print("Parler...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("identification...")
        req=r.recognize_google(audio,language="fr-FR")
        print(req)
    except Exception as e :
        print(e)
        parler("j'ai pas bien entendu, veuillez répetez ...")
        return "Rien"
    return req
#deb_politesse()
#politesse()

if __name__=="__main__" :
    deb_politesse()
    while True:
        #req=priseCMD().lower()
        req=priseCMDmicro().lower()
        if 'heure' in req :
            heure()
        elif 'date' in req :
            date()
        elif 'quitter' in req :
            parler("au revoir Monsieur")
            quit()