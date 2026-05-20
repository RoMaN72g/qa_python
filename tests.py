import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('bad_name', ['','a' * 41,'a' * 42])

    def test_add_new_book_not_add_with_invalid_name(self, bad_name):
        collector = BooksCollector()
        collector.add_new_book(bad_name)
        assert bad_name not in collector.get_books_genre()


    def test_set_book_genre_for_valid_book(self):
        collector = BooksCollector()
        book = 'Марсианские записки'
        genre = 'Фантастика'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    def test_set_book_genre_for_invalid_genre(self):
        collector = BooksCollector()
        book = 'Физика'
        genre = 'Наука'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) != genre


    def test_get_book_genre_returns_genre(self):
        collector = BooksCollector()
        book = 'Марсианские записки'
        genre = 'Фантастика'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre


    def test_get_books_with_specific_genre_returns_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга1', 'Книга2']

    def test_get_books_with_specific_genre_not_include_other_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_new_book('Книга3')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Фантастика')
        collector.set_book_genre('Книга3', 'Детективы')
        collector.get_books_with_specific_genre('Фантастика')
        assert 'Книга3' not in collector.get_books_with_specific_genre('Фантастика')


    def test_get_books_genre_returns_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Детективы')
        assert collector.get_books_genre() == {'Книга1': 'Фантастика', 'Книга2': 'Детективы'}


    def test_get_books_for_children_excludes_genre_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Детективы')
        assert collector.get_books_for_children() == ['Книга1']


    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        assert collector.get_list_of_favorites_books() == ['Книга1']

    def test_add_book_in_favorites_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга1')
        assert collector.get_list_of_favorites_books() == ['Книга1']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        collector.delete_book_from_favorites('Книга1')
        assert collector.get_list_of_favorites_books() == []




