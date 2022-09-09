# Kod som visar Discordmedlemmarna, får datan från en .txt fil.

def showList():
    list = open("list.txt", "rt")
    print(list.read())

def appentList():
    list = open("list.txt", "a")
    list.write("\n")
    list.write(input("Add to list: "))
    list.close()

# User menu
loop = 1

while loop == 1:

    print("\n1. Show all Discord users")
    print("2. Add new Discord user\n")

    state = int(input(""))

    # Show list of all users
    if state == 1:
        print("\n")
        showList()

    # Add new user
    elif state == 2:
        print("\n")
        appentList()

    loop = int(input("\n1. Return to main menu\n2. Exit\n"))