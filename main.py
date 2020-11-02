# Isabella Gomez A15305555
# ECE143 HW5

from interval_objects import Interval
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

    a = Interval(3,4)
    b = Interval(1,5)

