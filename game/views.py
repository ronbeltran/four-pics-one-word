import logging
from flask import render_template, request
from game import app


@app.route('/', methods=['GET', 'POST'])
def home():
    context = {}
    if request.method == "POST":
        length = request.form['length'] or 1
        letters = request.form['letters']
        context.update({
            'length': int(length),
            'letters': letters,
        })
    return render_template('index.html', **context)
