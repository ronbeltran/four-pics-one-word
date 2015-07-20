#!/usr/bin/env python
import os
import pickle

FILEPATH = os.path.abspath('google-books-common-words.txt')

WORD_LENGTHS = []


def convert_to_dict(filename):
    data = {}
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            key, value = line.split()
            data.update({key: int(value)})
        return data


def pickle_data(data, filename):
    if not isinstance(data, dict):
        raise TypeError('data should be a dict')
    with open(filename, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    print 'Data saved as: {}'.format(os.path.abspath(filename))


def unpickle_data(filename):
    data = None
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


if __name__ == "__main__":
    data = convert_to_dict(FILEPATH)
    pickle_data(data, 'google-books-common-words.bin')
#    _data = unpickle_data('google-books-common-words.bin')
#    print _data
