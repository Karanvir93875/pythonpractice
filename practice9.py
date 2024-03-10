import random

a = random.randint(1,9)
x = int(input("Enter a number"))
if (x < a):
    print ("you guessed too low")
elif (x > a):
    print("you guessed too high")
elif (x == a):
    print("you entered the correct number") 