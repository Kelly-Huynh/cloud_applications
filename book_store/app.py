from flask import Flask
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from flask import render_template
from flask import request

# instantiate a Flask app object
app = Flask(__name__)

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

# # NEW PART START

# # duplicate route
# @app.route('/hello', methods=['GET'])
# def hello_again():
#     return "Hello, hello and hello again!"

# # NEW PART END
# added as a workaround at end of iteration 2
@app.route('/seed', methods=['GET'])
def seed():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("seeds/book_store.sql")
    return "We probably seeded the books database"


@app.route('/books', methods=['GET'])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    print(books)
    return render_template("books.html", books=books)

@app.route('/books', methods=['POST'])
def create_book():
    # make a new db connection
    connection = DatabaseConnection()
    connection.connect()
    # make a new instance of BookRepository
    book_repository = BookRepository(connection)
    # get the request body
    book_details = request.form # no longer json and updated to form
    # my BookRepository expects an instance of Book, so make one here
    book = Book(title=book_details["title"], author=book_details["author"])
    # save the book
    book_repository.create(book)
    # print(book_details)
    # return a 201, which means "created"
    return "created", 201

@app.route('/initial_books', methods=['GET'])
def initial_books():
    book_list = [
        {
            "title": "The Gruffalo",
            "author": "Julia Donaldson"
        },
        {
            "title": "Ada Twist, Scientist",
            "author": "Andrea Beaty"
        },
        {
            "title": "The Girl Who Drank the Moon",
            "author": "Kelly Barnhill"
        },
        {
            "title": "Dragons in a Bag",
            "author": "Zetta Elliott"
        }
    ]
    return book_list

@app.route('/authors', methods=['GET'])
def authors():
    return render_template("authors.html")

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)

@app.route('/initial_authors', methods=['GET'])
def initial_authors():
    author_list = [
        {
        "name": "Julia Donaldson",
        "dob": "1948-09-16"
        },
        {
            "name": "Andrea Beaty",
            "dob": "1961-10-08"
        },
        {
            "name": "Kelly Barnhill",
            "dob": "1973-01-01"
        },
        {
            "name": "Zetta Elliott",
            "dob": "1979-11-11"
        }
    ]
    return author_list

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

