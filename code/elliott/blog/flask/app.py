from flask import Flask, render_template
app = Flask(__name__)


posts = [{
    'title': "Chillwave offal you probably haven't heard of them",
    'author': "Blogger McBlogface",
    'date': "October 14th, 2021",
    'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable port",
},

    {
        'title': "Chillwave offal you probably haven't heard of them",
        'author': "Blogger McBlogface",
        'date': "October 14th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable port",
},

    {
        'title': "Chillwave offal you probably haven't heard of them",
        'author': "Blogger McBlogface",
        'date': "October 14th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable port",
},

    {
        'title': "Chillwave offal you probably haven't heard of them",
        'author': "Blogger McBlogface",
        'date': "October 14th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable port",
}]


@app.route('/')
def index():
    return render_template('index.html', posts=posts)


app.run(debug=True)
