import requests
import json
import random
import os


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
    animalObject = {
                    'name' : animalName,
                    'URL' : animalURL
    }
    return animalObject

def getAnimalName(textfile):
    imageList = []
    for line in open(textfile,'r'):
        imageList.append(line)
    randomNumber = random.randint(0, len(imageList) - 1)
    animalName = imageList[randomNumber]
    return animalName
def readFile():
    for line in open(textfile,'r'):
        imageList.append(line)
def writeFile(animalObject):
    fo = open("next-animal.txt", "w")
    fo.write("Python is a great language.\nYeah its great!!\n");
    fo.close()

def main():
    my_path = "next-animal.txt"
    if os.path.exists(my_path):
        print('true')
    else:
        print('false')
    """
    if os.path.exists(my_path) and os.path.getsize(my_path) < 0:
        name = getAnimalName('/Docker/flask-app/animal-list.txt')
        print (name)
    else:
        print("failure")
    """
main()
# if file empty
    # get two objects, save the second
# else
    # read object from file
    # erase file
    # get one object and add to file
