import time
import sys, os
spot =["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]

# Status check
Player = 1
Win = 1
Draw = -1
Stop = 1
Running = 0
Game = Running
Mark = "X"


# Function that prints game board
def draw_board():
    print(f'''
       a        b        c
            |       |
    1   {spot[1]}   |   {spot[2]}   |    {spot[3]}
            |       |
     -------|-------|--------
            |       |
    2   {spot[4]}   |   {spot[5]}   |    {spot[6]}
            |       |
     -------|-------|--------
            |       |
    3   {spot[7]}   |   {spot[8]}   |    {spot[9]}
            |       |        
    ''')


# Function to check for spot availability
def available_spot(x):
    if spot[x] == '-':
        return True
    else:
        return False


def status_check():
    global Game

    # Checking for horizontal win
    if spot[1] == spot[2] and spot[2] == spot[3] and spot[1] != "-":
        Game = Win
    elif spot[2] == spot[5] and spot[5] == spot[6] and spot[4] != "-":
        Game = Win
    elif spot[7] == spot[8] and spot[8] == spot[9] and spot[7] != "-":
        Game = Win

    # Checking for vertical win
    if spot[1] == spot[4] and spot[4] == spot[7] and spot[1] != "-":
        Game = Win
    elif spot[2] == spot[5] and spot[5] == spot[8] and spot[2] != "-":
        Game = Win
    elif spot[3] == spot[6] and spot[6] == spot[7] and spot[3] != "-":
        Game = Win

    # Checking for vertical win
    if spot[1] == spot[5] and spot[5] == spot[9] and spot[5] != "-":
        Game = Win
    elif spot[2] == spot[5] and spot[5] == spot[7] and spot[5] != "-":
        Game = Win
    elif spot[1] != "-"\
            and spot[2] != "-"\
            and spot[3] != "-"\
            and spot[4] != "-"\
            and spot[5] != "-"\
            and spot[6] != "-"\
            and spot[7] != "-"\
            and spot[8] != "-"\
            and spot[9] != "-":
        Game = Draw


print("Welcome to Packan's TicTacToe!")
print("(code partly stolen from the internet...)\n")
player1 = input("P1 Enter name: ")
player2 = input("P2 Enter name: ")

print("\nSaving", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".")
time.sleep(0.5)

while Game == Running:
    draw_board()
    if Player % 2 != 0:
        print(f"{player1}'s turn!")
        Mark = "X"
    else:
        print(f"{player2}'s turn!")
        Mark = "O"
    choice = int(input("Enter spot position (1 - 9): "))
    if available_spot(choice):
        spot[choice] = Mark
        Player += 1
        status_check()

draw_board()
if Game == Draw:
    print("Tie!")
elif Game == Win:
    Player -= 1
    if Player % 2 != 0:
        print(f"{player1} won!")
    else:
        print(f"{player2} won!")