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

    words_occurrences = [(word, words.count(word)) for word in set(words)]
    new_sort = sorted(
        words_occurrences, key=itemgetter(0, 1), reverse=True)

    # sorted(
    #     new_sort, key=itemgetter(0), reverse=True)
    for item in new_sort:
        print(str(item[KEY]), ":", str(item[VALUE]))
