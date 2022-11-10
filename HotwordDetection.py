import speech_recognition as sr
import os


def Listen():

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
        #NOISE L M A O 
    try:
        print("Recognizing")
        query = r.recognize_google(audio,language="en")
        
    except:
        return ""
    
    query = str(query).lower()
    return query

def Wakeupdetected():
    query = Listen().lower()

    if "wake up" in query:
        os.startfile(r"C:\Users\Nasreen\OneDrive\Desktop\Eternity 154\Main.py")

    else:
        pass


while True:
    Wakeupdetected()
