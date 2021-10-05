import random

def clear():
    while n > 0:
        print("")
        n = n - 1

def lwmoney(vcp1):
    if vcp1 > 21 :
        money = money - bet
    if vcp2 == 21:
        money = money
    if vcp2 > 21:
        money = money + bet * 2

def ace(a, v):
    if a >= 10:
        v = 1
    else:
        v = 11

def bet(bet):
    bet = input("What is your bet?: ")
    bet = float(bet)
    if bet > money:
        print("refuse bet")


def double(bet, money, vcp1, cv1):
    if bet * 2 > money:
        print("refuse bet")
    bet = bet * 2
    print("")
    print("ok")
    print("")
    count2 = count2 + 1
    cv1 = random.randint(1, 10)
    ace(vcp1, cv1)
    vcp1 = vcp1 + cv1
    print("You drew", cv1)
    print("You have: ", vcp1)


def wincond(vcp1, vcp2 ):
    # how to use the "and" thing look it up on  google pls cause basically this does that if both are over 21 it ends in a tie.
    if vcp1 > 21 and vcp2 > 21:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("Tie")
    elif vcp1 == 21:
            print("")
            print("The AI had", vcp2)
            print("You had", vcp1)
            print("YOU WON!!!")

    elif vcp2 == 21:
            print("")
            print("The AI had", vcp2)
            print("You had", vcp1)
            print("YOU LOST lol")

    elif vcp1 > 21:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("YOU LOST lol")
    elif vcp2 > 21:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("YOU WON!!!")
    print("")
    print("end")

def play():
    money = 500

    if continuegame == True:
        vcp1 = 0
        vcp2 = 0
        v1 = 0
        v2 = 0
        tv2 = 0
        count2 = 0
        bet = input("How much do you bet?: ")
        bet = float(bet)

        if vcp1 == 0:
            vcp1 = random.randint(1,10)
        print("")
        print("You have drawn:", vcp1)
        hit1 = True

        if vcp2 == 0:
            vcp2 = random.randint(1,10)
        print("The AI has ", vcp2)

    while 1 > 0:
        task = input("hit, stop, stand, double?: ")
        if task == "hit" :
            print("")
            print("ok")
            print("")
            count2 = count2 + 1
            cv1 = random.randint(1, 10)
            ace(vcp1, cv1)
            vcp1 = vcp1 + cv1
            print("You drew", cv1)
            print("You have: ", vcp1)

            tv2 = random.randint(1,10)
            ace(vcp2, tv2)
            vcp2 = vcp2 + tv2
            if count2 == 1:
                print("The AI has drawn", tv2, "The AI has ", vcp2)
            if count2 > 1:
                print("The AI has drawn" )

            wincond(vcp1, vcp2)
            hit1 = False

            break

        if task == "stop" :
            break

        if hit1 is True:
            cv1 = random.randint(1,10)
        if task == "double" :
            double(bet, money, vcp1, cv1)
            break

        if task == "stand":
            tv2 = random.randint(1,10)
            vcp2 = vcp2 + tv2
            print("The AI has drawn: ")


            if vcp2 > 21:
                wincond(vcp1, vcp2)
                break
            if vcp2 == 21:
                wincond(vcp1,vcp2)
                break
            if vcp1 > vcp2 :
                print("")
                print("The AI had", vcp2)
                print("You had", vcp1)
                print("YOU WON!!!")
                print("")
                print("end")
                pwin = pwin + 1
                break
            if vcp1 < vcp2:
                print("")
                print("The AI had", vcp2)
                print("You had", vcp1)
                print("YOU LOST lol")
                print("")
                print("")
                print("end")
                aiwin = aiwin + 1
                break
        continue

gcount = 0
aiwin = 0
pwin = 0

while 1 < 2 :
    continuegame = True
    print("")
    print("You have played:", gcount, "Game(s).")
    print("")
    rp = input("start or quit: ")
    if rp == "start":
        gcount = gcount + 1
        play()
        continue
    elif rp == "quit":
        continuegame = False
        break
print("")
print("The game has been exited")
