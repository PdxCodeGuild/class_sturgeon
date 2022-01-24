from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def blog():
    
    articles = [
    {
        'title': "Chillwave microdose you probably haven't heard of them",
        'author': "Blogger McBlogface",
        'date': "October 14th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable portland tumblr mixtape sartorial. Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget velit aliquet sagittis id consectetur purus ut faucibus. Justo donec enim diam vulputate. Eget dolor morbi non arcu risus quis varius quam quisque. Nullam vehicula ipsum a arcu cursus vitae. Duis at tellus at urna condimentum. Massa tincidunt dui ut ornare lectus sit amet est. Molestie nunc non blandit massa enim. Est placerat in egestas erat imperdiet sed euismod nisi porta. Est sit amet facilisis magna. Consectetur adipiscing elit ut aliquam. Sed enim ut sem viverra aliquet eget sit. Interdum posuere lorem ipsum dolor sit amet consectetur. Lacus vestibulum sed arcu non odio euismod lacinia at quis. Aliquet sagittis id consectetur purus ut faucibus pulvinar elementum integer. Maecenas ultricies mi eget mauris pharetra. Porttitor lacus luctus accumsan tortor."
    }, 
    {
        'title': "Chez de un Cheeseburger Ipsum",
        'author': "Ham Hamburgular",
        'date': "July 1st, 2021",
        'body': "Epic cheeseburgers come in all kinds of manifestations, but we want them in and around our mouth no matter what. Slide those smashed patties with the gently caramelized meat fat between a toasted brioche bun and pass it over. You fall in love with the cheeseburger itself but the journey ain’t half bad either. They’re the childhood friend that knows your highest highs and lowest lows. They’ve been with you through thick and thin and they’re the best at skeeping secrets. Whether it’s dressed up or informal, cheeseburgers have your back. Facilisis magna etiam tempor orci. Eget sit amet tellus cras. Blandit volutpat maecenas volutpat blandit aliquam. Quis risus sed vulputate odio. Amet venenatis urna cursus eget nunc scelerisque viverra mauris in. Tortor vitae purus faucibus ornare suspendisse sed nisi lacus. Duis convallis convallis tellus id interdum velit laoreet id. Nunc scelerisque viverra mauris in aliquam sem fringilla ut. Facilisis leo vel fringilla est ullamcorper eget nulla facilisi. Viverra suspendisse potenti nullam ac tortor vitae purus. Vel pretium lectus quam id leo in. Ut eu sem integer vitae justo eget magna."
    },
    {
        'title': "Pallella del valle silvestre",
        'author': "Veg Vegetarian",
        'date': "January 16th, 2021",
        'body': "Brisket buffalo hamburger, ham hock rump bacon corned beef frankfurter. Fatback ham pork loin tail, shank rump picanha bacon venison biltong beef. Pork shankle tongue porchetta. Turkey cow corned beef, pork doner venison chuck meatball sirloin filet mignon spare ribs t-bone pig hamburger. Kevin shank buffalo pork. Swine prosciutto ribeye pastrami pork fatback chicken sausage spare ribs cupim pork chop pork loin bacon. Massa eget egestas purus viverra accumsan in nisl nisi scelerisque. Cursus eget nunc scelerisque viverra mauris in. Orci dapibus ultrices in iaculis nunc. Quis enim lobortis scelerisque fermentum dui faucibus in ornare. Sagittis orci a scelerisque purus. Pretium vulputate sapien nec sagittis aliquam. Scelerisque felis imperdiet proin fermentum leo. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium. Commodo odio aenean sed adipiscing diam donec. Tellus id interdum velit laoreet id donec ultrices tincidunt arcu. Amet dictum sit amet justo. Mauris rhoncus aenean vel elit scelerisque. Ligula ullamcorper malesuada proin libero nunc consequat interdum. Nunc sed velit dignissim sodales ut eu sem integer. Id diam maecenas ultricies mi eget mauris pharetra. Proin nibh nisl condimentum id venenatis a condimentum vitae. Scelerisque fermentum dui faucibus in ornare quam. Donec adipiscing tristique risus nec feugiat in. Urna nunc id cursus metus aliquam eleifend mi in nulla. Libero volutpat sed cras ornare arcu dui vivamus arcu."
    
    },
    {
        'title': "Commander's Log",
        'author': "William T. Riker",
        'date': "Stardate 99354.2",
        'body': "I can't. As much as I care about you, my first duty is to the ship. We finished our first sensor sweep of the neutral zone. A lot of things can change in twelve years, Admiral. I suggest you drop it, Mr. Data. I will obey your orders. I will serve this ship as First Officer. And in an attack against the Enterprise, I will die with this crew. But I will not break my oath of loyalty to Starfleet. I guess it's better to be lucky than good. Maybe if we felt any human loss as keenly as we feel one of those close to us, human history would be far less bloody. Besides, you look good in a dress. Could someone survive inside a transporter buffer for 75 years? Damage report! Massa eget egestas purus viverra accumsan in nisl nisi scelerisque. Cursus eget nunc scelerisque viverra mauris in. Orci dapibus ultrices in iaculis nunc. Quis enim lobortis scelerisque fermentum dui faucibus in ornare. Sagittis orci a scelerisque purus. Pretium vulputate sapien nec sagittis aliquam. Scelerisque felis imperdiet proin fermentum leo. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium. Commodo odio aenean sed adipiscing diam donec. Tellus id interdum velit laoreet id donec ultrices tincidunt arcu. Amet dictum sit amet justo. Mauris rhoncus aenean vel elit scelerisque. Ligula ullamcorper malesuada proin libero nunc consequat interdum. Nunc sed velit dignissim sodales ut eu sem integer. Id diam maecenas ultricies mi eget mauris pharetra. Proin nibh nisl condimentum id venenatis a condimentum vitae. Scelerisque fermentum dui faucibus in ornare quam. Donec adipiscing tristique risus nec feugiat in. Urna nunc id cursus metus aliquam eleifend mi in nulla. Libero volutpat sed cras ornare arcu dui vivamus arcu."
        
    },
    {
        'title': "Pinot Noir, an Ode",
        'author': "Titus Andromeda",
        'date': "Wine O'clock",
        'body': "Meat is paired well with reds. A wine has legs if it sticks to the inside of the glass when swirled. Sit and intelligently sip a glass. Spice, strawberries, oak and tar. Can't taste them? Drink more. A toast to one's health originated in Greece. Trichloroanisole, or stinky cork, is produced when chlorine used in sanitization comes into contact with natural cork-dwelling bacteria. Let mature reds breathe for twenty to thirty minutes, if you can. Pinot noir is French for black pinecone, a description of the grapes appearance. Lorem vino, dollar store blend. Pursing your lips and inhaling some air while the wine is still on your palate is also a nice way to spread the more complex flavors through your sinuses. Serve dry Semillon with clams, mussels, or pasta salad. Some whites age better in stainless steel. Etiam sit amet nisl purus in mollis. Porta non pulvinar neque laoreet suspendisse interdum. Odio tempor orci dapibus ultrices in iaculis. Diam ut venenatis tellus in metus vulputate. Lobortis scelerisque fermentum dui faucibus. Scelerisque varius morbi enim nunc faucibus a pellentesque sit amet. Diam in arcu cursus euismod quis viverra nibh. Vel elit scelerisque mauris pellentesque pulvinar pellentesque. Quam lacus suspendisse faucibus interdum posuere lorem ipsum. Pharetra et ultrices neque ornare aenean euismod elementum. Rhoncus est pellentesque elit ullamcorper. Iaculis eu non diam phasellus vestibulum lorem sed risus. Consectetur a erat nam at lectus. Sagittis vitae et leo duis ut diam quam nulla. Est ultricies integer quis auctor elit sed vulputate mi sit. Gravida dictum fusce ut placerat orci nulla pellentesque dignissim. Auctor elit sed vulputate mi sit amet. Sed velit dignissim sodales ut eu. Lorem sed risus ultricies tristique nulla aliquet."
    }
]
    return render_template("index.html", articles=articles, len=len(articles))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact(): 
    return render_template("contact.html")

#turns on the debugger
app.run(debug=True)