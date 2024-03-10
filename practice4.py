num = int(input("Enter a number: "))
a = []
for number in list(range(1,num+1)):
    if (num % number) == 0:
        a.append(number)
print(a)