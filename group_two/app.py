
from jsondb import JsonDB
from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)

db = JsonDB('db.json')

# db.load()
# x = db.get('priority', 0)
# y = db.get('text', 0)

# x += 1
# y += 1
# db.set('priority', x)
# db.save()

# print(todos[1]['priority'])


@app.route('/', methods=['GET'])
def index():

    db.load()
    todos = db.get('todos')

    return render_template('index.html', todos=todos)

# [{'priority': 'high', 'text': 'walk the dog'}, {'priority': 'medium', 'text': 'butter the cat'}, {'priority': 'low', 'text': 'wash dishes'}]


@app.route('/receive_form/', methods=['POST'])
def temperature():
    global todos
    text = request.form['text']  # Jane
    priority = request.form['priority']

    x = db.set('priority', priority)
    y = db.set('text', text)

    return redirect('/')


app.run(debug=True)
