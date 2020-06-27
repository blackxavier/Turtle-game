import turtle
import random
#first player
playerone = turtle.Turtle()
playerone.color("blue")
playerone.shape("circle")
playerone.penup()
playerone.goto(-200,100)

#secondplayer
playertwo = playerone.clone()
playertwo.color("magenta")
playertwo.shape("turtle")
playertwo.penup()
playertwo.goto(-200,-100)


#homes for the players
playerone.goto(300,60)
playerone.pendown()
playerone.circle(50)
playerone.penup()
playerone.goto(-200,100)

playertwo.goto(300,-140)
playertwo.pendown()
playertwo.circle(50)
playertwo.penup()
playertwo.goto(-200,-100)


#Creating the die
die  = [1,2,3,4,5,6]

#main logic
for i in range(20):
    if playerone.pos() >= (300,100):
        print("Player One wins")
        break
    elif playertwo.pos() >= (300,-100):
        print("Player two wins")
        quit()
        break
    else:
        playerone_turn = input("Press 'Enter' to roll the die for player 1: \n")
        die_outcome = random.choice(die)
        print("The result of the die is ",die_outcome)
        move = die_outcome*20
        print("The number of steps would be ",move)
        playerone.fd(move)

        playertwo_turn = input("Press 'Enter' to roll the die for player 2: \n")
        die_outcome = random.choice(die)
        print("The result of the die is ",die_outcome)
        move = die_outcome*20
        print("The number of steps would be ",move)
        playertwo.fd(move)




turtle.mainloop()