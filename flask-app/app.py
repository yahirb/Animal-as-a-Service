from flask import Flask, render_template
import random
import requests
from images.getimage import getImageURL

app = Flask(__name__)


@app.route('/')
def index():
    url = getImageURL('animal-list.txt')
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
