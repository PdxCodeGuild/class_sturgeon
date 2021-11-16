from flask import Flask, render_template
app = Flask(__name__)

posts = [ {
    'title': 'How to build a professional website',
    'img_url': 'images/web2.jpg',
    'author': 'The Creative Creator',
    'date': 'October 14th 2021',
    'body': 'Time to build a website, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
    {
    'title': 'How to build a professional blacksmithing business',
    'img_url': 'images/armory1.jpg',
    'author': 'The Creative Creator',
    'date': 'October 15th 2021',
    'body': 'Okay we have a website, time to make a business. Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
    {
    'title': 'How to build a professional castle w/ moat',
    'img_url': 'images/castle2.jpg',
    'author': 'The Creative Creator',
    'date': 'October 16th 2021',
    'body': 'Slinky aqquired, now let\'s build a castle. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
    {
    'title': 'How to build a professional horse',
    'img_url': 'images/horse1.jpg',
    'author': 'The Creative Creator',
    'date': 'October 17th 2021',
    'body': 'We\'re almost there, all we need now is a horse. Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
    {
    'title': '10 reasons no-one likes your website',
    'img_url': 'images/web3.jpg',
    'author': 'The Creative Creator',
    'date': 'October 18th 2021',
    'body': '1. You dont change more than the first sentence of each post. 2. Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
    {
    'title': 'How to fix that pesky drawbridge and other medieval furniture',
    'img_url': 'images/castle1.jpg',
    'author': 'The Creative Creator',
    'date': 'October 19th 2021',
    'body': 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
    {
    'title': 'What to do when you run out of grain',
    'img_url': 'images/grain1.jpg',
    'author': 'The Creative Creator',
    'date': 'October 20th 2021',
    'body': 'Go to the store and buy more grain. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    },
    {
    'title': '10 better blogs for medieval inventors',
    'img_url': 'images/oldblog1.jpg',
    'author': 'The Creative Creator',
    'date': 'October 21th 2021',
    'body': 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    }
]



#localhost:5000/
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

    

app.run(debug=True)