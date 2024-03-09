import time
import threading
from rich import print # Rich printing (colours, bolding, etc.)
from . import format # Game constants
from . import screen # Screen clearing etc.
from . import parcel_selection # Selection logic
from . import parcel_delivery # Delivery logic
from . import parcel_results # End screen logic


# Gameplay loop
def game_loop(player_list):
    game_parcel_list = parcel_selection.list_generate(test_parcels, test_airports) # Generate parcel options for current game.

    # 1: Player chooses their 5 parcels.
    for player in player_list:
        screen.new()
        option = False
        readyornot = input(f"""
[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][PAKETIN VALINTA][/italic #FF7F50]
[#6A5ACD]•[/#6A5ACD] Pelaajan [bold blue]{player["name"]}[/bold blue] vuoro valita pakettinsa! 
[#6A5ACD]•[/#6A5ACD] Sinulla on 30 sekuntia aikaa valita vapaasti viisi (5) pakettia listasta,
  jonka näet vuorosi alettua.

[yellow]*[/yellow] Paina [green]ENTER[/green] aloittaaksesi vuorosi [yellow]*[/yellow]
""")

        #while timer != 0:
        player["parcels_picked"] = parcel_selection.list_select(game_parcel_list)


    # 2: Players deliver their parcels.
    for player in player_list:
        screen.new()
        option = False
        readyornot = input(f"""
[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][PAKETIN TOIMITUS][/italic #FF7F50]
[#6A5ACD]•[/#6A5ACD] Pelaajan [bold blue]{player["name"]}[/bold blue] vuoro valita pakettinsa! 
[#6A5ACD]•[/#6A5ACD] Sinulla on 30 sekuntia aikaa valita vapaasti viisi (5) pakettia listasta,
  jonka näet vuorosi alettua.

[yellow]*[/yellow] Paina [green]ENTER[/green] aloittaaksesi vuorosi [yellow]*[/yellow]
""")

        #while timer != 0 or len(player["parcels_picked"]) == len(player["parcels_delivered"]):
        while len(player["parcels_picked"]) != len(player["parcels_delivered"]):
        
            # Player chooses parcel to deliver
            parcel_selected = parcel_delivery.select_delivery(player)
            player["parcels_delivered"].append(player["parcels_picked"][parcel_selected])
            
            # Player chooses delivery method
            player_co2_add = parcel_delivery.select_delivery_method(parcel_selected, player)
            
            # Tally co2 emissions
            #player_co2 = player["co2"]
            #player["co2"] = player_co2 + player_co2_add
            

    # 3: Players are shown the scoreboard
    screen.new()
    #parcel_results.ChangeMe()


# Startup sequence
def intro_static():
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

def intro_animated():
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
                player_new = format.player_structure(player_name) # Use player dict() structure from format.py
                player_list.append(player_new) # Add new player to next game participants
                screen.new()
                screen.feedback(player_name, "Pelaaja lisätty!")

        elif option == "2": # Start game
            screen.new()
            game_loop(player_list)
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
                        screen.feedback(player_remove, "Pelaaja poistettu!")
                    else:
                        screen.feedback(player_remove, "error")

        else: # If the user input other than predefined, throw error in feedback box.
            screen.new()
            screen.feedback(option, "error")
    
    player_list = list() # Reset player_list if the user leaves newgame menu.


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



## TEST DATA
test_parcels = [
("vasara",200,3,"Vasara on hieno vasara"),
("omena",300,1,"Omena on hieno omena"),
("tietokone",150,2,"tietoinen kone"),
("possu",175,1,"röh röh"),
("kaakao",500,2,"makeaa"),
("vaahtokarkki",1000,1,"kelluvaa"),
("takki",10,3,"lämmittää kivasti"),
("karkki",454,3,"aiai mun hampaat"),
("sitruuna",343,1,"kirpiää"),
("appelsiini",643,2,"appelsiini on hieno appelsiini")
]

test_airports = [
("Aavahelukka Airport","Suomi", 67.60359954833984,23.97170066833496),
("Ahmosuo Airport","Suomi",64.895302,25.752199),
("Alavus Airfield","Suomi",62.554699,23.573299),
("Jorvin Hospital Heliport","Suomi",60.220833,24.68639),
("Kilpisjärvi Heliport","Suomi",69.0022201538086,20.89638900756836),
("Enontekio Airport","Suomi",68.362602233887,23.424299240112),
("Eura Airport","Suomi",61.1161,22.201401),
("Forssa Airfield","Suomi",60.803683,23.650802),
("Genböle Airport","Suomi",60.086899,22.5219),
("Halli Airport","Suomi",61.856039,24.786686)
]
