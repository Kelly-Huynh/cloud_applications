
from playwright.sync_api import Page, expect
from flask import Flask
import sys
import os
from lib.database_connection import DatabaseConnection

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

# a descriptive test name
# def test_get_films_returns_a_200():
#     # here's where we make the test client
#     client = app.test_client()

#     # here's where we make the request
#     response = client.get("/films")

#     # here's where we assert that the response's status code is 200
#     assert response.status_code == 200

def test_get_films_returns_all_the_initial_films(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")
    actual_list = page.locator("ul").all_inner_texts()
    expected_list = [
        "The Hunger Games by Gary Ross\n"
        "Tenet by Christopher Nolan\n"
        "Project Hail Mary by Phil Lord\n"
        "Dune by Denis Villeneuve"
        ]
    assert actual_list == expected_list

def test_get_books_returns_a_200():
    # here's where we make the test client
    client = app.test_client()

    # here's where we make the request
    response = client.get("/books")

    # here's where we assert that the response's status code is 200
    assert response.status_code == 200

# test for iteration 1 part 1
# a descriptive test name
# def test_get_books_returns_all_the_initial_books():

#     client = app.test_client()
#     response = client.get("/initial_books")
#     print(response)
#     # here's where we assert that the response body contains all the books
#     # note that we need to call .json on the response
#     assert response.json == [
#         {
#             "title": "The Gruffalo",
#             "author": "Julia Donaldson"
#         },
#         {
#             "title": "Ada Twist, Scientist",
#             "author": "Andrea Beaty"
#         },
#         {
#             "title": "The Girl Who Drank the Moon",
#             "author": "Kelly Barnhill"
#         },
#         {
#             "title": "Dragons in a Bag",
#             "author": "Zetta Elliott"
#         }
#     ]

# def test_get_authors_returns_all_initial_authors():

#     client = app.test_client()
#     response = client.get("/initial_authors")

#     assert response.json == [
#         {
#             "name": "Julia Donaldson",
#             "dob": "1948-09-16"
#         },
#         {
#             "name": "Andrea Beaty",
#             "dob": "1961-10-08"
#         },
#         {
#             "name": "Kelly Barnhill",
#             "dob": "1973-01-01"
#         },
#         {
#             "name": "Zetta Elliott",
#             "dob": "1979-11-11"
#         }
#     ]

# def test_has_title(page: Page):
    
#     page.goto("http://127.0.0.1:5001/books")
    
#     h1 = page.locator("h1")
#     # print(h1)
#     expect(h1).to_have_text("My Books")

# def test_book_list_contains_all_books(page: Page):
#     connection = DatabaseConnection()
#     connection.connect()
#     connection.seed("./seeds/books.sql")
#     page.goto("http://127.0.0.1:5001/books")

#     books = page.locator("li")
#     expected_books = [
#         'The Hungry Caterpiller by Eric Carle',
#         'Amber the Orange Fairy by Daisy Meadows',
#         'The Elephant Vanishes by Haruki Murakami',
#         'Dune by Frank Herbert'
#     ]

    # actual_list = page.locator("li").all_inner_texts()

    # assert actual_list == expected_books

def test_create_new_book(page: Page):
    page.goto("http://localhost:5001/books")

    page.get_by_placeholder("Title").fill("Republic")

    page.get_by_placeholder("Author").fill("Plato")

    page.get_by_role("button", name="Submit").click()

    books = page.locator("li")

    new_book = books.all_inner_texts()[-1]

    assert new_book == "Republic by Plato"

    # expected_books = [
    #     'The Hungry Caterpiller by Eric Carle',
    #     'Amber the Orange Fairy by Daisy Meadows',
    #     'The Elephant Vanishes by Haruki Murakami',
    #     'Dune by Frank Herbert',
    #     'Republic by Plato'
    # ]

def test_create_new_film(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://localhost:5001/films")

    page.get_by_placeholder("Title").fill("Pulp Fiction")

    page.get_by_placeholder("Director").fill("Quentin Tarantino")

    page.get_by_role("button", name="Add Film").click()

    films = page.locator("li")

    new_film = films.all_inner_texts()[-1]

    assert new_film == "Pulp Fiction by Quentin Tarantino"
