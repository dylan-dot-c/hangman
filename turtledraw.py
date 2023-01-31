import turtle
import time

def table(p):
    p.goto(90, -50)
    p.lt(90)
    p.pensize(10)
    p.pencolor('black')
    p.fd(230)
    p.lt(90)
    p.fd(60)
    p.lt(90)

def drawStand(p):
    p = turtle.getpen()
    p.hideturtle()
    p.speed(3)
    p.color('blue')
    p.up()
    p.goto(0, -50)
    p.down()
    p.fillcolor('brown')
    p.begin_fill()
    for i in range(2):
        p.fd(100)
        p.right(90)
        p.fd(25)
        p.rt(90)
    p.end_fill()
    table(p)
    p.fd(20)
    p.rt(90)
    return p

def head(p):
    p.pencolor('yellow')
    p.fillcolor('yellow')
    p.begin_fill()
    p.circle(25)
    p.end_fill()
    p.left(90)

def body(p):
    p.up()
    p.fd(50)
    p.down()
    p.fd(100)
    p.up()
    p.bk(75)
    p.down()

def hand(dir, rotate, p):
    if dir ==1:
        p.rt(rotate)
    else:
        p.lt(rotate)
    p.fd(40)
    p.back(40)


if __name__=='__main__':
    s = turtle.getscreen()
    s.title('Hangman Game')
    s.bgcolor('purple')
    p = turtle.getpen()
    text = turtle.getpen()
    text.color('white')
    text.goto(350, 0)
    text.write('Hello There')
    drawStand(p)
    p.pensize(2)
    head(p)
    body(p)
    hand(1, 45, p)
    hand(0, 90, p)
    p.right(45)
    p.fd(75)
    hand(1, 45, p)
    hand(0, 90, p )
    # hand(0, 90, p)
    # s.bgcolor('red')
    # turtle.pencolor('green')
    # turtle.color('purple')
    # turtle.fd(100)
    # time.sleep(3)
    # s.bgcolor('green')
    input()