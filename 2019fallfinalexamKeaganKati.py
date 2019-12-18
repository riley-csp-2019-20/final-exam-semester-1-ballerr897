#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Keagan Kati
#Date
# 12/18/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle
keagan = turtle.Turtle()






player_bot = turtle.Turtle()


wall_width = 10
distance = 15 
keagan.left(90)
door_width = 10
keagan.ht()
keagan.pensize(15)


#create turtle
keagan.speed(0)
keagan.shape("arrow")
keagan.color("blue")
keagan.penup()
keagan.goto(0,0)
keagan.direction = "stop"



#movement function
def up():
    player_bot.setheading(90)
    player_bot.forward(5)




def down():
    player_bot.setheading(270)
    player_bot.forward(5)



def left():
    player_bot.setheading(180)
    player_bot.forward(5)



def right():
    player_bot.setheading(0)
    player_bot.forward(5)



def space():
    keagan.clearscreen()




def o():
    keagan.pensize(5)


def p():
    keagan.pensize(20)






#color/drawing functions
if pensize > 15 ():
    turtle.penup()
    turtle.pensize(5)
    turtle.pendown()
elif pensize > 15():
    turtle.penup()
    turtle.pensize(20)
    turtle.pendown()    



#create screen


#bind to keypresses

wn = turtle.Screen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress("space")
wn.onkeypress("o")
wn.onkeypress("p")
#listen
wn.listen()


#mainloop
wn.mainloop()
