
word_scrub_list = ["me", "as", "your", "an", "him", "her", "in", "a", "i", "at", "you", "he", "she", "we", "and", "or", "so", "for", "are", "were", "now", "with", "when", "where", "who", "what", "when", "had", "went", "on", "to", "the", "they", "there", "was"]


def focus_words(words):
    global word_scrub_list
    temp = []
    for word in words:
        if word.lower() not in word_scrub_list:
            temp.append(word)
    return temp
