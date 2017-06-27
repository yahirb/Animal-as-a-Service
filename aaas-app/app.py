from flask import Flask, render_template, request
import random
import requests
from images.getimage import getImageURL
from scripts.random_name import getRandomName
from scripts.next_animal import getNextAnimalObject

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        randomName = getRandomName('scripts/random-name-list.txt')
        animalObject = getImageURL("images/next-animal.txt")
        nextAnimalObject = getNextAnimalObject("images/next-animal.txt")
        return render_template('index.html',
                                randomName = animalObject['nickname'],
                                animalName = animalObject['name'],
                                randomNameNext = nextAnimalObject['nickname'],
                                animalNameNext = nextAnimalObject['name'],
                                url=animalObject['URL'])
    else:
        randomName = getRandomName('scripts/random-name-list.txt')
        animalObject = getImageURL("images/next-animal.txt")
        nextAnimalObject = getNextAnimalObject("images/next-animal.txt")
        return render_template('index.html',
                                randomName = animalObject['nickname'],
                                animalName = animalObject['name'],
                                randomNameNext = nextAnimalObject['nickname'],
                                animalNameNext = nextAnimalObject['name'],
                                url=animalObject['URL'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
