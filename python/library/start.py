from src.repository.binary_file_repository import RentalsBinaryFileRepository, ClientsBinaryFileRepository, \
    BooksBinaryFileRepository
from src.repository.memory_repository import RentalsMemoryRepository, ClientsMemoryRepository, BooksMemoryRepository
from src.repository.text_file_repository import RentalsTextFileRepository, BooksTextFileRepository, \
    ClientsTextFileRepository
from src.services.books_service import BooksService
from src.services.clients_service import ClientsService
from src.services.rentals_service import RentalsService
from src.services.undo_service import UndoService
from src.ui.console_ui import ConsoleUi
from src.ui.graphic_ui import GraphicUi
import tkinter as tk


def read_settings(file_path):
    settings = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                settings[key.strip()] = value.strip()
    return settings


def main():
    settings = read_settings('settings.properties')

    repo_type = settings.get('repository').strip()
    books_file = settings.get('books').strip() if settings.get('books') else None
    clients_file = settings.get('clients').strip() if settings.get('clients') else None
    rentals_file = settings.get('rentals').strip() if settings.get('rentals') else None
    ui = settings.get('ui').strip() if settings.get('ui') else 'console'

    if repo_type not in ['in-memory', 'text-file', 'binary-file']:
        raise ValueError("Invalid repository type! Must be 'in-memory', 'text-file', or 'binary-file'.")

    if repo_type in ['text-file', 'binary-file']:
        if not books_file or not clients_file:
            raise ValueError("File paths for books and clients must be provided for 'text-file' or 'binary-file' repository types.")

    if repo_type == 'in-memory':
        books_repo = BooksMemoryRepository()
        clients_repo = ClientsMemoryRepository()
        rentals_repo = RentalsMemoryRepository(books_repo, clients_repo)
    elif repo_type == 'text-file':
        books_repo = BooksTextFileRepository(books_file)
        clients_repo = ClientsTextFileRepository(clients_file)
        rentals_repo = RentalsTextFileRepository(books_repo, clients_repo, rentals_file)
    else:
        books_repo = BooksBinaryFileRepository(books_file)
        clients_repo = ClientsBinaryFileRepository(clients_file)
        rentals_repo = RentalsBinaryFileRepository(books_repo, clients_repo, rentals_file)

    undo_service = UndoService()
    rentals_service = RentalsService(undo_service, repo_type, books_file if books_file else None, clients_file if clients_file else None, rentals_file if rentals_file else None)
    books_service = BooksService(undo_service, rentals_service, repo_type, books_file if books_file else None)
    clients_service = ClientsService(undo_service, rentals_service, repo_type, clients_file if clients_file else None)


    if ui == 'console':
        ui = ConsoleUi(undo_service, books_service, clients_service, rentals_service)
        ui.run()
    elif ui == 'graphic':
        root = tk.Tk()
        app = GraphicUi(root, books_service, clients_service, rentals_service)
        root.mainloop()

if __name__ == '__main__':
    main()