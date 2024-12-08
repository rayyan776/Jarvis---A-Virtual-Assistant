import pyttsx3
import speech_recognition
import sys
import requests
import datetime
import bs4
from bs4 import BeautifulSoup
import threading
import pyautogui
import queue
import random
import os
import webbrowser
from plyer import notification
from pygame import mixer
import speedtest
from quiz import conduct_quiz

def check_password():
    for i in range(3):
        a = input("Enter Password to open Jarvis: ")
        
        
        try:
            with open("password.txt", "r") as pw_file:
                pw = pw_file.read().strip()  
        except FileNotFoundError:
            print("Password file not found. Please make sure 'password.txt' exists.")
            return

        if a == pw:
            print("WELCOME SIR! PLZ SPEAK [WAKE UP JARVIS] TO LOAD ME UP")
            break
        elif i == 2:
            print("Too many failed attempts. Exiting.")
            exit()
        else:
            print("Incorrect password. Try Again.")

check_password()



sys.stdout.reconfigure(encoding='utf-8')
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


speak_queue = queue.Queue()

def speak_thread():
    while True:
        audio = speak_queue.get()
        if audio is None:  
            break
        engine.say(audio)
        try:
            engine.runAndWait()   
        except RuntimeError:
            pass  

def speak(audio):
    speak_queue.put(audio)
    

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1.5
        r.energy_threshold = 400
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        return query
    except speech_recognition.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        speak("Sorry, I could not understand your speech.")
        return "None"
    except speech_recognition.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        speak("Network error. Could not reach speech recognition service.")
        return "None"
    except Exception as e:
        print(f"Error: {str(e)}")
        return "None"


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                    
                elif "play a game" in query:
                    from game import game_play
                    game_play() 
                    
                elif "career guidance" in query:
                    conduct_quiz()
                elif "exit" in query:
                    speak("Goodbye!")
                    break
                    
                elif "open" in query:   
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")     
                    
                elif "play a song" in query:  
                    speak("Playing your favourite song, sir")
                    song_choices = [
                        "https://www.youtube.com/watch?v=5CP9fycq8pk",  
                        "https://www.youtube.com/watch?v=o0LydWpBQts",  
                        "https://www.youtube.com/watch?v=asxmdFaIock"   
                        ]
                    random_song = random.choice(song_choices)
                    webbrowser.open(random_song)  
                    
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()  
                            
                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )            
                              
                          
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, sir")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)    
                    
                elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg") 
                     
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")     
                         
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
      

                elif "temperature" in query or "weather" in query:
                    search = "weather in Chennai"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    # Find temperature and condition
                    temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
                    condition = data.find("div", class_="BNeawe tAd8D AP7Wnd").text
                    speak(f"The current weather in Chennai is {condition} with a temperature of {temp}.")

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}") 

                elif "finally sleep" in query:
                    speak("Going to sleep, sir")
                    exit()
                    
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")    
                    
                elif "shutdown the system" in query:
                    speak("Are you sure you want to shut down? Please say yes or no.")
                    
                    
                    r = speech_recognition.Recognizer()
                    
                    with speech_recognition.Microphone() as source:
                        print("Listening for your response...")
                        audio = r.listen(source)

                    try:
                        response = r.recognize_google(audio, language='en-in').lower()
                        print(f"You said: {response}")

                        if "yes" in response:
                            speak("Shutting down the system now.")
                            os.system("shutdown /s /t 1")
                        elif "no" in response:
                            speak("Shutdown cancelled.")
                        else:
                            speak("I didn't hear a clear yes or no.")

                    except speech_recognition.UnknownValueError:
                        speak("Sorry, I could not understand your response.")
                    except Exception as e:
                        print(f"Error: {e}")
                
                    
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me " + remember.read())   