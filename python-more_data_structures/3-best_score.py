def best_score(a_dictionary):
    if a_dictionary == None or a_dictionary == {}:
        return None
    else:
        new = sorted(a_dictionary.values())
        for key, values in a_dictionary.items():
            if values == new[-1]:
                return key
            else:
                continue
