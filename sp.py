import os
import requests
from tkinter import *
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pyaudio
import time
root = Tk()
root.geometry("500x500")
root.configure(bg='LightBlue3')
root.title("TEXT TO SPEECH AND SPEECH TO TEXT")
Label(root, text = "TEXT_TO_SPEECH AND SPEECH_TO_TEXT", font = "arial 10 bold", bg='CadetBlue2').pack()
Label(text ="----THANK YOU----", font = 'arial 15 bold', bg ='CadetBlue2' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='pink2',fg='DarkOrchid3').place(x=195,y=250)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=100,y=300)
       
def Text_to_speech():
        Msg=entry_field.get()
        speech = gTTS(text = Msg)
        speech.save('music.mp3')
        playsound('music.mp3')
        os.remove('music.mp3')
def Exit():
    root.destroy()
def Reset():
     Msg.set("")
def Speech_to_text():
 recognizer = sr.Recognizer()
 with sr.Microphone() as inputs:
    recognizer.adjust_for_ambient_noise(inputs)
    print("Please speak now")
    listening = recognizer.listen(inputs,phrase_time_limit=4)
    print("Analysing...")
    try:
        print(recognizer.recognize_google(listening))
    except:
        print("please speak again")
   
Button(root, text = "Speech to text", font = 'arial 15 bold' , command = Speech_to_text ,width = '20').place(x=125,y=100)
Button(root, text = "Text to speech", font = 'arial 15 bold' , command = Text_to_speech ,width = '20').place(x=125,y=180)
Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4',bg='salmon').place(x=210,y=350)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'salmon').place(x=100 , y = 350)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset,bg='salmon').place(x=300,y=350)

root.mainloop()
print("hello")
