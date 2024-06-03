import tkinter as tk

def show_checked_status():
    status = []
    for var, text in zip(checkbox_vars, checkbox_texts):
        status.append(f"{text}: {'checked' if var.get() else 'unchecked'}")
    status_label.config(text="\n".join(status))

# Create the main window
root = tk.Tk()
root.title("Multiple Checkboxes Example")
root.geometry("300x300")

# Create a list to hold the BooleanVars and checkbox texts
checkbox_vars = []
checkbox_texts = ["Option 1", "Option 2", "Option 3"]

# Create multiple Checkbutton widgets
for text in checkbox_texts:
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(root, text=text, variable=var, command=show_checked_status)
    checkbox.pack(anchor=tk.W, padx=20, pady=5)
    checkbox_vars.append(var)

# Create a label to show the status of the checkboxes
status_label = tk.Label(root, text="")
status_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
