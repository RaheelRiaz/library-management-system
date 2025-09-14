import tkinter as tk
from tkinter import ttk, messagebox
from book import Book
from data_store import library, issues   # directly use datastore


class BooksPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        top = tk.Frame(self)
        top.pack(fill='x', pady=6)

        # Back to dashboard
        tk.Button(top, text='⬅ Dashboard',
                  command=lambda: master.show_dashboard(getattr(master, 'current_user', None))
                  ).pack(side='left', padx=5)

        tk.Label(top, text='Books Management', font=('Arial', 14)).pack(side='left', padx=10)
        tk.Button(top, text='Add Book', command=self.add_book_popup).pack(side='right', padx=5)

        # Treeview
        cols = ('ISBN', 'Title', 'Author', 'Copies')
        self.tree = ttk.Treeview(self, columns=cols, show='headings', height=15)
        for c in cols:
            self.tree.heading(c, text=c)
            if c == 'Title':
                self.tree.column(c, width=300)
            else:
                self.tree.column(c, width=120)
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

        # Actions
        act = tk.Frame(self)
        act.pack(fill='x', padx=10, pady=5)
        tk.Button(act, text='Edit Selected', command=self.edit_selected).pack(side='left', padx=5, pady=2)
        tk.Button(act, text='Delete Selected', command=self.delete_selected).pack(side='left', padx=5, pady=2)

        self.refresh()

    def refresh(self):
        """Reload Treeview from datastore"""
        for i in self.tree.get_children():
            self.tree.delete(i)

        for b in library.list_books():
            self.tree.insert('', 'end', values=(b.isbn, b.title, b.author, b.copies))

    def add_book_popup(self):
        popup = tk.Toplevel(self); popup.title('Add Book')
        popup.transient(self); popup.grab_set()

        tk.Label(popup, text='ISBN').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(popup, text='Title').grid(row=1, column=0, padx=5, pady=5)
        tk.Label(popup, text='Author').grid(row=2, column=0, padx=5, pady=5)
        tk.Label(popup, text='Copies').grid(row=3, column=0, padx=5, pady=5)

        e_isbn = tk.Entry(popup); e_title = tk.Entry(popup)
        e_author = tk.Entry(popup); e_copies = tk.Entry(popup)

        e_isbn.grid(row=0, column=1, padx=5, pady=5)
        e_title.grid(row=1, column=1, padx=5, pady=5)
        e_author.grid(row=2, column=1, padx=5, pady=5)
        e_copies.grid(row=3, column=1, padx=5, pady=5); e_copies.insert(0, '1')

        def do_add():
            isbn = e_isbn.get().strip(); title = e_title.get().strip(); author = e_author.get().strip()
            try:
                copies = int(e_copies.get().strip())
            except Exception:
                messagebox.showerror('Error', 'Copies must be a number')
                return
            if not isbn or not title:
                messagebox.showerror('Error', 'ISBN and Title required')
                return

            library.add_book(Book(isbn, title, author, copies))
            popup.destroy(); self.refresh()

        tk.Button(popup, text='Add', command=do_add).grid(row=4, column=0, columnspan=2, pady=8)

    def edit_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning('Select', 'Please select a book to edit'); return
        vals = self.tree.item(sel[0])['values']
        isbn = str(vals[0])

        book = library.books.get(isbn)
        if not book:
            messagebox.showerror('Error', 'Book not found'); return

        popup = tk.Toplevel(self); popup.title('Edit Book')
        popup.transient(self); popup.grab_set()

        tk.Label(popup, text='ISBN').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(popup, text='Title').grid(row=1, column=0, padx=5, pady=5)
        tk.Label(popup, text='Author').grid(row=2, column=0, padx=5, pady=5)
        tk.Label(popup, text='Copies').grid(row=3, column=0, padx=5, pady=5)

        e_isbn = tk.Entry(popup); e_title = tk.Entry(popup)
        e_author = tk.Entry(popup); e_copies = tk.Entry(popup)

        e_isbn.grid(row=0, column=1, padx=5, pady=5); e_isbn.insert(0, book.isbn)
        e_title.grid(row=1, column=1, padx=5, pady=5); e_title.insert(0, book.title)
        e_author.grid(row=2, column=1, padx=5, pady=5); e_author.insert(0, book.author)
        e_copies.grid(row=3, column=1, padx=5, pady=5); e_copies.insert(0, str(book.copies))

        def do_save():
            new_isbn = e_isbn.get().strip(); new_title = e_title.get().strip(); new_author = e_author.get().strip()
            try:
                new_copies = int(e_copies.get().strip())
            except Exception:
                messagebox.showerror('Error', 'Copies must be a number'); return

            if new_isbn != book.isbn:
                library.remove_book(book.isbn)
            library.add_book(Book(new_isbn, new_title, new_author, new_copies))
            popup.destroy(); self.refresh()

        tk.Button(popup, text='Save', command=do_save).grid(row=4, column=0, columnspan=2, pady=8)

    def delete_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning('Select', 'Please select a book to delete'); return
        vals = self.tree.item(sel[0])['values']
        isbn = str(vals[0])
        if not messagebox.askyesno('Confirm', f'Delete book {isbn}?'):
            return

        library.remove_book(isbn)
        # also clear from issues
        global issues
        issues = [r for r in issues if getattr(r, 'isbn', None) != isbn]

        self.refresh()