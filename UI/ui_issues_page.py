import tkinter as tk
from tkinter import ttk, messagebox
from issue_return import IssueRecord, issue_book, return_book
from data_store import members, issues, library


class IssuesPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Header bar
        top = tk.Frame(self)
        top.pack(fill='x', pady=6)

        tk.Button(top, text='⬅ Dashboard',
                  command=lambda: master.show_dashboard(getattr(master, 'current_user', None))
                  ).pack(side='left', padx=5)

        tk.Label(top, text='Issue & Return', font=('Arial', 14)).pack(side='left', padx=10)

        tk.Button(top, text='Issue Book', command=self.issue_popup).pack(side='right', padx=5)

        # Treeview
        cols = ('MemberID', 'ISBN', 'Title')
        self.tree = ttk.Treeview(self, columns=cols, show='headings')
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=150)
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

        # Action buttons
        act = tk.Frame(self)
        act.pack(fill='x', padx=10, pady=5)
        tk.Button(act, text='Return Selected', command=self.return_selected).pack(side='left', padx=5)
        tk.Button(act, text='Delete Selected Record', command=self.delete_selected).pack(side='left', padx=5)

        self.refresh()

    def refresh(self):
        """Reload issue records"""
        for i in self.tree.get_children():
            self.tree.delete(i)
        for r in issues:
            self.tree.insert('', 'end', values=(r.member_id, r.isbn, r.title))

    def issue_popup(self):
        popup = tk.Toplevel(self)
        popup.title('Issue Book')
        popup.transient(self)
        popup.grab_set()

        tk.Label(popup, text='Member ID').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(popup, text='Book ISBN').grid(row=1, column=0, padx=5, pady=5)

        e_mid = ttk.Combobox(popup, values=list(members.keys()))
        e_mid.grid(row=0, column=1, padx=5, pady=5)

        e_isbn = ttk.Combobox(popup, values=list(library.books.keys()))
        e_isbn.grid(row=1, column=1, padx=5, pady=5)

        def do_issue():
            mid = e_mid.get().strip()
            isbn = e_isbn.get().strip()
            if not mid or not isbn:
                messagebox.showerror('Error', 'Select member and book')
                return
            mem = members.get(mid)
            if not mem:
                messagebox.showerror('Error', 'Member not found')
                return
            if isbn not in library.books or library.books[isbn].copies <= 0:
                messagebox.showerror('Error', 'Book not available')
                return
            ok = issue_book(library, isbn, mem)
            if ok:
                issues.append(IssueRecord(mid, isbn, library.books[isbn].title))
                popup.destroy()
                self.refresh()
                messagebox.showinfo('Issued', 'Book issued successfully')
            else:
                messagebox.showerror('Error', 'Issue failed')

        tk.Button(popup, text='Issue', command=do_issue).grid(row=2, column=0, columnspan=2, pady=8)

    def return_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning('Select', 'Please select an issued record to return')
            return
        vals = self.tree.item(sel[0])['values']
        mid, isbn = str(vals[0]), str(vals[1])
        mem = members.get(mid)
        if not mem:
            messagebox.showerror('Error', 'Member not found')
            return
        ok = return_book(library, isbn, mem)
        if ok:
            # remove first matching issue record
            for r in issues:
                if r.member_id == mid and r.isbn == isbn:
                    issues.remove(r)
                    break
            self.refresh()
            messagebox.showinfo('Returned', 'Book returned')
        else:
            messagebox.showerror('Error', 'Return failed')

    def delete_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning('Select', 'Please select a record to delete')
            return
        vals = self.tree.item(sel[0])['values']
        mid, isbn = str(vals[0]), str(vals[1])
        if messagebox.askyesno('Confirm', 'Delete this issue record?'):
            global issues
            issues = [r for r in issues if not (r.member_id == mid and r.isbn == isbn)]
            self.refresh()