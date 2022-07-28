import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes
import random
import pyperclip
import re
import string
import requests
import json
import time as _time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import subprocess
import pickle
import os, signal
import pygame
#Decleraing global variables

# Get all the aspects for the name and other stuff
d = os.path.dirname(__file__)
pygame.mixer.init()
# Name fo the user
name_folder=d+"\\..\\..\\temp\\name.ttg"
name_set=open(name_folder,"r")
#dir for music
music_folder=d+"\\..\\..\\temp\\music.ttg"
music_set=open(music_folder,"r")
# To get child mode
child_folder=d+"\\..\\..\\temp\\child.ttg"
child_set=open(child_folder,"r")
child_act=child_set.readline()
child_act=child_act.strip()
print(child_act)
# To get ml model
clf=d+"\\clf_save"
cv=d+"\\cv_save"
# opening the ml profanity filter
def hate_speech(kuch_kuch):
    clfo=pickle.load(open(clf,"rb"))
    cvo=pickle.load(open(cv,"rb"))
    user=str(kuch_kuch)
    data=cvo.transform([user]).toarray()
    output = clfo.predict(data)
    if output == "No Hate and Offensive":
        return "fine"
    elif output == "Offensive Language":
        return "notatall"
    elif output == "Hate Speech":
        return "notatall"

def myvol(to):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if to == 100:
        volume.SetMasterVolumeLevel(-0.0, None) #max
    elif to> 50 and to<100:
        volume.SetMasterVolumeLevel(-5.0, None) #72%
    elif to==50:
        volume.SetMasterVolumeLevel(-10.0, None) #51%
    else:
        print("none")
def first_al_off():
    ppt_status_folder=d+"\\..\\..\\temp\\ppt.status"
    ppt_status_folder_set=open(ppt_status_folder,"w")
    ppt_status_folder_set.write("0")
    ppt_status_folder_set.close()
## QR
    qr_status_folder=d+"\\..\\..\\temp\\qr.status"
    qr_status_folder_set=open(qr_status_folder,"w")
    qr_status_folder_set.write("0")
    qr_status_folder_set.close()
###volume
    volume_status_folder=d+"\\..\\..\\temp\\volume.status"
    volume_status_folder_set=open(volume_status_folder,"w")
    volume_status_folder_set.write("0")
    volume_status_folder_set.close()
## emotion
    emotions_status_folder=d+"\\..\\..\\temp\\emotions.status"
    emotions_status_folder_set=open(emotions_status_folder,"w")
    emotions_status_folder_set.write("0")
    emotions_status_folder_set.close()
## MOUSE
    mouse_status_folder=d+"\\..\\..\\temp\\mouse.status"
    mouse_status_folder_set=open(mouse_status_folder,"w")
    mouse_status_folder_set.write("0")
    mouse_status_folder_set.close()
## aipainter
    aipainter_status_folder=d+"\\..\\..\\temp\\aipainter.status"
    aipainter_status_folder_set=open(aipainter_status_folder,"w")
    aipainter_status_folder_set.write("0")
    aipainter_status_folder_set.close()
##ai aitrainer
    aitrainer_status_folder=d+"\\..\\..\\temp\\aitrainer.status"
    aitrainer_status_folder_set=open(aitrainer_status_folder,"w")
    aitrainer_status_folder_set.write("0")
    aitrainer_status_folder_set.close()


print("stating......")
NAME=name_set.readline() #change it to your prefered NAME
songs_dir=music_set.readline() #add your music file directory here
ainame="isaac" # chang your personal assistant name here
engine=pyttsx3.init("sapi5") # micorphone driver sapi5
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id) #choosing male or female voice
def speak(text): #speaks the sent text
  engine.say(text)
  engine.runAndWait()

def wishMe(): #this code wishes the user and the global variable is set as NAME
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good morning.. "+NAME)
  elif hour>=12 and hour<6:
    speak("Good afternoon.. "+NAME)
  else:
    speak("Good evening "+NAME)

def stand():
    pygame.mixer.music.load(d+"\\..\\..\\temp\\stand.mp3")
    pygame.mixer.music.play()
    _time.sleep(1.2)
