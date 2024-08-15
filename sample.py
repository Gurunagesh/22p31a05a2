import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pyautogui
import pyaudio

eng=pyttsx3.init('sapi5')
voices=eng.getProperty('voices')
eng.setProperty('voices',voices[0].id)

def speak(audio):
    eng.say(audio)
    eng.runAndWait()
#speak(" hii hellow guru")

def commands():
    r=sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Listening.....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(sourse,duration=1)
        audio=r.listen(sourse)
    try:
        print("wait for few moments...")
        query=r.recognize_google(audio,language='en-in')
        print(f"you should said:{query}\n")
    except Exception as e:
        print(e)
        speak("please tell me again..")
        query="none"
    return query
#query=commands().lower()
def wakwUpCmds():
    r=sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Listening.....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(sourse,duration=1)
        audio=r.listen(sourse)
    try:
        print("wait for few moments...")
        query=r.recognize_google(audio,language='en-in')
        print(f"you should said:{query}\n")
    except Exception as e:
        print(e)
        speak("please tell me again..")
        query="none"
    return query


def wishings():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("good morning boss")
        speak("good morning boss")
    elif hour>=12 and hour<17:
        print("good after noon  boss")
        speak("good afternoon boss")
    elif hour>=17 and hour<21:
        print("good evining boss")
        speak("good evining boss")
    else:
        print("good night boss")
        speak("good night boss")

if __name__ =="__main__":
    #wishings()
    while True:
        query=commands().lower()
        if 'wake up' in query:
            wishings()
            speak("yes boss what can i help for you!")

            while True:
                query=commands().lower()
                if 'time' in query:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    print(strTime)
                    speak(f"sir,the time is{strTime}")
                elif 'open firefox' in query:
                    speak("openig the firefox application sir.")
                    os.startfile(f"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
                elif 'wikipedia' in query:
                    speak("searching the wikipedia sir..")
                    try:
                        query=query.replace("wikipedia"," ")
                        results=wikipedia.summary(query,sentences=1)
                        speak("according to wikipidea is"," ")
                        print(results)
                        speak(results)
                    except:
                        speak("no result is founnd..")
                        print("no result is found....")
                elif 'mute' in query:
                    speak("i am mutting sir!")
                    break
                if 'open google' in query or 'open chrome' in query:
                    speak("opening the chrome sir..")
                    os.startfile(f"C:\Program Files\Google\Chrome\Application\chrome.exe")
                    while True:
                        chrquery=commands().lower()
                        if 'search' in chrquery:
                            ytubequery=chrquery
                            ytubequery=ytubequery.replace("search",' ')
                            pyautogui.write(ytubequery)
                            pyautogui.press('enter')
                            speak("searching sir....")
                        elif 'close chrome' in query:
                            pyautogui.hotkey('ctrl','w')
                            speak("closing the chrome application sir...")
                            break
                elif "magic words" in query:
                    speak("yes sir! your pleasure sir")
                    speak("this my good habit sir guru sir")