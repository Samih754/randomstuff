import random

money = 500

def none():
    int(0 if value is None else value)

def lwmoney(vcp1):
    if vcp1 > 21 :
        money = money - bet
    if vcp2 == 21:
        money = money -bet
    if vcp2 > 21:
        money = money + bet * 2
def hit():
    random.randint(1, 10)

def ace(v):
    if v >= 10:
        v == 1

def bet(bet):
    bet = input("What is your bet?: ")
    bet = float(bet)
    if bet > money:
        print("refuse bet")

def double(m):
    if bet * 2 > money:
        print("refuse bet")
    bet = bet * 2
    hit()

if input('Restart press: start: ') == ('start'):
    vcp1 = 0
    vcp2 = 0
    v1 = 0
    v2 = 0
    tv2 = 0
    count2 = 0
    AIp = 0
    pp = 0

    if vcp1 == 0:
        vcp1 = random.randint(1,10)
    print("You have drawn:", vcp1)

    if vcp2 == 0:
        vcp2 = random.randint(1,10)
    print("The AI has ", vcp2)

while vcp1 or vcp2 <= 21:
    task = input("hit, stop, stand, double?: ")
    if task == "hit" :

        print("ok")
        print("")
        count2 = count2 + 1
        cv1 = random.randint(1, 10)
        ace(cv1)
        vcp1 = vcp1 + cv1
        print("You have: ", vcp1)

        tv2 = random.randint(1,10)
        ace(tv2)
        vcp2 = vcp2 + tv2
        if count2 == 1:
            print("The AI has drawn", tv2, "The AI has ", vcp2)
        if count2 > 1:
            print("The AI has drawn" )


    if task == "stop" :
        break

    if task == "double" :
        double()

    if task == "stand":
            tv2 = random.randint(1,10)
            vcp2 = vcp2 + tv2
            print("The AI has drawn: ")
            if vcp2 > 21:
                print("")
                print("The AI has", vcp2)
                print("You have", vcp1)
                print("YOU WON!!!")
            elif vcp1 > vcp2:
                print("")
                print("The AI has", vcp2)
                print("You have", vcp1)
                print("YOU WON!!!")
            elif vcp1 < vcp2:
                print("")
                print("The AI has", vcp2)
                print("You have", vcp1)
                print("YOU LOST lol")
            break

    elif vcp1 == 21:
        print("")
        print("You have won gg")
        print("The AI has", vcp2)
        print("You have", vcp1)
        break
    elif vcp2 == 21:
        print("")
        print("you lost lol get rekt")
        print("The AI has", vcp2)
        print("You have", vcp1)
        break

    elif vcp1 > 21:
        print("")
        print("The AI has", vcp2)
        print("You have", vcp1)
        print("YOU LOST lol")
        break
    elif vcp2 > 21:
        print("")
        print("The AI has", vcp2)
        print("You have", vcp1)
        print("YOU WON!!!")
        break


print("end")