def sea():
    pygame.mixer.music.load(d+"\\..\\..\\temp\\search.mp3")
    pygame.mixer.music.play()
    _time.sleep(1.5)
def ppttt():
    ppt_write_folder=d+"\\..\\..\\temp\\ppt.status"
    ppt_write_set=open(ppt_write_folder,"r")
    ppt12=int(ppt_write_set.readline())
    return ppt12
def qrttt():
    qr_write_folder=d+"\\..\\..\\temp\\qr.status"
    qr_write_set=open(qr_write_folder,"r")
    qr12=int(qr_write_set.readline())
    print(qr12)
    return qr12
def volumettt():
    volume_write_folder=d+"\\..\\..\\temp\\volume.status"
    volume_write_set=open(volume_write_folder,"r")
    volume12=int(volume_write_set.readline())
    return volume12
def emotionsttt():
    emotions_write_folder=d+"\\..\\..\\temp\\emotions.status"
    emotions_write_set=open(emotions_write_folder,"r")
    emotions12=int(emotions_write_set.readline())
    return emotions12
def aitrainerttt():
    aitrainer_write_folder=d+"\\..\\..\\temp\\aitrainer.status"
    aitrainer_write_set=open(aitrainer_write_folder,"r")
    aitrainer12=int(aitrainer_write_set.readline())
    return aitrainer12
def aipainterttt():
    aipainter_write_folder=d+"\\..\\..\\temp\\aipainter.status"
    aipainter_write_set=open(aipainter_write_folder,"r")
    aipainter12=int(aipainter_write_set.readline())
    return aipainter12
def mousettt():
    mouse_write_folder=d+"\\..\\..\\temp\\mouse.status"
    mouse_write_set=open(mouse_write_folder,"r")
    mouse12=int(mouse_write_set.readline())
    return mouse12

  #speak("I am your personal assistant how may I help you")
def create(name_acc,password):
    a=str(name_acc)
    b=str(password)
    d = os.path.dirname(__file__)
    f=open(d+"\password.txt", "a+")
    w=str(a+" -> "+b)
    f.write(w)
    f.close()



#this function take the voice and convert into command from the microphone
def takeCommand():
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print("listening")
    audio = r.listen(source)
    try:
      print("Recognising")
      query=r.recognize_google(audio,language='en-in')
      print(f"user said: {query}\n")
    except Exception as e:
      print("could not understand..")
      query="hello"
    return query
def dangerch():
    pygame.mixer.music.load(d+"\\..\\..\\temp\\reading.mp3")
    pygame.mixer.music.play()
    _time.sleep(5.5)
# Main program starts here
if child_act=='yes':
    pygame.mixer.music.load(d+"\\..\\..\\temp\\start.mp3")
    pygame.mixer.music.play()
    _time.sleep(7.2)
else:
    pygame.mixer.music.load(d+"\\..\\..\\temp\\startoff.mp3")
    pygame.mixer.music.play()
    _time.sleep(13.5)
