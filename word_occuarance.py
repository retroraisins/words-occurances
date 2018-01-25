import sys
import re
from operator import itemgetter

KEY = 0
VALUE = 1


def get_words_from(path):
    words = []
    with open(path) as file:
        for line in file:
            for word in re.sub("[^\w]", " ", line).split():
                words.append(str(word))
    return words


if __name__ == "__main__":
    file_path = sys.argv[1]
    words = get_words_from(file_path)

    words_occurrences = sorted(
        [(word, words.count(word)) for word in set(words)],
        key=itemgetter(0))

    for item in sorted(
            words_occurrences, key=itemgetter(1), reverse=True):
        print("{}: {}".format(item[KEY], item[VALUE]))
