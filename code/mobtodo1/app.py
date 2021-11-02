from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import json
from jsondb import JsonDB
db = JsonDB('db.json')



@app.route('/', methods=['GET'])
def index():
    db.load()
    to_do_list = db.get('todos')
    return render_template('index.html', to_do_list = to_do_list)

@app.route('/receive_form/', methods=['POST'])
def entry():
    db.load()
    text = request.form['text']
    priority = request.form['priority']
    
    new_stuff = db.get('todos')
    
    new_stuff.append({'priority' : priority, 'text': text})

    print(new_stuff)
    
    db.save()
    return redirect('/')

app.run(debug=True)

