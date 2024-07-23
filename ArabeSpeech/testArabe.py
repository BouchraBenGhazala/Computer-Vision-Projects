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
    parler("الوقت الحالي هو:\n")
    parler(Heure)

def date():
    annee =int(datetime.datetime.now().year)
    mois =int(datetime.datetime.now().month)
    jour=int(datetime.datetime.now().day)
    parler("التاريخ الحالي هو :\n")
    parler(jour)
    parler(mois)
    parler(annee)
def deb_politesse():
    h=datetime.datetime.now().hour
    if h>= 6 and h<12:
        parler("!صباح الخير")
    elif h>= 12 and h<18:
        parler("!مساء الخير")
    elif h>= 18 and h<24:
        parler("!مساء الخير")
    else :
        parler("!تصبح على خير")

def priseCMD():
    req=input("كيف يمكنني مساعدتك")
    return req

def politesse():
    heure()
    date()
    parler("بوشرى في خدمتك. كيف يمكنني مساعدتك؟")

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
    print("كيف يمكنني مساعدتك")
    r=rv.Recognizer()
    with rv.Microphone() as source:
        print("تحدث...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("...التعرف على الكالم")
        req=r.recognize_google(audio,language="ar-AR")
        print(req)
    except Exception as e :
        print(e)
        parler("...لم أسمع بشكل جيد، يرجى تكراره")
        return "لا شيء"
    return req
#deb_politesse()
#politesse()

if __name__=="__main__" :
    getvoices(2) 
    deb_politesse()
    while True:
        #req=priseCMD().lower()
        req=priseCMDmicro().lower()
        if 'الوقت' in req :
            heure()
        elif 'التاريخ' in req :
            date()
        elif 'انهاء' in req :
            parler("وداعًا")
            quit()