from logging import exception
from pytube import YouTube
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def openLocation():
    global name
    name = filedialog.askdirectory()
    
    if(len(name) > 0):
        error.config(text=name, fg="green")
        downloadVideo()
    else:
        error.config(text=name, fg="red")

def downloadVideo():
    try:
        choice = ytbChoice.get()
        url = URLentry.get()

        if(len(url) > 1):
            error1.config(text="")
            yt = YouTube(url)

            if(choice == choices[0]):
                stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
            
            elif(choice == choices[1]):
                stream = yt.streams.filter(progressive=True, file_extension="mp4").get_lowest_resolution()
            
            elif(choice == choices[2]):
                stream = yt.streams.filter(only_audio=True).first()

        else:
            error1.config(text="PAST URL AGAIN", fg="red")

        stream.download(name)
        error.config(text = "DOWNLOAD COMPLETED!", fg="green")

    except exception as err:
        print(err)    


window = Tk()
window.geometry("650x500")
window.minsize(650,500)
window.title("FREE YOUTUBE VIDEO DOWNLOADER(by BaDr-Junior-_)")

title = Label(window, text="Welcome to the best and free youtube video downloader", 
        fg="red", 
        font=('jost', 15)
        )
title.grid(row=0, padx=70, pady=20)

label1 = Label(window, text="enter a valid youtube URL: ",
         fg="black",
         font=('jost', 12)
         )
label1.grid(row=1)

URLentry = Entry(window, width=40, fg="blue", font=("jost", 15))
URLentry.grid(row=2)

error1 = Label(window, text="", fg="red", font=("jost", 13))
error1.grid(row=3, pady=20)

choiceLabel = Label(window, text="choose an option: ", fg="black", font=("jost", 15))
choiceLabel.grid(row=4)

choices = ["video high quality", "video low quality", "audio file"]
ytbChoice = ttk.Combobox(window, values=choices, font=("jost", 15))
ytbChoice.grid(row=5, pady=10)

downloadBtn = Button(window, command=openLocation,text="DOWNLOAD", width=20, fg="white",bg="red", font=("jost", 15))
downloadBtn.grid(row=6, pady=20)

error = Label(window, text="", fg="red", font=("jost", 13))
error.grid(row=7, pady=10)



window.mainloop()
"""

import tkinter as tk
from tkinter import filedialog as fd 

def callback():
    name= fd.askdirectory()
    if(len(name) > 0): 
        print(name)
    

tk.Button(text='Click to Open File', 
       command=callback).pack()
tk.mainloop()"""