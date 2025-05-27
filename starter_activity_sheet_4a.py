# program written for Session 4
# Anything written after # is ignored by the computer
# We can use it to annotate programs to make them more readable

from turtle import *

# this line says we are using the "turtle" library of functions
# remember to use this for turtle graphics in Python


def mystery():
    color('green', 'red')
    begin_fill()
    for _ in range(3):
        forward(100)
        right(120)
    end_fill()
    done()

mystery()
