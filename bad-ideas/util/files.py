from os import listdir
from os.path import isfile, join


memoryPath = "./memories"


def get_file_paths():
    return ["./memories/" + f for f in listdir(memoryPath) if isfile(join(memoryPath, f))]


def add_file(text):
    next = len([f for f in listdir(memoryPath) if isfile(join(memoryPath, f))])
    f = open(str(next) + ".txt", mode='w')
    f.write(text)
    f.close()