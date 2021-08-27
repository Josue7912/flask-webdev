from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to Emily's Dog Costumes! See my <a href=\"/services\">"\
        "services</a> and current line of <a href=\"/costumes\">costumes</a>"


@app.route('/services')
def services():
    return "I offer custom made costumes for your precious canine companion, "\
        "and a free in-home consultation, to get the measurements."


@app.route('/costumes')
def costumes():
    costumes_list = [
        {
            'header': 'Skeleton',
            'body': "This style is great if you are feeling something extra "\
                    "spooky for your pooch.",
            'image': '/static/skeleton.jpg',
        },
        {
            'header': 'Dracula',
            'body': "My friend Judy got a new puppy, and I just had to dress "\
                    "him up for Halloween! Super cute, and no coffins required.",
            'image': '/static/dracula.jpg',
        },
        {
            'header': 'Punk Rocker',
            'image': '/static/punk-rocker.jpg',
            'body': "I thought I was a huge Misfits fan, until I dressed "\
                    "my bff's dog Frank. I think he pulls off the punk "\
                    "rocker look better than me!",
        },
        {
            'header': 'Witch',
            'body': "Our dog Rose went with the husband out fishing, so I had "\
            "to dress the cat up in this bewitching costume.",
            'image': '/static/witch.jpg',
        },
    ]

    return f"Check out my costumes!"
