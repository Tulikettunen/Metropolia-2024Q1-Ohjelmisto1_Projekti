# Player dictionary structure
def player_structure(player_name):
    return { "name": player_name, "score": False, "co2": 0, "location": False, "parcels_picked": False, "percels_delivered": False }


# Parcel dictionary structure (not defined, decreed by the database itself!)
#parcel_structure = 


# Item heft classes
heft_classes = {1:(0.1,1), 2:(1,3), 3:(3,10)}


# Transport method speeds (1: km/h, ... rest are multiples of 1)
transport_speed1 = 800
transport_speed2 = 0.75
transport_speed3 = 1.50

