from src.exceptions.duplicate_id import DuplicateRentalIdException
from src.exceptions.not_found import RentalNotFoundException, ClientNotFoundException
from datetime import datetime

from src.exceptions.undo_exceptions import NoMoreUndosException, NoMoreRedosException


def print_menu():
    print('B - Manage books')
    print('C - Manage clients')
    print('M - Manage rentals')
    print('F - Find books or clients based on a given criteria')
    print('S - Show statistics')
    print('U - Undo')
    print('R - Redo')
    print('X - Exit')
    print()

class ConsoleUi:
    def __init__(self, undo_service, books_service, clients_service, rentals_service):
        self._books_service = books_service
        self._clients_service = clients_service
        self._rentals_service = rentals_service
        self._undo_service = undo_service

    def run(self):
        print('Welcome to the library!')
        while True:
            print_menu()
            opt = input('>> ').upper()
            if opt == 'B':
                self.manage_books()
            elif opt == 'C':
                self.manage_clients()
            elif opt == 'M':
                self.rent_return_book()
            elif opt == 'F':
                self.search_books_clients()
            elif opt == 'S':
                self.show_statistics()
            elif opt == 'U':
                self.undo()
            elif opt == 'R':
                self.redo()
            elif opt == 'X':
                print('Bye!')
                break
            else:
                print('Invalid command! Try again.')
        print()

    def manage_books(self):
        print('A - Add book')
        print('R - Remove book')
        print('U - Update book')
        print('L - List books')
        opt = input('>> ').upper()

        if opt == 'A':
            try:
                book_id = int(input('Book id: '))
                if self._books_service.find_book_by_id(book_id) is not None:
                    print(f'Book with id {book_id} already exists!')
                    return
                title = input('Title: ')
                author = input('Author: ')
                self._books_service.add_book(book_id, title, author)
            except ValueError:
                print('Book id must be an integer!')
            print()

        elif opt == 'R':
            try:
                book_id = int(input('Book id: '))
                if self._books_service.find_book_by_id(book_id) is None:
                    print(f'Book with id {book_id} does not exist!')
                    return
                self._books_service.remove_book(book_id)
            except ValueError:
                print('Book id must be an integer!')
            print()

        elif opt == 'U':
            try:
                book_id = int(input('Book id: '))
                if self._books_service.find_book_by_id(book_id) is None:
                    print(f'Book with id {book_id} does not exist!')
                    return
                new_title = input('New title: ')
                new_author = input('New author: ')
                self._books_service.update_book(book_id, new_title, new_author)
            except ValueError:
                print('Book id must be an integer!')

        elif opt == 'L':
            books = self._books_service.list_books()
            for book in books:
                print(book)
            print()

        else:
            print('Invalid choice! Try again.')

    def manage_clients(self):
        print('A - Add client')
        print('R - Remove client')
        print('U - Update client')
        print('L - List clients')
        opt = input('>> ').upper()

        if opt == 'A':
            try:
                client_id = int(input('Client id: '))
                if self._clients_service.find_client_by_id(client_id) is not None:
                    print(f'Client with id {client_id} already exists!')
                    return
                name = input('Name: ')
                self._clients_service.add_client(client_id, name)
            except ValueError:
                print('Client id must be an integer!')
            print()

        elif opt == 'R':
            try:
                client_id = int(input('Client id: '))
                if self._clients_service.find_client_by_id(client_id) is None:
                    print(f'Client with id {client_id} does not exist!')
                    return
                self._clients_service.remove_client(client_id)
            except ValueError:
                print('Client id must be an integer!')
            print()

        elif opt == 'U':
            try:
                client_id = int(input('Client id: '))
                if self._clients_service.find_client_by_id(client_id) is None:
                    print(f'Client with id {client_id} does not exist!')
                    return
                new_name = input('New name: ')
                self._clients_service.update_client(client_id, new_name)
            except ValueError:
                print('Client id must be an integer!')
            print()

        elif opt == 'L':
            clients = self._clients_service.list_clients()
            for client in clients:
                print(client)
            print()

        else:
            print('Invalid option! Try again.')

    def search_books_clients(self):
        print('B - Search books')
        print('C - Search clients')
        opt = input('>> ').upper()
        if opt == 'B':
            self.search_books()
        elif opt == 'C':
            self.search_clients()
        else:
            print('Invalid choice! Try again.')

    def search_books(self):
        criteria = input('Search criteria: ')
        try:
            criteria = int(criteria)
            books = [self._books_service.find_book_by_id(criteria)]
        except ValueError:
            books_dupl = self._books_service.find_books_by_title(criteria)
            books_dupl.extend(self._books_service.find_books_by_author(criteria))
            books = []
            for book in books_dupl:
                if book not in books:
                    books.append(book)

        if not books:
            print('No books found with the given criteria!')
        else:
            for book in books:
                print(book)
        print()

    def search_clients(self):
        criteria = input('Search criteria: ')
        try:
            criteria = int(criteria)
            clients = [self._clients_service.find_client_by_id(criteria)]
        except ValueError:
            clients = self._clients_service.find_clients_by_name(criteria)

        if not clients:
            print('No clients found with the given criteria!')
        else:
            for client in clients:
                print(client)
        print()

    def rent_return_book(self):
        print('R - Rent book')
        print('E - Return book')
        print('L - List rentals')

        opt = input('>> ').upper()
        if opt == 'R':
            self.rent_book()
        elif opt == 'E':
            self.return_book()
        elif opt == 'L':
            self.list_rentals()
        else:
            print('Invalid choice! Try again.')
        print()

    def rent_book(self):
        try:
            rental_id = int(input('Rental id: '))
            book_id = int(input('Book id: '))
            client_id = int(input('Client id: '))
            day = int(input('Day: '))
            month = int(input('Month: '))
            year = int(input('Year: '))
            rented_date = datetime(year, month, day)
            try:
                self._rentals_service.find_rental_by_id(rental_id)
            except RentalNotFoundException as e:
                print(e)

            try:
                self._clients_service.find_client_by_id(client_id)
            except ClientNotFoundException as e:
                print(e)

            if self._rentals_service.is_book_available(book_id, rented_date, None):
                try:
                    self._rentals_service.rent_book(rental_id, book_id, client_id, rented_date)
                    print(f'Book with id {book_id} has been rented successfully!')
                except DuplicateRentalIdException as e:
                    print(e)
            else:
                print('The rental could not be completed! The book is unavailable for the requested date.')
        except ValueError:
            print('Invalid input! Rental id, book id, and client id must be integers, and the date must be valid.')

    def return_book(self):
        try:
            rental_id = int(input('Rental id: '))
            if self._rentals_service.find_rental_by_id(rental_id) is None:
                print(f'Rental with id {rental_id} does not exist!')
                return
            day = int(input('Day: '))
            month = int(input('Month: '))
            year = int(input('Year: '))
            returned_date = datetime(year, month, day)
            try:
                self._rentals_service.return_book(rental_id, returned_date)
                print(f'Book has been returned successfully!')
            except RentalNotFoundException as e:
                print(e)
            except ValueError as e:
                print(e)
        except ValueError:
            print('Invalid input! Rental id must be an integer, and the date must be valid.')

    def list_rentals(self):
        rentals = self._rentals_service.list_rentals()
        for rental in rentals:
            print(rental)
        print()

    def show_statistics(self):
        print('B - Most rented books')
        print('C - Most active clients')
        print('A - Most rented authors')
        opt = input('>> ').upper()
        if opt == 'B':
            self.stats_most_rented_books()
        elif opt == 'C':
            self.stats_most_active_clients()
        elif opt == 'A':
            self.stats_most_rented_authors()
        else:
            print('Invalid choice! Try again.')
        print()

    def stats_most_rented_books(self):
        books = self._rentals_service.get_most_rented_books()
        for book_id, title, count in books:
            print(f'{book_id} - {title} - rented {count} times')
        print()

    def stats_most_active_clients(self):
        clients = self._rentals_service.get_most_active_clients()
        for client_id, name, days in clients:
            print(f'{client_id} - {name} - has {days} book rental days')
        print()

    def stats_most_rented_authors(self):
        authors = self._rentals_service.get_most_rented_authors()
        for name, count in authors:
            print(f'{name} - rented {count} times')
        print()

    def undo(self):
        try:
            self._undo_service.undo()
        except NoMoreUndosException as e:
            print(e)

    def redo(self):
        try:
            self._undo_service.redo()
        except NoMoreRedosException as e:
            print(e)


