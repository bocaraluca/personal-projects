from src.repository.memory_repository import BooksMemoryRepository, ClientsMemoryRepository
import unittest

class TestBookMemoryRepository(unittest.TestCase):
    def setUp(self):
        self.repo = BooksMemoryRepository()

    def test_add(self):
        self.repo.add_book(21, 'Ion', 'Liviu Rebreanu')
        new_book = self.repo.find_book(21)
        self.assertEqual(new_book.title, 'Ion')
        self.assertEqual(new_book.author, 'Liviu Rebreanu')

    def test_remove(self):
        self.repo.remove_book(20)
        self.assertEqual(len(self.repo.list_books()), 19)

    def test_update(self):
        self.repo.update_book(1, 'Ion', 'Liviu Rebreanu')
        book = self.repo.find_book(1)
        self.assertEqual(book.title, 'Ion')
        self.assertEqual(book.author, 'Liviu Rebreanu')

class TestClientMemoryRepository(unittest.TestCase):
    def setUp(self):
        self.repo = ClientsMemoryRepository()

    def test_add(self):
        self.repo.add_client(21, 'Ana Popescu')
        new_client = self.repo.find_client(21)
        self.assertEqual(new_client.name, 'Ana Popescu')

    def test_remove(self):
        self.repo.remove_client(20)
        self.assertEqual(len(self.repo.list_clients()), 19)

    def test_update(self):
        self.repo.update_client(1, 'Ana Popescu')
        client = self.repo.find_client(1)
        self.assertEqual(client.name, 'Ana Popescu')



