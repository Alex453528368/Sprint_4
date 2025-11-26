import pytest
from main import BooksCollector


class TestBooksCollector:

    # Тест 1 добавляет новую книгу в словарь без указания жанра
    @pytest.mark.parametrize('book_name', [
        'Тестирование ПО',
        'Harry Potter', 
        '1 + 1'
    ])
    def test_add_new_book_valid_name_book_added(self, book_name, collection):
        collection.add_new_book(book_name)
        assert book_name in collection.get_books_genre()

    # Тест 2 устанавливаем жанр книги, если книга есть в books_genreи её жанр входит в список genre
    @pytest.mark.parametrize('book_name, genre, expected_genre', [
        ('Война миров', 'Фантастика', 'Фантастика'),
        ('Оно', 'Ужасы', 'Ужасы'),
        ('Шерлок Холмс', 'Детективы', 'Детективы')
    ])
    def test_set_book_genre_valid_genre_genre_set(self, book_name, genre, expected_genre, collection):
        collection.add_new_book(book_name)
        collection.set_book_genre(book_name, genre)
        assert collection.get_book_genre(book_name) == genre

    # Тест 3 выводим жанр книги по её имени.
    def test_get_book_genre_book_with_genre_returns_genre(self, collection):
        collection.add_new_book('Война миров')
        collection.set_book_genre('Война миров', 'Фантастика')
        assert collection.get_book_genre('Война миров') == 'Фантастика'

    # Тест 4 выводим список книг с определённым жанром.
    def test_get_books_with_specific_genre_existing_genre_returns_books(self, collection_books):
        assert collection_books.get_books_with_specific_genre('Ужасы') == ['Оно']

    # Тест 5 выводит текущий словарь books_genre
    def test_get_books_genre_with_books_returns_dict(self, collection):
        collection.add_new_book('Война миров')
        collection.set_book_genre('Война миров', 'Фантастика')
        books_genre = collection.get_books_genre()
        assert books_genre == {'Война миров': 'Фантастика'}

    # Тест 6 возвращает книги, которые подходят детям.
    def test_get_books_for_children_mixed_genres_returns_child_friendly(self, collection_books):
        children_books = collection_books.get_books_for_children()
        assert len(children_books) == 3 and children_books == ['Гарри Поттер', 'Ну погоди!', 'Ирония судьбы']


    # Тест 7 добавляет книгу в избранное. Книга должна находиться в словаре books_genre.
    def test_add_book_in_favorites_existing_book_added(self, collection):
        first_book = 'Мцыри'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

    # Test 8 удаляем книгу из избранного, если она там есть.
    def test_delete_book_from_favorites_existing_book_removed(self, collection):
        first_book = 'Ведьмак'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(first_book)
        assert len(collection.get_list_of_favorites_books()) == 0

    # Test 9 получает список избранных книг.
    def test_get_list_of_favorites_books_with_favorites_returns_list(self, collection_books):
        collection_books.add_book_in_favorites('Гарри Поттер')
        collection_books.add_book_in_favorites('Ирония судьбы')
        favorites = collection_books.get_list_of_favorites_books()
        assert favorites == ['Гарри Поттер', 'Ирония судьбы']