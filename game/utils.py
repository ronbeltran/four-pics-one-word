import pickle
import logging


WORDS = pickle.load(open('./static/google-books-common-words.bin', 'r'))


def is_subset(word, choices):
    _choices = list(choices)
    for c in word:
        if c not in _choices:
            return False
        _choices.remove(c)
    return True


def get_words(length, letters):
    length = int(length)
    candidates = []
    selected = []
    for key, value in WORDS.iteritems():
        if len(key) == length:
            candidates.append(key)
    for word in candidates:
        if is_subset(word, letters):
            selected.append(word)
    logging.info('Got {0} matches with length of {1} where choices {2}'.format(
        len(selected), length, letters))
    return selected


def get_words_dict(length, letters):
    length = int(length)
    candidates = []
    selected = {}
    for key, value in WORDS.iteritems():
        if len(key) == length:
            candidates.append(key)
    for word in candidates:
        if is_subset(word, letters):
            selected.update({word: WORDS.get(word)})
    logging.info('Got {0} matches with length of {1} where choices {2}'.format(
        len(selected.keys()), length, letters))
    return selected
