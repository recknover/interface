import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
import conection
import os

#----------------------coisas de fora----------------------------------------------------------------------------------------------------------------------------

#leitor de listas
def leitor(arquivo):
    arquivo = open(f"{arquivo}", "r")
    items = []
    for i in arquivo:
        items.append(i)
    return items
#----------------------coisas de fora----------------------------------------------------------------------------------------------------------------------------

#------------------------------init----------------------------------------------------------------------------------------------------------------------------

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
        self.InsertWidgets(root)
        self.createMenu_bar(root)
        if os.path.exists("main.db"):
            pass
        else:          
            self.db = conection.db_create("main")
#------------------------------init----------------------------------------------------------------------------------------------------------------------------

#----------------menu bar functions----------------------------------------------------------------------------------------------------------------------------

    #createMenu_bar
    def createMenu_bar(self, root):
        self.menubar = tk.Menu(root)
        self.createFileMenu(root)
        self.createEditMenu()
        self.createHelpMenu()
        # coloca na tela
        root.config(menu=self.menubar)

    def createFileMenu(self, root):
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Open", command='#')
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        # adiciona na tela, qualquer coisa nova colocar na parte de cima
        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def createEditMenu(self):
        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.edit_menu.add_command(label="return values", command='#')
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="delete values", command='#')
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="insert values", command='#')
        # adiciona na tela, qualquer coisa nova colocar na parte de cima
        self.menubar.add_cascade(label="Windows", menu=self.edit_menu)

    def createHelpMenu(self):
        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label="About", command="#")
        # adiciona na tela, qualquer coisa nova colocar na parte de cima
        self.menubar.add_cascade(label="Help", menu=self.help_menu)


#----------------menu bar functions----------------------------------------------------------------------------------------------------------------------------------

#----------------create and place widgets----------------------------------------------------------------------------------------------------------------------------
        '''
        place_foget()
        criar outros widgets definir eles como
        #vazio pra resertar a tela
        (label vazia) ou algum comando pra resetar itens da tela
        #inserir dados
        (apenas renomear as funções que eu ja tenho)
        #retornar dados
        (label para mostrar a saida dos dados)(entry pra selecionar algo especifico de uma tabela)(botao pra mandar o comando)
        #deletar dados
        (label pra mostrar os dados)(entry pra selecionar id pra ser deletado)
        '''
    def InsertWidgets(self, root):
        self.createInsertWidgets(root)
        self.placeInsertWidgets()

    def ShowValuesWidgets(self, root):
        pass
    
    def RemoveValuesWidgets(self, root):
        pass

#----------------create and place widgets----------------------------------------------------------------------------------------------------------------------------

#----------------window and interface changes and confoguration-------------------------------------------------------------------------------------------------------


    #configure  
    def configureWindow(self, root):
        root.title("Interface v2")
        root.geometry(f"{self.windowx}x{self.windowy}")
        root.resizable(False, False)

    #atualizar a tela 
    def update_windowsChange(self, change):
            self.command_text.config(text=change)

#----------------window and interface changes and confoguration-------------------------------------------------------------------------------------------------------

#----------------place for the insert widgets-------------------------------------------------------------------------------------------------------------------------

    #list of widgets to create
    def createInsertWidgets(self, root):
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
        self.button_send = ttk.Button(text="send", command=self.enter_values)
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
    def placeInsertWidgets(self):
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

#----------------place for the insert widgets-------------------------------------------------------------------------------------------------------------------------

#----------------aplication funcions----------------------------------------------------------------------------------------------------------------------------------


    #id, nome, nf, dataEmissao, dataVencimento, tipo_produto
    def enter_values(self):
        nomeValor = self.input_dados.get()
        dataEmissao = self.data_entryD.get_date()
        dataVencimento = self.data_entryE.get_date()
        seletor = self.combo.get()
        nf = self.nf_entry.get()
        formaDePagamento = self.payment_selector.get()
        parcelas = self.parcelas_combobox.get()
        values = [nomeValor, dataEmissao, dataVencimento, seletor, nf, formaDePagamento, parcelas]
        print(values)
        self.update_windowsChange(values)
        conection.insertAll(self.db, values[0], values[1], values[2], values[3], values[4], values[5], values[6])

#----------------aplication funcions----------------------------------------------------------------------------------------------------------------------------------

#----------------final of the class app----------------------------------------------------------------------------------------------------------------------------------
        
root = tk.Tk()
app = app(root)
root.mainloop()
