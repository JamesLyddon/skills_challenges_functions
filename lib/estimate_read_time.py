import math 

def estimate_read_time(text, wpm=200):
    word_list = text.split()
    word_num = len(word_list)
    minutes_est = word_num / wpm
    frac, whole = math.modf(minutes_est)
    seconds = round(frac * 60)
    minutes = round(whole)

    return f"At {wpm}wpm this {word_num} word text would take you {minutes} minutes and {seconds} seconds to read."