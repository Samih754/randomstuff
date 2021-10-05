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

def ace(a, v,):
    if (a + 11) > 21:
        v = 1
    elif (a + 1) < 21:
        v = 11

    return v #magic

def betallowed(bet, money):
    bet = input("What is your bet?: ")
    bet = float(bet)
    if bet > money:
        print("refuse bet")

def money_bet(money, bet, win,):
    if win is True:
        money = money + bet
    if win is False:
        money = money - bet
    return win, money, bet

def double(bet, money, vcp1, cv1, vcp2, tv2):
    if bet > money:
        print("refuse bet")
    else:
        print("")
        print("ok")
        print("")
        count2 = count2 + 1
        cv1 = random.randint(1, 10)
        ace(vcp1, cv1)
        vcp1 = vcp1 + cv1
        apc.append(cv1)
        print("You drew", cv1)
        print("You have: ", vcp1)
    if vcp1 > 21:
        wincond(vcp1, vcp2, pwin, aip)
        money_bet(money, bet, win,)
    if vcp2 > 21:
        wincond(vcp1, vcp2, pwin, aip)
        money_bet(money, bet, win,)

    else:
        if vcp1 > vcp2:
            print("")
            print("The AI had", vcp2)
            print("You had", vcp1)
            print("YOU WON!!!")
            print("")
            print("All player cards,  ")
            print(apc)
            print("All AI cards are ")
            print(aaic)
            print("")
            print("end")

            win = True
            money_bet(money, bet, win,)

        else:
            print("")
            print("The AI had", vcp2)
            print("You had", vcp1)
            print("YOU LOST lol")
            print("")
            print("All player cards,  ")
            print(apc)
            print("All AI cards are ")
            print(aaic)
            print("")
            print("")
            print("end")

            win = False
            money_bet(money, bet, win,)


def wincond(vcp1, vcp2, win):

    if vcp1 == vcp2:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("")
        print("All player cards,  ")
        print(apc)
        print("All AI cards are ")
        print(aaic)
        print("TIE")
        print("YOU LOST lol")

        win = True
        money_bet(money, bet, win,)

    elif vcp1 > 21:
        if vcp2 > 21:
            print("")
            print("The AI had", vcp2)
            print("You had", vcp1)
            print("")
            print("All player cards,  ")
            print(apc)
            print("All AI cards are ")
            print(aaic)
            print("TIE")
            print("YOU LOST lol")

            win = True
            money_bet(money, bet, win,)


    elif vcp1 == 21:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("")
        print("All player cards,  ")
        print(apc)
        print("All AI cards are ")
        print(aaic)
        print("YOU WON!!!")

        win = True
        money_bet(money, bet, win,)

    elif vcp2 == 21:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("")
        print("All player cards,  ")
        print(apc)
        print("All AI cards are ")
        print(aaic)
        print("YOU LOST lol")

        win = False
        money_bet(money, bet, win,)


    elif vcp1 > 21:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("")
        print("All player cards,  ")
        print(apc)
        print("All AI cards are ")
        print(aaic)
        print("YOU LOST lol")

        win = False
        money_bet(money, bet, win,)

    elif vcp2 > 21:
        print("")
        print("The AI had", vcp2)
        print("You had", vcp1)
        print("")
        print("All player cards, ")
        print(apc)
        print("All AI cards are ")
        print(aaic)
        print("YOU WON!!!")

        win = True
        money_bet(money, bet, win,)



