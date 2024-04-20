from os import listdir
from os.path import isfile, join


memoryPath = "./memories"

def get_file_paths():
    return ["./memories/" + f for f in listdir(memoryPath) if isfile(join(memoryPath, f))]


def add_file(text):
    print("Adding...")
    print(text)
    next = len([f for f in listdir(memoryPath) if isfile(join(memoryPath, f))])
    print(next)
    f = open("./memories/" + str(next) + ".txt", mode='w')
    f.write(text)
    f.close()
