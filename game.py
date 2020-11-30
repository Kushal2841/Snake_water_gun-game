# Snake Water Gun Game

import random

Chances = 0
YourPoints = 0
ComputerPoints = 0

while Chances < 10:
    a = input("Enter s for Snake, w for Water, g for Gun")
    lst = ["Snake", "Water", "Gun"]
    choice = random.choice(lst)
    print("Our choice is:" + choice)
    if a == "s":
        if choice == "Snake":
            print("Its a tie")
        elif choice == "Water":
            print("You lose")
            ComputerPoints += 1
        elif choice == "Gun":
            print("You win")
            YourPoints = YourPoints + 1
        print("Your Points:" + str(YourPoints))
        print("Computer Points :"+str(ComputerPoints))
        print()
    elif a == "w":
        if choice == "Water":
            print("Its a Tie")
        elif choice == "Gun":
            print("You Lose")
            ComputerPoints += 1
        elif choice == "Snake":
            print("You Win")
            YourPoints = YourPoints+1
        print("Your Points:"+str(YourPoints))
        print("Computer Points:"+str(ComputerPoints))
        print()

    elif a == "g":
        if choice == "Gun":
            print("Its a Tie")
        elif choice == "Water":
            print("You Lose")
            ComputerPoints += 1
        elif choice == "Snake":
            print("You Win")
            YourPoints = YourPoints+1
        print("Your Points:" + str(YourPoints))
        print("Computer Points :" + str(ComputerPoints))
        print()

    else:
        print("Enter a valid input")
    Chances = Chances + 1

if YourPoints > ComputerPoints:
    print("Congrats! , You won the match")
elif YourPoints == ComputerPoints:
    print("Match is tied")
else:
    print("Sorry,You lose the match")
