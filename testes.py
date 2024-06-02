import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Foldable Item Selector Example")
root.geometry("400x300")

# Create a Treeview widget
tree = ttk.Treeview(root)

# Define columns (optional, can be used to create a multi-column treeview)
tree["columns"] = ("Description")

# Format columns
tree.column("#0", width=150, minwidth=150)
tree.column("Description", width=200, minwidth=200)

# Create column headings
tree.heading("#0", text="Item", anchor=tk.W)
tree.heading("Description", text="Description", anchor=tk.W)

# Insert parent items
parent1 = tree.insert("", "end", text="Parent 1", values=("Description of Parent 1"), open=True)
parent2 = tree.insert("", "end", text="Parent 2", values=("Description of Parent 2"), open=True)

# Insert child items under Parent 1
tree.insert(parent1, "end", text="Child 1.1", values=("Description of Child 1.1"))
tree.insert(parent1, "end", text="Child 1.2", values=("Description of Child 1.2"))

# Insert child items under Parent 2
tree.insert(parent2, "end", text="Child 2.1", values=("Description of Child 2.1"))
tree.insert(parent2, "end", text="Child 2.2", values=("Description of Child 2.2"))

# Pack the Treeview widget
tree.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Function to get selected item
def show_selection():
    selected_item = tree.selection()[0]  # Get selected item
    item_text = tree.item(selected_item, "text")
    item_description = tree.item(selected_item, "values")[0]
    label.config(text=f"Selected Item: {item_text}\nDescription: {item_description}")

# Create a button to show the selected item
button = tk.Button(root, text="Show Selection", command=show_selection)
button.pack(pady=10)

# Create a label to display the selected item
label = tk.Label(root, text="Selected Item:")
label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
