# blog

from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': "Lorizzle uhuh ... yih!",
        'author': "Gangsta Lorem",
        'date': "October 10th, 2021",
        'body': "yo sit amizzle, consectetizzle adipiscing elit. Nullizzle sapizzle velizzle, brizzle volutpat, suscipizzle go to hizzle, gravida vel, arcu. Pellentesque shiznit funky fresh. Sed erizzle. Mammasay mammasa mamma oo sa izzle dolor dapibus turpis tempizzle things. Maurizzle pellentesque we gonna chung shiznit shizzlin dizzle. Dizzle izzle tortor. Pellentesque eleifend yippiyo nisi. In hac habitasse platea dictumst. Fizzle dapibus. Curabitizzle boofron urna, pretizzle fo shizzle, mattizzle ac, dizzle vitae, crunk. Sizzle suscipizzle. Integizzle semper velizzle sizzle dang."
    }, {
        'title': "Curabitur mammasay mammasa mamma oo sa diam mofo nisi fizzle mollizzle",
        'author': "Gangsta Lorem",
        'date': "October 11th, 2021",
        'body': "Suspendisse potenti. Morbi odio. Shizzlin dizzle neque. Shiznit orci. Nizzle maurizzle fo shizzle, interdizzle fo shizzle, feugiat pizzle amizzle, mofo izzle, boom shackalack. Tellivizzle boom shackalack. Vestibulizzle go to hizzle mi, volutpizzle in, sagittis sed, sheezy sempizzle, fo. Cras hizzle ipsum. Aliquam volutpat fo shizzle vel orci. Cras pizzle crunk in purizzle sodales ornare. Its fo rizzle venenatizzle justo et fo shizzle. Nunc yo. Suspendisse crazy shiz gangster. Tellivizzle shizzle my nizzle crocodizzle ante. Nunc pharetra, leo bow wow wow boofron hendrerizzle, away felizzle elementizzle ass, in aliquizzle magna felis luctizzle pede. Hizzle a check out this. Pimpin' aptent my shizz check out this ad litora torquent ma nizzle conubia tellivizzle, pizzle mofo hymenizzle. Aliquam interdizzle, funky fresh sizzle elementizzle nonummy, nisl orci viverra leo, izzle shizznit risus arcu shizzlin dizzle sizzle."
    }, {
        'title': "Vivamizzle nizzle egizzle shiz consectetizzle mah nizzle",
        'author': "Gangsta Lorem",
        'date': "October 12th, 2021",
        'body': "Vivamus sizzle amizzle shizznit. Nam eu fizzle eget lacizzle auctor fo shizzle. Nizzle break it down viverra fo shizzle. Shiz izzle arcu. Vestibulizzle shit enizzle, yippiyo sizzle, fo shizzle mah nizzle fo rizzle, mah home g-dizzle my shizz, mofo nizzle, fo. Nullam vitae izzle shizznit fo shizzle posuere pharetra. Gangster pede pizzle, congue , auctizzle a, mollis sit amizzle, sheezy. For sure shiz dui. Aliquizzle risus bizzle, elementizzle dang, sollicitudin in, consequizzle imperdiet, turpizzle. Fo shizzle my nizzle yo ipsizzle phat my shizz dizzle vehicula. Curabitur doggy sagittizzle stuff. Pellentesque check it out morbi tristique bling bling doggy owned et malesuada fames izzle mah nizzle egestizzle. In est. Curabitur pizzle."
    }, {
        'title': "Sed metus urna, luctizzle et, stuff brizzle, sollicitudin rizzle, nulla",
        'author': "Gangsta Lorem",
        'date': "October 13th, 2021",
        'body': "Bizzle pharetra, nisi facilisis malesuada, get down get down justo shizzle my nizzle crocodizzle go to hizzle, mollis shizzlin dizzle shit yo mamma izzle purizzle. Class aptent fizzle doggy mah nizzle cool torquent pizzle nostra, bizzle inceptizzle break it down. Aliquam maurizzle orci, that's the shizzle its fo rizzle, iaculizzle vizzle, that's the shizzle izzle, elit. Nunc lacus. Fusce gangster urna, i'm in the shizzle shiznit, feugiat nizzle, gizzle ac, sapien. Curabitizzle shit. Shizzlin dizzle gangsta mofo non enim mattis pharetra. Gizzle nulla felizzle, nizzle id, bling bling ma nizzle, dope nizzle, ligula. Tellivizzle ut fo shizzle. Bling bling nibh. Funky fresh bow wow wow. Nulla blandit."
    }
]


@app.route('/')
def index():
    return render_template('index.html', posts=posts)

app.run(debug=True)
