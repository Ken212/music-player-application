from tkinter import *
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox

# Initialize the mixer
mixer.init()

# Create the main window
window = Tk()
window.geometry('400x400')
window.title("Python Music Player")
window.config(bg='#ADD8E6')  # Soft baby blue color

def help_me():
    tkinter.messagebox.showinfo("Help", "How can I help you?")

def browse_file():
    global filename
    filename = filedialog.askopenfilename()

# Create the menu bar
menubar = Menu(window)
submenu = Menu(menubar, tearoff=0)
window.config(menu=menubar)

menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=window.destroy)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About Us", menu=submenu)
submenu.add_command(label="Help", command=help_me)

def play_music():
    try:
        paused
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar["text"] = "Music is playing"
        except:
            tkinter.messagebox.showerror("File Error", "File Not Found")
    else:
        mixer.music.unpause()
        statusbar["text"] = "Music is resumed"

def stop_music():
    mixer.music.stop()
    statusbar["text"] = "Music is stopped"

def set_volume(value):
    volume = int(value) / 100
    mixer.music.set_volume(volume)

def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar["text"] = "Music is paused"

def rewind_music():
    play_music()
    statusbar["text"] = "Music is rewound"

# Create frames for layout
frame = Frame(window, bg='#ADD8E6')
frame.pack(pady=20)

# Play button
photo = PhotoImage(file='play1.png')
playButton = Button(frame, image=photo, command=play_music, bg='#ADD8E6', bd=0)
playButton.grid(row=0, column=0, padx=10)

# Stop button
stopphoto = PhotoImage(file="stop1.png")
stopButton = Button(frame, image=stopphoto, command=stop_music, bg='#ADD8E6', bd=0)
stopButton.grid(row=0, column=1, padx=10)

# Pause button
pausePhoto = PhotoImage(file="pause1.png")
pauseBtn = Button(frame, image=pausePhoto, command=pause_music, bg='#ADD8E6', bd=0)
pauseBtn.grid(row=0, column=2, padx=10)

# Bottom frame for volume control and rewind button
bottomframe = Frame(window, bg='#ADD8E6')
bottomframe.pack(pady=10)

# Rewind button
rewindPhoto = PhotoImage(file="rewind-button1.png")
rewindButton = Button(bottomframe, image=rewindPhoto, command=rewind_music, bg='#ADD8E6', bd=0)
rewindButton.grid(row=0, column=0, padx=10)

# Volume control
scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_volume, bg='#ADD8E6', highlightbackground='#ADD8E6')
scale.set(70)
scale.grid(row=0, column=1, padx=10)

# Status bar
statusbar = Label(window, text="Keep enjoying the music ...", relief=SUNKEN, anchor=W, bg='#ADD8E6', fg='black', font=('Arial', 10, 'italic'))
statusbar.pack(side=BOTTOM, fill=X)

window.mainloop()
