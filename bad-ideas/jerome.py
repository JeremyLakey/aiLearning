from util.files import get_file_paths
from util.memoryMap import MemoryMap

def main():
    files = get_file_paths()
    mem_map = MemoryMap(files)


    while True:
        input_text = input("You: ")


if __name__ == "__main__":
    main()

