import pyttsx3 #pip install pyttsx3 == installer texte to sppech
import datetime
engine = pyttsx3.init()
# prendre des commande à partir des commandes lignes
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
    parler("Alexa à votre service. Comment puis-je vous aider?")
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
   
deb_politesse()
politesse()

if __name__=="__main__" :
    deb_politesse()
    while True:
        req=priseCMD().lower()
        if 'heure' in req :
            heure()
        elif 'date' in req :
            date()