from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
import datetime
import os

os.environ["PATH"] += os.pathsep + "C:\\Ensamc\\CI\\S4\\AI\ffmpeg-7.0-essentials_build\\bin"

def parler(speech):
    tts = gTTS(text=speech, lang='ar')
    tts.save("output.mp3")
    audio = AudioSegment.from_mp3("output.mp3")
    play(audio)

def heure():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    parler("الوقت الحالي هو")
    parler(current_time)

def date():
    now = datetime.datetime.now()
    current_date = now.strftime("%d %B %Y")
    parler("التاريخ الحالي هو")
    parler(current_date)

def deb_politesse():
    h = datetime.datetime.now().hour
    if 6 <= h < 12:
        parler("!صباح الخير")
    elif 12 <= h < 18:
        parler("!مساء الخير")
    elif 18 <= h <= 23:
        parler("!مساء الخير")
    else:
        parler("!تصبح على خير")


def priseCMDmicro():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("...تحدث")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("...التعرف على الكالم")
        req = r.recognize_google(audio, language="ar-SA")
        print(req)
    except sr.UnknownValueError:
        print("...لم أسمع بشكل جيد، يرجى تكراره")
        return"لا شيء" 
    except sr.RequestError:
        parler(".لا يمكن الوصول إلى خدمة التعرف على الكالم يرجى التحقق من الاتصال بالإنترنت")
        return"لا شيء" 
    return req

if __name__ == "__main__":
    deb_politesse()
    while True:
        req = priseCMDmicro().lower()
        if 'الوقت 'in req:
            heure()
        elif 'التاريخ 'in req:
            date()
        elif 'انهاء 'in req:
            parler("وداعًا")
        quit()