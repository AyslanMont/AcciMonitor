from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkcalendar import Calendar, DateEntry
import sqlite3
import pickle
import json
from PIL import ImageTk, Image

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("AcciMonitor")
        self.janela.iconbitmap("assets/imgs/acidente.ico")
        self.janela.geometry("600x600+500+100")
        self.janela.resizable(False, False)

        #Cores 

        self.Background_da_Janela = "#E0E0E0"
        self.Azul_Primario = "#2196F3" 
        self.Azul_Secundario = "#03A9F4" 
        self.Verde_Sucesso = "#4CAF50" 
        self.Vermelho_Aviso = "#FF5722" 
        self.Amarelo_Alerta = "#FFC107" 
        

        self.Canvas_background = Canvas(self.janela, background=self.Background_da_Janela)
        self.Canvas_background.pack(fill="both", expand=True)

        #Menu Principal
        self.Menu_Principal = Menu(self.janela)
        self.Menu_Principal.add_command(label="Cadastro", command=lambda: (self.Limpar_Tela(),self.Exibir_Aba_Cadastro()))
        self.Menu_Principal.add_command(label="Consulta", command=lambda: (self.Limpar_Tela(),self.Exibir_Aba_Consulta()))

        self.janela.config(menu=self.Menu_Principal)

        #Informações

        self.Label_Titulo_Informacoes = Label(self.janela, text="Informações", background=self.Azul_Primario, font="Arial 20",anchor=CENTER)
        self.Label_Titulo_Informacoes.place(x=50, y=10, width=500)

        #Informações -- Data

        self.Label_Data = Label(self.janela, text="Data", background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Data.place(x=50, y=70, width=60, height=25)
        self.Entry_data = DateEntry(self.janela)  
        self.Entry_data.place(x=120, y=70, width=175, height=25)
        
        #Informações -- Hora

        self.Label_Hora = Label(self.janela, text="Hora", background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Hora.place(x=305, y=70, width=60, height=25)
        self.Entry_Hora = Entry(self.janela)
        self.Entry_Hora.place(x=375, y=70, width=175, height=25)

        #Informações -- Local

        self.Label_Local = Label(self.janela,text="Local",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Local.place(x=50, y=115, width=60, height=25)
        self.Entry_Local = Entry(self.janela)
        self.Entry_Local.place(x=120, y=115, width=430, height=25)


        #Informações -- Categoria

        self.Opcoes_de_Categoria = ["Colisões","Queda", "Incêndio", "Explosão", "Outro"]
        self.Label_Gravidade = Label(self.janela,text="Gravidade",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Gravidade.place(x=50, y=160,width=200, height=25)
        self.Entry_Gravidade = Combobox(self.janela, values=self.Opcoes_de_Categoria, font="Arial 10")
        self.Entry_Gravidade.place(x=50, y=195,width=200, height=25)
        self.Entry_Gravidade.set("Colisões")

        #Informações -- Descrição
        self.Label_Descricao = Label(self.janela,text="Descrição",background=self.Amarelo_Alerta, font="Arial 15",anchor=CENTER)
        self.Label_Descricao.place(x=260, y=160,width=290, height=25)
        self.Entry_Descricao = Text(self.janela)
        self.Entry_Descricao.place(x=260, y=195,width=290, height=200)

        #Informações -- Fotos
        self.ImageCarregada_anexar = PhotoImage(file='assets/imgs/acidente_png.png').subsample(3,3)
        self.Label_Imagem = Label(self.janela, image=self.ImageCarregada_anexar)
        self.Label_Imagem.place(x=65, y=230)
        self.ImageCarregada_anexar_logo =  PhotoImage(file='assets/imgs/upload.png')
        self.botao_Anexar_Imagem = Button(self.janela, text="Anexar Imagem", command=self.Selecionar_Imagem, background=self.Amarelo_Alerta, font="Arial 15",image=self.ImageCarregada_anexar_logo,compound = 'left')
        self.botao_Anexar_Imagem.place(x=50, y=420,width=200, height=40)

        #Informações -- Botão Registrar

        self.Image_Carregada = PhotoImage(file='assets/imgs/logo.png')
        self.botao_Registrar = Button(self.janela, text=" Registrar", background=self.Verde_Sucesso,anchor=CENTER, font="Arial 15",image=self.Image_Carregada,compound = 'left')
        self.botao_Registrar.place(x=260, y=420,width=290, height=40)

        self.janela.mainloop()

    def Exibir_Aba_Cadastro(self):
        pass
        
    def Exibir_Aba_Consulta(self):
        pass

    def Limpar_Tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def Selecionar_Imagem(self):

        arquivo = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])

        self.ImageCarregada_anexar = PhotoImage(file=arquivo).subsample(3,3)
        self.Label_Imagem.config(image=self.Image_Carregada)

if __name__ == "__main__":
    EXECUCAO = App()