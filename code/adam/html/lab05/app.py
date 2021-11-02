from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import json
from jsondb import JsonDB
import string
import random
db = JsonDB('db.json')

@app.route('/', methods=['GET'])
def index():
    db.load()
    converter = db.get('converter')
    return render_template('index.html', converter = converter)

@app.route('/receive_form/', methods=['POST'])
def entry():
    db.load()
    converter = db.get('converter')
    from_x = request.form['from_x']
    number = request.form['text']
    number = float(number)
    to = request.form['to']
    if from_x == 'feet':
        if to == 'inches' :
            return render_template('output.html', answer='Inches: ' + str(round(number*converter['feet_to_inches'], 2)))
        elif to == 'miles' :
            return render_template('output.html', answer='Miles: ' + str(round(number*converter['feet_to_miles'], 4)))
        elif to == 'feet' :
            return render_template('output.html', answer='Feet: ' + str(round(number*converter['feet_to_feet'], 2)))
        elif to == 'cm' :
            return render_template('output.html', answer='Centimeters: ' + str(round(number*converter['feet_to_cm'], 4)))
    elif from_x == 'inches':
        if to == 'inches' :
            return render_template('output.html', answer='Inches: ' + str(round(number*converter['inches_to_inches'], 8)))
        elif to == 'miles' :
            return render_template('output.html', answer='Miles: ' + str(round(number*converter['inches_to_miles'], 8)))
        elif to == 'feet' :
            return render_template('output.html', answer='Feet: ' + str(round(number*converter['inches_to_feet'], 2)))
        elif to == 'cm' :
            return render_template('output.html', answer='Centimeters: ' + str(round(number*converter['inches_to_cm'], 8)))
    elif from_x == 'miles':
        if to == 'inches' :
            return render_template('output.html', answer='Inches: ' + str(round(number*converter['miles_to_inches'], 2)))
        elif to == 'miles' :
            return render_template('output.html', answer='Miles: ' + str(round(number*converter['miles_to_miles'], 2)))
        elif to == 'feet' :
            return render_template('output.html', answer='Feet: ' + str(round(number*converter['miles_to_feet'], 20)))
        elif to == 'cm' :
            return render_template('output.html', answer='Centimeters: ' + str(round(number*converter['miles_to_cm'], 20)))
    elif from_x == 'cm':
        if to == 'inches' :
            return render_template('output.html', answer='Inches: ' + str(round(number*converter['cm_to_inches'], 20)))
        elif to == 'miles' :
            return render_template('output.html', answer='Miles: ' + str(round(number*converter['cm_to_miles'], 20)))
        elif to == 'feet' :
            return render_template('output.html', answer='Feet: ' + str(round(number*converter['cm_to_feet'], 20)))
        elif to == 'cm' :
            return render_template('output.html', answer='Centimeters: ' + str(round(number*converter['cm_to_cm'], 20)))
    db.save()
    return redirect('/')

@app.route('/password_form/', methods=['POST'])
def password_generation():
    password = ''
    password_length = int(request.form['password'])
    db.load()
    passwords = db.get('passwords')
    password_choices = passwords['symbols'] + passwords['numbers'] + passwords['letters']
    while len(password) < password_length:
        letters = random.choice(password_choices)
        password += letters
    return render_template('output.html', password=password)

@app.route('/rot_form/', methods=['POST'])
def route_generation():
    route_password = ''
    db.load()
    cipher_path = db.get('passwords')
    cipher_letters = cipher_path['letters'].lower()
    user_word = request.form['user_word'].lower()
    user_rotation_number = request.form['user_rotation_number']
    user_rotation_number = int(user_rotation_number)
    for letter in user_word:
        route_password += cipher_letters[(cipher_letters.find(letter)+user_rotation_number)%26]
    route_password += " "
    route_password = route_password.title()
    return render_template('output.html', route_password=route_password)

app.run(debug=True)