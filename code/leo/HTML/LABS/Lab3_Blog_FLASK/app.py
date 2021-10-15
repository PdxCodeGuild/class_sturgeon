from flask import Flask, render_template
import requests
import random

president = ['Adams, John', 'Adams, John Quincy', 'Arthur, Chester Alan', 'Biden, Joseph R.', 'Buchanan, James', 'Bush, George','Bush George W.' 'Carter, Jimmy','Cleveland, Grover','Clinton, Bill','Coolidge, Calvin','Eisenhower, Dwight D.','Fillmore, Millard','Ford, Gerald R.','Garfield, James A.','Grant, Ulysses S.','Harding, Warren G.','Harrison, Benjamin','Harrison, William Henry','Hayes, Rutherford Birchard','Hoover, Herbert','Jackson, Andrew','Jefferson, Thomas','Johnson, Andrew','Johnson, Lyndon B.','Kennedy, John F.','Lincoln, Abraham','Madison, James','McKinley, William','Monroe, James','Nixon, Richard M.','Obama, Barack','Pierce, Franklin','Polk, James K.','Reagan, Ronald','Roosevelt, Franklin D.','Roosevelt, Theodore','Taft, William H.','Taylor, Zachary','Truman, Harry S.','Trump, Donald J.','Tyler, John', 'Van Buren, Martin', 'Washington, George', 'Wilson, Woodrow']

app = Flask(__name__)

@app.route('/')

def index():
    author = random.choice(president)
    theresponse = requests.get('https://icanhazdadjoke.com/' , headers={'accept': 'application/json'})
    x = theresponse.json()
    y = str(x['joke'])
    posts = {'author' : author, 'body' : y }

    return render_template('index.html', author = posts['author'], body = posts['body'])

app.run(debug=True)