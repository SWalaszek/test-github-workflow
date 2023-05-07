"""
HELLO WSB.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """
    Returns a message.
    """
    return '<h1>Hello WSB!!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
