import os
import time
import random

def start():
    intro()
    mainmenu()
    outro()


# Printed INTRO menu
def menu_intro():
    print(f"Tervetulo pelaamaan Pakettipilottia!")
    print(f"asd")
    print(f"asdasd")
    print(f"asdasdasd")


# Printed MAIN menu
def menu_main():
    print(f"// [MENU]")
    print(f"// Valitse syöttämällä luku!")
    print(f"-- 1: Ohje")
    print(f"-- 2: Uusi peli")
    print(f"-- 3: Pistetaulukko")
    print(f"-- 4: EXIT")


# Printed HELP menu
def menu_help():
    print("BlaBla")
    print("BlaBla")
    print("BlaBla")


# Strtup intro
def intro():
    screen_clear()
    menu_intro()
    time.sleep(2)


# Main menu logic
def mainmenu():
    option = False
    screen_clear()
    
    while option != "4":
        menu_main()
        option = input("== ")
        if option == "1":
            help()
            screen_clear()
        elif option == "2":
            newgame()
            screen_clear()
        elif option == "3":
            hiscore()
            screen_clear()


# Help menu logic
def help():
    screen_clear()
    option = False
    while option != "":
        menu_help()
        print("")
        option = input("*Paina ENTER palataksesi alkuvalikkoon*")


def newgame():
    print("2")


def hiscore():
    print("3")


def screen_clear():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Unix/Linux
        os.system('clear')

