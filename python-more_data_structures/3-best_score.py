def best_score(a_dictionary):
    if a_dictionary == None or a_dictionary == {}:
        return None
    else:
        new = sorted(a_dictionary.values())
        return new[-1]