wishMe()
first_al_off()
def main():
    #ppt=ppttt()
    query=takeCommand()
    comm=query.lower()
    if ainame in comm:
        command=comm.replace(ainame,"")
        if "wikipedia" in command:#searching in wikipedia
            command=command.replace("wikipedia","")
            print(command)
            sea()
            if child_act=="yes":#child mode on
                beka=hate_speech(command)
                if beka =="fine":
                  speak("searching..")
                  results=wikipedia.wikipedia.summary(command,sentences=2)
                  speak(results)
                  page=wikipedia.wikipedia.page(results)# gets the page of wikki search
                  url=page.url# gets the url of the wikkipedia
                  speak("To know more check "+url)
                  print(url)
                elif beka=="notatall":
                    dangerch()
            elif child_act=="no":# child mode off
                speak("searching..")
                results=wikipedia.wikipedia.summary(command,sentences=2)
                speak(results)
                page=wikipedia.wikipedia.page(results)# gets the page of wikki search
                url=page.url# gets the url of the wikkipedia
                speak("To know more check "+url)
                print(url)

        elif "open youtube" in command:# to open youtube
            speak("opening youtube")
            webbrowser.open("https://youtube.com")

        ###############################################################################################################################
        elif "open ppt" in command:
            stand()
            ppt=ppttt()
            if ppt==1:
                speak("sorry ppt is already in use")
            elif ppt==0:
                ppt_fol=d+"\\..\\ppt.py"
                subprocess.call("start cmd /c "+ppt_fol, shell=True)
                ppt_status_folder=d+"\\..\\..\\temp\\ppt.status"
                ppt_status_folder_set=open(ppt_status_folder,"w")
                ppt_status_folder_set.write("1")
                ppt_status_folder_set.close()


        ### 2 ############2
        elif "open volume gesture" in command:
            stand()
            volume=volumettt(1)
            if volume==1:
                speak("sorry volume gesture is already in use")
            elif volume==0:
                volume_fol=d+"\\..\\volume.py"
                subprocess.call("start cmd /c "+volume_fol, shell=True)
                volume_status_folder=d+"\\..\\..\\temp\\volume.status"
                volume_status_folder_set=open(volume_status_folder,"w")
                volume_status_folder_set.write("1")
                volume_status_folder_set.close()
            else:
                print("went to else")

        ###### 3 #####
        elif "open qr code" in command:
            stand()
            qr1=qrttt()
            if qr1==1:
                speak("sorry qr code scanner is already in use")
            elif qr1==0:
                qr_fol=d+"\\..\\qr.py"
                subprocess.call("start cmd /c "+qr_fol, shell=True)
                qr_status_folder=d+"\\..\\..\\temp\\qr.status"
                qr_status_folder_set=open(qr_status_folder,"w")
                qr_status_folder_set.write("1")
                qr_status_folder_set.close()



        #######  4    @##############
        elif "open mouse" in command:
            stand()
            mouse=mousettt()
            if mouse==1:
                speak("sorry Mouse controll is already in use")
            elif mouse==0:
                mouse_fol=d+"\\..\\mouse.py"
                subprocess.call("start cmd /c "+mouse_fol, shell=True)
                mouse_status_folder=d+"\\..\\..\\temp\\mouse.status"
                mouse_status_folder_set=open(mouse_status_folder,"w")
                mouse_status_folder_set.write("1")
                mouse_status_folder_set.close()

        ######### 5 #######
       ''' elif "open emotion" in command:
            stand()
            emotions=emotionsttt()
            if emotions==1:
                speak("sorry emotion detection is already in use")
            elif emotions==0:
                emotion_fol=d+"\\..\\em\\Emotion\\emotions.py"
                subprocess.call("start cmd /c "+emotion_fol, shell=True)
                emotions_status_folder=d+"\\..\\..\\temp\\emotions.status"
                emotions_status_folder_set=open(emotions_status_folder,"w")
                emotions_status_folder_set.write("1")
                emotions_status_folder_set.close()'''

        ##############   6    ######
        elif "open painter" in command:
            stand()
            aipainter=aipainterttt()
            if aipainter==1:
                speak("sorry Ai painter is already in use")
            elif mouse==0:
                aipainter_fol=d+"\\..\\aipainter.py"
                subprocess.call("start cmd /c "+aipainter_fol, shell=True)
                aipainter_status_folder=d+"\\..\\..\\temp\\aipainter.status"
                aipainter_status_folder_set=open(aipainter_status_folder,"w")
                aipainter_status_folder_set.write("1")
                aipainter_status_folder_set.close()

        ##########     7     #$########
        elif "open trainer" in command:
            stand()
            aitrainer=aitrainerttt()
            if aitrainer==1:
                speak("sorry AI trainer is already in use")
            elif aitrainer==0:
                aitrainer_fol=d+"\\..\\aitriner.py"
                subprocess.call("start cmd /c "+aitrainer_fol, shell=True)
                aitrainer_status_folder=d+"\\..\\..\\temp\\aitrainer.status"
                aitrainer_status_folder_set=open(aitrainer_status_folder,"w")
                aitrainer_status_folder_set.write("1")
                aitrainer_status_folder_set.close()
