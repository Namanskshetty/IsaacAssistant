from tkinter import *
from tkinter import filedialog
import os
import subprocess
import webbrowser
import datetime
import pygame
import sys
import time
#initilozing the pygame for music interface
pygame.mixer.init()

e = datetime.datetime.now()# gets the date i.e now
d = os.path.dirname(__file__) # opens absoulte path of the file
install=d+"\\temp\\install.ttg"
v=d+"\\temp\\install.py"
n=d+"\\temp\\name.ttg"
cam_f=d+"\\temp\\cam.ttg"
music_file=d+"\\temp\\music.ttg"
icon=d+"\\temp\\logo.ico"
present=d+"\\temp\\present.ttg"
ins=open(install,"r")
inst=int(ins.readline())
#creating the window
window = Tk()
window.geometry('920x720')
window.title("TTG Project")
window.iconbitmap(icon)
window.config(bg = "black")
pygame.mixer.music.load(d+"\\temp\\song.mp3")
if inst==0:
    pygame.mixer.music.play(-1)
    def play_pause():
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.pause()
        elif pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.unpause()
    def close():
        sys.exit()
    def pro():
        webbrowser.open('https://nimmaai.tech/')
    def clicked_install():
        subprocess.call("start cmd /c "+v, shell=True)
        #print("Installation is done closing in 5 Seconds")
        #close()
    lbbl = Label(window, text="Installation page", font=("Arial Bold", 50),bg="black", fg="#DDDDDD")
    lbbl.place(relx=0.5, rely=0.09, anchor="center")
    lbb2=Label(window, text="This is one time process only/ಒಂದು ಬಾರಿ ಪ್ರಕ್ರಿಯೆ ಮಾತ್ರ",font=("Arial Bold", 15),bg="black", fg="#FF8C32")
    lbb2.place(relx=0.5, rely=0.2, anchor="center")
    btt=Button(window,text="Download & install",bg="yellow", fg="red",command=clicked_install)
    btt.place(relx=0.5, rely=0.25, anchor="center")
    lbb3=Label(window, text="*This uses data connection to dwonload required libraries, also it takes some time to install",font=("Arial Bold", 10),bg="black", fg="red")
    lbb3.place(relx=0.5, rely=0.5, anchor="center")
    btt2=Button(window,text="ಸಹಾಯ/Help",bg="#DDDDDD", fg="blue",command=pro)
    btt2.place(relx=0.5, rely=0.55, anchor="center")
    lo=str(e.strftime("%a, %b %d, %Y"))
    lb5=Label(window, text="Today: "+lo, font=("Arial Bold", 18) ,bg="black", fg="Green")
    lb5.place(relx=0.5, rely=0.6, anchor="center")
    lbb3=Label(window, text="*After installtion the page automaticlly closes, open the exe file again after closing (Do not close the process in middle)",font=("Arial Bold", 10),bg="black", fg="red")
    lbb3.place(relx=0.5, rely=0.7, anchor="center")
    lbb3_k=Label(window, text="*ಅನುಸ್ಥಾಪನೆಯ ನಂತರ ಪುಟವು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಮುಚ್ಚುತ್ತದೆ, ಮುಚ್ಚಿದ ನಂತರ exe ಫೈಲ್ ಅನ್ನು ಮತ್ತೆ ತೆರೆಯಿರಿ (ಪ್ರಕ್ರಿಯೆಯನ್ನು ಮಧ್ಯದಲ್ಲಿ ಮುಚ್ಚಬೇಡಿ)",font=("Arial Bold", 8),bg="black", fg="red")
    lbb3_k.place(relx=0.5, rely=0.73, anchor="center")
    btt_music=Button(window,text="Play/Pause",bg="yellow", fg="black",command=play_pause)
    btt_music.place(relx=0.5, rely=0.8, anchor="center")
