import pyttsx3
import datetime
import smtplib # serveur d'envoie de EMAIL
import speech_recognition as rv #Biblio de reconnaissance vocale
import wikipedia
from info_conf import adresse_envoi, pwd, vers # importer les info confidentielle de compte d'envoie
from email.message import EmailMessage
engine = pyttsx3.init()

def parler(texte) :
    engine.say(texte)
    engine.runAndWait()

def getVoices(id):
    voices = engine.getProperty('voices')
    if id == 1 :
        engine.setProperty('voice',voices[0].id)
    elif id == 2 :
        engine.setProperty('voice',voices[1].id)
    elif id == 3 :
        engine.setProperty('voice',voices[2].id)
    parler("Bonjour vous avez changer la voix...")

def date() :
    annee= datetime.datetime.now().year
    mois = datetime.datetime.now().month
    jour = datetime.datetime.now().day
    parler("la date d'aujourd'hui est:")
    parler(jour)
    parler(mois)
    parler(annee)
def heure():
    T=datetime.datetime.now().strftime("%I:%M:%S")
    parler("l'heure actuelle est :")
    parler(T)
def formPolitesse():
    h=datetime.datetime.now().hour
    if h>=6 and h<12 :
        parler("Bonjour Monsieur!")
    elif h>=12 and h<18 :
        parler("Bon aprés-midi Monsieur!")
    elif h>=18 and h<24 :
        parler("Bon soir Monsieur!")
    else :
        parler("Bon fin de soiré Monsieur!")
    parler("Votre assistante vocale a votre service")
    parler("Comment puis-je vous aider Monsieur?")
def priseCMD():
    question= input("Comment puis-je vous aider Monsieur?")
    return question
def priseCmdMic():
    r=rv.Recognizer()
    with rv.Microphone() as source:
        print("Parler...\n")
        r.pause_threshold=2
        audio = r.listen(source)#signal sonore
    try :
        print("identification...")
        txt=r.recognize_google(audio,language="fr-FR")
        print(txt)
    except Exception as e :
        print(e)
        parler("je n'ai pas bien entendu. veuillez répetez...")
        return "None"
    return txt
def envoyerEmail() :
    serveur=smtplib.SMTP('smtp.gmail.com',587) # Simple Mail Transfer Protocole
    serveur.starttls() # TLS Transfer Layer Security
    serveur.login(adresse_envoi,pwd)
    serveur.sendmail(adresse_envoi,vers,'Salut je suis votre assistant')
    serveur.close()

def envoyerEmail2(destinataire,objet,contenu) :
    serveur=smtplib.SMTP('smtp.gmail.com',587) # Simple Mail Transfer Protocole
    serveur.starttls() # TLS Transfer Layer Security
    serveur.login(adresse_envoi,pwd)
    email=EmailMessage()
    email['From'] = adresse_envoi
    email['To'] = destinataire
    email['Subject']= objet
    email.set_content(contenu)
    serveur.send_message(email)
    serveur.close()

#      LE PROGRAMME PRINCIPALE
if __name__ == "__main__" :
    formPolitesse()
    while True :
        qs=priseCmdMic().lower()
        if 'heure' in qs:
            heure()
        elif 'date' in qs:
            date()
        elif 'quitter' in qs:
            parler("Au revoir Monsieur")
            quit()
        elif 'email' in qs:
            email_liste = {'professeur' : 'adil.chergui@ensam-casa.ma', 'étudiant' : 'bouchra.benghazala@ensam-casa.ma'}
            try :
                parler("A quui voulez-vous envoyer l'email ")
                nom = priseCmdMic().lower()
                destinataire=email_liste[nom]
                parler("le objet de l'email")
                objet=priseCmdMic()
                parler("le messsage a transmettre ?")
                contenu = priseCmdMic()
                envoyerEmail2(destinataire,objet, contenu)
                parler("message transmis")
            except Exception as e:
                print(e)
                parler("email non envoyé")
        elif 'wikipédia' in qs :
            parler('recherche wikipedia')
            qs=qs.replace("wikipédia","")
            wikipedia.set_lang("fr")
            resultat = wikipedia.summary(qs, sentences =2)
            print(resultat)
            parler(resultat)