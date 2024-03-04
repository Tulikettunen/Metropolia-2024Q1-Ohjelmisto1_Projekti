# Parcel Delivery Logic
from geopy import distance
import model.format as format


## TEST DATA
#test_player_data = {"playername": "abc", "co2_produced": 0, "location": (60.3172, 24.963301), "player_parcels": [{'item': 'vasara', 'co2_item': 200, 'heft': 8.19, 'info': 'Vasara on hieno vasara', 'destination_airport': 'Aavahelukka Airport', 'destination_country': 'Suomi', 'latitude': 67.60359954833984, 'longitude': 23.97170066833496},
# {'item': 'omena', 'co2_item': 300, 'heft': 0.35, 'info': 'Omena on hieno omena', 'destination_airport': 'Ahmosuo Airport', 'destination_country': 'Suomi', 'latitude': 64.895302, 'longitude': 25.752199},
# {'item': 'tietokone', 'co2_item': 150, 'heft': 2.7, 'info': 'tietoinen kone', 'destination_airport': 'Alavus Airfield', 'destination_country': 'Suomi', 'latitude': 62.554699, 'longitude': 23.573299},
# {'item': 'possu', 'co2_item': 175, 'heft': 0.76, 'info': 'röh röh', 'destination_airport': 'Jorvin Hospital Heliport', 'destination_country': 'Suomi', 'latitude': 60.220833, 'longitude': 24.68639},
# {'item': 'kaakao', 'co2_item': 500, 'heft': 2.78, 'info': 'makeaa', 'destination_airport': 'Kilpisjärvi Heliport', 'destination_country': 'Suomi', 'latitude': 69.0022201538086, 'longitude': 20.89638900756836},
#], "player_delivered": [{'item': 'vasara', 'co2_item': 200, 'heft': 8.19, 'info': 'Vasara on hieno vasara', 'destination_airport': 'Aavahelukka Airport', 'destination_country': 'Suomi', 'latitude': 67.60359954833984, 'longitude': 23.97170066833496},
# {'item': 'omena', 'co2_item': 300, 'heft': 0.35, 'info': 'Omena on hieno omena', 'destination_airport': 'Ahmosuo Airport', 'destination_country': 'Suomi', 'latitude': 64.895302, 'longitude': 25.752199},
# {'item': 'kaakao', 'co2_item': 500, 'heft': 2.78, 'info': 'makeaa', 'destination_airport': 'Kilpisjärvi Heliport', 'destination_country': 'Suomi', 'latitude': 69.0022201538086, 'longitude': 20.89638900756836},
#] }
#test_player_data = {"playername": "abc", "co2_produced": 0, "location": (60.3172, 24.963301), "player_parcels": [{'item': 'vasara', 'co2_item': 200, 'heft': 8.19, 'info': 'Vasara on hieno vasara', 'destination_airport': 'Aavahelukka Airport', 'destination_country': 'Suomi', 'latitude': 67.60359954833984, 'longitude': 23.97170066833496},
# {'item': 'omena', 'co2_item': 300, 'heft': 0.35, 'info': 'Omena on hieno omena', 'destination_airport': 'Ahmosuo Airport', 'destination_country': 'Suomi', 'latitude': 64.895302, 'longitude': 25.752199},
# {'item': 'tietokone', 'co2_item': 150, 'heft': 2.7, 'info': 'tietoinen kone', 'destination_airport': 'Alavus Airfield', 'destination_country': 'Suomi', 'latitude': 62.554699, 'longitude': 23.573299},
# {'item': 'possu', 'co2_item': 175, 'heft': 0.76, 'info': 'röh röh', 'destination_airport': 'Jorvin Hospital Heliport', 'destination_country': 'Suomi', 'latitude': 60.220833, 'longitude': 24.68639},
# {'item': 'kaakao', 'co2_item': 500, 'heft': 2.78, 'info': 'makeaa', 'destination_airport': 'Kilpisjärvi Heliport', 'destination_country': 'Suomi', 'latitude': 69.0022201538086, 'longitude': 20.89638900756836},
#], "player_delivered": [] }


# Select which parcel to deliver
def select(player_data):
    """Takes the acting players data as input and lets the player choose a parcel to deliver.
    Returns the index of the parcel in the list: 'player_parcels' in player data."""

    # prints parcel options to the player
    for parcel in player_data.get("player_parcels"):
        parcel_number = player_data.get("player_parcels").index(parcel)+1

        if parcel in player_data.get("player_delivered"):
            parcel_number = "X"

        distance_from_player = distance.distance(player_data.get("location"), (parcel.get("latitude"), parcel.get("longitude")))

        print(f"[{parcel_number}]: Tuote: {parcel.get("item")}, Paino: {parcel.get("heft")} kg, Kohde: {parcel.get("destination_airport")}, Etäisyys: {float(str(distance_from_player)[:-3]):.2f} km")

    # creates a list of valid inputs to be used later to check if the players input is valid
    list_of_valid_inputs = []
    for parcel in player_data.get("player_parcels"):
        if parcel not in player_data.get("player_delivered"):
            list_of_valid_inputs.append(str(player_data.get("player_parcels").index(parcel)+1))

    # asks the player to give an input and doesn't let the player proceed until a valid input is given
    while True:

        player_input = input("Valitse kuljetettava paketti: ")

        if player_input in list_of_valid_inputs:
            print(f"Valitsit paketin {player_input}")
            break
        elif player_input in ["1","2","3","4","5"]:
            print(f"Olet jo kuljettanut tämän paketin")
        else:
            print("Tämä ei ole validi syöte")

    return str(int(player_input)-1) # Returns the parcel ( dict() ) index for which parcel the player wishes to deliver.


# Select form of delivery transport.
def plane(chosen_location, player_data):
    """Takes the chosen travel location and the data of the acting player,
    lets the player choose an airplane and returns the number corresponding to the chosen airplane.
    The numbers that correspond to the airplanes are:
    1. "Rahtikone"
    2. "Matkustajakone"
    3. "Yksityiskone" """

    #calculates the distance from players current location to the chosen destination
    distance_from_player = distance.distance(player_data.get("location"), ((player_data.get("player_parcels")[int(chosen_location)-1].get("latitude")), (player_data.get("player_parcels")[int(chosen_location)-1].get("longitude"))))

    #calculates the default flight time that is used to calculate the flight times of different airplane options
    default_flight_time = float(str(distance_from_player)[:-3]) / format.transport_speed1 # flight time in hours, 800km/h used as a default speed of a commercial airplane

    #prints the airplane options with flight_times for the player to see
    print(f"Valitsemasi kohde on {player_data.get("player_parcels")[int(chosen_location)].get("destination_airport")}, etäisyys {float(str(distance_from_player)[:-3]):.2f} km")
    print(f"[1]: Rahtilentokoneella kuljetus kestää {default_flight_time * format.transport_speed3:.1f} tuntia")
    print(f"[2]: Matkustajakoneella kuljetus kestää {default_flight_time:.1f} tuntia")
    print(f"[3]: Yksityiskoneella kuljetus kestää {default_flight_time * format.transport_speed2:.1f} tuntia")

    #asks the player to choose an airplane and doesn't let then proceed until a valid input is given
    while True:

        player_input = input("Valitse lentokone: ")

        if player_input in ["1","2","3"]:
            print(f"Valitsit lentokoneen {player_input}")
            break
        else:
            print("Tämä ei ole validi syöte")

    # CO2 emissions based on distance & delivery method. ADD BELOW
    

    return player_input

