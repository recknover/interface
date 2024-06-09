import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("tk vs ttk")
root.geometry("300x200")

# Create a traditional tk.Button
tk_button = tk.Button(root, text="Tk Button", bg="lightblue")
tk_button.pack(pady=10)

# Create a themed ttk.Button
ttk_button = ttk.Button(root, text="Ttk Button")
ttk_button.pack(pady=10)

style = ttk.Style()
style.configure("TButton", foreground="white", background="blue", font=("Arial", 12))

# Apply the style to ttk.Button
ttk_button = ttk.Button(root, text="Styled Ttk Button", style="TButton")
ttk_button.pack(pady=10)


# Start the Tkinter event loop
root.mainloop()

