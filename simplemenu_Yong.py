
from lab5_library_Yong import *
def simplemenu():
    while True:
        choice = '0'
        while choice == '0':
            print("Welcome! Please choose 1 of 5 choices to test the function.")
            print("Choose 1 for testing Vertical line")
            print("Choose 2 for testing Horizontal line")
            print("Choose 3 for testing Staircase")
            print("Choose 4 for testing Random pixel")
            print("Choose 5 for testing Clear Backlight")
            print("Choose 6 to exit python")
            choice = input("Please choose one of the options: ")
            if choice == "5":
                print("Clear Backlight")
                clearBacklight()
            elif choice == "4":
                print("Random pixel")
                print("Ctrl+c to stop")
                randompixel()
            elif choice == "3":
                print("Staircase")
                a=int(input("The x is "))
                b=int(input("The y is "))
                c=int(input("The w is "))
                d=int(input("The h is "))
                staircase(a,b,c,d)
            elif choice == "2":
                print("Horizontal line")
                e=int(input("Give me a Y: "))
                horizontalline(e)
            elif choice == "1":
                print("Vertical line")
                f = int(input("Give me a X: "))
                verticalline(f)
            elif choice == "6":
                print('Goodbye')
                exit()
            else:
                print("Please choose 1 to 5")


simplemenu()