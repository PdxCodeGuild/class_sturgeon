# blog

from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': "Cheese and biscuits",
        'author': "Mr. Cheddar",
        'date': "October 10th, 2021",
        'body': "Cheese and biscuits cheese and biscuits rubber cheese. Everyone loves cream cheese airedale fromage frais rubber cheese when the cheese comes out everybody's happy bavarian bergkase caerphilly. Gouda mascarpone mascarpone blue castello fromage frais airedale stinking bishop feta. When the cheese comes out everybody's happy."
    }, {
        'title': "Who moved my cheese?",
        'author': "Mrs. Brie",
        'date': "October 11th, 2021",
        'body': "Who moved my cheese cheddar taleggio. Pecorino danish fontina cheeseburger stinking bishop cheeseburger croque monsieur cut the cheese ricotta. Boursin when the cheese comes out everybody's happy queso st. agur blue cheese rubber cheese fromage danish fontina croque monsieur. Pecorino fromage frais cheese strings dolcelatte mascarpone goat danish fontina cottage cheese. Who moved my cheese."
    }, {
        'title': "Cream cheese",
        'author': "Miss Swiss",
        'date': "October 12th, 2021",
        'body': "Cream cheese cheese and biscuits queso. Cut the cheese stinking bishop cheese on toast stilton parmesan pepper jack brie taleggio. Everyone loves when the cheese comes out everybody's happy blue castello cheesy grin cauliflower cheese manchego emmental the big cheese. Say cheese cheese strings halloumi brie squirty cheese everyone loves pecorino cheese and wine. Squirty cheese cheddar cheesy feet emmental."
    }, {
        'title': "Cow who moved",
        'author': "Sir Humbolt Fog, Esq.",
        'date': "October 13th, 2021",
        'body': "Cow who moved my cheese bavarian bergkase. Cheese and wine st. agur blue cheese cauliflower cheese taleggio monterey jack cheese and wine pecorino halloumi. Cream cheese taleggio swiss emmental caerphilly cheese slices cheesecake cheese and biscuits. Pecorino."
    }
]


@app.route('/')
def index():
    return render_template('index.html', posts=posts)

app.run(debug=True)
