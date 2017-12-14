import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
from gtts import gTTS

from bs4 import BeautifulSoup

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    initial = True
    #with sr.Microphone() as source:
    r.dynamic_energy_threshold = True
    r.pause_threshold = 1

    while 1:
        print("Say something!")
        with sr.Microphone() as source:
            if initial == True:
                r.adjust_for_ambient_noise(source, duration=1 )
                initial = False
            audio = r.listen(source)
        # Speech recognition using Google Speech Recognition
        data = ""
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = r.recognize_google(audio, language = "en-IN")
            print("You said: " + data)
            break;
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            continue;
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

'''************************This function is used to fetch the Request Link for the given string name in the voice command*******************************'''
def fetchRequestLinkFromStringName(page, stringName):
    try:
        url = "Link Not Found"
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.find_all('a', href=True):
            print link.string.lower()
            #print link.get("href")
            
            if link.string.lower() == stringName.lower():
                print link.string.lower()
                url = link.get("href")
                print link.get("href")
                

    except Exception as e:
        print('Error:')
        print(e)
    return url

def fetchPostLinkFromClassName(page, stringName):
    try:
        url = "Link Not Found"
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.find_all('form', class_=stringName):
            print link.get('action')
            url = link.get('action')
            #print link.get("href")
            
                

    except Exception as e:
        print('Error:')
        print(e)
    return url
