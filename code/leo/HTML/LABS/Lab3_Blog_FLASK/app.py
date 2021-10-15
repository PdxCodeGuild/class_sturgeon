from flask import Flask, render_template
import requests
import random

president = ['Adams, John', 'Adams, John Quincy', 'Arthur, Chester Alan', 'Biden, Joseph R.', 'Buchanan, James', 'Bush, George','Bush George W.' 'Carter, Jimmy','Cleveland, Grover','Clinton, Bill','Coolidge, Calvin','Eisenhower, Dwight D.','Fillmore, Millard','Ford, Gerald R.','Garfield, James A.','Grant, Ulysses S.','Harding, Warren G.','Harrison, Benjamin','Harrison, William Henry','Hayes, Rutherford Birchard','Hoover, Herbert','Jackson, Andrew','Jefferson, Thomas','Johnson, Andrew','Johnson, Lyndon B.','Kennedy, John F.','Lincoln, Abraham','Madison, James','McKinley, William','Monroe, James','Nixon, Richard M.','Obama, Barack','Pierce, Franklin','Polk, James K.','Reagan, Ronald','Roosevelt, Franklin D.','Roosevelt, Theodore','Taft, William H.','Taylor, Zachary','Truman, Harry S.','Trump, Donald J.','Tyler, John', 'Van Buren, Martin', 'Washington, George', 'Wilson, Woodrow']

app = Flask(__name__)

@app.route('/')

def index():

    theresponse = requests.get('https://icanhazdadjoke.com/' , headers={'accept': 'application/json'})
    x = theresponse.json()
    body1 = str(x['joke'])

    theresponse = requests.get('https://icanhazdadjoke.com/' , headers={'accept': 'application/json'})
    y = theresponse.json()
    body2 = str(y['joke'])

    theresponse = requests.get('https://icanhazdadjoke.com/' , headers={'accept': 'application/json'})
    z = theresponse.json()
    body3 = str(z['joke'])

    theresponse = requests.get('https://icanhazdadjoke.com/' , headers={'accept': 'application/json'})
    z = theresponse.json()
    body4 = str(z['joke'])

    theresponse = requests.get('https://icanhazdadjoke.com/' , headers={'accept': 'application/json'})
    z = theresponse.json()
    body5 = str(z['joke'])

    theresponse = requests.get('https://icanhazdadjoke.com/' , headers={'accept': 'application/json'})
    z = theresponse.json()
    body6 = str(z['joke'])

    theresponse = requests.get('https://icanhazdadjoke.com/' , headers={'accept': 'application/json'})
    z = theresponse.json()
    body7 = str(z['joke'])

    theresponse = requests.get('https://icanhazdadjoke.com/' , headers={'accept': 'application/json'})
    z = theresponse.json()
    body8 = str(z['joke'])

    theresponse = requests.get('https://icanhazdadjoke.com/' , headers={'accept': 'application/json'})
    z = theresponse.json()
    body9 = str(z['joke'])

   
    posts = {
        'author1' : random.choice(president), 
        'author2' : random.choice(president),
        'author3' : random.choice(president),
        'author4' : random.choice(president),
        'author5' : random.choice(president),
        'author6' : random.choice(president),
        'author7' : random.choice(president),
        'author8' : random.choice(president),
        'author9' : random.choice(president),
        'body1' : body1,
        'body2' : body2, 
        'body3' : body3,
        'body4' : body4,
        'body5' : body5,
        'body6' : body6,
        'body7' : body7,
        'body8' : body8,
        'body9' : body9,
        }

    return render_template('index.html', 
                            author1 = posts['author1'], body1 = posts['body1'], 
                            author2 = posts['author2'], body2 = posts['body2'],
                            author3 = posts['author3'], body3 = posts['body3'],
                            author4 = posts['author4'], body4 = posts['body4'],
                            author5 = posts['author5'], body5 = posts['body5'],
                            author6 = posts['author6'], body6 = posts['body6'],
                            author7 = posts['author7'], body7 = posts['body7'],
                            author8 = posts['author8'], body8 = posts['body8'],
                            author9 = posts['author9'], body9 = posts['body9']
                            )

app.run(debug=True)
