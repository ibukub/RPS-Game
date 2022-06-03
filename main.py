b = True
while b == True:
    g = ['R' 'P' 'S']
    print("WELCOME!")
    print('This is the Rock paper scissors game')
    print('Enter R for Rock, P for Paper, S for scissors')
    a = input('Select R, P, or S: ')
    for letter in a:
        if letter in g:
            continue
        else:
            break
            print('value entered not valid')

    import random
    CPU = random.choice(g)
    print('User choice is: ', a) 
    print('CPU choice is: ' , CPU)
    if a == CPU:
        print('It is a tie')
    elif a == 'R' and CPU == 'P':   
        print('Computer wins')
    elif a == 'P' and CPU == 'R':   
        print('Congrats you win') 
    elif a == 'R' and CPU == 'S':   
        print('Congrats you win')
    elif a == 'S' and CPU == 'R':   
        print('Computer wins')  
    elif a == 'P' and CPU == 'S':   
        print('Computer wins')  
    elif a == 'S' and CPU == 'P':   
        print('Congrats you win')
    elif a not in g:
        print('wrong input')
    print('Do you want to play again, y or n')
    c = input('Enter y to continue or n to end: ')
    if c =="y":
        continue
    else:
        break
print('thanks for playing, see you again')
