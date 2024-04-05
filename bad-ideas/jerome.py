from util.files import get_file_paths
from util.memoryMap import MemoryMap
from util.focus import focus_words, punc_filter, get_score
from util.valueMap import get_values


def select_mems(text, mem_map):
    cycle = ["", "", ""]
    totals = []
    for word in focus_words(text):
        w = punc_filter(word.lower())
        cycle[2] = cycle[1]
        cycle[1] = cycle[0]

        if mem_map.cycle_attempt(cycle) != -1:
            total = 0
            for c in cycle:
                total += get_score(c)

            totals.append((total, w))

    totals.sort(reverse=True)
    if len(totals) < 3:
        return totals
    return totals[:3]


def build_message(text, mem_map, mems, values):

    final = "You value 5 things:"

    for v in values:
        final += "\n" + v

    final += "\n\nYou are asked: \n" + text + "\n"

    if len(mems) > 0:
        final += "\nYou remember " + str(len(mems)) + " things"
        for m in mems:
            final += "\n" + mem_map.get_memory(m[1])

    return final


def main():
    files = get_file_paths()
    mem_map = MemoryMap(files)


    while True:
        input_text = input("You: ")
        final_message = build_message(input_text, mem_map, select_mems(input_text, mem_map), get_values())
        print(final_message)




if __name__ == "__main__":
    main()

