from flask import Flask,jsonify
from books import Book

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
    book = Book()
    data = book.get_books_infos_limit()
    return jsonify(data)


if __name__ == '__main__':
    app.run()