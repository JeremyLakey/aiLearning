
word_scrub_list = ["me", "as", "your", "an", "him", "her", "in", "a", "i", "at", "you", "he", "she", "we", "and", "or", "so", "for", "are", "were", "now", "with", "when", "where", "who", "what", "when", "had", "went", "on", "to", "the", "they", "there", "was"]


def focus_words(words):
    global word_scrub_list
    temp = []
    for word in words:
        if word.lower() not in word_scrub_list:
            temp.append(word)
    return temp


remove_list = ['.', '$', '\"', ',', '#', "@", "!", "%", "^", "&", "*", "\'", ";", "+", "-", "(", ")", "[", "]", "{", "}", "=", "<", ">", "?", "`", "~"]


def punc_filter(word):
    for c in remove_list:
        word.replace(c, "")


score_alpha = {
    "a": 1,
    "b": 8,
    "c": 7,
    "d": 5,
    "e": 1,
    "f": 6,
    "g": 6,
    "h": 4,
    "i": 2,
    "j": 8,
    "k": 6,
    "l": 5,
    "m": 5,
    "n": 5,
    "o": 2,
    "p": 4,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 2,
    "u": 3,
    "v": 9,
    "w": 7,
    "x": 10,
    "y": 5,
    "z": 10,
}

def get_score(word):
    total = 0
    for c in word:
        if c in score_alpha:
            total += score_alpha[c]

    return total