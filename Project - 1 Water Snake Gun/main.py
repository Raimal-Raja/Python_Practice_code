'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w": -1, "g":0}
reverseDic = {1:"s",-1:"w", 0:"g"}
you = youDict[youstr]
print(f"you chose {reverseDic[you]}\nComputer chose {reverseDic[computer]}")


if(computer ==you):
    print("It's a draw")
else:
    if(computer == -1 and you ==1):
        print("You Win!")
    elif(computer == -1 and you ==0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you ==0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer ==0 and you ==1):
        print("You Lose!")
    else:
        print("Something went wrong")