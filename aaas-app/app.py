from flask import Flask, render_template, request
import random
import requests
from images.get_images import randomAnimalObject, getRandomNickname
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    nickname = getRandomNickname("scripts/random-name-list.txt")
    # Animal Object
    animalObject = randomAnimalObject()
    name = ''
    url = ''
    #nickname = "NICKNAME"
    for key,value in animalObject.items():
        name = key
        url = value
    return render_template('index.html',
                            nickname = nickname,
                            name = name,
                            url=random.choice(url))

if __name__ == "__main__":
    app.run(port=8080, debug = True)
