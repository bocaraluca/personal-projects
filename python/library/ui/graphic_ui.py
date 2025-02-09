import tkinter as tk
from tkinter import messagebox

from src.exceptions.duplicate_id import DuplicateClientIdException, DuplicateRentalIdException, DuplicateBookIdException
from src.exceptions.not_found import ClientNotFoundException, RentalNotFoundException, BookNotFoundException
from datetime import datetime


class GraphicUi:
    def __init__(self, root, books_service, clients_service, rentals_service):
        self.root = root
        self._books_service = books_service
        self._clients_service = clients_service
        self._rentals_service = rentals_service

        self.root.title("Library Management System")
        self.root.geometry("400x300")
        self.center_window(self.root, 400, 300)
        self.main_frame = tk.Frame(self.root, width=400, height=300)
        self.main_frame.pack(pady=20)

        self.create_main_menu()

    def center_window(self, window, width, height):
        """Center the window on the screen."""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calculate position for the window to be in the center
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set the position of the window
        window.geometry(f"{width}x{height}+{x}+{y}")

    def create_main_menu(self):
        tk.Button(self.main_frame, text="Manage Books", command=self.manage_books).pack(pady=5)
        tk.Button(self.main_frame, text="Manage Clients", command=self.manage_clients).pack(pady=5)
        tk.Button(self.main_frame, text="Manage Rentals", command=self.manage_rentals).pack(pady=5)
        tk.Button(self.main_frame, text="Find Books/Clients", command=self.search_books_clients).pack(pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit).pack(pady=5)

    def manage_books(self):
        # Hide the main window
        self.root.withdraw()

        # Create a new window for managing books
        books_window = tk.Toplevel(self.root)
        books_window.title("Manage Books")
        self.center_window(books_window, 600, 400)  # Center the books window

        actions_frame = tk.Frame(books_window)
        actions_frame.pack(pady=10)

        books_listbox = tk.Listbox(books_window, width=80, height=15)
        books_listbox.pack(pady=10)

        def refresh_books_listbox():
            books_listbox.delete(0, tk.END)
            try:
                for book in self._books_service.list_books():
                    books_listbox.insert(tk.END, f"{book.book_id} - {book.title} by {book.author}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        refresh_books_listbox()

        def add_book():
            def save_book():
                try:
                    book_id = int(book_id_entry.get())
                    title = title_entry.get()
                    author = author_entry.get()
                    if not title or not author:  # Check for empty title or author
                        messagebox.showerror("Error", "Fields cannot be empty!")
                        return
                    self._books_service.add_book(book_id, title, author)
                    refresh_books_listbox()
                    add_window.destroy()
                except DuplicateBookIdException as e:
                    messagebox.showerror("Error", str(e))
                except ValueError:
                    messagebox.showerror("Error", "Invalid book id!")

            add_window = tk.Toplevel(books_window)
            add_window.title("Add Book")
            self.center_window(add_window, 300, 200)

            add_frame = tk.Frame(add_window)
            add_frame.pack(expand=True)

            tk.Label(add_frame, text="Book ID:").grid(row=0, column=0, pady=5)
            book_id_entry = tk.Entry(add_frame)
            book_id_entry.grid(row=0, column=1, pady=5)
            tk.Label(add_frame, text="Title:").grid(row=1, column=0, pady=5)
            title_entry = tk.Entry(add_frame)
            title_entry.grid(row=1, column=1, pady=5)
            tk.Label(add_frame, text="Author:").grid(row=2, column=0, pady=5)
            author_entry = tk.Entry(add_frame)
            author_entry.grid(row=2, column=1, pady=5)
            tk.Button(add_frame, text="Save", command=save_book).grid(row=3, columnspan=2, pady=10)

        def remove_book():
            def delete_book():
                try:
                    book_id = int(book_id_entry.get())
                    self._books_service.remove_book(book_id)
                    refresh_books_listbox()
                    remove_window.destroy()
                except BookNotFoundException as e:
                    messagebox.showerror("Error", str(e))
                except ValueError:
                    messagebox.showerror("Error", "Invalid book id!")

            remove_window = tk.Toplevel(books_window)
            remove_window.title("Remove Book")
            self.center_window(remove_window, 300, 200)

            remove_frame = tk.Frame(remove_window)
            remove_frame.pack(expand=True)  # Expand to center content in the window

            tk.Label(remove_frame, text="Book ID:").grid(row=0, column=0, pady=5)
            book_id_entry = tk.Entry(remove_frame)
            book_id_entry.grid(row=0, column=1, pady=5)
            tk.Button(remove_frame, text="Delete", command=delete_book).grid(row=1, columnspan=2, pady=10)

        def update_book():
            def save_book():
                try:
                    book_id = int(book_id_entry.get())
                    title = title_entry.get()
                    author = author_entry.get()
                    if not title or not author:  # Check for empty fields
                        messagebox.showerror("Error", "Fields cannot be empty!")
                        return
                    self._books_service.update_book(book_id, title, author)
                    refresh_books_listbox()
                    update_window.destroy()
                except BookNotFoundException as e:
                    messagebox.showerror("Error", str(e))
                except ValueError:
                    messagebox.showerror("Error", "Invalid book id!")

            update_window = tk.Toplevel(books_window)
            update_window.title("Update Book")
            self.center_window(update_window, 300, 200)

            update_frame = tk.Frame(update_window)
            update_frame.pack(expand=True)  # Expand to center content in the window

            tk.Label(update_frame, text="Book ID:").grid(row=0, column=0, pady=5)
            book_id_entry = tk.Entry(update_frame)
            book_id_entry.grid(row=0, column=1, pady=5)
            tk.Label(update_frame, text="Title:").grid(row=1, column=0, pady=5)
            title_entry = tk.Entry(update_frame)
            title_entry.grid(row=1, column=1, pady=5)
            tk.Label(update_frame, text="Author:").grid(row=2, column=0, pady=5)
            author_entry = tk.Entry(update_frame)
            author_entry.grid(row=2, column=1, pady=5)
            tk.Button(update_frame, text="Save", command=save_book).grid(row=3, columnspan=2, pady=10)

        def go_back():
            books_window.destroy()
            self.root.deiconify()  # Show the main window again

        tk.Button(actions_frame, text="Add Book", command=add_book).pack(side=tk.LEFT, padx=5)
        tk.Button(actions_frame, text="Update Book", command=update_book).pack(side=tk.LEFT, padx=5)
        tk.Button(actions_frame, text="Remove Book", command=remove_book).pack(side=tk.LEFT, padx=5)
        tk.Button(actions_frame, text="Back", command=go_back).pack(side=tk.LEFT, padx=5)


    def manage_clients(self):
        self.root.withdraw()

        clients_window = tk.Toplevel(self.root)
        clients_window.title("Manage Clients")
        self.center_window(clients_window, 600, 400)  # Center the clients window

        actions_frame = tk.Frame(clients_window)
        actions_frame.pack(pady=10)

        clients_listbox = tk.Listbox(clients_window, width=80, height=15)
        clients_listbox.pack(pady=10)

        def refresh_clients_listbox():
            clients_listbox.delete(0, tk.END)
            try:
                for client in self._clients_service.list_clients():
                    clients_listbox.insert(tk.END, f"{client.client_id} - {client.name}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        refresh_clients_listbox()

        def add_client():
            def save_client():
                try:
                    client_id = int(client_id_entry.get())
                    name = name_entry.get()
                    if client_id == "" or name == "":
                        messagebox.showerror("Error", "Fields cannot be empty!")
                        return
                    self._clients_service.add_client(client_id, name)
                    refresh_clients_listbox()
                    add_window.destroy()
                except DuplicateClientIdException as e:
                    messagebox.showerror("Error", str(e))
                except ValueError:
                    messagebox.showerror("Error", "Invalid client id!")

            add_window = tk.Toplevel(clients_window)
            add_window.title("Add Client")
            self.center_window(add_window, 300, 200)

            add_frame = tk.Frame(add_window)
            add_frame.pack(expand=True)  # Expand to center content in the window

            tk.Label(add_frame, text="Client ID:").grid(row=0, column=0, pady=5)
            client_id_entry = tk.Entry(add_frame)
            client_id_entry.grid(row=0, column=1, pady=5)
            tk.Label(add_frame, text="Name:").grid(row=1, column=0, pady=5)
            name_entry = tk.Entry(add_frame)
            name_entry.grid(row=1, column=1, pady=5)
            tk.Button(add_frame, text="Save", command=save_client).grid(row=2, columnspan=2, pady=10)

        def remove_client():
            def delete_client():
                try:
                    client_id = int(client_id_entry.get())
                    if client_id == "":
                        messagebox.showerror("Error", "Client id cannot be empty!")
                        return
                    self._clients_service.remove_client(client_id)
                    refresh_clients_listbox()
                    remove_window.destroy()
                except ClientNotFoundException as e:
                    messagebox.showerror("Error", str(e))
                except ValueError:
                    messagebox.showerror("Error", "Invalid client id!")

            remove_window = tk.Toplevel(clients_window)
            remove_window.title("Remove Client")
            self.center_window(remove_window, 300, 200)  # Center the remove client window

            remove_frame = tk.Frame(remove_window)
            remove_frame.pack(expand=True)  # Expand to center content in the window

            tk.Label(remove_frame, text="Client ID:").grid(row=0, column=0, pady=5)
            client_id_entry = tk.Entry(remove_frame)
            client_id_entry.grid(row=0, column=1, pady=5)
            tk.Button(remove_frame, text="Delete", command=delete_client).grid(row=1, columnspan=2, pady=10)

        def update_client():
            def save_client():
                try:
                    client_id = int(client_id_entry.get())
                    name = name_entry.get()
                    if client_id == "" or name == "":
                        messagebox.showerror("Error", "Fields cannot be empty!")
                        return
                    self._clients_service.update_client(client_id, name)
                    refresh_clients_listbox()
                    update_window.destroy()
                except ClientNotFoundException as e:
                    messagebox.showerror("Error", str(e))
                except ValueError:
                    messagebox.showerror("Error", "Invalid client id!")

            update_window = tk.Toplevel(clients_window)
            update_window.title("Update Client")
            self.center_window(update_window, 300, 200)

            update_frame = tk.Frame(update_window)
            update_frame.pack(expand=True)

            tk.Label(update_frame, text="Client ID:").grid(row=0, column=0, pady=5)
            client_id_entry = tk.Entry(update_frame)
            client_id_entry.grid(row=0, column=1, pady=5)
            tk.Label(update_frame, text="Name:").grid(row=1, column=0, pady=5)
            name_entry = tk.Entry(update_frame)
            name_entry.grid(row=1, column=1, pady=5)
            tk.Button(update_frame, text="Save", command=save_client).grid(row=2, columnspan=2, pady=10)

        def go_back():
            clients_window.destroy()
            self.root.deiconify()  # Show the main window again

        button_frame = tk.Frame(clients_window)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Client", command=add_client).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update Client", command=update_client).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remove Client", command=remove_client).pack(side=tk.LEFT, padx=5)

        tk.Button(clients_window, text="Back", command=go_back).pack(pady=10)

    def manage_rentals(self):
        self.root.withdraw()

        rentals_window = tk.Toplevel(self.root)
        rentals_window.title("Manage rentals")
        self.center_window(rentals_window, 600, 400)

        rentals_frame = tk.Frame(rentals_window)
        rentals_frame.pack(pady=10)

        rentals_listbox = tk.Listbox(rentals_window, width=80, height=15)
        rentals_listbox.pack(pady=10)

        def refresh_rentals_listbox():
            rentals_listbox.delete(0, tk.END)
            try:
                for rental in self._rentals_service.list_rentals():
                    rentals_listbox.insert(tk.END, f"{rental.rental_id} - Book id: {rental.book_id} - Client id: {rental.client_id} - Rented date: {rental.rented_date} - Return date: {rental.returned_date}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        refresh_rentals_listbox()

        def rent_book():
            def save_rental():
                try:
                    rental_id = int(rental_id_entry.get())
                    book_id = int(book_id_entry.get())
                    client_id = int(client_id_entry.get())
                    try:
                        rented_date = datetime.strptime(rented_date_entry.get(), '%Y-%m-%d')
                        if rental_id == "" or book_id == "" or client_id == "":
                            messagebox.showerror("Error", "Fields cannot be empty!")
                            return
                        self._rentals_service.rent_book(rental_id, book_id, client_id, rented_date)
                        refresh_rentals_listbox()
                        rent_window.destroy()
                    except ValueError:
                        messagebox.showerror("Error", "Invalid date format!")
                except DuplicateRentalIdException as e:
                    messagebox.showerror("Error", str(e))
                except BookNotFoundException as e:
                    messagebox.showerror("Error", str(e))
                except ClientNotFoundException as e:
                    messagebox.showerror("Error", str(e))
                except ValueError:
                    messagebox.showerror("Error", "Invalid rental id, book id or client id!")

            rent_window = tk.Toplevel(rentals_window)
            rent_window.title("Rent book")
            self.center_window(rent_window, 300, 250)

            rent_frame = tk.Frame(rent_window)
            rent_frame.pack(expand=True)

            tk.Label(rent_frame, text="Rental ID:").grid(row=0, column=0, pady=5)
            rental_id_entry = tk.Entry(rent_frame)
            rental_id_entry.grid(row=0, column=1, pady=5)

            tk.Label(rent_frame, text="Book ID:").grid(row=1, column=0, pady=5)
            book_id_entry = tk.Entry(rent_frame)
            book_id_entry.grid(row=1, column=1, pady=5)

            tk.Label(rent_frame, text="Client ID:").grid(row=2, column=0, pady=5)
            client_id_entry = tk.Entry(rent_frame)
            client_id_entry.grid(row=2, column=1, pady=5)

            tk.Label(rent_frame, text="Rental Date (YYYY-MM-DD):").grid(row=3, column=0, pady=5)
            rented_date_entry = tk.Entry(rent_frame)
            rented_date_entry.grid(row=3, column=1, pady=5)

            tk.Button(rent_frame, text="Save", command=save_rental).grid(row=4, columnspan=2, pady=10)

        def return_book():
            def return_rental():
                try:
                    rental_id = int(rental_id_entry.get())
                    return_date = datetime.strptime(return_date_entry.get(), '%Y-%m-%d')
                    if rental_id == "":
                        messagebox.showerror("Error", "Rental id cannot be empty!")
                        return
                    self._rentals_service.return_book(rental_id, return_date)
                    refresh_rentals_listbox()
                    return_window.destroy()
                except RentalNotFoundException as e:
                    messagebox.showerror("Error", str(e))
                except ValueError:
                    messagebox.showerror("Error", "Invalid rental id or date format!")

            return_window = tk.Toplevel(rentals_window)
            return_window.title("Return Book")
            self.center_window(return_window, 300, 200)

            return_frame = tk.Frame(return_window)
            return_frame.pack(expand=True)

            tk.Label(return_frame, text="Rental ID:").grid(row=0, column=0, pady=5)
            rental_id_entry = tk.Entry(return_frame)
            rental_id_entry.grid(row=0, column=1, pady=5)

            tk.Label(return_frame, text="Return Date (YYYY-MM-DD):").grid(row=1, column=0, pady=5)
            return_date_entry = tk.Entry(return_frame)
            return_date_entry.grid(row=1, column=1, pady=5)

            tk.Button(return_frame, text="Return", command=return_rental).grid(row=2, columnspan=2, pady=10)

        def go_back():
            rentals_window.destroy()
            self.root.deiconify()

        button_frame = tk.Frame(rentals_window)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Rent Book", command=rent_book).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Return Book", command=return_book).pack(side=tk.LEFT, padx=5)

        tk.Button(rentals_window, text="Back", command=go_back).pack(pady=10)

    def search_books_clients(self):
        self.root.withdraw()

        search_window = tk.Toplevel(self.root)
        search_window.title("Search Books and Clients")
        self.center_window(search_window, 600, 400)

        # Frame for displaying search options
        search_frame = tk.Frame(search_window)
        search_frame.pack(pady=10)

        search_option_var = tk.StringVar(value="B")  # Default to searching books
        tk.Radiobutton(search_frame, text="Search Books", variable=search_option_var, value="B").pack(anchor=tk.W)
        tk.Radiobutton(search_frame, text="Search Clients", variable=search_option_var, value="C").pack(anchor=tk.W)

        tk.Label(search_frame, text="Search Criteria:").pack(pady=5)
        search_criteria_entry = tk.Entry(search_frame, width=40)
        search_criteria_entry.pack(pady=5)

        results_listbox = tk.Listbox(search_window, width=80, height=10)
        results_listbox.pack(pady=10)

        def refresh_search_results():
            results_listbox.delete(0, tk.END)
            criteria = search_criteria_entry.get()

            try:
                if search_option_var.get() == "B":  # Search Books
                    try:
                        criteria = int(criteria)
                        books = [self._books_service.find_book_by_id(criteria)]
                    except ValueError:
                        books_dupl = self._books_service.find_books_by_title(criteria)
                        books_dupl.extend(self._books_service.find_books_by_author(criteria))
                        books = list(dict.fromkeys(books_dupl))  # Remove duplicates

                    if not books:
                        results_listbox.insert(tk.END, "No books found with the given criteria!")
                    else:
                        for book in books:
                            results_listbox.insert(tk.END, f"{book.book_id} - {book.title} by {book.author}")

                elif search_option_var.get() == "C":  # Search Clients
                    try:
                        criteria = int(criteria)
                        clients = [self._clients_service.find_client_by_id(criteria)]
                    except ValueError:
                        clients = self._clients_service.find_clients_by_name(criteria)

                    if not clients:
                        results_listbox.insert(tk.END, "No clients found with the given criteria!")
                    else:
                        for client in clients:
                            results_listbox.insert(tk.END, f"{client.client_id} - {client.name}")

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(search_window, text="Search", command=refresh_search_results).pack(pady=10)

        def go_back():
            search_window.destroy()
            self.root.deiconify()

        tk.Button(search_window, text="Back", command=go_back).pack(pady=10)
