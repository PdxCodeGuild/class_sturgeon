
def mesurement(distance, input_unit, output_unit):

    measurements = {
        'ft': 0.3048,
        'mi': 1609.34,
        'm': 1,
        'km': 1000,
        'yard': 0.9144,
        'inch': 0.0254}

    meter_convertion = float(distance) * measurements[input_unit]

    if output_unit == "ft":
        answer = float(meter_convertion * 3.28084)

    elif output_unit == "mi":
        answer = float(meter_convertion * 0.000621371)

    elif output_unit == "m":
        answer = meter_convertion

    elif output_unit == "km":
        answer = float(meter_convertion * 0.001)

    elif output_unit == "yard":
        answer = float(meter_convertion * 1.09361)

    elif output_unit == "inch":
        answer = float(meter_convertion * 39.3701)

    
    return f'{distance} {input_unit} is equal to {round(answer, 1)} {output_unit}'
