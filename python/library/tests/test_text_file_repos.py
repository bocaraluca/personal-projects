import unittest
from src.repository.text_file_repository import BooksTextFileRepository, ClientsTextFileRepository

class TestBookTextFileRepository(unittest.TestCase):
    def setUp(self):
        self._reset_test_file('files/test_books.txt')
        self.repo = BooksTextFileRepository('files/test_books.txt')

    @staticmethod
    def _reset_test_file(filename):
        with open(filename, 'w') as file:
            file.truncate(0)

    def test_add(self):
        self.repo.add_book(21, 'Ion', 'Liviu Rebreanu')
        new_book = self.repo.find_book(21)
        self.assertEqual(new_book.title, 'Ion')
        self.assertEqual(new_book.author, 'Liviu Rebreanu')

    def test_remove(self):
        self.assertEqual(len(self.repo.list_books()), 20)
        self.repo.remove_book(20)
        self.assertEqual(len(self.repo.list_books()), 19)

    def test_update(self):
        self.repo.update_book(1, 'Ion', 'Liviu Rebreanu')
        book = self.repo.find_book(1)
        self.assertEqual(book.title, 'Ion')
        self.assertEqual(book.author, 'Liviu Rebreanu')


class TestClientTextFileRepository(unittest.TestCase):
    def setUp(self):
        self._reset_test_file('files/test_clients.txt')
        self.repo = ClientsTextFileRepository('files/test_clients.txt')

    @staticmethod
    def _reset_test_file(filename):
        with open(filename, 'w') as file:
            file.truncate(0)

    def test_add(self):
        self.repo.add_client(21, 'Ana Popescu')
        new_client = self.repo.find_client(21)
        self.assertEqual(new_client.name, 'Ana Popescu')

    def test_remove(self):
        self.assertEqual(len(self.repo.list_clients()), 20)
        self.repo.remove_client(20)
        self.assertEqual(len(self.repo.list_clients()), 19)

    def test_update(self):
        self.repo.update_client(1, 'Ana Popescu')
        client = self.repo.find_client(1)
        self.assertEqual(client.name, 'Ana Popescu')

