from flask import render_template, request
from game import app
from game import utils


@app.route('/', methods=['GET', 'POST'])
def home():
    context = {}
    if request.method == "POST":
        length = request.form['length'] or 1
        letters = request.form['letters'] or ''
        words = utils.get_words(length, letters.upper())
        context.update({
            'length': length,
            'letters': letters,
            'words': words,
        })
    return render_template('index.html', **context)
