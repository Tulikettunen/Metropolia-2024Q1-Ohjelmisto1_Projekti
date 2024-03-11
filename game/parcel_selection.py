# Parcel Selection Logic
import random
import time
from rich import print
from . import format
from . import screen
from . import parcel_delivery


# Define heft_classes from format.py
heft_classes = format.heft_classes


def list_generate(parcels_list, airports_list):
    """
    Takes: 1. parcels list, 2. airports list.
    Combines inputs into a single list as structured dictionaries, and returns it.
    
    { item, co2_item, heft, info, destination_airport, destination_country, latitude, longitude }
    """

    combined_list = []

    for i in range(len(parcels_list)):
        # Attribute a random weight for the item, based on its heft type.
        random_weight = float(f"{random.uniform(heft_classes.get(parcels_list[i][2])[0],heft_classes.get(parcels_list[i][2])[1]):.2f}")

        # Combine into single list
        combined_list.append({"item": parcels_list[i][0],"co2_item": parcels_list[i][1],
        "heft": random_weight,"info": parcels_list[i][3],"destination_airport": airports_list[i][0],
        "destination_country": airports_list[i][1], "latitude": airports_list[i][2],"longitude": airports_list[i][3]})

    return combined_list # Return the combined list


def list_print(game_parcel_list, options_list):
    """
    Print the game_parcel_list to the player,
    so they can choose their parcels.
    """
    
    i = 1 # Start counting from 1, so the menu indexes run from 1-10 (displayed to player).
    
    print(f"[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][PAKETIN VALINTA][/italic #FF7F50]\n")    
    print("[#C39BD3]// Valitse seuraavasta kymmenestä vaihtoehdosta viisi:[/#C39BD3]")
    for item in game_parcel_list:
        if str(i) in options_list:
            print(f"[#C39BD3]•[/#C39BD3] [[yellow]{i}[/yellow]]: {item.get('item')}: {item.get('info')}. Paino: {item.get('heft')} kg.")
        else:
            print(f"[#C39BD3]•[/#C39BD3] [[green]x[/green]]: {item.get('item')}: {item.get('info')}. Paino: {item.get('heft')} kg.")
        i += 1


#list_print(game_parcel_list)


def list_select(game_parcel_list):
    """
    The player is provided a list of selectable parcels,
    from which they must choose enough before the timer runs out.
    """
    start_time = time.time()
    option = False
    screen.feedback("time",parcel_delivery.how_much_time_is_left(start_time,format.parcel_selection_time_limit))
    options_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    list_print(game_parcel_list, options_list)
    option = input(">> ")
    i = 1
    player_parcel_list = []
    while i <= 5 and parcel_delivery.is_there_time_left(start_time, format.parcel_selection_time_limit):
        if option in options_list:
            player_parcel_list.append(game_parcel_list[int(option) - 1])
            options_list.remove(option)
            i += 1
            if i == 6:
                print(">> Kaikki paketit valittu!")
                time.sleep(1.5)
                break
            screen.feedback("time",parcel_delivery.how_much_time_is_left(start_time, format.parcel_selection_time_limit))
            list_print(game_parcel_list, options_list)
            option = input(">> ")
        elif option in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            screen.new()
            screen.feedback(option, "Paketti on jo valittu!")
            list_print(game_parcel_list, options_list)
            option = input(">> ")
        else:
            screen.new()
            screen.feedback(option, "error")
            list_print(game_parcel_list, options_list)
            option = input(">> ")
    return player_parcel_list



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

game_parcel_list = [{'item': 'vasara', 'co2_item': 200, 'heft': 8.19, 'info': 'Vasara on hieno '
                    'vasara', 'destination_airport': 'Aavahelukka Airport', 'destination_country':
    'Suomi', 'latitude': 67.60359954833984, 'longitude': 23.97170066833496}, {'item': 'omena',
    'co2_item': 300, 'heft': 0.35, 'info': 'Omena on hieno omena',
    'destination_airport': 'Ahmosuo Airport', 'destination_country': 'Suomi', 'latitude': 64.895302,
    'longitude': 25.752199}, {'item': 'tietokone', 'co2_item': 150, 'heft': 2.7,
    'info': 'tietoinen kone', 'destination_airport': 'Alavus Airfield', 'destination_country': 'Suomi',
    'latitude': 62.554699, 'longitude': 23.573299}, {'item': 'possu', 'co2_item': 175, 'heft': 0.76,
    'info': 'röh röh', 'destination_airport': 'Jorvin Hospital Heliport', 'destination_country': 'Suomi',
    'latitude': 60.220833, 'longitude': 24.68639}, {'item': 'kaakao', 'co2_item': 500, 'heft': 2.78,
    'info': 'makeaa', 'destination_airport': 'Kilpisjärvi Heliport', 'destination_country': 'Suomi',
    'latitude': 69.0022201538086, 'longitude': 20.89638900756836}, {'item': 'vaahtokarkki',
    'co2_item': 1000, 'heft': 0.58, 'info': 'kelluvaa', 'destination_airport': 'Enontekio Airport',
    'destination_country': 'Suomi', 'latitude': 68.362602233887, 'longitude': 23.424299240112},
    {'item': 'takki', 'co2_item': 10, 'heft': 6.74, 'info': 'lämmittää kivasti',
     'destination_airport': 'Eura Airport', 'destination_country': 'Suomi', 'latitude': 61.1161,
     'longitude': 22.201401}, {'item': 'karkki', 'co2_item': 454, 'heft': 3.87, 'info': 'aiai mun hampaat',
    'destination_airport': 'Forssa Airfield', 'destination_country': 'Suomi', 'latitude': 60.803683,
    'longitude': 23.650802}, {'item': 'sitruuna', 'co2_item': 343, 'heft': 0.51, 'info': 'kirpiää',
    'destination_airport': 'Genböle Airport', 'destination_country': 'Suomi', 'latitude': 60.086899,
    'longitude': 22.5219}, {'item': 'appelsiini', 'co2_item': 643, 'heft': 2.91,
    'info': 'appelsiini on hieno appelsiini', 'destination_airport': 'Halli Airport',
    'destination_country': 'Suomi', 'latitude': 61.856039, 'longitude': 24.786686}]

# antaa pelaajalle generoidusta pakettilistasta 10 vaitoehtoa, joista pelaaja valitsee 5
#import parcel_selector

# testilista


# siirtää parcel_compiler funktion avulla databasesta arvotut paketit ja
# lentokentät käytettäväksi listaksi
#game_parcel_list = parcel_selector.parcel_compiler(game_parcel_list, Noelin_airport_list)
