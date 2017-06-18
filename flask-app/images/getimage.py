import requests
import json
import random
import os
from scripts.random_name import getRandomName


def getAnimalObject(animalName):
    # Google Custom Search API
    searchTerm = animalName + 'cute'
    startIndex = '1'
    key = 'AIzaSyBBJojSr9WhfnjIyLRG4ktGdUagmfsnqZU'
    num = '1'
    cx = '000286809279331881489:zis0cegnbfy'
    searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + \
        searchTerm + "&num=" + num + "&start=" + startIndex + "&imgSize=" + "large" + "&key=" + key + "&cx=" + cx + \
        "&searchType=image"
    r = requests.get(searchUrl)
    response = r.content.decode('utf-8')
    result = json.loads(response)
    items = result['items']
    # Construction of Animal Object
    animalURL = ''
    for item in items:
        animalURL = item['link']
    nickname = getRandomName('scripts/random-name-list.txt')
    animalObject = {
                    'name' : animalName,
                    'URL' : animalURL,
                    'nickname' : nickname
    }
    return animalObject

def getAnimalName(textfile):
    imageList = []
    for line in open(textfile,'r'):
        imageList.append(line)
    randomNumber = random.randint(0, len(imageList) - 1)
    animalName = imageList[randomNumber]
    return animalName

def getImageURL(my_path):
    if os.path.exists(my_path) and (os.path.getsize(my_path) == 0):
        animalName = getAnimalName('images/animal-list.txt')
        animalObject = getAnimalObject(animalName)
        animalNameTemp = getAnimalName('images/animal-list.txt')
        animalObjectTemp = getAnimalObject(animalNameTemp)
        f = open(my_path, 'w')
        f.write(animalObjectTemp['name'] + animalObjectTemp['URL'])  #
        f.close()
        return animalObject
    else:
        animalObject = {}
        f = open(my_path, 'r')
        animalObject['name'] = f.readline()
        animalObject['URL'] = f.readline()
        animalObject['nickname'] = f.readline()
        f.close()
        # Erase File
        open(my_path, 'w').close()

        animalNameTemp = getAnimalName('images/animal-list.txt')
        animalObjectTemp = getAnimalObject(animalNameTemp)

        f = open(my_path, 'w')
        f.write(animalObjectTemp['name'] + animalObjectTemp['URL']  + '\n')
        f.write(animalObjectTemp['nickname'] + '\n')
        f.close()

        return animalObject;