elif inst==1:
    #this is written so that only after installation the program runs
    na=open(n,'r')
    nam=str(na.readline())
    def pro():
        webbrowser.open('https://nimmaai.tech/')

    # declaring string variable
    name_var=StringVar()
    pass_var=StringVar()
    pass_var1=StringVar()
    #main project goes here
    lbl = Label(window, text="Welcome to SetUp "+nam, font=("Arial Bold", 50),bg="black", fg="#C4DDFF")
    lbl.place(relx=0.5, rely=0.09, anchor="center")
    lb2=Label(window, text="Enter your Name",font=("Arial Bold", 15),bg="black", fg="white")
    tx1=Entry(window,textvariable = name_var).place(relx=0.66, rely=0.2, anchor="center")
    lb2.place(relx=0.5, rely=0.2, anchor="center")

    #adding the name to text file
    def clicked():
        res=name_var.get()
        if res=="":
            res="User"
        new_name=open(n,'w')
        new_name.write(res)
        new_name.close()
        name_var.set("")
    bt=Button(window,text="Name",command=clicked)
    bt.place(relx=0.77, rely=0.2, anchor="center")

    ########
    def password_create():
        check2=pass_var.get()
        to_create=d+"\\temp\\password.ttg"
        hii=open(to_create,"w")
        hii.write(check2)
        hii.close()
    opt=d+"\\temp\\password.ttg"
    pass_cond1=open(opt,"r")
    pass_cond=pass_cond1.readline()
    def password():
        check=pass_var1.get()
        if check==pass_cond:
            pygame.mixer.music.load(d+"\\temp\\pass.mp3")
            pygame.mixer.music.play()
            pass_file_to=d+"\\main\\voice\\password.txt"
            os.system(pass_file_to)
        else:
            pygame.mixer.music.load(d+"\\temp\\wrong.mp3")
            pygame.mixer.music.play(1)
            time.sleep(2.4)
            print("Password wrong")
            exit()

    if pass_cond != "":
        lbqw1=Label(window, text="Enter your Password",font=("Arial Bold", 15),bg="black", fg="white")
        txqw1=Entry(window,textvariable = pass_var1).place(relx=0.72, rely=0.25, anchor="center")
        lbqw1.place(relx=0.5, rely=0.25, anchor="center")
        btqw1=Button(window,text="Open!",command=password)
        btqw1.place(relx=0.85, rely=0.25, anchor="center")
    else:
        lbqw=Label(window, text="Enter new your Password",font=("Arial Bold", 15),bg="black", fg="white")
        txqw=Entry(window,textvariable = pass_var).place(relx=0.72, rely=0.25, anchor="center")
        lbqw.place(relx=0.5, rely=0.25, anchor="center")
        btqw=Button(window,text="Password",command=password_create)
        btqw.place(relx=0.85, rely=0.25, anchor="center")

    #for camera
    def clicked_cam():
        # as we know cam value can only take int as values so definig the actulal values
        res_cam=variable.get()
        if res_cam == "Default":
            act_cam=0
        elif res_cam == "Web-Cam 1":
            act_cam=1
        elif res_cam == "Web-Cam 2":
            act_cam=2
        elif res_cam == "":
            act_cam=0
        new_cam=open(cam_f,'w')
        new_cam.write(str(act_cam))
        new_cam.close()
        variable.set("")
    #for present one
    ca=open(cam_f,'r')
    ca12=str(ca.readline())
    ca1=int(ca12)

    #setting up the camera modules with its values
    if ca1==0:
        ga="Default"
    elif ca1==1:
        ga= "Web-Cam 1"
    elif ca1==2:
        ga= "Web-Cam 2"

    lb3=Label(window, text="Your camera", font=("Arial Bold", 15) ,bg="black", fg="green")
    lb3.place(relx=0.5, rely=0.3, anchor="center")

    variable = StringVar()
    variable.set(ga) # default value

    w = OptionMenu(window, variable, "Default", "Web-Cam 1", "Web-Cam 2").place(relx=0.5, rely=0.36, anchor="center")
    bt21=Button(window,text="Submit Cam",command=clicked_cam)
    bt21.place(relx=0.5, rely=0.42, anchor="center")
    ##### for music folder ####

    mu=open(music_file,'r')
    music_name=str(mu.readline())

    #reads the file for ppt
    pu=open(present,'r')
    pre_name=str(pu.readline())

    #defining the clicking of music folder button
    def clicked_music():
        open_file = filedialog.askdirectory()
        music_name_dir=open(music_file,'w')
        music_name_dir.write(open_file)
        music_name_dir.close

    #defining the clicking of ppt folder button
    def clicked_pre():
        open_file2 = filedialog.askdirectory()
        pre_name_dir=open(present,'w')
        pre_name_dir.write(open_file2)
        pre_name_dir.close
    #starting voice module
    def start_pro():
        my_voice=d+"\\main\\voice\\main.py"
        subprocess.call("start cmd /c "+my_voice, shell=True)
        sys.exit()

    #startting of the page for the folder and date
    lb4=Label(window, text="Music folder: "+music_name, font=("Arial Bold", 18) ,bg="black", fg="yellow")
    lb4.place(relx=0.5, rely=0.5, anchor="center")
    bt22=Button(window,text="Select Dir",command=clicked_music)
    bt22.place(relx=0.5, rely=0.54, anchor="center")
    lb5=Label(window, text="PPT folder: "+pre_name, font=("Arial Bold", 18) ,bg="black", fg="#FFCD38")
    lb5.place(relx=0.5, rely=0.6, anchor="center")
    bt222=Button(window,text="Select Dir",fg="#6D8B74",command=clicked_pre)
    bt222.place(relx=0.5, rely=0.64, anchor="center")
    lo=str(e.strftime("%a, %b %d, %Y"))
    lb6=Label(window, text="Today: "+lo, font=("Arial Bold", 18) ,bg="black", fg="#F32424")
    lb6.place(relx=0.5, rely=0.7, anchor="center")
    btt_help=Button(window,text="ಸಹಾಯ/Help",bg="white", fg="blue",command=pro)
    btt_help.place(relx=0.5, rely=0.75, anchor="center")
    nam=nam.strip()
    music_name=music_name.strip()
    if nam=="User" and music_name=="Not found":
        print("give name")
    elif nam!="User":
        btt_start=Button(window,text="Start program",bg="white", fg="blue",command=start_pro)
        btt_start.place(relx=0.5, rely=0.8, anchor="center")
#do not try to add the update menu with the tkinter as pygame do not support
window.mainloop()#This makes the window open
