#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary is None) or (len(a_dictionary) == 0):
        return None
    v_list = []
    for values in a_dictionary.values():
        v_list.append(values)
    max_score = v_list[0]
    for i in v_list:
        if i > max_score:
            max_score = i
    for name, score in a_dictionary.items():
        if score == max_score:
            return name
