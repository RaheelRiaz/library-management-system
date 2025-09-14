# ui_search_page.py
import tkinter as tk
from tkinter import ttk, messagebox
from search import search_by_title, search_by_author, search_by_isbn
from data_store import library


class SearchPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Top bar (back to dashboard)
        top = tk.Frame(self)
        top.pack(fill='x', pady=6)
        tk.Button(top, text='⬅ Dashboard',
                  command=lambda: master.show_dashboard(getattr(master, 'current_user', None))
                  ).pack(side='left', padx=5)
        tk.Label(top, text='Search Books', font=('Arial', 14)).pack(side='left', padx=10)

        # Search form
        frm = tk.Frame(self)
        frm.pack(pady=10, fill='x', padx=10)
        tk.Label(frm, text='Query').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        tk.Label(frm, text='By').grid(row=0, column=2, padx=5, pady=5, sticky='w')

        self.q = tk.Entry(frm, width=40)
        self.q.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.opt = ttk.Combobox(frm, values=['title', 'author', 'isbn'], state='readonly', width=10)
        self.opt.grid(row=0, column=3, padx=5, pady=5, sticky='w')
        self.opt.set('title')

        tk.Button(frm, text='Search', command=self.do_search, width=10).grid(row=0, column=4, padx=8)
        tk.Button(frm, text='Clear', command=self.clear_results, width=8).grid(row=0, column=5, padx=4)

        # Results Treeview
        cols = ('ISBN', 'Title', 'Author', 'Copies')
        self.tree = ttk.Treeview(self, columns=cols, show='headings', height=14)
        for c in cols:
            self.tree.heading(c, text=c)
            if c == 'Title':
                self.tree.column(c, width=350)
            else:
                self.tree.column(c, width=120)
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

        # double-click to show details
        self.tree.bind('<Double-1>', self.on_double_click)

    def do_search(self):
        q = self.q.get().strip()
        opt = self.opt.get()
        if not q:
            messagebox.showwarning('Empty query', 'Please enter a search query.')
            return

        results = []
        if opt == 'title':
            results = search_by_title(library, q)
        elif opt == 'author':
            results = search_by_author(library, q)
        elif opt == 'isbn':
            b = search_by_isbn(library, q)
            if b:
                results = [b]

        # populate tree
        for i in self.tree.get_children():
            self.tree.delete(i)

        if not results:
            messagebox.showinfo('No results', 'No books found.')
            return

        for b in results:
            self.tree.insert('', 'end', values=(b.isbn, b.title, b.author, b.copies))

    def clear_results(self):
        self.q.delete(0, 'end')
        for i in self.tree.get_children():
            self.tree.delete(i)

    def on_double_click(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        vals = self.tree.item(sel[0])['values']
        isbn = vals[0]
        book = library.books.get(isbn)
        if not book:
            messagebox.showerror('Error', 'Book not found')
            return

        # details popup
        popup = tk.Toplevel(self)
        popup.title('Book Details')
        popup.transient(self)
        popup.grab_set()
        tk.Label(popup, text=f"Title: {book.title}", anchor='w').pack(fill='x', padx=12, pady=6)
        tk.Label(popup, text=f"Author: {book.author}", anchor='w').pack(fill='x', padx=12, pady=6)
        tk.Label(popup, text=f"ISBN: {book.isbn}", anchor='w').pack(fill='x', padx=12, pady=6)
        tk.Label(popup, text=f"Copies available: {book.copies}", anchor='w').pack(fill='x', padx=12, pady=6)
        tk.Button(popup, text='Close', command=popup.destroy).pack(pady=8)