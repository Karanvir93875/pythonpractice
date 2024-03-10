def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-1-i]
    return x

word = input("give me a word")
x = reverse(word)
if x == word:
    print("this is a palindrome")
else: 
    print("this is not a palindrome")