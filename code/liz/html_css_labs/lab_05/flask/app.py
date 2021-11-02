# -----flask redo---unit converter---- #

from flask import Flask, render_template, request
app = Flask(__name__)


distance = {
    'feet': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        units_from = request.form['units-from']
        units_to = request.form['units-to']
        start_distance = float(request.form['distance'])
        distance_in_meters = start_distance * distance[units_from]
        distance_from_meters = round(distance_in_meters / distance[units_to], 4)
        return render_template('index.html', start_distance=start_distance, units_from=units_from, units_to=units_to, result_distance=distance_from_meters)

app.run(debug=True)