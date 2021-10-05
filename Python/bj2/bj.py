import os
import random

# we are going to put all of the variables to global. and equal to zero or false. This will change as the user inputs scripts like run etc..
#This project does blackjack. Started the 9th of january at 18.12 pm in paris france by Sami alias AlliagePiano10

#how many cards the player has hit. same for the ai
global numbofplayercards
numbofplayercards = 0.0

global numbofaicards
numbofaicards = 0.0

#it will be thevlaue chosen when the player presses hit or double. will be reset at each hit. Same thing for the AI
global playerdrawvalue
playerdrawvalue = 0.0

global aidrawvalue
aidrawvalue = 0.0

#the addition of all the card he hit. same for the ai
global playertotalcardvalue
playertotalcardvalue = 0.0

global aitotalvardvalue
aitotalvardvalue = 0.0

#player money will be how much money the player has it will cghange in fucntion of the how much he bet and iuf he won or not.
global money
money = 100

#how much the player bet. will be reset at each game.
global bet
bet = 0.0

#this will determine what function will be executed hit stand double or quit.
global action
action = (""

#how many gaem