def play():

    if gcount == 0:

        global bet
        bet = 0


    if continuegame == True:
        vcp1 = 0
        vcp2 = 0
        v1 = 0
        v2 = 0
        tv2 = 0
        count2 = 0
        bet = 0
        win = None
        betallowed(bet, money)

        if vcp1 == 0:
            vcp1 = random.randint(2,11) #cause if its a 1 it will become a 11
            apc.append(vcp1)
        print("")
        print("You have drawn:", vcp1)
        hit1 = True

        if vcp2 == 0:
            vcp2 = random.randint(2,11)# cause if its a 1 it will become a 11
            aaic.append(vcp2)
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
            apc.append(cv1)
            print("You drew", cv1)
            print("You have: ", vcp1)

            while vcp2 > 21:
                tv2 = random.randint(1,10)
                ace(vcp2, tv2)
                vcp2 = vcp2 + tv2
                aaic.append(tv2)
                if count2 == 1:
                    print("The AI has drawn", tv2, "The AI has ", vcp2)
                    if count2 > 1:
                        print("The AI has drawn" )

            #To

            wincond(vcp1, vcp2, win)
            money_bet(money, bet, win,)
            hit1 = False

            if vcp1 > 21:
                break
            if vcp2 > 21:
                break

        if task == "stop" :
            break

        if hit1 is True:
            cv1 = random.randint(1,10)
            apc.append(cv1)
        if task == "double" :
            double(bet, money, vcp1, cv1, vcp2, tv2)
            wincond(vcp1, vcp2, win)
            money_bet(money, bet, win,)
            break

        if task == "stand":
            if vcp2 < vcp1:

                tv2 = random.randint(1,10)
                ace(vcp2, tv2)
                vcp2 = vcp2 + tv2
                aaic.append(tv2)
                print("The AI has drawn: ")


            if vcp2 > 21:
                wincond(vcp1, vcp2, win)
                money_bet(money, bet, win,)
                break
            elif vcp2 == 21:
                wincond(vcp1,vcp2,  win)
                money_bet(money, bet, win,)
                break
            elif vcp1 > vcp2 :
                print("")
                print("The AI had", vcp2)
                print("You had", vcp1)
                print("")
                print("All player cards, ")
                print(apc)
                print("All AI cards are ")
                print(aaic)
                print("YOU WON!!!")
                print("")
                print("end")
                win = True
                money_bet(money, bet, win,)
                break
            elif vcp1 < vcp2:
                print("")
                print("The AI had", vcp2)
                print("You had", vcp1)
                print("")
                print("All player cards, ")
                print(apc)
                print("All AI cards are ")
                print(aaic)
                print("YOU LOST lol")
                print("")
                print("")
                print("end")
                win = False
                money_bet(money, bet, win,)
                break
        continue
# How many times the game has been played +1 is added every time the wile loop has happened.
global gcount
gcount = 0.0
#points that the AI has acumulated +1 is added after each outcome that has the AI has won is used.
global aip
aip = 0.0
#Points of the player idem to le AI
global pwin
pwin = 0.0
#to clear the beard for each action
global nclear
nclear = 25
#total money
global money
money = 500
#Basically apc is all p cards and aaic is the same for the ai. So it stores what cards each person draws so we can ee it at the end
global apc
apc = [1, 2 ]

global aaic
aaic = [1, 2]

#vcp1 is value player card and vcp2 is the value of the ai card this is updated at each hit
global vcp1
vcp1 = 0.0

global vcp2
vcp2 = 0.0

#the win var is used to see if the bet was succesfulor not so to see if the winner wins or loses money
global win
win = True

while 1 < 2 :
    continuegame = True

    if win is True:
        pwin += 1       #Point logic
    elif win is False:
        aip += 1

    if gcount == 0:
        pwin = int(0)
        aip = int(0)
    elif gcount == 1:
        if win is True:       #This is because win is set as True so it gives a point to the player no matter what
            pwin -= 0.0
        elif win is False:
            aip -= 0.0


    print("")
    print("You have played:", gcount , "Games.")
    print("")
    print("The AI has: ", aip, "Points.  You have:", pwin, "Points")
    print("You have: ", money, "dollars")
    print("")
    rp = input("start or quit: ")
    if rp == "start":
        clear(nclear)
        apc *= 0
        aaic *= 0
        gcount = gcount + 1
        play()
        continue
    elif rp == "quit":
        continuegame = False
        break
print("")
print("The game has been exited")

print(win)


#31/10/2020 fixed everything i think only thing left is betting and making the code cleaner.
#smae day but at 21h30 variable win is not working for now and the how lmuchis your bet has been asked twice isuggest you ru some tests again tmr before starting
#The game doesnt end and basically im usingwin to see who gets the point but when i define it i gets 2 values so it wont work
# 24/11/2020 the pint system is working but the ai isnt
