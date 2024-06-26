import random
from .focus import focus_words, punc_filter

def shift(cycle):

    i = len(cycle) - 1
    while i > 0:
        cycle[i] = cycle[i - 1]
        i -= 1


def insert_to_map(cycle, m, i):
    if cycle[0] not in m:
        m[cycle[0]] = {}

    if cycle[1] not in m[cycle[0]]:
        m[cycle[0]][cycle[1]] = {}

    if cycle[2] not in m[cycle[0]][cycle[1]]:
        m[cycle[0]][cycle[1]][cycle[2]] = []

    m[cycle[0]][cycle[1]][cycle[2]].append(i)


def get_from_map(cycle, m):
    if cycle[0] not in m:
        return -1

    if cycle[1] not in m[cycle[0]]:
        return -1

    if cycle[2] not in m[cycle[0]][cycle[1]]:
        return -1

    if m[cycle[0]][cycle[1]][cycle[2]] is None or len(m[cycle[0]][cycle[1]][cycle[2]]) == 0:
        return -1
    return random.choice(m[cycle[0]][cycle[1]][cycle[2]])


class MemoryMap:
    def __init__(self, files):
        self.m = {}
        self.files = {}
        for i, file in enumerate(files):
            self.load_file(file, i)

    def load_file(self, file, i):
        f = open(file)

        line = f.readline().lower()
        self.files[i] = line
        words = focus_words(line.split(" "))
        cycle = ["", "", ""]
        for word in words:
            w = punc_filter(word)
            shift(cycle)
            cycle[0] = w

            insert_to_map(cycle, self.m, i)

    # returns -1 on missing
    def cycle_attempt(self, cycle):
        return get_from_map(cycle, self.m)

    def get_memory(self, i):
        if i not in self.files:
            return ""
        return self.files[i]