################################################################################
        ##########   close  #####
        ####          1         ################
        elif "close ppt" in command:
            ppt=ppttt()
            if ppt==0:
                speak("sorry ppt is not opened")
            elif ppt==1:
                ppt_ttg_fol=d+"\\..\\..\\temp\\ppt.pid"
                ppt_pid_op=open(ppt_ttg_fol,"r")
                ppt_pid=int(ppt_pid_op.readline())
                os.kill(ppt_pid,9)
                ppt_status_folder=d+"\\..\\..\\temp\\ppt.status"
                ppt_status_folder_set=open(ppt_status_folder,"w")
                ppt_status_folder_set.write("0")
                ppt_status_folder_set.close()

        ########    2      ##########
        elif "close volume gesture" in command:
            volume=volumettt()
            if volume==0:
                speak("sorry volume gesture is not opened")
            elif volume!=0:
                print("VLOUME CLOSE")
                volume_ttg_fol=d+"\\..\\..\\temp\\volume.pid"
                volume_pid_op=open(volume_ttg_fol,"r")
                volume_pid=int(volume_pid_op.readline())
                print(volume_pid)
                os.kill(volume_pid,9)
                volume_status_folder=d+"\\..\\..\\temp\\volume.status"
                volume_status_folder_set=open(volume_status_folder,"w")
                volume_status_folder_set.write("0")
                volume_status_folder_set.close()

        ###########      3          ###########
        elif "close qr" in command:
            qr1=qrttt()
            if qr1==0:
                speak("sorry qr code scanner is not opened")
            elif qr1==1:
                qr_ttg_fol=d+"\\..\\..\\temp\\qr.pid"
                qr_pid_op=open(qr_ttg_fol,"r")
                qr_pid=int(qr_pid_op.readline())
                os.kill(qr_pid,9)
                qr_status_folder=d+"\\..\\..\\temp\\qr.status"
                qr_status_folder_set=open(qr_status_folder,"w")
                qr_status_folder_set.write("0")
                qr_status_folder_set.close()

        ###############      4    ################
        elif "close painter"  in command:
            aipainter=aipainterttt()
            if aipainter==0:
                speak("sorry aipainter is not opened")
            elif aipainter==1:
                aipainter_ttg_fol=d+"\\..\\..\\temp\\aipainter.pid"
                aipainter_pid_op=open(aipainter_ttg_fol,"r")
                aipainter_pid=int(aipainter_pid_op.readline())
                os.kill(aipainter_pid,9)
                aipainter_status_folder=d+"\\..\\..\\temp\\aipainter.status"
                aipainter_status_folder_set=open(aipainter_status_folder,"w")
                aipainter_status_folder_set.write("0")
                aipainter_status_folder_set.close()

        ################        5        #####
        elif "close trainer" in command:
            aitrainer=aitrainerttt()
            if aitrainer==0:
                speak("sorry aitrainer is not opened")
            elif aitrainer==1:
                aitrainer_ttg_fol=d+"\\..\\..\\temp\\aitrainer.pid"
                aitrainer_pid_op=open(aitrainer_ttg_fol,"r")
                aitrainer_pid=int(aitrainer_pid_op.readline())
                os.kill(aitrainer_pid,9)
                aitrainer_status_folder=d+"\\..\\..\\temp\\aitrainer.status"
                aitrainer_status_folder_set=open(aitrainer_status_folder,"w")
                aitrainer_status_folder_set.write("0")
                aitrainer_status_folder_set.close()

        ################        6        #####
        elif "close mouse" in command:
            mouse=mousettt()
            if mouse==0:
                speak("sorry mouse is not opened")
            elif mouse==1:
                mouse_ttg_fol=d+"\\..\\..\\temp\\mouse.pid"
                mouse_pid_op=open(mouse_ttg_fol,"r")
                mouse_pid=int(mouser_pid_op.readline())
                os.kill(mouse_pid,9)
                mouse_status_folder=d+"\\..\\..\\temp\\mouse.status"
                mouse_status_folder_set=open(mouse_status_folder,"w")
                mouse_status_folder_set.write("0")
                mouse_status_folder_set.close()

        ##############        7              #####
    '''    elif "close emotion" in command:
            emotions=emotionsttt()
            if emotions==0:
                speak("sorry emotion is not opened")
            elif emotions==1:
                emotion_ttg_fol=d+"\\..\\..\\temp\\emotion.pid"
                emotion_pid_op=open(emotion_ttg_fol,"r")
                emotion_pid=int(emotion_pid_op.readline())
                os.kill(emotion_pid,9)
                emotions=0'''
