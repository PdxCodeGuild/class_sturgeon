from flask import Flask, render_template
app = Flask(__name__)

#first route, returns main.
@app.route('/')
def index():
    
    posts = [
    {
        'title': "Chillwave offal you probably haven't heard of them",
        'author': "Blogger McBlogface",
        'date': "October 14th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable portland tumblr mixtape sartorial. Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher."
    }, 
    {
        'title': "Put A Cheeseburger In Your Ipsum",
        'author': "Ham Hamburgular",
        'date': "July 1st, 2021",
        'body': "Epic cheeseburgers come in all kinds of manifestations, but we want them in and around our mouth no matter what. Slide those smashed patties with the gently caramelized meat fat between a toasted brioche bun and pass it over. You fall in love with the cheeseburger itself but the journey ain’t half bad either. They’re the childhood friend that knows your highest highs and lowest lows. They’ve been with you through thick and thin and they’re the best at keeping secrets. Whether it’s dressed up or informal, cheeseburgers have your back."
    },
    {
        'title': "A model proposal",
        'author': "Veg Vegetarian",
        'date': "January 16th, 2021",
        'body': "Brisket buffalo hamburger, ham hock rump bacon corned beef frankfurter. Fatback ham pork loin tail, shank rump picanha bacon venison biltong beef. Pork shankle tongue porchetta. Turkey cow corned beef, pork doner venison chuck meatball sirloin filet mignon spare ribs t-bone pig hamburger. Kevin shank buffalo pork. Swine prosciutto ribeye pastrami pork fatback chicken sausage spare ribs cupim pork chop pork loin bacon."
    
    },
    {
        'title': "Commander's Log",
        'author': "William T. Riker",
        'date': "Stardate 99354.2",
        'body': "I can't. As much as I care about you, my first duty is to the ship. We finished our first sensor sweep of the neutral zone. A lot of things can change in twelve years, Admiral. I suggest you drop it, Mr. Data. I will obey your orders. I will serve this ship as First Officer. And in an attack against the Enterprise, I will die with this crew. But I will not break my oath of loyalty to Starfleet. I guess it's better to be lucky than good. Maybe if we felt any human loss as keenly as we feel one of those close to us, human history would be far less bloody. Besides, you look good in a dress. Could someone survive inside a transporter buffer for 75 years? Damage report!"
        
    },
    {
        'title': "Pinot Noir, an Ode",
        'author': "Titus Andromeda",
        'date': "Wine O'clock",
        'body': "Meat is paired well with reds. A wine has legs if it sticks to the inside of the glass when swirled. Sit and intelligently sip a glass. Spice, strawberries, oak and tar. Can't taste them? Drink more. A toast to one's health originated in Greece. Trichloroanisole, or stinky cork, is produced when chlorine used in sanitization comes into contact with natural cork-dwelling bacteria. Let mature reds breathe for twenty to thirty minutes, if you can. Pinot noir is French for black pinecone, a description of the grapes appearance. Lorem vino, dollar store blend. Pursing your lips and inhaling some air while the wine is still on your palate is also a nice way to spread the more complex flavors through your sinuses. Serve dry Semillon with clams, mussels, or pasta salad. Some whites age better in stainless steel. "
    }
]

    return render_template("home.html", posts=posts)

#turns on the debugger
app.run(debug=True)

