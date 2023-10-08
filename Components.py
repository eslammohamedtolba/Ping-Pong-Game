# module turtle
import turtle


# Create the window where the two player will play on and determine its title, size and background
window = turtle.Screen() 
window.title("Ping Pong Game") 
window.bgcolor("black")
window.setup(width=800,height=600) 
window.tracer(0) # stops the window from updating itself automatically

# Create first racket and determine its shape, size, color, position and the score for this player
Fracket = turtle.Turtle()
Fracket.speed(0)
Fracket.shape("square")
Fracket.shapesize(stretch_wid=5,stretch_len=1)
Fracket.color("blue")
Fracket.penup() # stops drawing lines 
Fracket.goto(-380,0) 
Score1=0

# Create second racket and determine its shape, size, color, position and the score for this player
Sracket = turtle.Turtle()
Sracket.speed(0)
Sracket.shape("square")
Sracket.shapesize(stretch_wid=5,stretch_len=1)
Sracket.color("red")
Sracket.penup() # stops drawing lines 
Sracket.goto(370,0) # right
Score2 = 0

# Create Ball which the two players will play by and determine its shape, color, position and the delta or rate of change for x and y
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup() # stops drawing lines 
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

# Create the Scores for two playes and determine its color, position and the test that will write in
Scores = turtle.Turtle()
Scores.speed(0)
Scores.color("white")
Scores.penup() # stops drawing lines 
Scores.hideturtle()
Scores.goto(0,260)
Scores.write(f"Player1: {Score1} , Player2: {Score2}",align="center",font=("Courier",24,"normal"))
