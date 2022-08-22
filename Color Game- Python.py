# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:40:44 2021

@author: sheemam
"""
#TASK1 - Working with Modules, Functions, Loops, IFs, 

#import the Modules
import tkinter, random
#Create a list of the possible colors
colours=['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White','Purple', 'Brown']
score=0
#the game time feft, initially 30 seconds
timeleft = 30
#function that will start the game
def startGame(event):
    if timeleft ==30:
        #start the countdown times
        countdown()
    #run the function to choose the next color
    nextColour()
#Function to choose and display the next Color
def nextColour():
    #use the globally declared variables 'score' and 'timeleft'
    global score
    global timeleft
    #if the game is currently in play
    if timeleft >0:
        #make the test entry box active
        e.focus_set()
        #if the color typed is equal to the color of the text increase the score
        if e.get().lower()==colours[1].lower():
            score+=1
        #Clear the entry box 
        e.delete(0, tkinter.END)
        #Change the color to type, by changing the text and 
        #the color to a random color value
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        #Display the score
        scoreLabel.config(text="Score: "+ str(score))
#Countdown timer function
def countdown():
    global timeleft
    #if the game is currently in play
    if timeleft >0:
        #decrement the timer
        timeleft -=1
        #update the timeleft label
        timeLabel.config(text="Time Left: "+ str(timeleft))
        #run the function again after 1 second
        timeLabel.after(1000, countdown)
#Driver Code
#Create the GUI (window)    
root = tkinter.Tk()
#set the title for the GUI
root.title("COLORGAME")
#set the size
root.geometry("375x200")
#add the instructions label
instructions=tkinter.Label(root, text="Type in the color of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()
#add the score label
scoreLabel=tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()
#add the time left label
timeLabel=tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()
#add the label for displaying the colors
label=tkinter.Label(root,  font=('Helvetica', 60))
label.pack()
#add a text entry box to type the colors
e=tkinter.Entry(root)
#Run the startGame function when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
#set the focus on the entry box
e.focus_set()
#start the GUI
root.mainloop()