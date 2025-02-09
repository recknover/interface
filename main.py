import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
import conection
import os
import sqlite3

#----------------------coisas de fora----------------------------------------------------------------------------------------------------------------------------

#leitor de listas
def leitor(arquivo):
    arquivo = open(f"{arquivo}", "r")
    items = []
    for i in arquivo:
        items.append(i)
    return items

#----------------------coisas de fora----------------------------------------------------------------------------------------------------------------------------

#------------------------------init------------------------------------------------------------------------------------------------------------------------------

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
        self.ShowValuesWidgets(root)
        self.checkDatabase()
        self.createMenu_bar(root)
        self.whitescreen()
#------------------------------init----------------------------------------------------------------------------------------------------------------------------

#----------------menu bar functions----------------------------------------------------------------------------------------------------------------------------

    #createMenu_bar
    def createMenu_bar(self, root):
        self.menubar = tk.Menu(root)
        self.createFileMenu(root)
        self.createEditMenu()
        self.createHelpMenu()
        self.whitescreenMenu()
        # coloca na tela
        root.config(menu=self.menubar)
        root.update_idletasks()
        

    def createFileMenu(self, root):
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Open", command='#')
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        # adiciona na tela, qualquer coisa nova colocar na parte de cima
        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def createEditMenu(self):
        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.edit_menu.add_command(label="return values", command=self.MenuShow)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="delete values", command='#')
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="insert values", command=self.MenuInsert)
        # adiciona na tela, qualquer coisa nova colocar na parte de cima
        self.menubar.add_cascade(label="Windows", menu=self.edit_menu)

    def createHelpMenu(self):
        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label="About", command="#")
        # adiciona na tela, qualquer coisa nova colocar na parte de cima
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

    def whitescreenMenu(self):
        self.whiteMenu = tk.Menu(self.menubar, tearoff=0)
        self.whiteMenu.add_command(label="clear screen", command=self.whitescreen)
        # adiciona na tela, qualquer coisa nova colocar na parte de cima
        self.menubar.add_cascade(label="Clear", menu=self.whiteMenu)

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
        self.whitescreen()
        self.createInsertWidgets(root)
        self.placeInsertWidgets()

    def ShowValuesWidgets(self, root):
        self.whitescreen()
        self.createShowValues(root)
        self.placeShowValues()
    
    def RemoveValuesWidgets(self, root):
        pass

    #menu insert func
    def MenuInsert(self):
        self.whitescreen()
        self.placeInsertWidgets()

    #menu show func
    def MenuShow(self):
        self.whitescreen()
        self.placeShowValues()

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

    #list of "isertwidgets" to create
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
        root.update_idletasks()

    #list of "insertwidget" positions
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

#----------------place for the return values widgets------------------------------------------------------------------------------------------------------------------

    #list of "Showvalues"widgets to create
    def createShowValues(self, root):
        #button
        self.showValuesbutton = tk.Button(text="return", command="#", bd=2, relief="solid")
        #labels
        self.name_nf_filter_label = tk.Label(text="nome ou nf", bd=2, relief="solid")
        self.date_filter_expiration_label = tk.Label(text="data vencimento", bd=2, relief="solid")
        self.date_filter_emission_label = tk.Label(text="data emissao", bd=2, relief="solid")
        self.type_filter_label = tk.Label(text="tipo", bd=2, relief="solid")
        self.screen = tk.Label(bg="black")
        #datas
        self.date_filter_emission = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, bg="red")
        self.date_filter_expiration = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, bg="red")
        #combobox
        self.name_nf_filter = ttk.Combobox(root, values="nome nf", state="readonly") 
        self.type_filter = ttk.Combobox(root, values=self.items, state="readonly")
        #comboboxes sets
        self.name_nf_filter.set("selecione")  
        self.type_filter.set("selecione")  
        #entrys
        self.name_nf_entry = tk.Entry(text="placeholder", width=100, bd=2, relief="solid")
        root.update_idletasks()

    #list of showvalues"widgets positions
    def placeShowValues(self):
        self.screen.place(x=2, y=100, width=996, height=298)
        self.showValuesbutton.place(x=50, y=50, width=120)
        self.name_nf_entry.place(x=190, y=53, width=120)
        self.name_nf_filter.place(x=330, y=53, width=120)
        self.type_filter.place(x=480,y=53, width=120)
        self.date_filter_emission.place(x=620, y=53, width=120)
        self.date_filter_expiration.place(x=760, y=53, width=120)
        self.name_nf_filter_label.place(x=190, y=30, width=260)
        self.type_filter_label.place(x=480, y=30, width=120)
        self.date_filter_emission_label.place(x=620, y=30, width=120)
        self.date_filter_expiration_label.place(x=760, y=30, width=120)



#----------------place for the return values widgets------------------------------------------------------------------------------------------------------------------

#----------------aplication functions----------------------------------------------------------------------------------------------------------------------------------
    
    def checkDatabase(self):
        if os.path.exists("main.db"):
            self.db = "main.db"
        else:
            self.db = conection.db_create("main")

    #id, nome, nf, dataEmissao, dataVencimento, tipo_produto, parcelas, forma de pagamento
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
        return values

    def whitescreen(self):
        try:
            for attr_name in dir(self):
                attr = getattr(self, attr_name)
                if isinstance(attr, (tk.Widget, ttk.Widget)):
                    attr.place_forget()
        except AttributeError:
            pass    

''' def whitescreen(self):
        try:
            widgets = [self.menu,self.input_dados_text,self.data_textD,self.data_textE,self.texto_seletor,
                self.nf_entry_text,self.payment_label,self.parcelas_text,self.command_window,
                self.command_text,self.texto_combo,self.input_dados,self.nf_entry,self.button_send,
                self.data_entryE,self.data_entryD,self.combo,self.parcelas_combobox,self.payment_selector, self.showValuesbutton]
            for widget in widgets:
                widget.place_forget()
        except AttributeError:
            pass
'''




#----------------aplication funcions-------------------------------------------------------------------------------------------------------------------------------------

#----------------final of the class app----------------------------------------------------------------------------------------------------------------------------------
        
root = tk.Tk()
app = app(root)
root.mainloop()
