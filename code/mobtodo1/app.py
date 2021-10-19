from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import json
from jsondb import JsonDB
db = JsonDB('db.json')
# db.load()
# x = db.get('x', 0)
# x += 1
# db.set('x', x)
# db.save()




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['textarea']
        print(text)
    db.load()
    to_do_list = db.get('todos')
    db.save()
    return render_template('index.html', to_do_list = to_do_list)

app.run(debug=True)