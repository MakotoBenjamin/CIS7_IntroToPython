import random

userNum = eval(input("scissor (0), rock (1), paper (2): "))

compNum = random.randint(0,2)

userHand = "null"
compHand = "null"

#Assigning string value based on number user inputs
if userNum > 2:
    print("!Invalid entry!\n---Exiting Program---")
    quit()
elif userNum == 0:
    userHand = "scissor"
elif userNum == 1:
    userHand = "rock"
else:
    userHand = "paper"

#Assigning string value based on number generated for computer
if compNum == 0:
    compHand = "scissor"
elif compNum == 1:
    compHand = "rock"
else:
    compHand = "paper"

if userNum == compNum:
    print("The computer is " + compHand + ". You are " + userHand + ". It is a draw.")
elif (userNum == 0 and compNum == 2) or (userNum == 1 and compNum == 0) or (userNum == 2 and compNum == 1):
    print("The computer is " + compHand + ". You are " + userHand + ". You won.")
else:
    print("The computer is " + compHand + ". You are " + userHand + ". You lose.")
