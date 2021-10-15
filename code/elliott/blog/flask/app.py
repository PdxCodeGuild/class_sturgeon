

from flask import Flask, render_template
app = Flask(__name__)


posts = [{
    'body': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quibusdam est, blanditiis debitis quasi eaque recusandae sed quos consectetur nobis impedit.Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quam facilis placeat tempore ratione in dicta vitae?",
    'author': "Elusive man",
    'date': "October 02th, 2021",

},

    {
        'body': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quibusdam est, blanditiis debitis quasi eaque recusandae sed quos consectetur nobis impedit.Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quam facilis placeat tempore ratione in dicta vitae?",
        'author': "someone",
        'date': "October 08th, 2021",
},

    {
        'body': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quibusdam est, blanditiis debitis quasi eaque recusandae sed quos consectetur nobis impedit.Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quam facilis placeat tempore ratione in dicta vitae?",
        'author': "--aa--",
        'date': "October 14th, 2021", },


    {
        'body': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quibusdam est, blanditiis debitis quasi eaque recusandae sed quos consectetur nobis impedit.Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quam facilis placeat tempore ratione in dicta vitae?",
        'author': "Blogger ",
        'date': "October 17th, 2021", }]


@ app.route('/')
def index():
    return render_template('index.html', posts=posts)


app.run(debug=True)
