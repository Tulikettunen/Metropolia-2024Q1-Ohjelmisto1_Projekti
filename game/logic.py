import time
from rich import print
from . import screen
#from . import parcel_selection # Selection logic
#from . import parcel_delivery # Delivery logic
#from . import parcel_results # End screen logic


# Gameplay loop
def game_loop():
    screen.new()
    parcel_selection.start

    screen.new()
    parcel_delivery.start

    screen.new()
    parcel_results.start

    screen.new()

# Startup sequence
def intro():
    screen.clear()
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
    screen.clear()
    print(f"""Kiitos kun pelasit![#3CB371]
 _   _  _   _  _                     _  _         _ 
| \ | |(_) (_)| |                   (_)(_)       | |
|  \| |  __ _ | | __ ___  _ __ ___   _  _  _ __  | |
| . ` | / _` || |/ // _ \| '_ ` _ \ | || || '_ \ | |
| |\  || (_| ||   <|  __/| | | | | || || || | | ||_|
|_| \_| \__,_||_|\_|\___||_| |_| |_||_||_||_| |_|(_)
[/#3CB371]""")
    time.sleep(1.5)
    screen.clear()


# Start menu
def menu():
    screen.new()
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
            screen.new()
            help()
            screen.new()
        elif option == "2":
            screen.new()
            newgame()
            screen.new()
        elif option == "3":
            screen.new()
            hiscore()
            screen.new()
        else: # If the user input other than predefined, throw error in feedback box.
            screen.clear()
            screen.feedback(option, "error")


# Begin a new game
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
            screen.clear()
            screen.feedback(option, "error")


# Display help
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


# Display hiscores
def hiscore():
    option = False
    # TBD

