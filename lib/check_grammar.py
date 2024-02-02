def check_grammar(text):
    ending_puncuation = ('!', '?', '.')
    if type(text) != str or not len(text):
        raise Exception("Text argument must be a non-empty string.")
    if text[0].isupper() and text[-1] in ending_puncuation:
        return True
    return False