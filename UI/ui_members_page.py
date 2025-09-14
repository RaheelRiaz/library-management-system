import tkinter as tk
from tkinter import ttk, messagebox
from member import Member
from data_store import members, issues


class MembersPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Header bar
        top = tk.Frame(self)
        top.pack(fill='x', pady=6)

        # Back to dashboard (pass current_user from master)
        tk.Button(top, text='⬅ Dashboard',
                  command=lambda: master.show_dashboard(getattr(master, 'current_user', None))
                  ).pack(side='left', padx=5)

        tk.Label(top, text='Member Management', font=('Arial', 14)).pack(side='left', padx=10)

        tk.Button(top, text='Add Member', command=self.add_member_popup).pack(side='right', padx=5)

        # Treeview
        cols = ('ID', 'Name', 'Borrowed')
        self.tree = ttk.Treeview(self, columns=cols, show='headings', height=15)
        for c in cols:
            self.tree.heading(c, text=c)
            if c == 'Name':
                self.tree.column(c, width=200)
            else:
                self.tree.column(c, width=120)
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

        # Actions
        act = tk.Frame(self)
        act.pack(fill='x', padx=10, pady=5)
        tk.Button(act, text='Edit Selected', command=self.edit_selected).pack(side='left', padx=5)
        tk.Button(act, text='Delete Selected', command=self.delete_selected).pack(side='left', padx=5)

        self.refresh()

    def refresh(self):
        """Reload member list"""
        for i in self.tree.get_children():
            self.tree.delete(i)
        for m in members.values():
            self.tree.insert('', 'end', values=(m.member_id, m.name, len(m.borrowed_books)))

    def add_member_popup(self):
        popup = tk.Toplevel(self)
        popup.title('Add Member')
        popup.transient(self)
        popup.grab_set()

        tk.Label(popup, text='Member ID').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(popup, text='Name').grid(row=1, column=0, padx=5, pady=5)

        e_id = tk.Entry(popup)
        e_name = tk.Entry(popup)
        e_id.grid(row=0, column=1, padx=5, pady=5)
        e_name.grid(row=1, column=1, padx=5, pady=5)

        def do_add():
            mid = e_id.get().strip()
            name = e_name.get().strip()
            if not mid or not name:
                messagebox.showerror('Error', 'Fields required')
                return
            if mid in members:
                messagebox.showerror('Error', 'Member ID exists')
                return
            members[mid] = Member(str(mid), name)
            popup.destroy()
            self.refresh()

        tk.Button(popup, text='Add', command=do_add).grid(row=2, column=0, columnspan=2, pady=8)

    def edit_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning('Select', 'Please select a member to edit')
            return
        vals = self.tree.item(sel[0])['values']
        mid = str(vals[0])
        mem = members.get(mid)
        if not mem:
            messagebox.showerror('Error', 'Member not found')
            return

        popup = tk.Toplevel(self)
        popup.title('Edit Member')
        popup.transient(self)
        popup.grab_set()

        tk.Label(popup, text='Member ID').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(popup, text='Name').grid(row=1, column=0, padx=5, pady=5)

        e_id = tk.Entry(popup)
        e_name = tk.Entry(popup)
        e_id.grid(row=0, column=1, padx=5, pady=5)
        e_id.insert(0, mem.member_id)
        e_id.config(state='readonly')

        e_name.grid(row=1, column=1, padx=5, pady=5)
        e_name.insert(0, mem.name)

        def do_save():
            name = e_name.get().strip()
            if not name:
                messagebox.showerror('Error', 'Name required')
                return
            mem.name = name
            popup.destroy()
            self.refresh()

        tk.Button(popup, text='Save', command=do_save).grid(row=2, column=0, columnspan=2, pady=8)

    def delete_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning('Select', 'Please select a member to delete')
            return
        vals = self.tree.item(sel[0])['values']
        mid = str(vals[0])
        if messagebox.askyesno('Confirm', 'Delete member ' + mid + '?'):
            members.pop(mid, None)
            # also remove issue records
            global issues
            issues = [r for r in issues if r.member_id != mid]
            self.refresh()