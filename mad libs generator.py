from tkinter import *  

Screen = Tk() #create main window
Screen.config(bg='pink') #set the background color of the window
Screen.title('MyApp') #set window title
Screen.geometry('400x400') #set window size
#create label first then pack it


label =Label(Screen,
              text ='PythonGeeks Mad Lib Generator',
              fg = 'black', #foreground color
              bg = 'pink', #background color
              font =('Franklin', 20,'bold ') #set font, size and style
             )
label.pack(padx =10, pady=20) # .pack() is used to position the label in the window 
label.place(x=1000 ,y=20) # use .place() to position the label at specific coordinates
label.config(font=('Arial', 20, 'bold'), fg='blue') #set fg means foreground color, font and size of the label

#creating buttons
Story1Button = Button(Screen , text = "memorial day", font =('Times New Roman', 12) , command=lambda: Story1(Screen), bg ='blue')
Story1Button.place(x=100, y=100) #place the button at the specific conditions
Story2Button = Button (Screen , text = 'Ambitions', font = ('Times  New Roman', 15), command =lambda: Story2(Screen), bg= "yellow")
Story2Button.place(x=100,y=200)

Screen.update() #update the screen to show the changes
Screen.mainloop() # Show window and wait for user interaction
