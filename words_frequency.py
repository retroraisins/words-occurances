import sys
import re
from operator import itemgetter
from collections import Counter

if __name__ == "__main__":
    file_path = sys.argv[1]
    words = re.findall(r'\w+', open(file_path, 'r').read().lower())

    words_frequency_sorted = sorted(Counter(words).items(), key=itemgetter(0))

    for word, frequency in sorted(
            words_frequency_sorted, key=itemgetter(1), reverse=True):
        print("{}: {}".format(word, frequency))
