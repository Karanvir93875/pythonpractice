a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []
for element in a: 
    if (element< 5):
        b.append(element)
        b.sort()
print(b)

x = int(input("Enter a number"))
for element in a:
    if (x > element):
        c.append(element)
        c.sort()

print(c)
