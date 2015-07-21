import operator

from flask import render_template, request
from game import app
from game import utils


@app.route('/', methods=['GET', 'POST'])
def home():
    context = {}
    if request.method == "POST":
        length = request.form['length'] or 1
        letters = request.form['letters'] or ''
        words = utils.get_words_dict(length, letters.upper())
        sorted_words = sorted(words.items(), key=operator.itemgetter(1))
        sorted_words.reverse()
        context.update({
            'length': length,
            'letters': letters,
            'words': sorted_words,
        })
    return render_template('index.html', **context)
