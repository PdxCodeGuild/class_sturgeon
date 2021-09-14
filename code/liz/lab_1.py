distance = input("what is the distance? ")
distance = float(distance)
from_units = input('what units are you converting from? enter ft, mi, m, km, yd, in ')
to_units = input("what units are you converting to? enter ft, mi, m, km, yd, in ")


def converter_to_meters (distance, from_units):
    if from_units == 'ft':
        return distance * 0.3048
    elif from_units == 'mi':
        return distance *1609.34
    elif from_units == 'm':
        return distance
    elif from_units == 'km':
        return distance * 1000
    elif from_units == 'yd':
        return distance * 0.9144
    elif from_units == 'in':
        return distance * 0.0254


distance_in_meters = converter_to_meters(distance, from_units)


def converter_from_meters (distance_in_meters, to_units):
    if to_units == 'ft':
        return distance_in_meters / 0.3048
    elif to_units == 'mi':
        return distance_in_meters / 1609.34
    elif to_units == 'm':
        return distance_in_meters
    elif to_units == 'km':
        return distance_in_meters / 1000
    elif to_units == 'yd':
        return distance_in_meters / 0.9144
    elif to_units == 'in':
        return distance_in_meters / 0.0254

distance_from_meters = converter_from_meters(distance_in_meters, to_units)


print(f"{distance} {from_units}. is {distance_from_meters:.7}{to_units}")
