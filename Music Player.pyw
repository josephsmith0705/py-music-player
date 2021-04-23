from pygame import mixer  
from tkinter import filedialog 
from tkinter import *
import mutagen 

class Player:
    def __init__(self, master=None):
        self.master=master
        global pauseText
        global muteText
        global songName 
        global songLength
        muteText = StringVar()
        pauseText = StringVar()
        songName = StringVar()
        songLength = StringVar()
        muteText.set("🔇")
        self.master.title("Media Player") 
        self.master.configure(background="#FFEDF2")
        self.button=Button(text="📁", command=browseFile, font="verdana", bg="#F23269", fg="white", activebackground="#FF497D", activeforeground="white", height=1, width=6, bd=0, highlightthickness=5) #Creates the browse button
        self.button.place(relx=0.025, rely=0.5, anchor=W)#positions the button centre-left
        self.button=Button(textvariable=muteText, command=mute, font="verdana", bg="#F23269", fg="white", activebackground="#FF497D", activeforeground="white", height=1, width=6, bd=0, highlightthickness=5) #Creates the browse button
        self.button.place(relx=0.975, rely=0.5, anchor=E)#positions the button centre-left
        self.button=Button(textvariable=pauseText, command=pauseToggle, font="verdana 20", bg="#F23269", fg="white", activebackground="#FF497D", activeforeground="white", height=1, width=4, highlightthickness=6, bd=0)
        self.button.place(relx=0.5, rely=0.5, anchor=CENTER) #positions the button centre
        self.button=Button(text="+", command=volumeUp, font="verdana", bg="#F23269", fg="white", activebackground="#FF497D", activeforeground="white", height=1, width=6, bd=0)
        self.button.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.button=Button(text="-", command=volumeDown, font="verdana", bg="#F23269", fg="white", activebackground="#FF497D", activeforeground="white", height=1, width=6, bd=0)
        self.button.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.label=Label(textvariable=songName, font="verdana", bg="#FFEDF2")
        self.label.place(relx=0.5, rely=0.1, anchor=CENTER)
        
def browseFile():
    global musicRunning
    pauseText.set("⏸")
    fileName = filedialog.askopenfilename(filetypes = (("mp3 files",".mp3"),("wav files",".wav"))) 
    try: 
        mixer.music.load(fileName) 
        mixer.music.play()
        musicRunning=True
        metadata=mutagen.File(fileName, easy=True) 
        artist=str(metadata['artist'])[2:-2]
        title=str(metadata['title'])[2:-2]#Removes the first and last 2 characters as these are the square brackets
        songName.set(artist+" - "+title) 
    except: #If the program can't load the file, this may be because the user has cancelled the file dialog box. So, allow this error.
        pass

def pauseToggle():
    global musicRunning
    global fileName
    if musicRunning==True:
        mixer.music.pause()
        musicRunning=False
        pauseText.set("►")
    elif musicRunning==False:
        mixer.music.unpause()
        musicRunning=True
        pauseText.set("⏸")

def volumeUp():
    volume=mixer.music.get_volume()
    volume=volume+0.1
    mixer.music.set_volume(volume)

def volumeDown():
    volume=mixer.music.get_volume()
    volume=volume-0.1
    mixer.music.set_volume(volume)

def mute():
    global volume
    global musicMuted
    if musicMuted==True:
        mixer.music.set_volume(volume)
        musicMuted=False
        muteText.set("🔇")
    elif musicMuted==False:
        volume=mixer.music.get_volume()
        mixer.music.set_volume(0)
        musicMuted=True
        muteText.set("🔊")

musicMuted=False 
musicRunning=False
mixer.init()    
root = Tk() 
root.geometry("300x220") 
app = Player(root) 
root.resizable(0,0) 
browseFile()
root.mainloop()


