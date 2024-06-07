import tkinter as tk #Importar a biblioteca com um nome abreviado
from tkinter import messagebox #Importar partes específicas da biblioteca
import csv

class CadastroCliente:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")

        self.nome_label = tk.Label(root, text="Nome:")
        self.nome_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)

        self.idade_label = tk.Label(root, text="Idade:")
        self.idade_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.idade_entry = tk.Entry(root)
        self.idade_entry.grid(row=1, column=1, padx=10, pady=5)

        self.renda_label = tk.Label(root, text="Renda Anual:")
        self.renda_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.renda_entry = tk.Entry(root)
        self.renda_entry.grid(row=2, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)

        self.cadastrar_button = tk.Button(root, text="Cadastrar", command=self.cadastrar_cliente)
        self.cadastrar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.cliente_id = 1

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        renda = self.renda_entry.get()
        email = self.email_entry.get()


root = tk.Tk()
app = CadastroCliente(root)
root.mainloop()