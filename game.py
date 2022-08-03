import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player=[]
computer=[]
pscore=0
cscore=0
flag=0
# player=[10,11]#remove later
for n in range(2):
    player.append(random.choice(cards))
    computer.append(random.choice(cards))

for n in range(2):
    pscore+=player[n]
    cscore+=computer[n]

def printCards():
    print("You cards are: ")
    print(player)
    
    print("computer's cards are:")
    print(computer)

if pscore==cscore==21:
    flag=1
    print("draw14")

if pscore==21 and flag!=1:
    flag=1
    printCards()
    print("you won9")
    
if cscore==21 and flag!=1:
    flag=1
    printCards()
    print("the computer won13")

while flag!=1:
    print(player)
    choice=input("Do you wana draw another card?: ")
    
    if choice=='y':
        card=11
        #card=random.choice(cards)
        player.append(card)
        pscore+=card
        if pscore==21:
            flag=1
            printCards()
            print("you won1")
            break
        if cscore==21:
            flag=1
            printCards()
            print("the computer won2")
            break
        if pscore>21 :
            if 11 in player:
                print(player) 
                pscore=pscore-11+1
                for n in range(len(player)):
                    if player[n]==11:
                        player[n]=1
                print("after modification:")
                print(player)
                print("---------------------")
                if pscore>21:
                    flag=1
                    print("\n")
                    printCards()
                    print("the computer won3")
                    break
            else:
                flag=1
                printCards()
                print("the computer won7")
                break
    else:
        break


#computer
if flag==0:
    if cscore<17:
        while not cscore>17:
            card=random.choice(cards)
            computer.append(card)
            cscore+=card
    
    printCards()
    
    if cscore>21:
        print("you won4")
    elif cscore>pscore:
        print("computer won5")
    elif cscore<pscore:
        print("you won6")
    else:
        print("its a draw")