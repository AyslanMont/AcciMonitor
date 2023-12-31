from tkinter import *
from tkinter import messagebox, Listbox
from tkinter.ttk import Combobox, Checkbutton
from tkcalendar import Calendar, DateEntry
import sqlite3
import pickle

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("AcciMonitor")
        self.janela.iconbitmap("assets/imgs/acidente.ico")
        self.janela.geometry("600x400+500+100")
        self.janela.resizable(False, False)

        #Cores 

        self.Background_da_Janela = "#E0E0E0"
        self.Azul_Primario = "#2196F3" 
        self.Azul_Secundario = "#03A9F4" 
        self.Verde_Sucesso = "#4CAF50" 
        self.Vermelho_Aviso = "#FF5722" 
        self.Amarelo_Alerta = "#FFC107"
        self.Branco = "White"
        self.Verde_Claro = "#8AFFC0"
        

        self.Canvas_background = Canvas(self.janela, background=self.Background_da_Janela)
        self.Canvas_background.pack(fill="both", expand=True)

        #Menu Principal
        self.Menu_Principal = Menu(self.janela)
        self.Menu_Principal.add_command(label="Cadastro", command=self.Exibir_Aba_Cadastro)
        self.Menu_Principal.add_command(label="Consulta", command=self.Exibir_Aba_Consulta)
        self.Menu_Principal.add_command(label="Administrador", command=self.Exibir_Aba_Administrador)
        self.janela.config(menu=self.Menu_Principal)

        #Tela Inicial
        self.Criar_Layout_Cadastro()  
        self.janela.mainloop()
    
    def Criar_Layout_Cadastro(self):

        self.Canvas_background = Canvas(self.janela, background=self.Background_da_Janela)
        self.Canvas_background.pack(fill="both", expand=True)

        self.Menu_Principal = Menu(self.janela)
        self.Menu_Principal.add_command(label="Cadastro", command=self.Exibir_Aba_Cadastro)
        self.Menu_Principal.add_command(label="Consulta", command=self.Exibir_Aba_Consulta)
        self.Menu_Principal.add_command(label="Administrador", command=self.Exibir_Aba_Administrador)
        self.janela.config(menu=self.Menu_Principal)

        self.Label_Titulo_Informacoes = Label(self.janela, text="Informações", background=self.Azul_Primario, font="Arial 20",anchor=CENTER)
        self.Label_Titulo_Informacoes.place(x=50, y=10, width=500)

        self.Label_Data = Label(self.janela, text="Data", background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Data.place(x=50, y=70, width=60, height=25)
        self.Entry_data = DateEntry(self.janela)  
        self.Entry_data.place(x=120, y=70, width=175, height=25)

        self.Label_Hora = Label(self.janela, text="Hora", background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Hora.place(x=305, y=70, width=60, height=25)
        self.Entry_Hora = Entry(self.janela)
        self.Entry_Hora.place(x=375, y=70, width=175, height=25)

        self.Label_Local = Label(self.janela,text="Local",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Local.place(x=50, y=115, width=60, height=25)
        self.Entry_Local = Entry(self.janela)
        self.Entry_Local.place(x=120, y=115, width=430, height=25)

        self.Opcoes_de_Categoria = ["Colisões","Queda", "Incêndio", "Explosão", "Outro"]
        self.Label_Categoria = Label(self.janela,text="Categoria",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Categoria.place(x=50, y=160,width=200, height=25)
        self.Entry_Categoria = Combobox(self.janela, values=self.Opcoes_de_Categoria, font="Arial 10")
        self.Entry_Categoria.place(x=50, y=195,width=200, height=25)
        self.Entry_Categoria.set("Colisões")

        self.Opcoes_de_Gravidade = ["Ileso", "Ferido leve", "Ferido grave", "Morto"]
        self.Label_Gravidade = Label(self.janela,text="Gravidade",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Gravidade.place(x=50, y=240,width=200, height=25)
        self.Entry_Gravidade = Combobox(self.janela, values=self.Opcoes_de_Gravidade, font="Arial 10")
        self.Entry_Gravidade.place(x=50, y=275,width=200, height=25)
        self.Entry_Gravidade.set("Ileso")

        self.Label_Descricao = Label(self.janela,text="Descrição",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Descricao.place(x=260, y=160,width=290, height=25)
        self.Entry_Descricao = Text(self.janela)
        self.Entry_Descricao.place(x=260, y=195,width=290, height=105)

        self.Image_Carregada = PhotoImage(file='assets/imgs/logo_botao_registrar.png')
        self.botao_Registrar = Button(self.janela, text=" Registrar", background=self.Verde_Sucesso,anchor=CENTER, font="Arial 15",image=self.Image_Carregada,compound = 'left',command=self.Registrando)
        self.botao_Registrar.place(x=150, y=320,width=300, height=40)

    def Criar_Layout_Consulta(self):
        self.Canvas_background = Canvas(self.janela, background=self.Background_da_Janela)
        self.Canvas_background.pack(fill="both", expand=True)

        self.Menu_Principal = Menu(self.janela)
        self.Menu_Principal.add_command(label="Cadastro", command=self.Exibir_Aba_Cadastro)
        self.Menu_Principal.add_command(label="Consulta", command=self.Exibir_Aba_Consulta)
        self.Menu_Principal.add_command(label="Administrador", command=self.Exibir_Aba_Administrador)
        self.janela.config(menu=self.Menu_Principal)

        self.Label_Titulo_Informacoes = Label(self.janela, text="Consulta", background=self.Azul_Primario, font="Arial 20",anchor=CENTER)
        self.Label_Titulo_Informacoes.place(x=50, y=10, width=500)

        self.Check_var_Data = IntVar()
        self.botao_Check_Data = Checkbutton(self.janela, text="Data", variable=self.Check_var_Data,command=self.Atualizar_Widgets)
        self.botao_Check_Data.place(x=50, y=60, width=84)

        self.Check_var_Local = IntVar()
        self.botao_Check_Local = Checkbutton(self.janela, text="Local", variable=self.Check_var_Local,command=self.Atualizar_Widgets)
        self.botao_Check_Local.place(x=154, y=60, width=84)

        self.Check_var_Hora = IntVar()
        self.botao_Check_Hora = Checkbutton(self.janela, text="Hora", variable=self.Check_var_Hora,command=self.Atualizar_Widgets)
        self.botao_Check_Hora.place(x=258, y=60, width=84)

        self.Check_var_Categoria = IntVar()
        self.botao_Check_Categoria = Checkbutton(self.janela, text="Categoria", variable=self.Check_var_Categoria,command=self.Atualizar_Widgets)
        self.botao_Check_Categoria.place(x=362, y=60, width=84)

        self.Check_var_Gravidade= IntVar()
        self.botao_Check_Gravidade = Checkbutton(self.janela, text="Gravidade", variable=self.Check_var_Gravidade,command=self.Atualizar_Widgets )
        self.botao_Check_Gravidade.place(x=466, y=60, width=84)

        self.Label_Data = Label(self.janela, text="Data", background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Data.place(x=50, y=120, width=60, height=25)
        self.Entry_data = DateEntry(self.janela, state="disabled")  
        self.Entry_data.place(x=120, y=120, width=175, height=25)

        self.Label_Hora = Label(self.janela, text="Hora", background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Hora.place(x=305, y=120, width=60, height=25)
        self.Entry_Hora = Entry(self.janela, state="disabled")
        self.Entry_Hora.place(x=375, y=120, width=175, height=25)

        self.Label_Local = Label(self.janela,text="Local",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Local.place(x=50, y=165, width=60, height=25)
        self.Entry_Local = Entry(self.janela, state="disabled")
        self.Entry_Local.place(x=120, y=165, width=430, height=25)

        self.Opcoes_de_Categoria = ["Colisões","Queda", "Incêndio", "Explosão", "Outro"]
        self.Label_Categoria = Label(self.janela,text="Categoria",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Categoria.place(x=50, y=210,width=240, height=25)
        self.Entry_Categoria = Combobox(self.janela, values=self.Opcoes_de_Categoria, font="Arial 10", state="disabled")
        self.Entry_Categoria.place(x=50, y=245,width=240, height=25)
        self.Entry_Categoria.set("Colisões")

        self.Opcoes_de_Gravidade = ["Ileso", "Ferido leve", "Ferido grave", "Morto"]
        self.Label_Gravidade = Label(self.janela,text="Gravidade",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Gravidade.place(x=310, y=210,width=240, height=25)
        self.Entry_Gravidade = Combobox(self.janela, values=self.Opcoes_de_Gravidade, font="Arial 10", state="disabled")
        self.Entry_Gravidade.place(x=310, y=245,width=240, height=25)
        self.Entry_Gravidade.set("Ileso")

        self.Image_Carregada = PhotoImage(file='assets/imgs/consulta.png')
        self.botao_Consultar = Button(self.janela, text="Consultar", background=self.Branco,anchor=CENTER, font="Arial 15",image=self.Image_Carregada,compound = 'left',command=self.Consultando)
        self.botao_Consultar.place(x=150, y=320,width=300, height=40)

    def Criar_Layout_Administrador(self):
        self.Canvas_background = Canvas(self.janela, background=self.Background_da_Janela)
        self.Canvas_background.pack(fill="both", expand=True)

        self.Menu_Principal = Menu(self.janela)
        self.Menu_Principal.add_command(label="Cadastro", command=self.Exibir_Aba_Cadastro)
        self.Menu_Principal.add_command(label="Consulta", command=self.Exibir_Aba_Consulta)
        self.Menu_Principal.add_command(label="Administrador", command=self.Exibir_Aba_Administrador)
        self.janela.config(menu=self.Menu_Principal)

        self.Label_Titulo_Informacoes = Label(self.janela, text="Administrador", background=self.Azul_Primario, font="Arial 20",anchor=CENTER)
        self.Label_Titulo_Informacoes.place(x=50, y=10, width=500)

        self.Check_var_Data = IntVar()
        self.botao_Check_Data = Checkbutton(self.janela, text="Data", variable=self.Check_var_Data,command=self.Atualizar_Widgets)
        self.botao_Check_Data.place(x=50, y=60, width=84)

        self.Check_var_Local = IntVar()
        self.botao_Check_Local = Checkbutton(self.janela, text="Local", variable=self.Check_var_Local,command=self.Atualizar_Widgets)
        self.botao_Check_Local.place(x=154, y=60, width=84)

        self.Check_var_Hora = IntVar()
        self.botao_Check_Hora = Checkbutton(self.janela, text="Hora", variable=self.Check_var_Hora,command=self.Atualizar_Widgets)
        self.botao_Check_Hora.place(x=258, y=60, width=84)

        self.Check_var_Categoria = IntVar()
        self.botao_Check_Categoria = Checkbutton(self.janela, text="Categoria", variable=self.Check_var_Categoria,command=self.Atualizar_Widgets)
        self.botao_Check_Categoria.place(x=362, y=60, width=84)

        self.Check_var_Gravidade= IntVar()
        self.botao_Check_Gravidade = Checkbutton(self.janela, text="Gravidade", variable=self.Check_var_Gravidade,command=self.Atualizar_Widgets)
        self.botao_Check_Gravidade.place(x=466, y=60, width=84)

        self.Label_Data = Label(self.janela, text="Data", background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Data.place(x=50, y=120, width=60, height=25)
        self.Entry_data = DateEntry(self.janela, state="disabled")  
        self.Entry_data.place(x=120, y=120, width=175, height=25)

        self.Label_Hora = Label(self.janela, text="Hora", background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Hora.place(x=305, y=120, width=60, height=25)
        self.Entry_Hora = Entry(self.janela, state="disabled")
        self.Entry_Hora.place(x=375, y=120, width=175, height=25)

        self.Label_Local = Label(self.janela,text="Local",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Local.place(x=50, y=165, width=60, height=25)
        self.Entry_Local = Entry(self.janela, state="disabled")
        self.Entry_Local.place(x=120, y=165, width=430, height=25)

        self.Opcoes_de_Categoria = ["Colisões","Queda", "Incêndio", "Explosão", "Outro"]
        self.Label_Categoria = Label(self.janela,text="Categoria",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Categoria.place(x=50, y=210,width=240, height=25)
        self.Entry_Categoria = Combobox(self.janela, values=self.Opcoes_de_Categoria, font="Arial 10", state="disabled")
        self.Entry_Categoria.place(x=50, y=245,width=240, height=25)
        self.Entry_Categoria.set("Colisões")

        self.Opcoes_de_Gravidade = ["Ileso", "Ferido leve", "Ferido grave", "Morto"]
        self.Label_Gravidade = Label(self.janela,text="Gravidade",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Gravidade.place(x=310, y=210,width=240, height=25)
        self.Entry_Gravidade = Combobox(self.janela, values=self.Opcoes_de_Gravidade, font="Arial 10", state="disabled")
        self.Entry_Gravidade.place(x=310, y=245,width=240, height=25)
        self.Entry_Gravidade.set("Ileso")

        self.Image_Carregada_1 = PhotoImage(file='assets/imgs/lixeira.png')
        self.botao_Deletar_Tudo = Button(self.janela, text="Deletar tudo", background=self.Vermelho_Aviso,anchor=CENTER, font="Arial 15",image=self.Image_Carregada_1,compound = 'left',command=self.Deletando_Tudo)
        self.botao_Deletar_Tudo.place(x=50, y=320,width=160, height=40)

        self.Image_Carregada_2 = PhotoImage(file='assets/imgs/backup.png')
        self.botao_Backup = Button(self.janela, text=" Backup", background=self.Verde_Sucesso,anchor=CENTER, font="Arial 15",image=self.Image_Carregada_2,compound = 'left',command=self.Fazendo_Backup)
        self.botao_Backup.place(x=220, y=320,width=160, height=40)

        self.Image_Carregada_3 = PhotoImage(file='assets/imgs/lixeira.png')
        self.botao_Deleta_Especifica = Button(self.janela, text="Deletar", background=self.Vermelho_Aviso,anchor=CENTER, font="Arial 15", image=self.Image_Carregada_3,compound = 'left',command=self.Fazendo_Deleta_Especifica)
        self.botao_Deleta_Especifica.place(x=390, y=320,width=160, height=40)
        
    def Exibir_Aba_Cadastro(self):
        self.Limpar_Tela()
        self.Criar_Layout_Cadastro ()
    
    def Exibir_Aba_Consulta(self):
        self.Limpar_Tela()
        self.Criar_Layout_Consulta()

    def Exibir_Aba_Administrador(self):
        self.Limpar_Tela()
        self.Criar_Layout_Administrador()
        
    def Limpar_Tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def Atualizar_Widgets(self):
        if self.Check_var_Data.get() == 0:
            self.Entry_data.config(state='disabled')
        else:
            self.Entry_data.config(state='normal')

        if self.Check_var_Hora.get() == 0:
            self.Entry_Hora.config(state='disabled')
        else:
            self.Entry_Hora.config(state='normal')

        if self.Check_var_Local.get() == 0:
            self.Entry_Local.config(state='disabled')
        else:
            self.Entry_Local.config(state='normal')

        if self.Check_var_Categoria.get() == 0:
            self.Entry_Categoria.config(state='disabled')
        else:
            self.Entry_Categoria.config(state='normal')

        if self.Check_var_Gravidade.get() == 0:
            self.Entry_Gravidade.config(state='disabled')
        else:
            self.Entry_Gravidade.config(state='normal')

    def Registrando (self):

        con = sqlite3.connect("Registro_de_Acidentes.db")
        banco = con.cursor()

        try:
            Valor_Data = self.Entry_data.get()
            Valor_Local = self.Entry_Local.get()
            Valor_Hora = self.Entry_Hora.get()
            Valor_Categoria = self.Entry_Categoria.get()
            Valor_Gravidade = self.Entry_Gravidade.get()
            Valor_Descricao= self.Entry_Descricao.get("1.0", "end-1c")

            self.Verifica_Hora(Valor_Hora)
            self.Verifica_Local(Valor_Local)

        except Exception as err:
            messagebox.showinfo("Formato inválido", f"{err}")

        else:

            Dados_Serializados = {"Data":Valor_Data,
            "Local": Valor_Local,
            "Hora":Valor_Hora,
            "Categoria":Valor_Categoria,
            "Gravidade":Valor_Gravidade,
            "Descricao":Valor_Descricao
            }

            arquivo = open("Arquivo_de_Registros_binario.bin",'ab')
            pickle.dump(Dados_Serializados, arquivo)
            arquivo.close()

            banco.execute("INSERT INTO Registros VALUES (?,?,?,?,?,?)", (Valor_Data, Valor_Local, Valor_Hora, Valor_Categoria, Valor_Gravidade, Valor_Descricao))
            con.commit()
            con.close()

            self.Entry_data.delete(0, END)
            self.Entry_Local.delete(0, END)
            self.Entry_Hora.delete(0, END)
            self.Entry_Categoria.delete(0, END)
            self.Entry_Gravidade.delete(0, END)
            self.Entry_Descricao.delete("1.0", END)
            messagebox.showinfo("Sucesso!", "O registro foi inserido com sucesso!")

    def Consultando (self):

        con = sqlite3.connect("Registro_de_Acidentes.db")
        banco = con.cursor()
        dados = []

        if self.Check_var_Data.get() == 1:
            Valor_Data = self.Entry_data.get()
            banco.execute("SELECT * FROM Registros WHERE Data = ?", (Valor_Data,))
            registros = banco.fetchall()
            for registro in registros:
                if registro not in dados:
                    dados.append(registro)

        if self.Check_var_Hora.get() == 1:
            try:
                Valor_Hora = self.Entry_Hora.get()
                self.Verifica_Hora(Valor_Hora)
            except Exception as err:
                messagebox.showinfo("Formato inválido", f"{err}")
            else:       
                banco.execute("SELECT * FROM Registros WHERE Hora = ?", (Valor_Hora,))
                registros = banco.fetchall()
                for registro in registros:
                    if registro not in dados:
                        dados.append(registro)
            

        if self.Check_var_Local.get() == 1:
            try:
                Valor_Local = self.Entry_Local.get()
                self.Verifica_Local(Valor_Local)
            except Exception as err:
                messagebox.showinfo("Formato inválido", f"{err}")
            else:
                banco.execute("SELECT * FROM Registros WHERE Local = ?", (Valor_Local,))
                registros = banco.fetchall()
                for registro in registros:
                    if registro not in dados:
                        dados.append(registro) 

        if self.Check_var_Categoria.get() == 1:
            Valor_Categoria = self.Entry_Categoria.get()
            banco.execute("SELECT * FROM Registros WHERE Categoria = ?", (Valor_Categoria,))
            registros = banco.fetchall()
            for registro in registros:
                if registro not in dados:
                    dados.append(registro) 

        if self.Check_var_Gravidade.get() == 1:
            Valor_Gravidade = self.Entry_Gravidade.get()
            banco.execute("SELECT * FROM Registros WHERE Gravidade = ?", (Valor_Gravidade,))
            registros = banco.fetchall()
            for registro in registros:
                if registro not in dados:
                    dados.append(registro)
        self.Exebindo_Dados(dados)

    def Verifica_Hora(self, hora):
        lista_hora = hora.split(":")
        if len(lista_hora) == 2:
            for i in lista_hora:
                if len(i) != 2:
                    raise ValueError("Formato de hora inválido, por favor use (00:00)")
        else:
            raise ValueError("Formato de hora inválido, por favor use (00:00)")

    def Verifica_Local(self, local):
        lista_local = local.split("/")
        if len(lista_local) != 4:
            raise ValueError("Formato de local inválido, por favor use (Estado/Cidade/Bairro/Rua)")
    
    def Exebindo_Dados(self, Dados):
        toplevel = Toplevel(self.janela)
        toplevel.geometry("500x500+500+100")
        toplevel.resizable(0,0)

        Caixa_de_lista = Listbox(toplevel)
        for registro in Dados:
            registro_formatado = [f"Data: {registro[0]}", f"Hora: {registro[2]}", f"Local: {registro[1]}", f"Categoria: {registro[3]}", f"Gravidade: {registro[4]}", f"Descrição: {registro[5]}"]
            tamanho = len(registro_formatado)
            cont = 0
            while cont < tamanho:
                Caixa_de_lista.insert("end",registro_formatado[cont])       
                cont += 1
            Caixa_de_lista.insert("end", "")     

        Caixa_de_lista.config(
        font=('Arial', 12),
        bg=self.Branco,
        fg='black',
        selectbackground='gray', 
        selectforeground='white')
        Caixa_de_lista.pack(expand=True, fill=BOTH)

    def Deletando_Tudo(self):
        con = sqlite3.connect("Registro_de_Acidentes.db")
        banco = con.cursor()   
        banco.execute("DELETE FROM Registros")
        con.commit()
        con.close()
        messagebox.showinfo("Sucesso!","Todos os registros foram apagados")

    def Fazendo_Backup(self):
        
        arquivo = open("Arquivo_de_Registros_binario.bin",'rb')
        Dados_Deserializados = []
        con = sqlite3.connect("Registro_de_Acidentes.db")
        banco = con.cursor()
        while True:
            try:
                objeto = pickle.load(arquivo)
                Dados_Deserializados.append(objeto)
            except Exception as err:
                break
        arquivo.close()
        for Dicionario in Dados_Deserializados:
            banco.execute("INSERT INTO Registros VALUES (?,?,?,?,?,?)", (Dicionario["Data"], Dicionario["Local"],Dicionario["Hora"], Dicionario["Categoria"], Dicionario["Gravidade"], Dicionario["Descricao"]))
        con.commit()
        con.close()

    def Fazendo_Deleta_Especifica(self):
        con = sqlite3.connect("Registro_de_Acidentes.db")
        banco = con.cursor()
        cont = 0

        if self.Check_var_Data.get() == 1:
            Valor_Data = self.Entry_data.get()
            banco.execute("DELETE FROM Registros WHERE Data = ?", (Valor_Data,))
            cont += 1

        if self.Check_var_Hora.get() == 1:
            try:
                Valor_Hora = self.Entry_Hora.get()
                self.Verifica_Hora(Valor_Hora)
            except Exception as err:
                messagebox.showinfo("Formato inválido", f"{err}")
            else:       
                banco.execute("DELETE FROM Registros WHERE Hora = ?", (Valor_Hora,))
                cont += 1
            
        if self.Check_var_Local.get() == 1:
            try:
                Valor_Local = self.Entry_Local.get()
                self.Verifica_Local(Valor_Local)
            except Exception as err:
                messagebox.showinfo("Formato inválido", f"{err}")
            else:
                banco.execute("DELETE FROM Registros WHERE Local = ?", (Valor_Local,))
                cont += 1

        if self.Check_var_Categoria.get() == 1:
            Valor_Categoria = self.Entry_Categoria.get()
            banco.execute("DELETE FROM Registros WHERE Categoria = ?", (Valor_Categoria,))
            cont += 1

        if self.Check_var_Gravidade.get() == 1:
            Valor_Gravidade = self.Entry_Gravidade.get()
            banco.execute("DELETE FROM Registros WHERE Gravidade = ?", (Valor_Gravidade,))
            cont += 1
        con.commit()
        con.close()
        if cont != 0:
            messagebox.showinfo("Sucesso!","Os registros foram apagados")
        else:
            messagebox.showinfo("Sucesso!","Não tem registros a serem apagados")
        self.Entry_data.delete(0, END)
        self.Entry_Local.delete(0, END)
        self.Entry_Hora.delete(0, END)
        self.Entry_Categoria.delete(0, END)
        self.Entry_Gravidade.delete(0, END)

if __name__ == "__main__":
    EXECUCAO = App() 