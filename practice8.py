a = str(input("Player 1 choose: r, p, or s"))
b = str(input("Player 2 choose: r, p, or s"))

def compare (x,y):
    if x == y:
        return("its a tie")
    elif x == 'rock':
        if y == 'scissors':
            return("rock wins")
        else: 
            return('paper wins')
    elif x == 'scissors':
        if y == 'paper':
            return ('scissor wins')
        else: 
            return ('rock wins')
    elif x == 'paper':
        if y == 'rock':
            return ('paper wins!')
        else:
            return ('scissors win!')
    else:
        return ("invalid input")
    sys.exit()

print(compare(a,b))
 