import os
import time
import random

def start():
    intro()
    mainmenu()
    #outro()


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
    
    screen_clear()


# Main menu logic
def mainmenu():
    option = False
    screen_feedback(option, "none")

    while option != "4":
        menu_main()
        option = input("== ")
        if option == "1":
            screen_clear()
            help()
        elif option == "2":
            screen_clear()
            newgame()
        elif option == "3":
            hiscore()
        else:
            screen_clear()
            screen_feedback(option, "error")


# Help menu logic
def help():
    screen_clear()
    option = False
    while option == False:
        menu_help()
        print("")
        option = input("*Paina ENTER palataksesi alkuvalikkoon*\n\n")
        screen_clear()


def newgame():
    print("2")


def hiscore():
    print("3")


def screen_clear():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Unix/Linux
        os.system('clear')

def screen_feedback(input, feedback_type):
    if feedback_type == "error":
        print(f"[ Virheellinen syöte: \"{input}\" ! ]")
        print("")
    elif feedback_type == "none":
        print(f"[ {'~' * 24} ]")
        print("")

