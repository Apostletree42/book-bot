def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    res = {}
    for char in text:
        if char.isalpha():
            res[char.lower()] = res.get(char.lower(), 0) + 1
    return res

def get_sorted_dicts(dict):
    res = []
    for key in dict.keys():
        item = {}
        item["char"] = key
        item["num"] = dict[key]
        res.append(item)
    res.sort(reverse=True, key=sort_on)
    return res
    
def sort_on(dict):
    return dict["num"]