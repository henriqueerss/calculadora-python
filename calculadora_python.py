#calculadora Python

import tkinter as tk

#Função para calcular o resultado:
def calcular():
    try:
        expressao = entrada.get()
        result = str(eval(expressao))
        result_label.config(text="Resultado\n" + result)
    
    except Exception as e:
        result_label.config(Text="erro")

#Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")

#Entrada de texto
entrada = tk.Entry(janela, width=20, font=("Times New Roman", 22), justify="center", bd=12, insertwidth=6)
entrada.pack()

#Botão para calcular
calcular_button = tk.Button(janela, text="Calcular", command=calcular)
calcular_button.pack(button="enter")

#Rótulo para exibir o resultado
result_label = tk.Label(janela, text="Resultado: ")
result_label.pack()

#Abrir janela
janela.mainloop()