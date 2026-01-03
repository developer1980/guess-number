
import random
print("Hello,Welcome to my tiny app")
print("Computer choose a number between 1 and 100,you find it")
number=random.randrange(1,100)
for i in range(0,100):
    #print("cpu choosen " + str(number))  //cpu hint
    user= input("choose a number between 1 an 100\nEnter a number: ")
    if int(user)<number:
        print("you number is smaller than cpu")
    elif int(user)>number:
        print("you number is biger than cpu")
    elif int(user)== number:
        print("YOU WIN with TRY " +str(i+1))
        break