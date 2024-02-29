import os
import time
import random
from rich import print


def start():
    screen_clear()
    intro()
    
    screen_new()
    mainmenu()
    screen_clear()    

    outro()
    screen_clear()


# Startup sequence
def intro():
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
    time.sleep(2)


# Exit sequence
def outro():
    print(f"""Kiitos kun pelasit![#3CB371]
 _   _  _   _  _                     _  _         _ 
| \ | |(_) (_)| |                   (_)(_)       | |
|  \| |  __ _ | | __ ___  _ __ ___   _  _  _ __  | |
| . ` | / _` || |/ // _ \| '_ ` _ \ | || || '_ \ | |
| |\  || (_| ||   <|  __/| | | | | || || || | | ||_|
|_| \_| \__,_||_|\_|\___||_| |_| |_||_||_||_| |_|(_)
[/#3CB371]""")
    time.sleep(1.5)


# Gameplay loop (package selection -> package delivery -> end screen)
def game_loop():
    screen_new()
    parcel_selection()

    screen_new()
    parcel_delivery()

    screen_new()
    parcel_results()

    screen_new()


# Players select their packages
def parcel_selection():
    print("tbd: parcel_selection")


# Players deliver their packages
def parcel_delivery():
    print("tbd: parcel_delivery")


# Players are shown their scores
def parcel_results():
    print("tbd: parcel_results")


# Primary game menu
def mainmenu():
    option = False

    while option != "4":
        print(f"""
[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][ALKUVALIKKO][/italic #FF7F50]
[#6A5ACD]•[/#6A5ACD] [bold blue]1:[/bold blue] Ohje
[#6A5ACD]•[/#6A5ACD] [bold blue]2:[/bold blue] Uusi peli
[#6A5ACD]•[/#6A5ACD] [bold blue]3:[/bold blue] Pistetaulukko
[#6A5ACD]•[/#6A5ACD] [bold blue]4:[/bold blue] EXIT
""")
        option = input(">> ")
        if option == "1":
            screen_new()
            help()
            screen_new()
        elif option == "2":
            screen_new()
            newgame()
            screen_new()
        elif option == "3":
            screen_new()
            hiscore()
            screen_new()
        else: # If the user input other than predefined, throw error in feedback box.
            screen_clear()
            screen_feedback(option, "error")


# TBD
def newgame():
    option = False

    while option != "3":
        print(f"""
[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][UUSI PELI][/italic #FF7F50]
[#6A5ACD]•[/#6A5ACD] [bold blue]1:[/bold blue] Lisää uusi pelaaja
[#6A5ACD]•[/#6A5ACD] [bold blue]2:[/bold blue] Aloita peli
[#6A5ACD]•[/#6A5ACD] [bold blue]3:[/bold blue] Palaa alkuvalikkoon
""")
        option = input(">> ")
        if option == "1": # Add new player to current game
            print("Added new player!")
        elif option == "2": # Start game
            game_loop()
            break # Return to main menu after gameplay loop is complete.
        else: # If the user input other than predefined, throw error in feedback box.
            screen_clear()
            screen_feedback(option, "error")


# Help menu screen
def help():
    option = False
    while option == False:
        print(f"""
[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][OHJE][/italic #FF7F50]
[#6A5ACD]•[/#6A5ACD] Pelin tavoitteena on toimittaa kaikki pelivuoron alussa
  valitut paketit niiden kohteeseen, ennen määräajan loppumista.
[#6A5ACD]•[/#6A5ACD] Peliä voi pelata kerrallaan yksi tai useampi henkilö.
[#6A5ACD]•[/#6A5ACD] Suoritus pisteytetään pelaajan hiilidioksidipäästöjen mukaan.
  Päästöjen suuruuteen vaikuttaa: [yellow]tavaranimikkeen tyyppi[/yellow], [yellow]kuljettu matka[/yellow] ja [yellow]kuljetusmuoto[/yellow].

[yellow]*[/yellow] Paina [green]ENTER[/green] palataksesi alkuvalikkoon [yellow]*[/yellow]
""")
        option = input()


# Hiscore menu logic
def hiscore():
    option = False
    # TBD


# Clear terminal function
def screen_clear():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Unix/Linux
        os.system('clear')


# Print feedback box at top of the CLI.
def screen_feedback(user_input, feedback_type):
    if feedback_type == "error":
        print(f"[ Virheellinen syöte: [red]\"{user_input}\"[/red] ! ]")
    elif feedback_type == "none":
        print(f"[ {'~' * 24} ]")


# Clears screen and sets EMPTY feedback box.
def screen_new():
    screen_clear()
    option = False
    screen_feedback(option, "none")

