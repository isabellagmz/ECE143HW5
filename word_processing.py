# Isabella Gomez A15305555
# ECE143 HW5

# imports:
import re

def get_average_word_length(words):
    '''
    This function takes in a list of words and computes the average length
    of the words in the list.

    :param words: list of words
    :return: average length of the words in the list
    '''

    # check that words is a list of strings
    assert type(words) == list
    for word in range(len(words)):
        assert type(words[word]) == str

    average_length = 0

    # get average length of all words in list
    for word in range(len(words)):
        average_length = average_length + len(words[word])
    average_length = average_length / len(words)

    return average_length

def get_longest_word(words):
    '''
    Gets the longest word in the list

    :param words: list of words
    :return: returns the string of the longest word
    '''

    # check that words is a list of strings
    assert type(words) == list
    for word in range(len(words)):
        assert type(words[word]) == str

    list_of_lenghts = []

    # make a list with all the word lengths
    for word in range(len(words)):
        list_of_lenghts.append(len(words[word]))

    longest_word_length = max(list_of_lenghts)

    for l in range(len(list_of_lenghts)):
        if list_of_lenghts[l] == longest_word_length:
            longest_word = words[l]

    return longest_word

def get_longest_words_startswith(words,start):
    '''
    This function finds the longest word that begins with the letter
    "start"

    :param words: list with all words
    :param start: the letter with which the longest word will start
    :return: the longest word that begins with the given letter
    '''

    # check that words is a list of strings
    assert type(words) == list
    for word in range(len(words)):
        assert type(words[word]) == str

    # check that start is a single letter and str
    assert type(start) == str
    assert len(start) == 1

    # make start lowercase
    if start.isupper() == True:
        start = start.lower()

    words_with_start_letter = []

    for word in range(len(words)):
        first_letter = words[word][0]
        # make a list with all words that begin with "start"
        if start == first_letter:
            words_with_start_letter.append(words[word])

    list_of_lenghts = []

    # make a list with all the word lengths
    for word in range(len(words_with_start_letter)):
        list_of_lenghts.append(len(words_with_start_letter[word]))

    longest_word_length = max(list_of_lenghts)

    for l in range(len(list_of_lenghts)):
        if list_of_lenghts[l] == longest_word_length:
            longest_word = words_with_start_letter[l]

    return longest_word

def get_most_common_start(words):
    '''
    This function checks what beginning letter is most common
    amongst the list of words

    :param words: list of words
    :return: string of most common letter
    '''

    # check that words is a list of strings
    assert type(words) == list
    for word in range(len(words)):
        assert type(words[word]) == str

    first_letter_list = []

    # make a list of first letters
    for word in range(len(words)):
        first_letter_list.append(words[word][0])

    # finding most common letter
    most_common = max(set(first_letter_list), key=first_letter_list.count)

    return most_common

def get_most_common_end(words):
    '''
    This function checks what beginning letter is most common
    amongst the list of words

    :param words: list of words
    :return: string of most common letter
    '''

    # check that words is a list of strings
    assert type(words) == list
    for word in range(len(words)):
        assert type(words[word]) == str

    last_letter_list = []

    # make a list of last letters
    for word in range(len(words)):
        last_letter_list.append(words[word][-1])

    # finding most common letter
    most_common = max(set(last_letter_list), key=last_letter_list.count)

    return most_common
