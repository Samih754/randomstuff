import random


def clear(n):
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

def betallowed(bet, money):
    bet = input("What is your bet?: ")
    bet = float(bet)
    if bet > money:
        print("refuse bet")

def money_bet(money, bet, win, )

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


def wincond(vcp1, vcp2, tpp1, taip):
    if vcp1 == 21:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("YOU WON!!!")
        tpp1 = ttp1 + 1
    if vcp2 == 21:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("YOU LOST lol")
        taip = taip + 1

    if vcp1 > 21:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("YOU LOST lol")
        taip = taip + 1
    if vcp2 > 21:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("YOU WON!!!")
        tpp1 += 1
    print("")
    print("end")

def play():

    money = 500
    if gcount == 0:
        global taip
        taip = 0.0
        global tpp1
        tpp1 = 0.0
        global bet
        bet = 0

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

            wincond(vcp1, vcp2, tpp1, taip)
            hit1 = False

            if vcp1 > 21:
                break
            if vcp2 > 21:
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
                wincond(vcp1, vcp2, tpp1, taip)
                break
            if vcp2 == 21:
                wincond(vcp1,vcp2, tpp1, taip)
                break
            if vcp1 > vcp2 :
                print("")
                print("The AI had", vcp2)
                print("You had", vcp1)
                print("YOU WON!!!")
                print("")
                print("end")
                tpp1 = tpp1 + 1
                break
            if vcp1 < vcp2:
                print("")
                print("The AI had", vcp2)
                print("You had", vcp1)
                print("YOU LOST lol")
                print("")
                print("")
                print("end")
                taip = taip + 1
                break
        continue
# How many times the game has been played +1 is added every time the wile loop has happened.
global gcount
gcount = 0.0
#points that the AI has acumulated +1 is added after each outcome that has the AI has won is used.
global taip
taip = 0.0
#Points of the player idem to le AI
global tpp1
tpp1 = 0.0
#to clear the beard for each action
global nclear
nclear = 25
#for bets to see if they work
global lose
lose = None
global win
win = None

while 1 < 2 :
    continuegame = True
    print("")
    print("You have played:", gcount , "Games.")
    print("")
    print("The AI has: ", taip, "Points.  You have:", tpp1, "Points")
    rp = input("start or quit: ")
    if rp == "start":
        clear(nclear)
        gcount = gcount + 1
        play()
        continue
    elif rp == "quit":
        continuegame = False
        break
print("")
print("The game has been exited")

#31/10/2020 fixed everything i think only thing left is betting and making the code cleaner.
