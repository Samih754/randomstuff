import random


def pcguess():
    win = False
    #lower and higher is the range in which the numlber will be in
    print("")
    lower = int(input("From what number: "))
    print("")
    higher = int(input("Up to what number: "))

    numbtofind = int(input("choose a number: "))
    #number of tentavtives
    times = 0

    while win == False:
        times += 1
        a = random.randint(lower, higher ) #chooses randoim numlber between what the user wrote for hihjer and lower
        print("")
        print(a)
        if a == numbtofind:   #checks to see if the number it chose is the same that the player chose if it is it will porint the folowing sequence
            print("")
            print("Your number is, ", a)
            print("")
            print("The PC won")
            win = True #makes win True so that the infinite loop ends
        else:
            print("")
            search = input("higher or lower?: ")
            print("")
            if search == "higher":
                lower = a + 1        #if its higher then the lowest possible nulebr will be the  number the PC found +1
            elif search == "lower":
                higher = a - 1  #same as above but the opposite
            else:
                print("please write higher or lower: ")

    print("")
    print("It took the PC", times, "tries to find your number")

def youguess():
    win2 = False

    times2 = 0

    lower2 = int(input("From what number?: "))
    higher2 = int(input("Until what number?: "))
    guess = 0.0


    numbtofind2 = random.randint(lower2, higher2)
    while win2 == False:
        guess = int(input("Guess a number between: "))

        times2 += 1

        if guess == numbtofind2:
            win2 = True
            print("")
            print(" You guessed right!!: the number to find was ", numbtofind2, "")
            print("")
            print("It took you", times2, "Times to guess the right number")
        elif guess < numbtofind2:
            print("")
            print("You guessed too low. Choose a number above", guess,"and lower than", higher2, ": ")
        elif guess > numbtofind2:
            print("")
            print("You guessed too high. Choose a number below", guess,"and higher than", lower2, ": ")

print("")
action = input("Press 1 to have the PC play agint you. Press 2 to play againt the PC: ")
print("")
if action == "1":
    pcguess()
elif action == "2":
    youguess()
