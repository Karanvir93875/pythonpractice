num = int(input("Enter a number: "))
check = int(input("Give me a number to divide by:"))
mod = num % 2
if mod > 0:
    print("you picked an odd number.")
else: 
    print("You picked an even number.")

if num % 4 == 0:
    print(num, " is a multiple of 4.")
elif num % 2 == 0:
    print(num, " is an odd number.")
else:
    print(num, "is na odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)    