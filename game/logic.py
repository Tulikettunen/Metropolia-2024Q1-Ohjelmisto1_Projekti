def start():
    mainmenu()


# Printed MAIN menu
def menu_main():
    print(f"[MENU]")
    print(f"1: Ohje")
    print(f"2: Uusi peli")
    print(f"3: Pistetaulukko")
    print(f"4: EXIT")


# Printed HELP menu
def menu_help():
    print("BlaBla")
    print("BlaBla")
    print("BlaBla")


# Main menu logic
def mainmenu():
    option = False
    while option != "4":
        menu_main()
        option = input("== ")
        
        if option == "1":
            help()
        elif option == "2":
            newgame()
        elif option == "3":
            hiscore()


# Help menu logic
def help():
    option = False
    while option != "":
        menu_help()
        option = input("*Paina ENTER palataksesi alkuvalikkoon*")


def newgame():
    print("2")


def hiscore():
    print("3")


