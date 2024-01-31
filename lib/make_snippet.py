def make_snippet(string):
    if type(string) != str:
        raise Exception("Argument must be a string.")
    word_list = string.split()
    if len(word_list) < 6:
        return string
    else:
        return " ".join(word_list[:5]) + '...'