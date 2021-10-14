from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': "No matter what, you keep finding something to fight for",
        'author': "Blogger McBlogface",
        'date': "October 15th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable portland tumblr mixtape sartorial. Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher."
    }, {
        'title': "Happy Birthday, kiddo",
        'author': "Blogger McBlogface",
        'date': "October 14th, 2021",
        'body': "The only people who have anything to fear from free software are those whose products are worth even less. (David Emery) If debugging is the process of removing software bugs, then programming must be the process of putting them in. (Edsger Dijkstra) First, solve the problem. Then, write the code. (John Johnson) Come to think of it, there are already a million monkeys on a million typewriters, and Usenet is nothing like Shakespeare. (Blair Houghton) The Internet? Is that thing still around? (Homer Simpson)"
    }, {
        'title': "The 3rd is the third",
        'author': "Blogger McBlogface",
        'date': "October 13th, 2021",
        'body': "The trouble with programmers is that you can never tell what a programmer is doing until it’s too late. (Seymour Cray) Deleted code is debugged code. (Jeff Sickel) The Internet? Is that thing still around? (Homer Simpson) Writing code has a place in the human hierarchy worth somewhere above grave robbing and beneath managing. (Gerald Weinberg) Programming is like sex. One mistake and you have to support it for the rest of your life. (Michael Sinz)"
    }, {
        'title': "The fourth is the fourth and the fourth",
        'author': "Blogger McBlogface",
        'date': "October 12th, 2021",
        'body': "Controlling complexity is the essence of computer programming. (Brian Kernigan) Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the universe trying to produce bigger and better idiots. So far, the universe is winning. (Rick Cook) Good programmers use their brains, but good guidelines save us having to think out every case. (Francis Glassborow) The Web is like a dominatrix. Everywhere I turn, I see little buttons ordering me to Submit. (Nytwind) Software is like sex: It’s better when it’s free. (Linus Torvalds)"
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts = posts)

app.run(debug=True)