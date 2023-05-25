from tkinter import filedialog
from tkinter import*
import pygame
import os

root = Tk()
root.title("music player")
root.geometry("500x300")
pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs =[]
current_song =""
paused = False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext =='.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection.set(0)
    current_song = songs[songlist.curselection()[0]]

def play_music():
    global current_song, paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory,current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global pause
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song,paused

    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)+1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
def previous_music():
    global current_song, paused
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song)-1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


organise_menu=Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder',command=load_music)
menubar.add_cascade(label='Organise',menu=organise_menu)

songlist = Listbox(root, bg="black",fg="white", width=100,height=15)
songlist.pack()

next_btn_image = PhotoImage(file='next.png')
pause_btn_image = PhotoImage(file='pause.png')
play_btn_image = PhotoImage(file='play.png')
previous_btn_image = PhotoImage(file='previous.png')

control_frame = Frame(root)
control_frame.pack()
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command= next_music)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command= pause_music)
play_btn = Button(control_frame, image=play_btn_image, borderwidth=0,command= play_music)
previous_btn = Button(control_frame, image=previous_btn_image, borderwidth=0, command= previous_music)

next_btn.grid(row=0, column=0 ,padx=7, pady=10)
pause_btn.grid(row=0, column=1 ,padx=7, pady=10)
play_btn.grid(row=0, column=2 ,padx=7, pady=10)
previous_btn.grid(row=0, column=3 ,padx=7, pady=10)
root.mainloop()