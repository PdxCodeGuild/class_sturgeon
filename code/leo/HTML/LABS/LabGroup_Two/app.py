
from jsondb import JsonDB
from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)

db = JsonDB('db.json')


@app.route('/', methods=['GET'])
def index():
    db.load()
    todos = db.get('todos')
    return render_template('index.html', todos=todos)


@app.route('/receive_form/', methods=['POST'])
def temperature():

    db.load()
    todos = db.get('todos')

    db.data["todos"].append(request.form)

    db.save()

    return redirect('/')


app.run(debug=True)