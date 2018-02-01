import sys
import re
from operator import itemgetter

KEY = 0
VALUE = 1


def get_words_from(path):
    words = []
    with open(path) as file:
        for line in file:
            words += re.sub("[^\w]", " ", line).split()
    return words


if __name__ == "__main__":
    file_path = sys.argv[1]
    words = get_words_from(file_path)
    words_frequency = {}

    for word in words:
        if str(word) in words_frequency:
            words_frequency[str(word)] += 1
        else:
            words_frequency[str(word)] = 1

    words_frequency_sorted = sorted(words_frequency.items(), key=itemgetter(0))

    for item in sorted(
            words_frequency_sorted, key=itemgetter(1), reverse=True):
        print("{}: {}".format(item[KEY], item[VALUE]))
