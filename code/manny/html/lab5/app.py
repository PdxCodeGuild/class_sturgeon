from flask import Flask, render_template, request

app = Flask(__name__)


meter_multiplier = {
    "feet" : 0.3048,
    "miles" : 1609.34,
    "meters" : 1,
    "kilometers" : 1000,
    "yards" : 0.9144, 
    "inches" : 0.0254
}

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        value_from = float(request.form["value_from"])       
        units_from = request.form["units_from"]        
        units_to = request.form["units_to"]
        meter_convert = value_from * meter_multiplier[units_from]
        final_conversion = round(meter_convert / meter_multiplier[units_to], 2)

        return render_template('index.html', units_from=units_from, final_conversion=final_conversion)

if __name__ == "__main__":
    app.run(debug=True)
