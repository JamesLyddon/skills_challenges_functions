import math 

def estimate_read_time(text, wpm=200):
    word_list = text.split()
    word_num = len(word_list)
    minutes_est = word_num / wpm
    frac, whole = math.modf(minutes_est)
    seconds = round(frac * 60)
    minutes = round(whole)
    sec_text = "seconds"
    if seconds == 1:
        sec_text = sec_text[:-1]
    min_text = "minutes"
    if minutes == 1:
        min_text = min_text[:-1]

    return f"At {wpm}wpm this {word_num} word text would take you {minutes} {min_text} and {seconds} {sec_text} to read."