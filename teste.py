import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Menu Example")
        self.root.geometry("600x400")
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        self.menubar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)

        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        self.root.config(menu=self.menubar)

    def create_widgets(self):
        # Create a Treeview widget
        self.tree = ttk.Treeview(self.root, columns=('Column1', 'Column2'), show='headings')
        self.tree.heading('Column1', text='Column 1')
        self.tree.heading('Column2', text='Column 2')
        self.tree.pack(expand=True, fill='both')

        # Create a Text widget
        self.text_widget = tk.Text(self.root, height=5)
        self.text_widget.pack(expand=True, fill='both')

        # Create a Listbox widget
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(expand=True, fill='both')

    def new_file(self):
        data = "New File created!"
        self.show_data_in_text_widget(data)

    def open_file(self):
        data_list = ["Item 1", "Item 2", "Item 3"]
        self.show_data_in_listbox(data_list)

    def save_file(self):
        data_table = [(1, 'Row 1'), (2, 'Row 2'), (3, 'Row 3')]
        self.show_data_in_treeview(data_table)

    def undo(self):
        messagebox.showinfo("Undo", "Undo action!")

    def redo(self):
        messagebox.showinfo("Redo", "Redo action!")

    def cut(self):
        messagebox.showinfo("Cut", "Cut action!")

    def copy(self):
        messagebox.showinfo("Copy", "Copy action!")

    def paste(self):
        messagebox.showinfo("Paste", "Paste action!")

    def about(self):
        messagebox.showinfo("About", "This is a Tkinter menu example!")

    def show_data_in_label(self, data):
        self.data_label.config(text=data)

    def show_data_in_text_widget(self, data):
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, data)

    def show_data_in_listbox(self, data_list):
        self.listbox.delete(0, tk.END)
        for item in data_list:
            self.listbox.insert(tk.END, item)

    def show_data_in_treeview(self, data):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in data:
            self.tree.insert('', 'end', values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
