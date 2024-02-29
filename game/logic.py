import os
import time
import random
from rich import print


def start():
    intro()
    mainmenu()
    outro()


# Printed INTRO menu
def menu_intro():
    print(f"""Tervetuloa pelaamaan Pakettipilottia!
[#B0C4DE]
[#BC8F8F]   .+---------+[/#BC8F8F]
[#BC8F8F] .' |       .'|[/#BC8F8F]                  .
[#BC8F8F]+----+----+'  |[/#BC8F8F]   .. ............;;.
[#BC8F8F]|   |    |    |[/#BC8F8F]    ..::::::::::::;;;;.
[#BC8F8F]|  .+----+----+[/#BC8F8F]  . . ::::::::::::;;:'
[#BC8F8F]|.'      |  .'[/#BC8F8F]                  :'
[#BC8F8F]+--------+'[/#BC8F8F]
[/#B0C4DE]""")


def menu_outro():
    print(f"""Kiitos kun pelasit![#3CB371]
  _   _  _   _  _                     _  _         _ 
 | \ | |(_) (_)| |                   (_)(_)       | |
 |  \| |  __ _ | | __ ___  _ __ ___   _  _  _ __  | |
 | . ` | / _` || |/ // _ \| '_ ` _ \ | || || '_ \ | |
 | |\  || (_| ||   <|  __/| | | | | || || || | | ||_|
 |_| \_| \__,_||_|\_|\___||_| |_| |_||_||_||_| |_|(_)
[/#3CB371]""")


# Printed MAIN menu
def menu_main():
    print(f"""
[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][ALKUVALIKKO][/italic #FF7F50]
[#6A5ACD]•[/#6A5ACD] [bold blue]1:[/bold blue] Ohje
[#6A5ACD]•[/#6A5ACD] [bold blue]2:[/bold blue] Uusi peli
[#6A5ACD]•[/#6A5ACD] [bold blue]3:[/bold blue] Pistetaulukko
[#6A5ACD]•[/#6A5ACD] [bold blue]4:[/bold blue] EXIT
""")


# Printed HELP menu
def menu_help():
    print(f"""
[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][OHJE][/italic #FF7F50]

[#6A5ACD]•[/#6A5ACD] Pelin tavoitteena on toimittaa kaikki pelivuoron alussa
  valitut paketit niiden kohteeseen, ennen määräajan loppumista.
[#6A5ACD]•[/#6A5ACD] Peliä voi pelata kerrallaan yksi tai useampi henkilö.
[#6A5ACD]•[/#6A5ACD] Suoritus pisteytetään pelaajan hiilidioksidipäästöjen mukaan.

[yellow]*[/yellow] Paina [green]ENTER[/green] palataksesi alkuvalikkoon [yellow]*[/yellow]""")

# Startup intro
def intro():
    screen_clear()
    menu_intro()
    time.sleep(2)
    
    screen_clear()


# Exit outro
def outro():
    screen_clear()
    menu_outro()
    time.sleep(1.5)

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
        screen_feedback(option, "none")
        menu_help()
        option = input()
        
        screen_clear()
        screen_feedback(option, "none")


def newgame():
    print("2")


def hiscore():
    print("3")


def screen_clear():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Unix/Linux
        os.system('clear')


def screen_feedback(user_input, feedback_type):
    if feedback_type == "error":
        print(f"[ Virheellinen syöte: [red]\"{user_input}\"[/red] ! ]")
    elif feedback_type == "none":
        print(f"[ {'~' * 24} ]")

