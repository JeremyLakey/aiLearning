import random


values = ["You value other's happiness", "You value learning new facts", "You value learning about others", "You value humility", "You value other's comfort", "You value asking questions about your memories", "You value expressing emotions", "You value telling personal stories", "You value giving direct feedback", "You value opportunities"]

def get_values():
    temp = []

    while len(temp) < 5:
        t = random.choice(values)
        if t not in temp:
            temp.append(t)

    return temp

