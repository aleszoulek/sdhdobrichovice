from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route('/')
def hello_world():
    return render_template(
        'homepage.html',
        #STATIC='/sdhdobrichovice/static',
        STATIC='/static',
        SITENAME='Hasiči Dobřichovice',
        SITEURL='/',
    )
