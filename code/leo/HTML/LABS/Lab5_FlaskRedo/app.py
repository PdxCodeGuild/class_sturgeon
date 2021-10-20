from mesurement import mesurement
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])

def index():

    if request.method == 'POST':
  
        result = mesurement(request.form['distance'], request.form['input_unit'], request.form['output_unit'])
    
        return render_template('index.html', result=result)
    
    else:

        return render_template('index.html')


app.run(debug=True)