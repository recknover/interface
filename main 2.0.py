import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
import conection

#leitor de listas
def leitor(arquivo):
    arquivo = open(f"{arquivo}", "r")
    items = []
    for i in arquivo:
        items.append(i)
    return items

class app:
    def __init__(self, root):
        #listas
        self.payments = [1, 2, 3 ,4 ]
        self.items = leitor("items.txt")
        self.parcelas = ["1x 7d", "1x 14d", "1x 21d", "2x 14/21d", "2x 14/21d", "3x 7/14/21d"]
       
        # Create the main window
        self.windowx = 1000
        self.windowy = 400
        self.configureWindow(root)
        

        # Default dimensions
        self.x = 50
        self.y = 50
        self.height = 50
        self.width = 250
        
        #inicialize the widgets
        self.createWidgets(root)
        self.placeWidgets()

    def configureWindow(self, root):
        root.title("Interface v1")
        root.geometry(f"{self.windowx}x{self.windowy}")
        root.resizable(False, False)

    #list of widgets to create
    def createWidgets(self, root):
        #labels
        self.menu = tk.Label(text="nome", bg="lightgray", fg="black", bd=3, relief="solid")
        self.input_dados_text = tk.Label(text="add dados abaixo", fg="black", bg="lightgray", bd=2, relief="solid")
        self.data_textD = tk.Label(text="data de vencimento", fg="black", bd=2, relief="solid", bg="lightgray")
        self.data_textE = tk.Label(text="data de emissao", fg="black", bd=2, relief="solid", bg="lightgray")
        self.texto_seletor = tk.Label(text="seletor", fg="black", bd=2, relief="solid", bg="lightgray")
        self.nf_entry_text = tk.Label(text="numero NF", fg="black", bd=2, relief="solid", bg="lightgray")
        self.payment_label = tk.Label(text="forma de pagamento", fg="black", bd=2, relief="solid", bg="lightgray")
        self.parcelas_text = tk.Label(text="parcelas", fg="black", bg="lightgray", bd=2, relief="solid")
        self.command_window = tk.Label(bg="black")
        self.command_text = tk.Label(text="Loading", bg="black", fg="green")
        self.texto_combo = tk.Label(text="seletor", fg="black", bd=2, relief="solid", bg="lightgray")
        #entrys
        self.input_dados = tk.Entry(text="placeholder", width=100, bd=2, relief="solid")
        self.nf_entry = tk.Entry(width=19, bd=2, relief="solid",)
        #buttons
        self.button_send = ttk.Button(text="send", command="#")
        #entry dates
        self.data_entryE = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, bg="red")
        self.data_entryD = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, bg="red")
        #comboboxes
        self.combo = ttk.Combobox(root, values=self.items, state="readonly") 
        self.parcelas_combobox = ttk.Combobox(root, values=self.parcelas, state="readonly")
        self.payment_selector = ttk.Combobox(root, values=self.payments, state="readonly")
        #comboboxes sets
        self.payment_selector.set("selecione")  
        self.combo.set("Selecione") 
        self.parcelas_combobox.set("selecione")

    #list of widget positions
    def placeWidgets(self):
        self.menu.place(x=0, y=0, width=self.windowx - 245, height=50)
        self.input_dados_text.place(x=10, y=60, width=100 ,height=20)
        self.input_dados.place(x=10, y=85 )
        self.data_textE.place(x=10, y=150, width=120)
        self.data_entryE.place(x=10, y=175, width=120)
        self.data_textD.place(x=200, y=150, width=120)
        self.data_entryD.place(x=200, y=175, width=120)
        self.texto_combo.place(x=10, y=215, width=120)
        self.combo.place(x=10, y=240, width=120)
        self.nf_entry_text.place(x=10, y = 280, width=120)
        self.nf_entry.place(x=10, y=305)
        self.payment_label.place(x=200, y=215, width=120)
        self.payment_selector.place(x=200, y=240, width=120)
        self.parcelas_text.place(x=200, y=280, width=120)
        self.parcelas_combobox.place(x=200, y=305, width=120)
        self.command_window.place(x = 758, y = 3, height=395, width=240)
        self.command_text.place(x = 758 , y = 10)
        self.button_send.place(x = 125, y = 340)

    #atualizar a tela 
    def update_windowsChange(self, change):
            self.command_text.config(change)


root = tk.Tk()
app = app(root)
root.mainloop()