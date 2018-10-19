
# coding: utf-8

# In[2]:


import tkinter.messagebox
from pygame import mixer
from tkinter import *
from tkinter import filedialog
import os
from mutagen.mp3 import MP3
import time
import threading
from tkinter import ttk
from ttkthemes import themed_tk as tk



#creating a frame/window- Contains the Stauts bar, right frame & left frame
window = tk.ThemedTk()
window.get_themes()
window.set_theme('clearlooks')

#initializing mixer
mixer.init()

threadstatus = FALSE
def song_details(current_file):
    global threadstatus
    global total_length
    songtext['text'] = "Playing : " + os.path.basename(current_file)
    print("hello1")
    file_data = os.path.splitext(current_file)#splitting the filepath and extension
    print("hello2")
    if file_data[1] ==".mp3":
        audio = MP3(current_file)
        total_length = audio.info.length
    else:
    # Calculating the lenght of the song
        a = mixer.Sound(current_file)
        total_length = a.getlength()

    mins, secs = divmod(total_length, 60)
    mins=int(mins)
    secs=int(secs)
    timeformat = '{:02d}:{:02d}'.format(mins,secs)
    lengthlabel['text'] = "Total length : " + timeformat

    thread1 = threading.Thread(target=start_count, args=(total_length,))
    thread1.start()


def start_count(t):
    #mixer.music.get_busy() returns TRUE/FALSE value based on if music is STOPPED.
    global paused
    current_time_count=0
    while t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time_count, 60)
            mins = int(mins)
            secs = int(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = "Current Time : " + timeformat
            time.sleep(1)
            current_time_count +=1


#currentfile = "C:\\Users\\ramola\\Desktop\\Git_Hub\\MusicPlayer\\Songs\\01 Ishq Di Baajiyaan - Soorma  (SongsMp3.Com).mp3"
paused = FALSE
def play_btn():
    global paused
    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"
        paused = FALSE
    else:
        try:
            stop_btn()
            time.sleep(1)
            selected_song = listbx.curselection()
            selected_song = int(selected_song[0])
            currentfile_path = playlist[selected_song]
            mixer.music.load(currentfile_path)
            mixer.music.play()
            statusbar['text'] = 'Playing Song :'+ " " + os.path.basename(currentfile_path)
            song_details(currentfile_path)

        except Exception as err:
            print(err)
            tkinter.messagebox.showerror("No Song Selected","Please select a song first.")





def pause_btn():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = 'Music Paused :' + " " + os.path.basename(currentfile_path)

def stop_btn():
    mixer.music.stop()
    statusbar['text'] = 'Music Stopped :' + " " + os.path.basename(currentfile_path)

def set_volume(val):
    if int(val) ==0:
        mutebtn.config(image=volumephoto)
    else:
        volume = int(val)/100 #set_volume takes value b/w 0 and 1
        mixer.music.set_volume(volume)
        mutebtn.config(image=mutephoto)

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
        mixer.music.set_volume(.2)
        scale.set(20)
        mutebtn.config(image=mutephoto)
        muted = FALSE
    else:
        mutebtn.config(image=volumephoto)
        mixer.music.set_volume(0)
        scale.set(0)
        muted = TRUE

def on_closing_window():
    mixer.music.stop()
    window.destroy()
    
def about_us():
    tkinter.messagebox.showinfo("MusicPlayer","This is version 1.0")
    
def browse_file():
    global currentfile_path
    currentfile_path = filedialog.askopenfilename()
    add_to_playlist(currentfile_path)

def delete_song():
    selected_song = listbx.curselection()
    selected_song = int(selected_song[0])
    listbx.delete(selected_song)
    playlist.remove(selected_song)

#function to add songs to the playlist
index=0
playlist = []
def add_to_playlist(songvar):
    global index
    listbx.insert(index,os.path.basename(songvar))
    playlist.insert(index,currentfile_path)
    index += 1

#adding title
window.geometry('550x320')
window.title("DeepuRadioPlayer")
window.iconbitmap(r'C:\Users\ramola\Desktop\Python\Projects\MediaPlayer\img\tower.ico')

#creating status bar
statusbar = Label(window,text="Status :", relief = SUNKEN, anchor = W)
statusbar.pack(side=BOTTOM, fill = X)

#Events define on closing window
window.protocol("WM_DELETE_WINDOW",on_closing_window)

#adding title
#window.geometry('550x320')
window.title("DeepuRadioPlayer")
window.iconbitmap(r'C:\Users\ramola\Desktop\Python\Projects\MediaPlayer\img\tower.ico')


#.............................................Frame Area..........................................................
        
#creaing a left frame & right frame
leftframe =Frame(window)
leftframe.pack(side = LEFT, padx=10)
rightframe = Frame(window)
rightframe.pack(side = RIGHT,padx=10)


#Adding frame in the window
#Adding a top frame in right frame
topframe = Frame(rightframe)
topframe.pack(side = TOP)

#adding middle frame in right frame
middleframe = Frame(rightframe)
middleframe.pack(pady=10)

#Adding a bottom frame
bottomframe = Frame(rightframe)
bottomframe.pack(side = BOTTOM, pady=10)




#............................Label.........................................................
#adding label
songtext= Label(topframe,text="DeepuRadio : Enjoy it !")
songtext.pack()


#adding song length label
lengthlabel =  Label(topframe,text="Total Time --:--")
lengthlabel.pack(pady=10,padx=10)


#adding current time label
currenttimelabel = Label(topframe,text='Current time : --:--')
currenttimelabel.pack()


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

#creating a list box
listbx = Listbox(leftframe,  relief = RAISED)
listbx.pack(side = TOP)

#creating Add song button
addsongbtn = Button(leftframe,text = "Add Songs", command = browse_file)
addsongbtn.pack(side = LEFT)

#creating delete song button
deletesongbtn = Button(leftframe,text = "Delete Songs", command = delete_song)
deletesongbtn.pack(side = RIGHT)

#looping the window to appear for infinite time until user kills it.
window.mainloop()

