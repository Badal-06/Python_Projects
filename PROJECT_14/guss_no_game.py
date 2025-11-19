import random
target =random.randint(1,100)
attempts=0
while True:
    userChoice =int(input("guess the target:"))
    attempts+=1
    if (userChoice==target):
        print("success: correct guess!!")
        break
    elif(userChoice<target):
        print("your no was too small.take a bigger guess..")
    else:
        print("your no is too big .take a smalller guess ..")
print(f"you guss the number in {attempts} attempts") 