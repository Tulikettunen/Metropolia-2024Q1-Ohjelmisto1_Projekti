import time
import threading
from rich import print
from . import screen
#from . import parcel_selection # Selection logic
#from . import parcel_delivery # Delivery logic
#from . import parcel_results # End screen logic


# Gameplay loop
def game_loop():
    #parcel_selection
    for player in players:
        screen.new()
        turn(parcel_selection.ChangeMe, 30, event)
    
    #parcel_delivery
    for player in players:
        screen.new()
        turn(parcel_delivery.ChangeMe, 120, event)
    
    #parcel_results
    screen.new()
    parcel_results.ChangeMe()


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
    screen.clear() # Return user to clean terminal


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
            menu_help()
            screen.new()
        elif option == "2":
            menu_newgame()
            screen.new()
        elif option == "3":
            menu_hiscore()
            screen.new()
        else: # If the user input other than predefined, throw error in feedback box.
            screen.feedback(option, "error")


# Begin a new game
def menu_newgame():
    screen.new()
    option = False
    player_list = list()
    
    while option != "4":
        if player_list != []:
            print(f"""
[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][UUSI PELI][/italic #FF7F50]
[#6A5ACD]•[/#6A5ACD] [bold blue]1:[/bold blue] Lisää uusi pelaaja
[#6A5ACD]•[/#6A5ACD] [bold blue]2:[/bold blue] Aloita peli
[#6A5ACD]•[/#6A5ACD] [bold blue]3:[/bold blue] Poista pelaaja
[#6A5ACD]•[/#6A5ACD] [bold blue]4:[/bold blue] Palaa alkuvalikkoon

[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][PELAAJAT][/italic #FF7F50]""")
            for player in player_list:
                print(f"[#6A5ACD]•[/#6A5ACD] [bold blue]{player['name']}[/bold blue]")
        if player_list == []:
            print(f"""
[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][UUSI PELI][/italic #FF7F50]
[#6A5ACD]•[/#6A5ACD] [bold blue]1:[/bold blue] Lisää uusi pelaaja
[#6A5ACD]•[/#6A5ACD] [bold blue]2:[/bold blue] Aloita peli
[#6A5ACD]•[/#6A5ACD] [bold blue]4:[/bold blue] Palaa alkuvalikkoon

[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][PELAAJAT][/italic #FF7F50]""")
        
        option = input("\n>> ")
        if option == "1": # Add player
            player_name = input(">> Syötä pelaajan nimi: ")
            player_in_list = False
            
            for player in player_list:
                if player.get("name") == player_name:
                    player_in_list = True
            
            if player_in_list:
                screen.new()
                screen.feedback(player_name, "Nimimerkki on jo käytössä!")
            else:
                player_new = player_structure(player_name)
                player_list.append(player_new)
                screen.new()
                screen.feedback(player_name, "Pelaaja lisätty!")

        elif option == "2": # Start game
            screen.new()
            game_loop()
            break # Return to main menu
        
        elif option == "3": # Remove player
            if player_list == []:
                screen.new()
                screen.feedback(option, "error")
            else: 
                player_remove = input(">> Poista pelaaja: ")
                for player in player_list:
                    if player.get("name") == player_remove: # If player present
                        player_list.remove(player)
                        screen.new()
                    else:
                        screen.feedback(player_remove, "error")
        
        else: # If the user input other than predefined, throw error in feedback box.
            screen.new()
            screen.feedback(option, "error")
    
    player_list = list()


# Display help
def menu_help():
    screen.new()
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
def menu_hiscore():
    option = False
    # TBD


# Turnclock
def clock(time_seconds, event):
    for i in range(time_seconds, -1, -1): # Sleep through time_seconds
        #print(i)
        time.sleep(1)
    event.set() # Set event to signal completion


# Turn-logic (runs "loop" until "time_seconds" runs out)
def turn(loop, clock, time_seconds, event):
    # Define threads for loop & clock
    thread_loop = threading.Thread(target=loop, args=())
    thread_clock = threading.Thread(target=clock, args=(time_seconds, event))

    # Start our threads
    thread_loop.start()
    thread_clock.start()

    # Wait for thread_clock to signal completion via event=True
    thread_clock.join()

def player_structure(player_name):
    return { "name": player_name, "score": False, "co2": 0, "location": False, "parcel_list_picked": False, "parcel_list_delivered": False }