##################################################


        elif "open gmail" in command:# to open gmail
            speak("opening gmail")
            url = "https://mail.google.com/"
            webbrowser.open(url)

        elif "child mode off" in command: #turning the child mode off
            speak("Turning child mode off")
            pygame.mixer.music.load(d+"\\..\\..\\temp\\choff.mp3")
            pygame.mixer.music.play()
            _time.sleep(1)
            child_folder1=d+"\\..\\..\\temp\\child.ttg"
            child_set1=open(child_folder1,"w")
            child_set1.write("no")
            child_set1.close()

        elif "child mode on" in command: #turning the child mode on
            speak("Turning child mode on")
            pygame.mixer.music.load(d+"\\..\\..\\temp\\chon.mp3")
            pygame.mixer.music.play()
            _time.sleep(1)
            child_folder1=d+"\\..\\..\\temp\\child.ttg"
            child_set1=open(child_folder1,"w")
            child_set1.write("yes")
            child_set1.close()

        elif "open protonmail" in command:# to open protonmail
            speak("opening proton mail")
            url = "https://protonmail.com/"
            webbrowser.open(url)

        elif "open whatsapp" in command:# to open whatsapp
            speak("opening whatsapp web in browser")
            url = "https://web.whatsapp.com/"
            webbrowser.open(url)

        elif "open project" in command:# to open project on github
            speak("opening nimmaAI official website")
            url = "https://nimmaai.tech"
            webbrowser.open(url)

        elif "on youtube" in command: # to play music on youtube
            song=command.replace("on youtube","")
            sea()
            if child_act=="yes":#child mode on
                beka=hate_speech(song)
                if beka =="fine":
                    if "play" in song:
                        song=command.replace("play","")
                    speak("playing"+song)
                    pywhatkit.playonyt(song)
                elif beka=="notatall":
                    dangerch()
            elif child_act=="no":#child mode off
                if "play" in song:
                    song=command.replace("play","")
                speak("playing"+song)
                pywhatkit.playonyt(song)

        elif 'time' in command:# to tell the time
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)

        elif 'joke' in command:# search for pyjokes
            speak(pyjokes.get_joke())

        elif "play music" in command:# plays music on default music player
            if songs_dir=="Not found!!":
                speak("please specify your music directory in the code")
            else:
                speak("playing music on default music player")
                songs=os.listdir(songs_dir)# lists all the music from the directory
                print(len(songs))
                ma=int(len(songs))#suffles the music
                i=random.randint(0,ma)
                os.startfile(os.path.join(songs_dir,songs[i])) #This opens the file

        elif "search" in command:# this performs woogle searching
            sea()
            if child_act=="yes":#child mode on
                ui=command.replace("search","")
                beka=hate_speech(ui)
                if beka =="fine":

                    webbrowser.open("https://whoogle.sdf.org/search?q="+ui)
                else:
                    speak("Child mode on cannot search with the hate speach")
            elif child_act=="no":#child mode Off
                ui=command.replace("search","")
                webbrowser.open("https://whoogle.sdf.org/search?q="+ui)
            #can also replace the open with empty string and add the desired extension to the website in order to go the website of choice

        elif "generate password" in command:#generates password
            try:
                num = [int(word) for word in command.split() if word.isdigit()] # finds the integer value in the text
                lon = num[0]# limits the integer value to the first one
                letters = string.ascii_lowercase + string.digits + string.punctuation
                password = ''.join(random.choice(letters) for i in range(lon)) #gets the digit form the user
                print(password)
                pyperclip.copy(password)
                speak("password generated check password.txt file for the password also clipboard")
                name_acc=re.findall("for (\w+)",command)
                create(name_acc,password)
            except:
                letters = string.ascii_lowercase + string.digits + string.punctuation
                password = ''.join(random.choice(letters) for i in range(8)) # if user dosent specify the size of password 8 is used as default
                print(password)
                pyperclip.copy(password)
                speak("password generated with default size check password.txt file for the password also clipboard")
                name_acc=re.findall("for (\w+)",command)#searches for the account name
                create(name_acc,password)# create the file
        elif "set volume" in command:
            io=command.replace("set volume to","")
            to=int(io)
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            if volume.GetMute==0:
                myvol(to)
            else:
                volume.SetMute(0,None)#to make surte the the speakeres are not muted
                myvol(to)

        elif "mute" in command:
            print("mute")
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            volume.SetMute(1,None)
        elif "news headlines" in command:
            try:
                url = ('https://newsapi.org/v2/top-headlines?''country=in&'
                       'apiKey=a1061e9ef7a84860a763d1eda933c048')
                response = requests.get(url)
                news = json.loads(response.text)
                i=0
                for new in news['articles']:
                    # print(str(new['title']), "\n\n")
                    news_title = (str(new['title']))
                    speak(news_title)
                    _time.sleep(1)
                    i=i+1
                    if i==3:
                        break
            except:
                speak("No internet connection")
        elif "news description" in command:
            try:
                url = ('https://newsapi.org/v2/top-headlines?''country=in&'
                       'apiKey=a1061e9ef7a84860a763d1eda933c048')
                response = requests.get(url)
                news = json.loads(response.text)
                i=0
                for new in news['articles']:
                    # print(str(new['title']), "\n\n")
                    news_title = (str(new['description']))
                    speak(news_title)
                    _time.sleep(1)
                    i=i+1
                    if i==3:
                        break
            except:
                speak("No internet connection")
        #elif "volume gesture" in command:
            #d = os.path.dirname(__file__)
            #subprocess.call('start python '+d+'\volume.py', shell=True)

        elif "exit" in command:
            speak("bye.....")
            #### to remove all the process  ###
            ppt=ppttt()
            qr=qrttt()
            volume=volumettt()
            mouse=mousettt()
            aipainter=aipainterttt()
            emotions=emotionsttt()
            aitrainer=aitrainerttt()
            #for total exit
            if ppt==1:
                ppt_ttg_fol=d+"\\..\\..\\temp\\ppt.pid"
                ppt_pid_op=open(ppt_ttg_fol,"r")
                ppt_pid=int(ppt_pid_op.readline())
                os.kill(ppt_pid,9)
            if qr==1:
                qr_ttg_fol=d+"\\..\\..\\temp\\qr.pid"
                qr_pid_op=open(qr_ttg_fol,"r")
                qr_pid=int(qr_pid_op.readline())
                os.kill(qr_pid,9)
            if volume==1:
                volume_ttg_fol=d+"\\..\\..\\temp\\volume.pid"
                volume_pid_op=open(volume_ttg_fol,"r")
                volume_pid=int(volume_pid_op.readline())
                os.kill(volume_pid,9)
            if mouse==1:
                mouse_ttg_fol=d+"\\..\\..\\temp\\mouse.pid"
                mouse_pid_op=open(mouse_ttg_fol,"r")
                mouse_pid=int(mouser_pid_op.readline())
                os.kill(mouse_pid,9)
            if aipainter==1:
                aitrainer_ttg_fol=d+"\\..\\..\\temp\\aitrainer.pid"
                aitrainer_pid_op=open(aitrainer_ttg_fol,"r")
                aitrainer_pid=int(aitrainer_pid_op.readline())
                os.kill(aitrainer_pid,9)
            if emotions==1:
                emotion_ttg_fol=d+"\\..\\..\\temp\\emotion.pid"
                emotion_pid_op=open(emotion_ttg_fol,"r")
                emotion_pid=int(emotion_pid_op.readline())
                os.kill(emotion_pid,9)
            if aitrainer==1:
                aitrainer_ttg_fol=d+"\\..\\..\\temp\\aitrainer.pid"
                aitrainer_pid_op=open(aitrainer_ttg_fol,"r")
                aitrainer_pid=int(aitrainer_pid_op.readline())
                os.kill(aitrainer_pid,9)
            # returning to main program
            return 0 # changes the value of the while loop and stops the program

while True:
    a=main()
    if a==0: # if the function returns 0 the break statement stops the code from executing
        break
