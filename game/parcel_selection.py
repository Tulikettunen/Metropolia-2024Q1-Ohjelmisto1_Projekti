# Parcel Selection Logic
import random
import model.format as format


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

#the minimum and maximum weights of the heft classes in kg
heft_classes = format.heft_classes

def generate_list(list_of_parcels, lista_of_airports):
    """Takes a list of parcels and a list of airports and combines them into a single
    list with dictionaries containing all the information from the aforementioned lists"""

    list_of_parcels_with_destinations = []

    for i in range(len(list_of_parcels)):
        # Chooses a random weight for the item based on its heft type.
        random_weight = float(f"{random.uniform(heft_classes.get(list_of_parcels[i][2])[0],
        heft_classes.get(list_of_parcels[i][2])[1]):.2f}")

        # combines all the values including the randomized weight into a single dictionary and adds it to the list of parcels with location information
        # STRUCTURE = { item, co2_item, heft, info, destination_airport, destination_country, latitude, longitude }
        list_of_parcels_with_destinations.append({"item": list_of_parcels[i][0],"co2_item": list_of_parcels[i][1],
        "heft": random_weight,"info": list_of_parcels[i][3],"destination_airport": lista_of_airports[i][0],
        "destination_country": lista_of_airports[i][1], "latitude": lista_of_airports[i][2],"longitude": lista_of_airports[i][3]})

    # returns a complete list of dictionaries
    return list_of_parcels_with_destinations


# antaa pelaajalle generoidusta pakettilistasta 10 vaitoehtoa, joista pelaaja valitsee 5
#import parcel_selector

# testilista
Noelin_parcel_list = [{'item': 'vasara', 'co2_item': 200, 'heft': 8.19, 'info': 'Vasara on hieno '
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

# siirtää parcel_compiler funktion avulla databasesta arvotut paketit ja
# lentokentät käytettäväksi listaksi
#new_parcel_list = parcel_selector.parcel_compiler(Noelin_parcel_list, Noelin_airport_list)


def players_parcel_selection_print(new_parcel_list,optilist):
    i = 1
    print("Voit valita seuraavista 10 vaihtoehdosta 5: \n")
    for item in new_parcel_list:
        if str(i) in optilist:
            print(f"[{i}]: {item.get("item")}: {item.get("info")}. Paino: {item.get("heft")} kg.")
        else:
            print(f"[x]: {item.get("item")}: {item.get("info")}. Paino: {item.get("heft")} kg.")
        i += 1
    print("")


#players_parcel_selection_print(Noelin_parcel_list)


def players_parcel_selection(new_parcel_list):
    """Pelaaja valitsee mitä paketteja haluaa listaansa. Käyttäjävirheet huomioitu, printtaa myös
    valittavien asioiden listan jokaisen uuden valinnan yhteydessä ja merkkaa jo valitut x:llä """

    options_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    players_parcel_selection_print(Noelin_parcel_list, options_list)
    selection = input("Syötä numero (1-10) minkä paketin haluat valita kuljetettavaan listaan: \n")
    i = 1
    lista = []
    while i <= 5:
        if selection in options_list:
            lista.append(new_parcel_list[int(selection) - 1])
            options_list.remove(selection)
            i += 1
            if i == 6:
                print("Hienoa! Valitsit kaikki 5 pakettia!")
                break
            players_parcel_selection_print(Noelin_parcel_list, options_list)
            selection = input("Hienoa! Anna seuraavan paketin numero: \n")
        elif selection in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            players_parcel_selection_print(Noelin_parcel_list, options_list)
            selection = input("Olet jo valinnut kyseisen paketin, valitse toinen: \n")
        else:
            players_parcel_selection_print(Noelin_parcel_list, options_list)
            selection = input("Anna validi luku (1-10): \n")
    return lista

