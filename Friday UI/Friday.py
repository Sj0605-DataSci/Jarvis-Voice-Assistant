import subprocess
import sys
import pyttsx3
import winshell
import pyjokes
import ctypes
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib
import time
import requests
import sys
import operator
import cv2
import urllib.request as ur
import numpy as np
from urllib3 import *
from bs4 import BeautifulSoup
from requests import get
from selenium import *
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.uic import loadUiType
from FridayUI import  Ui_FridayGUI
from selenium_web import infow
from YT_auto import music
#from message import sendmessage


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('rate', 180)
engine.setProperty('voice', voices[0].id)

chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s"

def speak(audio):
        engine.say(audio)
        engine.runAndWait()
  

 

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning Sir !")

        elif hour>=12 and hour<18:
            speak("Good Afternoon Sir !")

        else:
            speak("Good Evening Sir !")

        assiname = ("Friday ")
        speak("I am your Assistant")
        speak(assiname)    
        speak("How may i help you")

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('xyz@gmail.com', 'password')
        server.sendmail('xyz2@gmail.com',to,content)
        server.close()


class Mainthread(QThread):
    def __init__(self):
        super(Mainthread,self).__init__()
    
    def run(self):
        self.TaskExecution()

    def username(self):
        speak("What should I call you Sir?")
        uname = self.takeCommand()
        speak("Welcome")
        speak(uname)

    def takeCommand(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.energy_threshold = 100000
                r.adjust_for_ambient_noise(source, 1.4)
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source,phrase_time_limit=5)
            try:
                    print("Recognising....")
                    query = r.recognize_google(audio, language='en-in')
                    print(f"User said: {query}\n")

            except Exception as e:
                # print(e)

                speak("Say that again please...")
                print("Say that again please...")
                self.takeCommand().lower()
            return query
    
    

    def TaskExecution(self):
        wishMe()
        self.username()
    
        while True:

            self.query = self.takeCommand().lower()

            if "write a note"  in self.query:
                speak("What should i write, sir")
                print("What should i write, sir")
                note = self.takeCommand()
                file = open('jarvis.txt', 'w')
                speak("Sir, Should i include date and time")
                print("Sir, Should i include date and time")
                snfm = self.takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
                
            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("jarvis.txt", "r")
                print(file.read())
                speak(file.read(6))
                
            if "wikipedia" in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=1)
                speak("According to wikipedia")
                print(results)
                speak(results)
            
            

            
            
            elif 'the time' in self.query:

                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif "open code" in self.query:
                codePath = "C:\\Users\\Sanyam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif "email to" in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand().lower()
                    to = "sanyam0605@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent !")

                except Exception as e:
                    print(e)
                    speak("Sorry Sir, I am not able to send this Email")
                    
            elif 'how are you' in self.query:
                speak("I am fine, Thank you !")
            
            elif 'who made you' in self.query:
                speak("I have been created by Sanyam.")
                    
            elif 'tell me a joke' in self.query:
                jokes = pyjokes.get_joke()
                speak(jokes)
                print(jokes)
                    
            elif 'who am i' in self.query:
                speak("If you talk then definately your human.")

            elif "why you came to the world" in self.query:
                speak("Thanks to Sanyam. further It's a secret")

            elif "is love" in self.query:
                speak("It is 7th sense that destroy all other senses")

            elif "who are you" in self.query:
                speak("I am your virtual assistant created by Sanyam")

            elif "reason for you" in self.query:
                speak("I was created as a Minor project by Mister Sanyam ")

            elif 'change background' in self.query:
                ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
                speak("Background changed succesfully")

            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'shutdown system' in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                        
            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")

            elif 'stop listening' in self.query:
                speak("for how much time you want to stop jarvis from listening commands")
                a = int(self.takeCommand())
                time.sleep(a)
                print(a)

            elif 'restart' in self.query:
                subprocess.call(["shutdown", "/r"])
                    
            elif 'sleep' in self.query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

            elif 'sign out' in self.query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            

            elif 'weather' in self.query:
                speak("which city weather you wanna know?")
                search = self.takeCommand().lower()
                url = f"https://www.google.com/search?q=weather+" + search
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current {search} is {temp}")
                
                

            elif 'will you be my gf' in self.query or 'will you be my bf' in self.query:  
                    speak("I'm not sure about, may be you should give me some time")
        
            elif 'how are you' in self.query:
                speak("I'm fine, glad you me that")
        
            elif 'i love you' in self.query:
                speak("It's hard to understand")
        
            
            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}") 
                print(ip)

            elif 'where am i' in self.query:
                res = requests.get('https://ipinfo.io/')
                data = res.json()
                
                country = data['country']
                city = data['city']
                region = data['region']
                print("Country:", country)
                print("Region:", region)
                print("City:", city)


            elif 'open youtube' in self.query:
                speak("Which song or video you want me to play?")
                x = self.takeCommand().lower()
                q = music()
                q.play(x)
            
            elif 'open google' in self.query:
                speak("What do you want me to search on google?")
                y = self.takeCommand().lower()
                q = infow()
                q.get_info(y)

            #elif "send message"  in self.query:
                #w = sendmessage()
                

            elif "can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate, example: 3 plus 3")
                    print("Say what you want to calculate, example: 3 plus 3")
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source, 1.2)
                    print("Listening...")
                    r.pause_threshold = 1
                    audio = r.listen(source,phrase_time_limit=5)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                        '+' : operator.add, #plus
                        '-' : operator.sub, #minus
                        '*' : operator.mul, #multiplied by
                        'divided' : operator.__truediv__,
                    }[op]

                def eval_binary_expr(op1,oper,op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1,op2)
                speak("your result is:")
                print("your result is:")
                speak(eval_binary_expr(*(my_string.split))) 
                print(eval_binary_expr(*(my_string.split)))   

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()        

            elif "open mobile camera" in self.query:
                URL = "http://192.168.0.100:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(ur.urlopen(URL).read()),dtype = np.uint8)
                    img = cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPWebcam',img)
                    q = cv2.waitKey(1)
                    if q ==  ord("q"):
                        break;
                cv2.destroyAllWindows() 

            elif "open team " or "open teams" in self.query:
                os.system("Microsoft Teams")           






            speak("Do you want me to do any other task?")
            print("Do you want me to do any other task?")
            u = self.takeCommand()
            if 'no' in u or 'exit' in u:
                speak("Thank you for your time")
                print("Thank you for your time")
                sys.exit()
            

                    




            
            



               

startExe = Mainthread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =  Ui_FridayGUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\Sanyam_Jain\\Desktop\\New folder\\iron-man-wallpaper-gif-1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\Sanyam_Jain\\Desktop\\New folder\\giphy.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\Sanyam_Jain\\Desktop\\New folder\\T8bahf.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExe.start()

    def showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date =now.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())