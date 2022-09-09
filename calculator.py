# PACKAN LIMITED EDITION CALCULATOR, 2022
import math

print("WELCOME TO PACKAN'S CALCULATOR, THE BEST CALCULATOR SINCE SLICED BREAD!\n")
print("Choose an operator, bitch\n")

select = int(input("1. ADD\n2. SUBTRACT\n3. MULTIPLY\n4. DIVIDE\n5. SHOW ME PI\n \n"))

if select == 1:

    print("\nYou chose ADD\n")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    res = num1 + num2

    print(str(num1) + " + " + str(num2) + " = " + str(res))


elif select == 2:

    print("\nYou chose SUBTRACT\n")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    res = num1 - num2

    print(str(num1) + " - " + str(num2) + " = " + str(res))


elif select == 3:

    print("\nYou chose MULTIPLY\n")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    res = num1 * num2

    print(str(num1) + " x " + str(num2) + " = " + str(res))


elif select == 4:

    print("\nYou chose DIVIDE\n")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    res = num1 / num2

    print(str(num1) + " / " + str(num2) + " = " + str(res))


elif select == 5:
    print(math.pi)