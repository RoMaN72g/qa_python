# qa_python
В проекте реализовано 13 тестов:
1. test_add_new_book_add_two_books - исправлен исходный тест (замена несуществующего метода get_book_rating на get_book_genre).
2. test_add_new_book_positive_with_dict_check - проверяем добавление новой книги в словарь.
3. test_add_new_book_not_add_invalid_name - параметризованный тест: невалидные имена не добовляются.
4. test_set_book_genre_for_valid_book - установка существующего жанра существующей книге.
5. test_set_book_genre_for_invalid_genre - проверяем невозможность установить несуществующий жанр.
6. test_get_book_genre_returns_genre - получение жанра книги по названию книги.
7. test_get_books_with_specific_genre_returns_correct_list - возврат списка книг по жанру.
8. test_get_books_with_specific_genre_not_include_other_genre - проверка того что книги с другим жанром не попадают в список книг по жанру.
9. test_get_books_genre_returns_books_genre - возврат полного словаря книг.
10. test_get_books_for_children_excludes_genre_age_rating - проверка что книги с возрастным жанром не попадают в список книг для детей.
11. test_add_book_in_favorites - проверка на добавление книги в избранное.
12. test_add_book_in_favorites_duplicate_not_added - повторное добавление книги в избранное не дублируется в списке.
13. test_delete_book_from_favorites - удаление книги из избранного.
14. test_test_delete_book_from_favorites_nonexistent_book - проверяем что при попытке удалить книгу, которой нет в избранном, метод не падает и не изменяет список избранного.