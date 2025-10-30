from collections import Counter

def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_char_counts(text):
    return Counter(list(text.lower()))

def get_sorted_char_counts(_d):
    list_of_char_counts = [{"char":k, "num":v} for k,v in _d.items()]
    list_of_char_counts.sort(key=lambda el: el["num"], reverse=True)
    return list_of_char_counts
