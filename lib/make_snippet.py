def make_snippet(string):
    word_list = string.split()
    if len(word_list) < 6:
        return string
    else:
        return " ".join(word_list[:5]) + '...'