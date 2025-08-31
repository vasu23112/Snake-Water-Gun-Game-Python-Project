import random
'''
1 = snake
-1 = water
0 = gun
'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youdict = {"s":1 ,"w":-1 ,"g":0}
reversedict = {1:"Snake", -1:"Water", 0:"Gun"}

you = youdict[youstr]
print(f"you choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")

if(computer==you):
    print("Thats a Draw")
else:
    '''  
    if(computer == -1 and you== 1):             -2
        print("you win! snake drink the water")
    elif(computer == -1 and you== 0):           -1
        print("you lose! water drawn the gun")
    elif(computer == 1 and you== -1):               2
        print("you lose! snake drink the water")
    elif(computer == 1 and you== 0):            1
        print("you win! Gun shoots the snake")
    elif(computer == 0 and you== -1):           1
        print("you win! water drawn the gun")
    elif(computer == 0 and you== 1):            -1
        print("you lose! Gun shoots the snake")
    else:
        print("Something went wrong")
    '''
    if((computer - you)== 1 or (computer - you)== -2):
        print("you win")
    else:
        print("you lose")

