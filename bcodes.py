from os import system

def display():
    print("BUNKER/SHACK ACCESS CODES")
    print()
    print("1. PRISON SHACK")
    print("2. FARMLAND")
    print("3. SOUTH NEAR BONEYARD")
    print("4. NORTH NEAR BONEYARD")
    print("5. PARK")
    print("6. TV STATION")
    print()

def optionDisplay():
    option = input("Would you like to try a different option? (Y/N): ")
    if option == 'Y' or option == 'y':
        system("cls")
        main()
    elif option == 'N' or option == 'n':
        system("cls")
        print("EXITING PROGRAM . . .")
    else:
        print("INVALID INPUT! PLEASE TRY AGAIN")
        print()
        optionDisplay()
    
def codes():
    choice = input("Please choose one of the following options: ")
    while True:
        system("cls")
        if choice == '1':
            print("PRISON SHACK: \n\n7-2-9-4-8-5-3-1 \n")
        elif choice == '2':
            print("FARMLAND: \n\n4-9-2-8-5-1-6-3 \n")
        elif choice == '3':
            print("SOUTH NEAR BONEYARD: \n\n9-7-2-6-4-1-3-8 \n")
        elif choice == '4':
            print("NORTH NEAR BONEYARD: \n\n8-7-6-2-4-8-5-1 \n")
        elif choice == '5':
            print("PARK: \n\n6-0-2-7-4-5-1-3 \n")
        elif choice == '6':
            print("TV STATION: \n\n2-7-4-9-5-8-1-0 \n")
        else:
            print("INVALID INPUT! PLEASE TRY AGAIN")
            print()
            
        optionDisplay()
        break
            

def main():
    display()
    codes()

main()
