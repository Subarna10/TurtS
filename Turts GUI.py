import turtle
from tkinter import *

# Functions Start

def showturtle():                           # Function for showing turtle
    turtle.showturtle()


def pup_pdn():                              # function for PenUp and PenDown toggle button
    if pup_pdn_button.config('relief')[-1] == 'sunken':
        pup_pdn_button.config(relief="raised")
        pup_pdn_button.config(text="Pen Up")
        turtle.penup()
    else:
        pup_pdn_button.config(relief="sunken")
        pup_pdn_button.config(text="Pen Down")
        turtle.pendown()


def turn_left():                            # Function for moving left
    turtle.left(int(turn_left_entry.get()))


def move_forward():                         # Function for moving forward
    turtle.forward(int(move_forward_entry.get()))


def draw_circle():                          # Function for drawing circle
    turtle.circle(int(draw_circle_entry.get()))


def pen_size():                             # Function for changing pen size
    turtle.pen(pensize=int(pen_size_entry.get()))


def change_color():                         # Function for changing turtle's color
    turtle.color(change_color_entry.get())


def change_bg():                            # Function for changing background color
    turtle.bgcolor(change_bg_entry.get())

# Function End

window = Tk()
window.title("Turtle")

heading = Label(window, text="TURTLE GUI")                                          #Heading Label
heading.grid(row=0, column=0)

showturtle_button = Button(window, text="Show Turtle", command=showturtle)          #Showing turtle button
showturtle_button.grid(row=0, column=1)

pup_pdn_button = Button(window, text="Pen Down", relief="sunken", command=pup_pdn)  #PenUp and PenDown Button
pup_pdn_button.grid(row=0, column=2)

turn_left_entry = Entry(window)                                                     #Entry for left angle
turn_left_entry.grid(row=1, column=0, columnspan=2)

turn_left_button = Button(window, text="Turn Left", command=turn_left)              #Button for left angle
turn_left_button.grid(row=1, column=2)

move_forward_entry = Entry(window)                                                  #Entry for move distance
move_forward_entry.grid(row=1, column=3, columnspan=2)

move_forward_button = Button(window, text="Move Forward", command=move_forward)     #Button for moving
move_forward_button.grid(row=1, column=5)

draw_circle_entry = Entry(window)                                                   #Entry for circle size
draw_circle_entry.grid(row=2, column=0, columnspan=2)

draw_circle_button = Button(window, text="Draw Circle", command=draw_circle)        #Button for drawing circle
draw_circle_button.grid(row=2, column=2)

pen_size_entry = Entry(window)                                                      #Entry for changing pensize
pen_size_entry.grid(row=2, column=3, columnspan=2)

pen_size_button = Button(window, text="Change PenSize", command=pen_size)           #Button for changing pensize
pen_size_button.grid(row=2, column=5)

change_color_entry = Entry(window)                                                  #Entry for changing pencolor
change_color_entry.grid(row=3, column=0, columnspan=2)

change_color_button = Button(window, text="Change Color", command=change_color)     #Button for changing pencolor
change_color_button.grid(row=3, column=2)

change_bg_entry = Entry(window)                                                     #Entry for changing background color
change_bg_entry.grid(row=3, column=3, columnspan=2)

change_bg_button = Button(window, text="Change BG Color", command=change_bg)        #Button for changing background color
change_bg_button.grid(row=3, column=5)

window.mainloop()
