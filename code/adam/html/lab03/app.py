from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': "No matter what, you keep finding something to fight for",
        'author': "Blogger McBlogface",
        'date': "Posted on October 15th, 2021",
        'body': "Let's see, scorpions are pretty creepy. Ummm, being by myself. I'm scared of ending up alone. Well into the game, Ellie meets a new friend named Sam, and the two get to talking about the state of the world, and what it's like to survive. Eventually, the conversation shifts to greatest fears and Ellie reveals hers."
    }, {
        'title': "Happy Birthday, kiddo",
        'author': "Blogger McBlogface",
        'date': "Posted on October 14th, 2021",
        'body': "I lost most of my crew trying to get here, I pretty much lost everything. And then you show up and somehow we find you just in time to save her. Maybe it was meant to be. After waking up in a hospital bed, Joel comes face to face with Marlene, just as she's prepping Ellie for surgery to find a possible cure for the cordyceps epidemic. At first, Joel remarks that Ellie 'fought like hell' to reach the Fireflies."
    }, {
        'title': "It’s the normal people that scare me.",
        'author': "Blogger McBlogface",
        'date':  "Posted on October 13th, 2021",
        'body': "Once upon a time, I had somebody that I cared about. It was a partner. Somebody I had to look after. And in this world, that sort of s**t's good for one thing: Gettin' ya killed. Bill exposes his own nihilism when he utters this quote about caring for people in the aftermath of a destroyed world. It's an important message about the dangers of losing one's own humanity when things become dire."
    }, {
        'title': "What did the green grape say to the purple grape? Breathe, you idiot!",
        'author': "Blogger McBlogface",
        'date': "Posted on October 12th, 2021",
        'body': "The Last Of Us does a good job at making zombies terrifying, but it does an even better job of making regular people out to be the worst monsters. Zombies kill a person because they’re driven by biological urges to spread the infection, humans do it because they can. Ultimately Bill points out that free will and human greed make people much scarier. A zombie you know what you’re dealing with, but that kind man who helped you bag a deer and save your life could also very well be a cannibal."
    }, {
        'title': "After all we’ve been through. Everything that I’ve done. It can’t be for nothing.",
        'author': "Blogger McBlogface",
        'date': "Posted on October 11th, 2021",
        'body': "After Joel proposes going back to Tommy’s settlement and living a normal life Ellie quickly shuts it down saying all the hardship, heartbreak, and what she considers vile acts on her part (killing David) can’t be in vain.All of those things are okay if they manage to get a cure out of this, which makes Joel’s statement that she needs to find another reason to survive so important in the previous entry."
    }, {
        'title': "Hello? Anyone? Cure for mankind here!",
        'author': "Blogger McBlogface",
        'date': "Posted on October 10th, 2021",
        'body': "This amusing line perfectly conveys the frustration and hope Ellie has at trying to find the Fireflies. After being told for so long they were at the university they arrive to find the Fireflies are gone, having moved on even further across the country.Despite knowing the importance of her immunity, Ellie can’t help but be a kid and feel frustrated that things just keep going wrong. Turns out being the savior of mankind can be a little frustrating if the story doesn’t play out like the fairy tale it should be."
    }, {
        'title': "Just one peaceful night; a clean conscience…all gone…",
        'author': "Blogger McBlogface",
        'date': "Posted on October 9th, 2021",
        'body': "Lyin’ on the couch watchin’ Sunday football. That… greasy smell of a downtown hot dog. 4th of July, family barbecues. The sound of a plane flying overhead. Just one peaceful night; a clean conscience…all gone… – Joel. In the midst of the apocalypse, Joel has become aware of how much he took for granted from the early days. The food, the company, the boring activities, and just the simple peace of not watching over your shoulder every minute of every day or worried what might happen in your sleep. But perhaps what he misses most of all is a life where he never made bad decisions or did horrible things to survive."
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts = posts)

app.run(debug=True)