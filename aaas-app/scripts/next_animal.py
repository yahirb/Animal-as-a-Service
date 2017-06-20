def getNextAnimalObject(my_path):
    animalObject = {}
    f = open(my_path, 'r')
    animalObject['name'] = f.readline()
    animalObject['URL'] = f.readline()
    animalObject['nickname'] = f.readline()
    f.close()
    return animalObject
