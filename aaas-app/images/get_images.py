########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import random

# This script has a primary definition that returns a list of URLS based on a
# search term. This search used is Azure

# Returns list of URLs
def imageURLSearch(searchTerm):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '542b275938cd471790ddf38ee94a2d7d',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'q': searchTerm,
        'count': '10',
        'offset': '0',
        'mkt': 'en-us',
        'safesearch': 'Moderate',
        'size': 'Large'
    })

    conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
    conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    result = json.loads(data)
    # Checks for image results
    if 'images' in result:
        image_dicts = result['images']['value']
        image_url_list = []
        for image_dict in image_dicts:
            image_url = image_dict['contentUrl']
            image_url_list.append(image_url)
        conn.close()
        return image_url_list
    else:
        return ['URL NOT FOUND']

# Gets an animal list and uses image search function to create a list of
# dictionaries containing animal name and list of URLS for respective animals
def convertToObjects():
    # Read animal list file
    animalNames = []
    with open("animal-data.txt", "r") as json_data:
        animalNames = json.load(json_data)
    # list of dictionaries containing animal name as key and list of URLS as value
    animalObjects = []
    for animalName in animalNames:
        animalURLS = imageURLSearch(animalName)
        animalObject = {animalName : animalURLS}
        animalObjects.append(animalObject)
        print (animalName)
    # Write to data file
    f = open('animal-data-new.txt', 'w')
    f.write(json.dumps(animalObjects))
    f.close()

# takes a text file containin json list of dictionaries that contain a single key (animal string) and value (list of URLs)
# and returns an object containing a single dictionary
def randomAnimalObject():
    animalObjects = []
    with open('animal-data-modified.txt', "r") as json_data:
        animalObjects = json.load(json_data)
    randomNumber = random.randint(0, len(animalObjects) - 1)
    randomAnimal = animalObjects[randomNumber]
    return randomAnimal
