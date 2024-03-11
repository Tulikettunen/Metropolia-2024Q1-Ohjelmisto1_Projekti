# Parcel Delivery Logic
from geopy import distance
from . import format
from . import screen
from rich import print
import time


# Select which parcel to deliver
def select_delivery(player_data):
    """
    Takes the players data as input and lets them choose a parcel to deliver.
    Returns the index of the parcel in the list: 'parcels_picked' in player data.
    """

    # creates a list of valid inputs to be used later to check if the players input is valid
    list_of_valid_inputs = []
    for parcel in player_data.get("parcels_picked"):
        if parcel not in player_data.get("parcels_delivered"):
            list_of_valid_inputs.append(str(player_data.get("parcels_picked").index(parcel)+1))

    # asks the player to give an input and doesn't let the player proceed until a valid input is given
    while True:
        print(f"[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][PAKETIN KULJETUS][/italic #FF7F50]\n")
        print(f"[#C39BD3]// Valitse paketti, jonka haluat kuljettaa:[/#C39BD3]")

        # prints parcel options to the player
        for parcel in player_data.get("parcels_picked"):
            parcel_number = f"[yellow]{player_data.get('parcels_picked').index(parcel)+1}[/yellow]"
            if parcel in player_data.get("parcels_delivered"):
                parcel_number = "[green]X[/green]"

            distance_from_player = distance.distance(player_data.get("location"), (parcel.get("latitude"), parcel.get("longitude")))
            print(f"[#C39BD3]•[/#C39BD3] [{parcel_number}]: Tuote: {parcel.get('item')}, Paino: {parcel.get('heft')} kg, Kohde: {parcel.get('destination_airport')}, Etäisyys: {float(str(distance_from_player)[:-3]):.2f} km")
        
        option = input(">> ")

        if option in list_of_valid_inputs:
            #screen.feedback(option, "Paketti valittu")
            break
        elif option in ["1","2","3","4","5"]:
            screen.feedback(option, "Paketti on jo toimitettu!")
        else:
            screen.feedback(option, "error")

    return int(option)-1 # Returns the parcel ( dict() ) index for which parcel the player wishes to deliver.


# Select form of delivery transport.
def select_delivery_method(chosen_location, player_data, start_time):
    """
    Takes the chosen travel location and the data of the acting player,
    lets the player choose an airplane and returns the number corresponding to the chosen airplane.
    The numbers that correspond to the airplanes are:
    1. "Rahtikone"
    2. "Matkustajakone"
    3. "Yksityiskone"
    """
    
    #calculates the distance from players current location to the chosen destination
    distance_from_player = distance.distance(player_data.get("location"), ((player_data.get("parcels_picked")[int(chosen_location)].get("latitude")), (player_data.get("parcels_picked")[int(chosen_location)].get("longitude"))))

    #calculates the default flight time that is used to calculate the flight times of different airplane options
    default_flight_time = float(str(distance_from_player)[:-3]) / format.transport_speed1 # flight time in hours, 800km/h used as a default speed of a commercial airplane
    
    screen.feedback("time",how_much_time_is_left(start_time,format.parcel_delivery_time_limit))

    #asks the player to choose an airplane and doesn't let them proceed until a valid input is given
    while True:
        print(f"[#6A5ACD]//[/#6A5ACD] [italic #FF7F50][PAKETIN KULJETUS / TOIMITUSTAPA][/italic #FF7F50]")
        print(f"[#6A5ACD]•[/#6A5ACD]Kohteena: [#76D7C4]{player_data.get('parcels_picked')[int(chosen_location)].get('destination_airport')}[/#76D7C4], etäisyys: {float(str(distance_from_player)[:-3]):.0f} km\n")
        print(f"[#C39BD3]Valitse toimitustapa![/#C39BD3]")
        print(f"[#C39BD3]•[/#C39BD3] [[yellow]1[/yellow]]: Rahtikone ({default_flight_time * format.transport_speed3:.1f} tuntia)")
        print(f"[#C39BD3]•[/#C39BD3] [[yellow]2[/yellow]]: Matkustajakone ({default_flight_time:.1f} tuntia")
        print(f"[#C39BD3]•[/#C39BD3] [[yellow]3[/yellow]]: Yksityiskone ({default_flight_time * format.transport_speed2:.1f} tuntia)")
        option = input(">> ")

        if option in ["1","2","3"]:
            #print(f"Valitsit lentokoneen {option}")
            break
        else:
            screen.feedback(option, "error")

    # CO2 emissions based on distance & delivery method.
    match option:
        case "1":
            CO2_multiplier = format.transport1_co2
        case "2":
            CO2_multiplier = format.transport2_co2
        case "3":
            CO2_multiplier = format.transport3_co2

    delivery_CO2 = float(str(distance_from_player)[:-3]) * 0.36 * CO2_multiplier
    parcel_CO2 = player_data["parcels_picked"][chosen_location].get("co2_item")
    CO2_full = delivery_CO2 + parcel_CO2

    return CO2_full


