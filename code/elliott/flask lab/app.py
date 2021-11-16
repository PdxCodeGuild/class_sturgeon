import string
import random
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template("index.html")

    elif request.method == 'POST':
        len_pass = int(request.form['password'])
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        length = len_pass

        all = lower + upper + num + symbols
        temp = random.sample(all, length)
        password = "".join(temp)

        return render_template("index.html", password=password)


app.run(debug=True)

'''
@app.route('/receive_form/', methods=['POST'])
def password():

    return redirect('/')
'''
