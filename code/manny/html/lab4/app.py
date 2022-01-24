from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_form/', methods=['POST'])
def order():
    print(request.form)
    request.form['person_name']
    request.form['telephone']
    request.form['tortilla']
    request.form['meat']
    request.form['beans']
    request.form['rice']
    request.form['special']
    return render_template('response.html')

app.run(debug=True)