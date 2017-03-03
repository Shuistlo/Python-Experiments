#Shu Lo and Ryan Wilson (12:30 - 2)
#CS8, Project 2, Lab Section 1: Tues 11:00am - 12:20 am
import turtle
import random
import math

#initialize function: sets the world coordinates to (-2,-1) for the lower left hand side and (2,1) for the upper right hand side of the screen
#initialize function will also hide the turtle from view
#this function will also draw two parallel lines at y=0.5 and y=-0.5
def initialize(myTurtle):
        turtle.setworldcoordinates(-2,-1,2,1)
        myTurtle.ht()
        myTurtle.up()
        myTurtle.goto(-2,-0.5)
        myTurtle.down()
        myTurtle.color('red')
        myTurtle.goto(2,-0.5)
        myTurtle.up()
        myTurtle.goto(-2,0.5)
        myTurtle.down()
        myTurtle.goto(2,0.5)
        
#randomDotOutside function: makes a random dot which will differ in color dependin on whether it falls between the two lines created by the initialize function
#randomDotOutside will return False if the dot falls between the lines and True if it falls outside
def randomDotOutside(myTurtle):
    x=random.uniform(-2,2)
    y=random.uniform(-1,1)
    if -0.5<y<0.5:
        myTurtle.color('blue')
        W=False
    else:
        myTurtle.color('purple')
        W=True
    myTurtle.up()
    myTurtle.goto(x,y)
    myTurtle.down()
    myTurtle.dot(10)
    return W

#proportionDotsOutside function: finds the proportion of times a random dot will fall outside of the space between the two lines
#proportionDotsOutside will have parameters myTurtle and ntimes, the number of times a random dot will be generated
def proportionDotsOutside(myTurtle,ntimes):
    initialize(myTurtle)
    acc = 0
    for i in range(ntimes):
        if randomDotOutside(myTurtle):
            acc+=1
    return acc/ntimes

#the value should be close to 0.5
#the value will increase if the distance between the two lines decreases

#dropNeedle function: this function will draw a random line of length 1 on the graphics interface and will change colors
#depending on if the line passes through the the lines drawn by the initialize function
#dropNeedle will return True if the line crosses the lines from the initialize function
def dropNeedle(myTurtle):
    myTurtle.up()
    x=random.uniform(-2,2)
    y=random.uniform(-0.5,0.5)
    myTurtle.goto(x,y)
    myTurtle.seth(0)
    myTurtle.left(random.uniform(0,180))
    myTurtle.forward(0.5)
    deltaY = myTurtle.position()[1]-y
    if (deltaY+y > 0.5) | (y-deltaY<-0.5):
        myTurtle.color('purple')
        W=True
    else:
        myTurtle.color('blue')
        W=False
    myTurtle.left(180)
    myTurtle.down()
    myTurtle.forward(1)
    return W

#buffonPi function:this function will approximate the value of pi using the dropNeedle function
#buffonPi has two parameters, myTurtle, and ntimes the number of times the needle is dropped
def buffonPi(myTurtle,ntimes):
    initialize(myTurtle)
    acc=0
    for i in range(ntimes):
        if dropNeedle(myTurtle):
            acc+=1
    return (ntimes<<1)/acc
    myTurtle.forward(1)

#approxHits function:this function will approximate the number of times a randomly drawn line will hit the lines drawn by the
#initialize function using the approximation for pi in the buffonPi function
def approxHits(ntimes):
    return (ntimes<<1)/math.pi

