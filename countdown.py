#Create Countdown Clock & Timer using Python

#Importing the required libraries and Modules
#import datetime module
from threading import Timer
import time
import tkinter as tk
from tkinter import *
from datetime import datetime 
from win10toast import ToastNotifier
import winsound

#Creating the GUI window (Labels, Button and Entry Field)
#creating  a window 
window = Tk()
window.geometry('600x600') # giving  size
window.title(" MyProject") #giving title 
head  = Label(window , text= " Countdown Clock and Timer", font = " Franklin 15") #a label
head.pack(padx= 30, pady=40)
Label( window , text = " Enter the time in HH:MM:SS", font =('bold')).pack()
hours = StringVar()
minutes =StringVar()
seconds = StringVar()
Entry(window, textvariable=hours , width = 40).pack()
Entry(window, textvariabl=minutes , width = 40).pack()
Entry(window, textvariable=seconds, width = 40).pack()
check = BooleanVar()

Checkbutton(text = "check for Music",onvalue  = True,variable =check).pack() # creating checkbox#Displaying the current time
def countdown():
    print(" countdown started")
Button(window ,text = "Set Countdown", command = countdown , bg = 'yellow').place(x= 260, y= 230) # create button 

# Displaying the Current Time: 
now = datetime.now()
current_time = now.strftime("%H-%M-%S")
Label(window , text= current_time ).pack()

#Creating the Timer and Countdown Function
#to print the window
def countdown():
    try:
        t = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    except ValueError:
        Label(window, text="Invalid input! Please enter numbers.", fg="red").pack()
        return
    while t:
        mins, secs = divmod(t, 60)
        display = (' {:02d}:{:02d}'.format(mins, secs))
        time.sleep(1)  # sleep time in 1 sec
        t -= 1
        Label(window, text=display).pack()
    Label(window, text="Time's-up", font=('bold', 14)).place(x=20, y=20)

#Adding Desktop Notification
#display notification on desktop
    toast = ToastNotifier() #create toast notifier object
    toast.show_toast('Notification' #title of the notification
                     , "Timer is OFF" #message body
                     , duration = 20  #duration in seconds
                    , icon_path = NONE, #no ico
                     threaded = True ) #run in a seperate thread
    
#Adding a Beep Sound
if (check.get() ==True): #if the value f check is True 
        winsound.Beep(440,1000) #beep sound
window.update()
window.mainloop()
