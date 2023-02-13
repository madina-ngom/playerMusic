import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

super_groove= tkr.Tk()
super_groove.title('Groove Music Player')
super_groove.geometry("450x350")
super_groove.config(cursor="circle")
super_groove.config(bg="blue")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(super_groove, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE)

pygame.init()
pygame.mixer.init()


def playsong():
    currentsong = playlist.get(tkr.ACTIVE)
    print(currentsong)
    pygame.mixer.music.load(currentsong)
    pygame.mixer.music.play()

def pausesong():
    pygame.mixer.music.pause()

def resumesong():
    pygame.mixer.music.unpause()

def stopsong():
    pygame.mixer.music.stop()

def volume():
    pygame.mixer.music.set_volume(float/100)


pygame.mixer.init()
songstatus = tkr.StringVar()
playlist = tkr.Listbox(super_groove,selectmode=tkr.SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=35)
playlist.grid(columnspan=6)

for s in songstatus: 
    playlist.insert()


pausebtn=tkr.Button(super_groove, text="PAUSE", font="Roboto", command=pausesong, fg='DodgerBlue2', relief="groove", padx=7, pady=7)
pausebtn.grid(row=1, column=0)

playbtn=tkr.Button(super_groove, text="PLAY", font="Roboto", command=playsong, fg='DodgerBlue2', relief="groove", padx=7, pady=7)
playbtn.grid(row=1, column=1)

stopbtn=tkr.Button(super_groove, text="STOP", font="Roboto", command=stopsong, fg='DodgerBlue2', relief="groove", padx=7, pady=7)
stopbtn.grid(row=1, column=2)

unpausebtn=tkr.Button(super_groove, text="UNPAUSE", font="Roboto", command=resumesong, fg='DodgerBlue2', relief="groove", padx=7, pady=7)
unpausebtn.grid(row=1, column=3)

var = tkr.StringVar() 
song_title = tkr.Label(super_groove, font="Helvetica 12 bold", textvariable=var)


super_groove.mainloop()