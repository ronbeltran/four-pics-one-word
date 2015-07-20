from game import app


@app.route('/')
def home():
    return '4 Pics 1 Word Solver'
