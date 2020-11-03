# Isabella Gomez A15305555
# ECE143 HW5

from random_slash import gen_rand_slash
from interval_objects import Interval
from urllib.request import urlopen
import numpy as np
from matplotlib.pylab import subplots, cm
import matplotlib.pyplot as plt

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

    a = Interval(-4,6)
    b = Interval(-2,-1)

    #print(gen_rand_slash())
    fig, axs = subplots(3, 3, sharex=True, sharey=True)
    for ax in axs.flatten():
        ax.imshow(gen_rand_slash(), cmap=cm.gray_r)
    plt.show()
