import sys
import re
from operator import itemgetter
from collections import defaultdict

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
    words_frequency = defaultdict(int)

    for word in words:
        words_frequency[word] += 1

    words_frequency_sorted = sorted(words_frequency.items(), key=itemgetter(0))

    for item in sorted(
            words_frequency_sorted, key=itemgetter(1), reverse=True):
        print("{}: {}".format(item[KEY], item[VALUE]))
