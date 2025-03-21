def count_words(book_text):
    return len(book_text.split())

def count_chars(book_text):
    characters_dict = {}

    for char in book_text:
        lower_char = char.lower()
        if lower_char in characters_dict:
            characters_dict[lower_char] += 1
        else:
            characters_dict[lower_char] = 1
    
    return characters_dict

def sorted_dict(dict):
    return dict["count"]

def dict_to_sorted_list(char_dict):
    sorted_list = []

    for key in char_dict:
        if key.isalpha():
            dict_tmp = {}
            dict_tmp["char"] = key
            dict_tmp["count"] = char_dict[key]
            sorted_list.append(dict_tmp)
    
    sorted_list.sort(reverse=True, key=sorted_dict)
    return sorted_list
