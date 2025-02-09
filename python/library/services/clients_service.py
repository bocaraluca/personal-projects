from src.exceptions.not_found import ClientNotFoundException
from src.repository.memory_repository import ClientsMemoryRepository
from src.repository.text_file_repository import ClientsTextFileRepository
from src.repository.binary_file_repository import ClientsBinaryFileRepository
from src.services.undo_service import UndoService, FunctionCall, Operation, CascadedOperation


class ClientsService:
    def __init__(self, undo_service, rentals_service, repo_type, file_path=None):
        self._undo_service = undo_service
        self._rentals_service = rentals_service
        if repo_type == 'in-memory':
            self._clients_repo = ClientsMemoryRepository()
        elif repo_type == 'text-file':
            if file_path is None:
                raise FileNotFoundError('No file path provided!')
            self._clients_repo = ClientsTextFileRepository(file_path)
        elif repo_type == 'binary-file':
            if file_path is None:
                raise FileNotFoundError('No file path provided!')
            self._clients_repo = ClientsBinaryFileRepository(file_path)
        else:
            raise ValueError('Invalid repository type! Repository type should be in-memory, text-file or binary-file.')

    def add_client(self, client_id, name):
        self._clients_repo.add_client(client_id, name)
        undo = FunctionCall(self._clients_repo.remove_client, client_id)
        redo = FunctionCall(self._clients_repo.add_client, client_id, name)
        operation = Operation(undo, redo)
        self._undo_service.record_operation(operation)

    def remove_client(self, client_id):
        client = self.find_client_by_id(client_id)
        if client is None:
            raise ClientNotFoundException

        rentals_to_remove = [rental for rental in self._rentals_service.list_rentals() if rental.client_id == client_id]

        undo_remove_client = FunctionCall(self._clients_repo.add_client, client_id, client.name)
        redo_remove_client = FunctionCall(self._clients_repo.remove_client, client_id)

        cascaded_op = CascadedOperation()
        cascaded_op.add_undo_function(undo_remove_client)
        cascaded_op.add_redo_function(redo_remove_client)

        for rental in rentals_to_remove:
            undo_remove_rental = FunctionCall(self._rentals_service.rent_book, rental.rental_id, rental.book_id, rental.client_id, rental.rented_date)
            redo_remove_rental = FunctionCall(self._rentals_service.remove_rental, rental.rental_id)
            cascaded_op.add_undo_function(undo_remove_rental)
            cascaded_op.add_redo_function(redo_remove_rental)

        self._clients_repo.remove_client(client_id)
        for rental in rentals_to_remove:
            self._rentals_service.remove_rental(rental.rental_id)

        self._undo_service.record_operation(cascaded_op)

    def update_client(self, client_id, new_name):
        client = self.find_client_by_id(client_id)
        old_name = client.name
        if client:
            self._clients_repo.update_client(client_id, new_name)
            undo = FunctionCall(self._clients_repo.update_client, client_id, old_name)
            redo = FunctionCall(self._clients_repo.update_client, client_id, new_name)
            operation = Operation(undo, redo)
            self._undo_service.record_operation(operation)

    def list_clients(self):
        clients = self._clients_repo.list_clients()
        sorted_clients = sorted(clients, key=lambda client: client.client_id)
        return sorted_clients

    def find_client_by_id(self, client_id):
        for client in self._clients_repo.list_clients():
            if client.client_id == client_id:
                return client
        return None

    def find_clients_by_name(self, name):
        return [client for client in self._clients_repo.list_clients() if name.lower() in client.name.lower()]