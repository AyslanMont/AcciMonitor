from tkinter import *
import sqlite3
import pickle

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("AcciMonitor")
        self.janela.iconbitmap("assets/imgs/acidente.ico")
        self.janela.geometry("800x500")

        self.Canvas_background = Canvas(self.janela, background="Gray")
        self.Canvas_background.pack(fill="both", expand=True)

        #Menu Principal
        self.Menu_Principal = Menu(self.janela)
        self.Menu_Principal.add_command(label="Cadastro", command=lambda: (self.Limpar_Tela(),self.Exibir_Aba_Cadastro()))
        self.Menu_Principal.add_command(label="Consulta", command=lambda: (self.Limpar_Tela(),self.Exibir_Aba_Consulta()))

        self.janela.config(menu=self.Menu_Principal)

        self.janela.mainloop()

    def Exibir_Aba_Cadastro(self):
        pass
        
    def Exibir_Aba_Consulta(self):
        pass

    def Limpar_Tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    EXECUCAO = App()