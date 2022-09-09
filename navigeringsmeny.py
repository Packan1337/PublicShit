# Experiment menynavigering

mainMenu = ["1. Bygg ny bil", "2. Köp begangnad bil", "3. Sälj din bil"]
bilMenu = ["1. Mercedes-AMG S65 4MATIC+ Coupé", "2. Bentley Continental GT", "3. BMW M8 Competition xDrive"]

print("")
print("Välkommen till menynavigering!\n")

for i in mainMenu:
        print(i)

print("")
userAnsw = int(input("Välj alternativ: "))

if userAnsw == 1:
    print("")
    print("Bygg ny bil\n")

    for i in bilMenu:
        print(i)

    print("")
    userAnsw = int(input("Välj alternativ: "))

    if userAnsw == 1:
        print("")
        print("Du vill bygga en Mercedes-AMG S65 4MATIC+ Coupé.")

    elif userAnsw == 2:
        print("")
        print("Du vill bygga en Bentley Continental GT.")

    elif userAnsw == 3:
        print("")
        print("Du vill bygga en BMW M8 Competition xDrive")

elif userAnsw == 2:
    print("Köp begangnad bil\n")
    print("Välj från listan\n")

    for i in bilMenu:
        print(i)

    print("")
    userAnsw = int(input("Välj alternativ: "))

    if userAnsw == 1:
        print("")
        print("Du vill köpa en begagnad Mercedes-AMG S65 4MATIC+ Coupé.")

    elif userAnsw == 2:
        print("")
        print("Du vill köpa en begangnad Bentley Continental GT.")

    elif userAnsw == 3:
        print("")
        print("Du vill köpa en begangnad BMW M8 Competition xDrive")

elif userAnsw == 3:
    print("jag orkar inte göra den här delen än")
