import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk


# variaveis de altura e largura padrao
x = 50
y = 50
height = 50
width = 250

# Create the main window
windowx = 1000
windowy = 400
root = tk.Tk()
root.title("Interface v1")
root.geometry(f"{windowx}x{windowy}")
bg = tk.Label(bg="white", bd=1, relief="solid")
bg.place(x=10 , y=10 , width=980, height=380)



# parte do nome
nome_texto = tk.Label(text="nome", bg="red", fg="black", bd=5, relief="solid")
nome_texto.place(x=x, y=y, width=width, height=height)


# input de dados com botao
inputx = x
inputy_texto = y + height + 10
input_bar = inputy_texto + 22

input_dados_text = tk.Label(text="add dados abaixo", fg="black", bg="red", bd=2, relief="solid")
input_dados = tk.Entry(text="placeholder", width=100, bd=2, relief="solid")
input_dados_text.place(x=inputx, y=inputy_texto, width=100 ,height=20)
input_dados.place(x=inputx, y=input_bar)
root.update_idletasks()

buttonX = x + input_dados.winfo_width() + 5
buttonY = input_dados_text.winfo_y() + 20
button_bar = tk.Button(text="send", command="#")
button_bar.place(x = buttonX, y = buttonY)


# seletor de datas esquerdo
dataentryH = input_bar + 50

data_text = tk.Label(text="data de emissao", fg="black", bd=2, relief="solid", bg="red")
data_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, bg="red")
data_text.place(x=50, y=dataentryH)
data_entry.place(x=50, y=dataentryH + 25)


# seletor de datas direito
dataentryH = input_bar + 50

data_text = tk.Label(text="data de vencimento", fg="black", bd=2, relief="solid", bg="red")
data_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, bg="red")
data_text.place(x=200, y=dataentryH)
data_entry.place(x=200, y=dataentryH + 25)
root.update_idletasks()

# selector of items
def on_select(event):
    selected_value = combo.get()
    #selection_label.config(text=f"Selected: {selected_value}")

# Create a Combobox widget
combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3", "Option 4"], state="readonly") 
combo.set("Select an option")  # Set the default value
combo.place(x = x, y = data_entry.winfo_y() + 40)

combo.bind("<<ComboboxSelected>>", on_select)

# window of changes
command_window = tk.Label(bg="black")
command_window.place(x = button_bar.winfo_x() + button_bar.winfo_width() + 10, y = 13, height=bg.winfo_height() - 6, width=280)

#numero da nota

#forma de pagamento

#parcelas



# Start the Tkinter event loop
root.mainloop()