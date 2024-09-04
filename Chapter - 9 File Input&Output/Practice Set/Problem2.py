'''
    the game() function in a program let's a user 
    play a game and returns the score as an integer. you need to read a file
    "Hi-score.txt" which is either blank or contains the previous Hi-score. you need to write a 
    program to update the Hi-score whenever the game() function breaks the Hi-score.
'''
import random
def game():
    print("you are playing the game...")
    score = random.randint(1,65)
    #fetch the hiscore
    with open("Hi-score.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore ==int(hiscore)
        else:
            hiscore =0
    print(f"your score: {score}")
    if(score>int(hiscore)):
        #write this hiscore to the file
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
    return score
game()