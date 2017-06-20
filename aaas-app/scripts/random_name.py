import random

def getRandomName(textfile):
    nameList = []
    for line in open(textfile,'r'):
        nameList.append(line)
    randomNumber = random.randint(0, len(nameList) - 1)
    randomName = nameList[randomNumber]
    return randomName
