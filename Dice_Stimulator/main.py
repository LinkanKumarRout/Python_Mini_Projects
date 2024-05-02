import random

print(".......Welcome to Dice Stimulator.......")
while True:
    print("\nYou have these options...\n")
    print("1. Roll the Dice (Press 1)")
    print("2. Exit (Press 2)")
    user_input = int(input("\nEnter your choice: "))
    if user_input == 1:
        number = random.randint(1,6)
        if number == 1:
            print("===========")
            print("|         |")
            print("|    O    |")
            print("|         |")
            print("===========")

        if number == 2:
            print("===========")
            print("|         |")
            print("| O     O |")
            print("|         |")
            print("===========")

        if number == 3:
            print("===========")
            print("|    O    |")
            print("|    O    |")
            print("|    O    |")
            print("===========")

        if number == 4:
            print("===========")
            print("| O     O |")
            print("|         |")
            print("| O     O |")
            print("===========")
            
        if number == 5:
            print("===========")
            print("| O     O |")
            print("|    O    |")
            print("| O     O |")
            print("===========")
            
        if number == 6:
            print("===========")
            print("| O     O |")
            print("| O     O |")
            print("| O     O |")
            print("===========")
    elif user_input == 2:
        print("\nBye....\n")
        break
    else:
        print("\nPlease enter a valid option !!\n")