import tkinter as tk
from UI.ui_books_page import BooksPage
from UI.ui_members_page import MembersPage
from UI.ui_issues_page import IssuesPage
from UI.ui_search_page import SearchPage
from data_store import user_db, issues, library, members

class Dashboard(tk.Frame):
    def __init__(self, master, username="User"):
        super().__init__(master)

        # Title
        tk.Label(self, text="📊 Library Dashboard", font=("Arial", 18, "bold")).pack(pady=20)

        # Welcome message
        tk.Label(self, text=f"Welcome, {username}!", font=("Arial", 14), fg="green").pack(pady=5)

        # Options heading
        tk.Label(self, text="Choose an option:", font=("Arial", 14)).pack(pady=15)

        # Main menu buttons
        tk.Button(
            self, text="📚 Books Management", width=30,
            command=lambda: master.show_page(BooksPage)
        ).pack(pady=5)

        tk.Button(
            self, text="👥 Members Management", width=30,
            command=lambda: master.show_page(MembersPage)
        ).pack(pady=5)

        tk.Button(
            self, text="📖 Issue & Return Records", width=30,
            command=lambda: master.show_page(IssuesPage)
        ).pack(pady=5)

        tk.Button(
            self, text="🔍 Search Books", width=30,
            command=lambda: master.show_page(SearchPage)
        ).pack(pady=5)

        # Logout button at bottom
        tk.Button(
            self, text="Logout", width=20, fg="black", bg="red",
            command=master.logout
        ).pack(side="bottom", pady=30)