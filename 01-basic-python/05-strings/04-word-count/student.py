def word_count(string):
    if len(string) == 0:
        return 0
    else:
        return len(string.split(" "))