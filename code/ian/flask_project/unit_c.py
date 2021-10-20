from flask import Flask, render_template, request, redirect
app = Flask(__name__)

conversions = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yard' : 0.9144,
    'in' : 0.0254
}


@app.route('/')
def index():
    return render_template('index.html', conversions=conversions)

@app.route('/receive_form/', methods=['POST'])
def entry():
    distance_in = request.form['distance_in']
    units_in = request.form['units_in']
    units_out = request.form['units_out']
    meter_output = int(distance_in) * conversions[units_in]
    new_distance_out = meter_output / conversions[units_out]
    new_distance_out = round(new_distance_out, 2)
    return render_template('index.html', 
    conversions=conversions, 
    meter_output=meter_output, 
    new_distance_out=new_distance_out, 
    distance_in=distance_in,
    units_in=units_in,
    units_out=units_out)

app.run(debug=True)