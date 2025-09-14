import tkinter as tk
from tkinter import messagebox
from auth_system import authenticate
from data_store import user_db, issues, library, members


class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # make window wider + center it
        self.master.title("Library Management System - Login")
        win_w, win_h = 900, 600   # wider size
        screen_w = self.master.winfo_screenwidth()
        screen_h = self.master.winfo_screenheight()
        x = (screen_w // 2) - (win_w // 2)
        y = (screen_h // 2) - (win_h // 2)
        self.master.geometry(f"{win_w}x{win_h}+{x}+{y}")
        self.master.resizable(True, True)

        tk.Label(self, text="Library Management System", font=("Arial", 18)).pack(pady=20)

        frm = tk.Frame(self)
        frm.pack(pady=10)

        tk.Label(frm, text="Username").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(frm, text="Password").grid(row=1, column=0, padx=5, pady=5)

        self.username = tk.Entry(frm)
        self.username.grid(row=0, column=1, padx=5, pady=5)
        self.password = tk.Entry(frm, show="*")
        self.password.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self, text="Login", command=self.do_login).pack(pady=10)

    def do_login(self):
        u = self.username.get().strip()
        p = self.password.get().strip()
        if authenticate(u, p, user_db):
            self.master.show_dashboard(u)
        else:
            messagebox.showerror("Login failed", "Invalid username or password")