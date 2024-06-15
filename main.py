import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk


#leitor de listas
def leitor(arquivo):
    arquivo = open(f"{arquivo}", "r")
    items = []
    for i in arquivo:
        items.append(i)
    return items
items = leitor("items.txt")


# variaveis de altura e largura padrao
x = 50 #50
y = 50 #50
height = 50 #50
width = 250 #250
 

# Create the main window
windowx = 1000
windowy = 400
root = tk.Tk()
root.title("Interface v1")
root.geometry(f"{windowx}x{windowy}")
bg = tk.Label(bg="white", bd=1, relief="solid")
bg.place(x=10 , y=10 , width=980, height=380)


# parte do nome
nome_texto = tk.Label(text="nome", bg="lightgray", fg="black", bd=5, relief="solid")
nome_texto.place(x=x, y=y, width=width, height=height)


# input de dados com botao
inputx = x
inputy_texto = y + height + 10
input_bar = inputy_texto + 22

input_dados_text = tk.Label(text="add dados abaixo", fg="black", bg="lightgray", bd=2, relief="solid")
input_dados = tk.Entry(text="placeholder", width=100, bd=2, relief="solid")
input_dados_text.place(x=inputx, y=inputy_texto, width=100 ,height=20)
input_dados.place(x=inputx, y=input_bar)
root.update_idletasks()

buttonX = x + input_dados.winfo_width() + 5
buttonY = input_dados_text.winfo_y() + 20
button_bar = ttk.Button(text="send", command="#")
button_bar.place(x = buttonX, y = buttonY)


# seletor de datas esquerdo
dataentryH = input_bar + 50

data_textE = tk.Label(text="data de emissao", fg="black", bd=2, relief="solid", bg="lightgray")
data_entryE = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, bg="red")
data_textE.place(x=50, y=dataentryH)
root.update_idletasks()
data_entryE.place(x=50, y=dataentryH + 25, width=data_textE.winfo_width())
root.update_idletasks()


# seletor de datas direito
dataentryH = input_bar + 50

data_textD = tk.Label(text="data de vencimento", fg="black", bd=2, relief="solid", bg="lightgray")
data_entryD = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, bg="red")
data_textD.place(x=200, y=dataentryH)
root.update_idletasks()
data_entryD.place(x=200, y=dataentryH + 25, width=data_textD.winfo_width())
root.update_idletasks()


# selector of items
def on_select(event):
    selected_value = combo.get()
    #selection_label.config(text=f"Selected: {selected_value}")


# Create a Combobox widget com nome
texto_seletor = tk.Label(text="seletor", fg="black", bd=2, relief="solid", bg="lightgray")
texto_seletor.place(x=x, y=data_entryE.winfo_y() + 40, width=data_entryE.winfo_width() + 10)
root.update_idletasks()

combo = ttk.Combobox(root, values=items, state="readonly") 
combo.set("Selecione")  # Set the default value
combo.place(x = x, y = texto_seletor.winfo_y() + 23, width=data_entryE.winfo_width() + 10)
root.update_idletasks()
combo.bind("<<ComboboxSelected>>", on_select)
root.update_idletasks()


# window of changes
command_window = tk.Label(bg="black")
command_window.place(x = button_bar.winfo_x() + button_bar.winfo_width() + 10, y = 13, height=bg.winfo_height() - 6, width=240)


#numero da nota
nf_entry_text = tk.Label(text="numero NF", fg="black", bd=2, relief="solid", bg="lightgray")
nf_entry = tk.Entry(width=17, bd=2, relief="solid")
nf_entry.place(x=data_entryD.winfo_x(), y=texto_seletor.winfo_y() + 23)
root.update_idletasks()
nf_entry_text.place(x=data_entryD.winfo_x(), y = texto_seletor.winfo_y(), width=nf_entry.winfo_width())


#forma de pagamento
payment_label = tk.Label(text="forma de pagamento", fg="black", bd=2, relief="solid", bg="lightgray")
payment_label.place(x=x, y=combo.winfo_y() + 40, width=120)
root.update_idletasks()
payments = [1, 2, 3 ,4 ]
payment_selector = ttk.Combobox(root, values=payments, state="readonly")
payment_selector.set("selecione")
payment_selector.place(x=x, y=payment_label.winfo_y()+23, width=120)


#parcelas
parcelas_text = tk.Label(text="parcelas", fg="black", bg="lightgray", bd=2, relief="solid")
parcelas_text.place(x=nf_entry.winfo_x(), y=payment_label.winfo_y(), width=108)
'''
selecionar quantidade de parcelas, e frequencia 7/14/21/28
valores predefinidos
cada valor é uma funcao, dependendo da funcao ela copia os outros valores e adiciona ao banco de dados
se nf tem 3 parcelas padrao 7/14/21 selecionar "padrao 3x" copiar: nome, valor da parcela, numero da nota, forma de pagamento
pegar a data de emissao, e acrescendar os dias das parcelas de acordo com o modelo
1x 7d
1x 14d
1x 21d
1x 28d
2x 7/14d
2x 14/21d
2x 21/28d
2x 7/21d
3x 7/14/21d
4x 7/14/21/28d



'''
# Start the Tkinter event loop
root.mainloop()
