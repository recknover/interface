import tkinter as tk
from tkcalendar import DateEntry


# variaveis de altura e largura padrao
x = 50
y = 50
height = 50
width = 250

# Create the main window
root = tk.Tk()
root.title("Interface v1")
root.geometry("1000x400")


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

# selector of items



# Start the Tkinter event loop
root.mainloop()