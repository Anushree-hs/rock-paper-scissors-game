import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


player_choice = input("Player's choice:\nEnter...\n1 for rock\n2 for paper\n3 for scissors\n\n")
player = int(player_choice)
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2 or 3.")

computer_choice = random.choice("123")
computer = int(computer_choice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.','') + ".")
print("Computer chose " + str(RPS(computer)).replace('RPS.','') + ".")
print("")

if player == 1 and computer == 3:
    print("🥳 You Win!")
elif player == 2 and computer == 1:
    print("🥳 You Win!")
elif player == 3 and computer == 2:
    print("🥳 You Win!")
elif player == computer:
    print("😯 Its a Tie")
else:
    print("🐍 Computer Won!")