def is_there_time_left(start_time, time_limit):
    if time.time() - start_time > time_limit:
        return False
    return True


def how_much_time_is_left(start_time, time_limit):
    #Returns the remaining time represented as a boxes -> string
    number_of_boxes = int(40 * (time_limit - (time.time() - start_time)) / time_limit) * "█"
    if len(number_of_boxes) > 25:
        return f"[#40ff19]{number_of_boxes}[/#40ff19]"
    elif len(number_of_boxes) > 10:
        return f"[#ffec17]{number_of_boxes}[/#ffec17]"
    else:
        return f"[#ff1717]{number_of_boxes}[/#ff1717]"

## TEST DATA
#test_player_data = {"playername": "abc", "co2_produced": 0, "location": (60.3172, 24.963301), "parcels_picked": [{'item': 'vasara', 'co2_item': 200, 'heft': 8.19, 'info': 'Vasara on hieno vasara', 'destination_airport': 'Aavahelukka Airport', 'destination_country': 'Suomi', 'latitude': 67.60359954833984, 'longitude': 23.97170066833496},
# {'item': 'omena', 'co2_item': 300, 'heft': 0.35, 'info': 'Omena on hieno omena', 'destination_airport': 'Ahmosuo Airport', 'destination_country': 'Suomi', 'latitude': 64.895302, 'longitude': 25.752199},
# {'item': 'tietokone', 'co2_item': 150, 'heft': 2.7, 'info': 'tietoinen kone', 'destination_airport': 'Alavus Airfield', 'destination_country': 'Suomi', 'latitude': 62.554699, 'longitude': 23.573299},
# {'item': 'possu', 'co2_item': 175, 'heft': 0.76, 'info': 'röh röh', 'destination_airport': 'Jorvin Hospital Heliport', 'destination_country': 'Suomi', 'latitude': 60.220833, 'longitude': 24.68639},
# {'item': 'kaakao', 'co2_item': 500, 'heft': 2.78, 'info': 'makeaa', 'destination_airport': 'Kilpisjärvi Heliport', 'destination_country': 'Suomi', 'latitude': 69.0022201538086, 'longitude': 20.89638900756836},
#], "parcels_delivered": [{'item': 'vasara', 'co2_item': 200, 'heft': 8.19, 'info': 'Vasara on hieno vasara', 'destination_airport': 'Aavahelukka Airport', 'destination_country': 'Suomi', 'latitude': 67.60359954833984, 'longitude': 23.97170066833496},
# {'item': 'omena', 'co2_item': 300, 'heft': 0.35, 'info': 'Omena on hieno omena', 'destination_airport': 'Ahmosuo Airport', 'destination_country': 'Suomi', 'latitude': 64.895302, 'longitude': 25.752199},
# {'item': 'kaakao', 'co2_item': 500, 'heft': 2.78, 'info': 'makeaa', 'destination_airport': 'Kilpisjärvi Heliport', 'destination_country': 'Suomi', 'latitude': 69.0022201538086, 'longitude': 20.89638900756836},
#] }
#test_player_data = {"playername": "abc", "co2_produced": 0, "location": (60.3172, 24.963301), "parcels_picked": [{'item': 'vasara', 'co2_item': 200, 'heft': 8.19, 'info': 'Vasara on hieno vasara', 'destination_airport': 'Aavahelukka Airport', 'destination_country': 'Suomi', 'latitude': 67.60359954833984, 'longitude': 23.97170066833496},
# {'item': 'omena', 'co2_item': 300, 'heft': 0.35, 'info': 'Omena on hieno omena', 'destination_airport': 'Ahmosuo Airport', 'destination_country': 'Suomi', 'latitude': 64.895302, 'longitude': 25.752199},
# {'item': 'tietokone', 'co2_item': 150, 'heft': 2.7, 'info': 'tietoinen kone', 'destination_airport': 'Alavus Airfield', 'destination_country': 'Suomi', 'latitude': 62.554699, 'longitude': 23.573299},
# {'item': 'possu', 'co2_item': 175, 'heft': 0.76, 'info': 'röh röh', 'destination_airport': 'Jorvin Hospital Heliport', 'destination_country': 'Suomi', 'latitude': 60.220833, 'longitude': 24.68639},
# {'item': 'kaakao', 'co2_item': 500, 'heft': 2.78, 'info': 'makeaa', 'destination_airport': 'Kilpisjärvi Heliport', 'destination_country': 'Suomi', 'latitude': 69.0022201538086, 'longitude': 20.89638900756836},
#], "parcels_delivered": [] }
