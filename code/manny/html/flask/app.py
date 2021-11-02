from flask import Flask, render_template, templating

app = Flask(__name__)

who_is_cool = "Manny"
temperature = 72
cars = ["toyota", "chrysler", "ford", "holden"]

@app.route("/")
def index():
    return render_template('index.html', who_is_cool=who_is_cool, temperature = temperature, cars = cars)

app.run(debug=True) 