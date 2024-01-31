def count_words(string):
    if type(string) != str:
        raise Exception("Argument must be a string.")
    word_list = string.split()
    return len(word_list)