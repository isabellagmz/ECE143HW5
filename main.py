# Isabella Gomez A15305555
# ECE143 HW5

from word_processing import get_average_word_length
from word_processing import get_longest_word
from word_processing import get_longest_words_startswith
from word_processing import get_most_common_start
from word_processing import get_most_common_end
from urllib.request import urlopen

class Homework5:
    def __init__(self):
        pass

if __name__ == '__main__':

    my_Homework5 = Homework5()

    u = 'https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
    response = urlopen(u)
    words = [i.strip().decode('utf8') for i in response.readlines()]
    start = 'A'
    # print(get_average_word_length(words))
    # print(get_longest_word(words))
    # print(get_longest_words_startswith(words, start))
    # print(get_most_common_start(words))
    print(get_most_common_end(words))

