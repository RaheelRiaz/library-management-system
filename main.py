import tkinter as tk
from book import Book
from member import Member
from UI.ui_login_page import LoginPage
from UI.ui_dashboard_page import Dashboard
from data_store import issues, library, members

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("600x500")

        self.current_user = None
        self.current_page = None

        self.show_login()

    def show_login(self):
        """Show login screen"""
        if self.current_page:
            self.current_page.destroy()
        self.current_page = LoginPage(self)
        self.current_page.pack(fill="both", expand=True)

    def show_dashboard(self, username):
        """Show dashboard after login"""
        if self.current_page:
            self.current_page.destroy()
        self.current_user = username
        self.current_page = Dashboard(self, username=username)
        self.current_page.pack(fill="both", expand=True)

    def show_page(self, PageClass):
        """Navigate to another page (Books, Members, Issues, Search)"""
        if self.current_page:
            self.current_page.destroy()
        self.current_page = PageClass(self)
        self.current_page.pack(fill="both", expand=True)

    def logout(self):
        """Logout and return to login screen"""
        self.current_user = None
        self.show_login()


if __name__ == "__main__":
    app = App()
    app.mainloop()