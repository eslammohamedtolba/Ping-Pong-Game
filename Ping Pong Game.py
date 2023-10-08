"""
Pong is a simple two-player game that simulates table tennis. 
The game features two paddles and a ball, with the goal being to score points by hitting the ball past your opponent’s paddle. 
The first player to reach 10 points wins the game.

To play Pong, you’ll need to use the arrow keys on your keyboard to move your paddle up and down.
The left paddle is controlled using the “W” and “S” keys, while the right paddle is controlled using the up and down arrow keys. 
When the ball comes towards your paddle, you’ll need to move your paddle in the direction of the ball to hit it back.

If you miss the ball, your opponent will score a point. 
The game continues until one player reaches 10 points, at which point they are declared the winner.
"""
import time
from Components import *
from MovesFunctions import *


# Start the game
while True:
    window.update()
    # move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # borderY check
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.dy *=-1

    # borderX check
    if ball.xcor()>400:
        ball.dx*= -1
        ball.goto(0,0)
        Score1+=1
        Scores.clear()
        Scores.write(f"Player1: {Score1} , Player2: {Score2}",align="center",font=("Courier",24,"normal"))
    if ball.xcor()<-400:
        ball.dx*= -1
        ball.goto(0,0)
        Score2+=1
        Scores.clear()
        Scores.write(f"Player1: {Score1}   Player2: {Score2}",align="center",font=("Courier",24,"normal"))
    
    # crashing between ball and rackets
    if (ball.xcor()==350) and (ball.ycor()<Sracket.ycor()+60 and ball.ycor()>Sracket.ycor()-60):
        ball.dx *=-1
    if (ball.xcor()==-360) and (ball.ycor()<Fracket.ycor()+60 and ball.ycor()>Fracket.ycor()-60):
        ball.dx *=-1
    
    # checks if any of the player won the game by reaching its score to the target score for winning
    if Score1==10 or Score2==10:
        Scores.clear()
        Scores.write(f"Player {1 if Score1==10 else 2} won!",align="center",font=("Courier",24,"normal"))
        ball.dx=ball.dy=0
        ball.goto(0,0)
        window.update()
        time.sleep(2)
        break


