#creating a game by using pythons built in function, got help from online sources, @TokyoEdTech.

import turtle

game = turtle.Screen()
game.title("Pong by Nicholas Gomes")
game.setup(height=600,width=800)
game.tracer(0)
game.bgcolor("red")

#creating paddles A,B, and the Ball 

pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("blue")
pad_a.shapesize(stretch_len=1,stretch_wid=5)
pad_a.penup()
pad_a.goto(-350,0)

pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("blue")
pad_b.shapesize(stretch_len=1,stretch_wid=5)
pad_b.penup()
pad_b.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
# setting ball movement by using the dx or delta rate of change on x and y axis.
ball.dx = .20
ball.dy = .20

#creating movement
def pad_a_up():
    y = pad_a.ycor()
    y = y+20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y = y+20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)    

#making the game responsive to user action!
#.listen() means anything after it will be used upon user action
game.listen()
game.onkeypress(pad_a_up,"w")
game.onkeypress(pad_a_down,"s")
# Can set it to the arrow keys by setting the press to "Up","Down" or Left Right ect. they must be capitalized!
game.onkeypress(pad_b_up,"o")
game.onkeypress(pad_b_down,"l")


while True:
    game.update()

    # creating ball movement in here
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # setting borders for the ball to bounce of the y axis
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
#the above lines resets the ball movements on line 75
# adding the x axis border control for them game so the ball goes back to center upon passing the pads.
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = -.20

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = .20
    
#*need to study this part* Making the ball bounce of the paddles.
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() > pad_a.ycor() - 40 and ball.ycor() < pad_a.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1 
o
