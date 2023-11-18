from tkinter import *
import sqlite3
import pickle

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("AcciMonitor")
        self.janela.geometry("800x800")

        self.janela.mainloop()

if __name__ == "__main__":
    EXECUCAO = App()