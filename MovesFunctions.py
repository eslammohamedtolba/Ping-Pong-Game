from Components import *


# Create moves functions that allow the rackets to move up or down
def Fracket_up():
    Fracket.sety(Fracket.ycor()+30)
def Fracket_down():
    Fracket.sety(Fracket.ycor()-30)

def Sracket_up():
    Sracket.sety(Sracket.ycor()+30)
def Sracket_down():
    Sracket.sety(Sracket.ycor()-30)


# Create keyboard bindings that link the window with the keyboard
window.listen()
window.onkeypress(Fracket_up,"w")
window.onkeypress(Fracket_down,"s")

window.onkeypress(Sracket_up,"Up")
window.onkeypress(Sracket_down,"Down")