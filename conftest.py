import pytest
from main import BooksCollector


@pytest.fixture
def collection():
    collection = BooksCollector()
    return collection


@pytest.fixture
def collection_books(collection):
    collect = collection
    books = ['Гарри Поттер', 'Ну погоди!', 'Оно', 'Ирония судьбы', 'Шерлок Холмс']
    genre = ['Фантастика', 'Мультфильмы', 'Ужасы', 'Комедии', 'Детективы']
    for i in range(5):
        collect.add_new_book(books[i])

    for i in range(5):
        collect.set_book_genre(books[i], genre[i])
    return collect