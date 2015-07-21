import logging
import operator

from flask import render_template, request
from google.appengine.api import memcache

from game import app
from game import utils

EXPIRE_TIME = 60 * 60 * 24  # 24 hours


@app.route('/', methods=['GET', 'POST'])
def home():
    context = {}
    if request.method == "POST":
        length = request.form['length'] or 1
        letters = request.form['letters'] or None
        if letters is None:
            context.update({
                'length': length,
                'letters': '',
            })
            return render_template('index.html', **context)
        letters = letters.upper()
        key = '{0}_{1}'.format(str(length), ''.join(sorted(letters)))
        cached_data = memcache.get(key)
        if cached_data is None:
            logging.info('{} not found in memcache'.format(key))
            words = utils.get_words_dict(length, letters)
            sorted_words = sorted(words.items(), key=operator.itemgetter(1))
            sorted_words.reverse()
            memcache.add(key, sorted_words, EXPIRE_TIME)
        else:
            logging.info('{} found in memcache'.format(key))
            sorted_words = cached_data
        context.update({
            'length': length,
            'letters': letters,
            'words': sorted_words,
        })
    return render_template('index.html', **context)
