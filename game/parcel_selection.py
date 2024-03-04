# Parcel Selection Logic
import random


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
min_and_max_of_heft_classes = {1:(0.1,1), 2:(1,3), 3:(3,10)}

def parcel_compiler(list_of_parcels, lista_of_airports):
    """Takes a list of parcels and a list of airports and combines them into a single
    list with dictionaries containing all the information from the aforementioned lists"""

    list_of_parcels_with_destinations = []

    for i in range(len(list_of_parcels)):
        # Chooses a random weight for the item based on its heft type.
        random_weight = float(f"{random.uniform(min_and_max_of_heft_classes.get(list_of_parcels[i][2])[0],
        min_and_max_of_heft_classes.get(list_of_parcels[i][2])[1]):.2f}")

        # combines all the values including the randomized weight into a single dictionary and adds it to the list of parcels with location information
        list_of_parcels_with_destinations.append({"item": list_of_parcels[i][0],"co2_item": list_of_parcels[i][1],
        "heft": random_weight,"info": list_of_parcels[i][3],"destination_airport": lista_of_airports[i][0],
        "destination_country": lista_of_airports[i][1], "latitude": lista_of_airports[i][2],"longitude": lista_of_airports[i][3]})

    # returns a complete list of dictionaries
    return list_of_parcels_with_destinations

print(parcel_compiler(test_parcels, test_airports))

