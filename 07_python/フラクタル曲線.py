from turtle import Turtle
import turtle

STEP = 13.0

def hilbert(level,angle):
    if level <=0:
        turtle.rt(angle)
        hilbert(level-1,-angle)
        turtle.fd(STEP)
        turtle.lt(angle)
        hilbert(level-1,angle)
        turtle.fd(STEP)
        hilbert(level-1,angle)
        turt