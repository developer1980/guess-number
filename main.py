
import random
print("Hello,Welcome to my tiny app")
print("Computer choose a number between 1 and 100,you find it")
number=random.randrange(1,100)
for i in range(0,100):
    print("cpu choosen " + str(number))
    user= input("choose a number between 1 an 100\nEnter a number: ")
    if int(user)== number:
        print("YOU WIN")
        break
    elif int(user)<number:
        print("you number is smaller than cpu")
        user= input("choose a number between 1 an 100\nEnter a number: ")
    elif int(user)>number:
        print("you number is biger than cpu")
        user= input("choose a number between 1 an 100\nEnter a number: ")