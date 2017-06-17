import requests
import json
import random

imageList = []
for line in open("../animal-list.txt",'r'):
    imageList.append(line)

randomNumber = random.randint(0, len(imageList) - 1)

searchTerm = imageList[randomNumber]
startIndex = '1'
key = 'AIzaSyBBJojSr9WhfnjIyLRG4ktGdUagmfsnqZU'
num = '1'
cx = '000286809279331881489:zis0cegnbfy'
searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + \
    searchTerm + "&num=" + num + "&start=" + startIndex + "&key=" + key + "&cx=" + cx + \
    "&searchType=image"
r = requests.get(searchUrl)
response = r.content.decode('utf-8')
result = json.loads(response)
print(searchUrl)
print(r)
print(result)

tasks = result.get('items', [])
for task in tasks:
    print (task['title'])
