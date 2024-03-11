# Player dictionary structure
def player_structure(player_name):
    return { "name": player_name, "score": False, "co2": 0, "location": [60.3172, 24.963301], "parcels_picked": [], "parcels_delivered": [], "gameover": False }


# Parcel dictionary structure (not defined, decreed by the database itself!)
#parcel_structure = 


# Item heft classes
heft_classes = {1:(0.1,1), 2:(1,3), 3:(3,10)}


# Transport method speeds (1: km/h, ... rest are multiples of 1)
transport_speed1 = 800
transport_speed2 = 0.75
transport_speed3 = 1.50

transport1_co2 = 0.75
transport2_co2 = 1
transport3_co2 = 1.5

parcel_selection_time_limit = 30
parcel_delivery_time_limit = 120

