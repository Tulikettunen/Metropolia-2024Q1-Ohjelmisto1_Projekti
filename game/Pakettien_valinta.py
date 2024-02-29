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


players_selected_parcels_list = players_parcel_selection(Noelin_parcel_list)
print(players_selected_parcels_list)
