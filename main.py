#program to implement hangman
import random
import turtledraw as td
import time
import turtle

group = {
            'fruits': ('mango', 'apple', 'cherry', 'banana', 'Pineapple','tomato', 'blueberry', 'passion', 'watermelon', 'grape', 'jackfruit', 'guava'),
            'vegetables': ('carrot', 'calaloo', 'potato', 'yam', 'cabbage', 'lettuce', 'cucumber', 'beetroot'),
            'cars': ('mercedes', 'honda', 'toyota', 'Tesla', 'Lamborghini', 'ferrari', 'Audi', 'BMW', 'Bently'),
            'games': ('minecraft', 'fortnite', 'FreeFire', 'Halo', 'Valorant','Roblox'),
            'tech Companies': ('google', 'Windows', 'Amazon', 'Facebook', 'Twitter', 'Instagram', 'Apple', 'Adobe')
        }

def table(p):
    p.goto(90, -50)
    p.lt(90)
    p.pensize(10)
    p.pencolor('black')
    p.fd(230)
    p.lt(90)
    p.fd(60)
    p.lt(90)
    # p.pensize(3)

def drawStand(p):
    # p = turtle.getpen()
    # p.hideturtle()
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
    p.pensize(3)
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

def main():
    # print("WELCOME")
    keys = list(group.keys())
    l = len(keys)

    s = turtle.getscreen()
    s.title('HANGMAN GAME')
   
    # p = turtle.Turtle()

    choice = 1
    # td.drawStand()
    # res = s.textinput('Select A category', 'Food\nMinecraft\n')
    string = ''
    for i,grp in enumerate(keys):
            string += f'{i+1}: {grp}\n'
    while choice != 0:   
        p = turtle.getpen()
        p.hideturtle()
        mistakes = 0
        won = False
        s.bgcolor('cyan')
        textpen = turtle.Turtle()
        textpen.hideturtle()
        p = drawStand(p)
        textpen.hideturtle()
        textpen.up()
        textpen.goto(0, 230)
        textpen.down()
        # print('Select A category')
        choice = s.numinput('Select A Category', string, 1, minval=0, maxval = 5)
        choice = int(choice)
        
        if choice==0: break

        category = keys[choice-1]

        word =  random.choice(group[category]).lower()
        
        dashedWord = list('_ '* len(word))
        resWord = list(' '*len(word))
        chances = 6
        while chances>0 and won == False:
            textpen.write(f'Category: {category} \n'+ ''.join(dashedWord), align='center', font=('Times New Roman', 20, 'normal'))            
            # print()
            # print(f'Your ans {resWord}')
            # c = input('Enter a letter\n>>>')
            c = turtle.textinput('Input', 'Enter a letter')[0].lower()
            if c in word:
                for i in range(len(word)):
                    if word[i]==c:
                        resWord[i]=c
                        dashedWord[2*(i+1) - 2] = c
            else:
                # print('Incorrect letter')
                mistakes+=1
                if mistakes==1:
                    head(p)
                if mistakes==2:
                    body(p)
                if mistakes==3:
                    hand(1, 45, p)
                if mistakes==4:
                    hand(0, 90, p)
                    p.right(45)
                    p.fd(75)
                if mistakes==5:
                    hand(1, 45, p)
                if mistakes==6:
                    hand(0, 90, p)
                chances -=1

                # print(f'You have {chances} chances left')
            if word == ''.join(resWord):
                won = True
                textpen.undo()
                break

            textpen.undo()

        if won:
            # print('Congratulations, You have won!!!!')
            for i in range(2):
                textpen.undo()
                textpen.color('white')
                s.bgcolor('blue')
                time.sleep(1)
                textpen.undo()
                textpen.color('orange')
                s.bgcolor('green')
                textpen.write('Congratulations, You have won!!!!', align='center', font=('Times New Roman', 20, 'normal'))
                time.sleep(1)
        else:
            textpen.color('black')
            s.bgcolor('red')
            textpen.write(f'I\'m Sorry, but you have died. RIP\nThe word was {word}', align='center', font=('Cursive', 20, 'normal'))

        choice = s.numinput('Play Again??', 'Do you wish to play again:\n1-Yes\n0-No\n> ', 1, minval = 0, maxval = 1)
        choice = int(choice)       
        s.clearscreen()
        

main()