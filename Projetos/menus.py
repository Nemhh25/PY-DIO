import tkinter as tk
from tkinter import messagebox
import string
import random

# Função para gerar a senha
def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            raise ValueError
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        resultado_var.set(senha)
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido maior que 0")

# Criando a janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("300x200")

# Campo para inserir o tamanho
tk.Label(janela, text="Tamanho da senha:").pack(pady=5)
entry_tamanho = tk.Entry(janela)
entry_tamanho.pack()

# Botão para gerar a senha
btn_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
btn_gerar.pack(pady=10)

# Área para exibir o resultado
resultado_var = tk.StringVar()
tk.Label(janela, textvariable=resultado_var, fg="blue", font=("Helvetica", 12)).pack(pady=10)

# Rodar o app
janela.mainloop()