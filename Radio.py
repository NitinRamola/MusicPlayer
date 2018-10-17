
# coding: utf-8

# In[2]:


import tkinter.messagebox
from pygame import mixer
from tkinter import *
from tkinter import filedialog
import os

#creating a frame/window
window = Tk()

#initializing mixer
mixer.init()

#adding title
#window.geometry('450x420')
window.title("DeepuRadioPlayer")
window.iconbitmap(r'C:\Users\ramola\Desktop\Python\Projects\MediaPlayer\img\tower.ico')

#adding label
text= Label(window,text="DeepuRadio : Enjoy it !")
text.pack()

#currentfile = "C:\\Users\\ramola\\Desktop\\Git_Hub\\MusicPlayer\\Songs\\01 Ishq Di Baajiyaan - Soorma  (SongsMp3.Com).mp3"

def play_btn():
    try:
        paused
    except:

        try:
            mixer.music.load(currentfile)
            mixer.music.play()
            statusbar['text'] = 'Playing Song :'+ " " + os.path.basename(currentfile)
        except :
            tkinter.messagebox.showerror("No Song Selected","Please select a song first.")

    else:
        mixer.music.unpause()
    
def pause_btn():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = 'Music Paused :' + " " + os.path.basename(currentfile)

def stop_btn():
    mixer.music.stop()
    statusbar['text'] = 'Music Stopped :' + " " + os.path.basename(currentfile)

def set_volume(val):
    volume = int(val)/100 #set_volume takes value b/w 0 and 1
    mixer.music.set_volume(volume)


def next_btn():
    mixer.music.play()
    statusbar['text'] = "Playing next song"

def rewind_btn():
    mixer.music.play()
    statusbar['text'] = "Playing Again"

muted  = FALSE
def mute_btn():
    global muted
    if muted:
        mixer.music.set_volume(20)
        mutebtn.config(image=mutephoto)
        muted = FALSE
    else:
        mutebtn.config(image=volumephoto)
        mixer.music.set_volume(0)
        muted = TRUE

def on_closing_window():
    mixer.music.stop()
    window.destroy()
    
def about_us():
    tkinter.messagebox.showinfo("MusicPlayer","This is version 1.0")
    
def browse_file():
    global currentfile
    currentfile = filedialog.askopenfilename()



        
#Events define on closing window
window.protocol("WM_DELETE_WINDOW",on_closing_window)

#Adding frame in the window
middleframe = Frame(window)
middleframe.pack(padx=10,pady=10)

#Adding a bottom frame
bottomframe = Frame(window)
bottomframe.pack(padx=10,pady=10)

#adding play button 
playphoto = PhotoImage(file='C:\\Users\\ramola\\Desktop\\Git_Hub\\MusicPlayer\\img\\play.png')
playbtn = Button (middleframe, image = playphoto,command = play_btn)
playbtn.grid(row=0, column=2)

#adding pause button
pausephoto = PhotoImage(file='C:\\Users\\ramola\\Desktop\\Git_Hub\\MusicPlayer\\img\\pause.png')
pausebtn = Button(middleframe,image =pausephoto,command =pause_btn)
pausebtn.grid(row=0, column=1)

#adding stop button
stopphoto = PhotoImage(file='C:\\Users\\ramola\\Desktop\\Git_Hub\\MusicPlayer\\img\\stop.png')
stopbtn = Button(middleframe, image =stopphoto, command = stop_btn)
stopbtn.grid(row=0, column=3)

#adding next button
nextphoto = PhotoImage(file='C:\\Users\\ramola\\Desktop\\Git_Hub\\MusicPlayer\\img\\next.png')
nextbtn= Button(middleframe, image=nextphoto, command = next_btn)
nextbtn.grid(row=0,column=4)

#adding rewind button
rewindphoto = PhotoImage(file='C:\\Users\\ramola\\Desktop\\Git_Hub\\MusicPlayer\\img\\rewind.png')
rewindbtn = Button(middleframe,image=rewindphoto, command = rewind_btn)
rewindbtn.grid(row=0,column=0)

#creating a mute button
mutephoto = PhotoImage(file='C:\\Users\\ramola\\Desktop\\Git_Hub\\MusicPlayer\\img\\mute.png')
volumephoto = PhotoImage(file='C:\\Users\\ramola\\Desktop\\Git_Hub\\MusicPlayer\\img\\volume.png')
mutebtn = Button(bottomframe,image=mutephoto, command = mute_btn)
mutebtn.grid(row=0,column=0)


#Creating a scale widget
scale = Scale(bottomframe,from_=0, to =100, orient=HORIZONTAL,command = set_volume)
scale.set(20)
mixer.music.set_volume(20/100)
scale.grid(row=0, column=1 , padx = 10)

#creating a menubar
menubar = Menu(window)
window.config(menu=menubar)

#creating a File submenu
menu1 = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=menu1)
menu1.add_command(label="Open",command = browse_file)
menu1.add_command(label="Exit", command=on_closing_window)

#creating a Help submenu
menu2= Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=menu2)
menu2.add_command(label="About",command=about_us)
menu2.add_command(label="Contact Us")

#creating status bar
statusbar = Label(window,text="Status :", relief = SUNKEN, anchor = W)
statusbar.pack(side=BOTTOM, fill = X)

#looping the window to appear for infinite time until user kills it.
window.mainloop()

