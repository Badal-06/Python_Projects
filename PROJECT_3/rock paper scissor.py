'''-1 = rock
0 = paper
1 = scissor'''

import  random
computer =random.choice([-1,0,1])
youstr =input("enter ur choice (r for rock, p for paper, s for scissor): ")
youdict={"r":-1,"p":0,"s":1}
revDict={-1:"rock",0:"paper",1:"scissor"}
you=youdict[youstr]
print(f"you chose {revDict[you]}\ncomputer chose {revDict[computer]}")
if(computer==you):
    print("IT'S A DRAW !!")
else:
    if(computer==-1 and you==0):
        print("YOU WIN !!")
    elif(computer==-1 and you==1):
        print("YOU LOSE !! ")
    elif(computer==0 and you==-1):
        print("YOU LOSE !! ")
    elif(computer==0 and you==1):
        print("YOU WIN !! ")
    elif(computer==1 and you==-1):
        print("YOU WIN !! ")
    elif(computer==1 and you==0):
        print("YOU LOSE !! ")
    else:
        print("Somthing wents wrong ???")