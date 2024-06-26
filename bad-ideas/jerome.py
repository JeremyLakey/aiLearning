import random

from util.files import get_file_paths, add_file
from util.memoryMap import MemoryMap
from util.focus import focus_words, punc_filter, get_score
from util.valueMap import get_values
from util.chat import do_chat

files = None
mem_map = None

def filter_mem_tups(tuples):
    if tuples is None:
        return []
    visited = {}
    i = 0
    while i < len(tuples):
        tup = tuples[i]

        if tup[1] in visited:
            tuples.pop(i)
        else:
            visited[tup[1]] = 1
            i += 1
    return tuples
def select_mems(text, mem_map):
    cycle = ["", "", ""]
    totals = []
    for word in focus_words(text.split()):
        w = punc_filter(word.lower())
        cycle[2] = cycle[1]
        cycle[1] = cycle[0]
        cycle[0] = w
        result = mem_map.cycle_attempt(cycle)
        if result != -1:
            total = 0
            for c in cycle:
                total += get_score(c)

            totals.append((total, result))
    totals.sort(reverse=True)
    finals = filter_mem_tups(totals)
    if len(finals) < 3:
        return finals
    return finals[:3]


# builds the prompt to send to chap GPT
def build_prompt(text, mem_map, mems, values):

    final = "Your name is Jerome\n\nYou value 5 things:"

    for v in values:
        final += "\n" + v


    if len(mems) > 0:
        if len(mems) == 1:
            final += "\n\nYou remember 1 thing:"
            final += "\n" + mem_map.get_memory(mems[0][1])
        else:
            final += "\n\nYou remember " + str(len(mems)) + " things:"
            for m in mems:
                final += "\n" + mem_map.get_memory(m[1])

    return final + "\n\nUser says: " + text


def maybe_add_memory(reply):
    if random.randint(0, 5) != 0:
        return

    s = reply.split(".")
    t1 = random.choice(s)
    t2 = random.choice(s)
    if t1 != t2:
        add_file(t1 + ". " + t2 + ".")
    else:
        add_file(t1 + ".")


def set_up_jerome():
    global files, mem_map
    files = get_file_paths()
    mem_map = MemoryMap(files)


def do_chat_jerome(input_text):
    global files, mem_map
    final_text = build_prompt(input_text, mem_map, select_mems(input_text, mem_map), get_values())
    reply = do_chat(input_text)
    print("Jerome: " + reply)
    #add_file(reply.split(".")[0])
    return reply


def main():
    global files, mem_map
    set_up_jerome()


    while True:
        input_text = input("\nYou: ")
        do_chat_jerome(input_text)




if __name__ == "__main__":
    main()

