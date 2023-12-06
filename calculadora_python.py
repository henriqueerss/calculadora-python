import tkinter as tk

autor = ("Henrique Ribeiro Siqueira")
print(autor)

# Função para adicionar um caractere à expressão
def adicionar_caractere(caractere):
    entrada.insert(tk.END, caractere)

# Função para calcular o resultado
def calcular():
    try:
        expressao = entrada.get()
        resultado = str(eval(expressao))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, resultado)
        resultado_label.config(text="Resultado: " + resultado)
        adicionar_historico(expressao, resultado)
    except Exception as e:
        resultado_label.config(text="Erro")

# Função para adicionar à lista de histórico
def adicionar_historico(expressao, resultado):
    historico_lista.insert(0, f"{expressao} = {resultado}")
    if len(historico_lista.get(0, tk.END)) > 10:
        historico_lista.delete(tk.END)

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)
    resultado_label.config(text="Resultado: ")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Entrada de texto
entrada = tk.Entry(janela, width=20, font=("Arial", 22), justify="center", bd=10, insertwidth=4)
entrada.grid(row=0, column=0, columnspan=4)

# Estilo dos botões
estilo_botao = {
    'padx': 20,
    'pady': 20,
    'font': ("Arial", 16),
    'bg': "#d4d4d2",
    'activebackground': "#c2c2c0"
}

# Botões numéricos
numeros = ['7'], ['8'], ['9']
row_val = 1
col_val = 0

for numero in numeros:
    tk.Button(janela, text=numero, command=lambda n=numero: adicionar_caractere(n), padx=20, pady=20, font=("Arial", 16), bg="#d4d4d2", activebackground="#c2c2c0").grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 5:
        col_val = 3
        row_val += 4


numeros = ['4'], ['5'], ['6']
row_val = 2
col_val = 0

for numero in numeros:
    tk.Button(janela, text=numero, command=lambda n=numero: adicionar_caractere(n), padx=20, pady=20, font=("Arial", 16), bg="#d4d4d2", activebackground="#c2c2c0").grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 5:
        col_val = 3
        row_val += 4


numeros = ['1'], ['2'], ['3']
row_val = 3
col_val = 0

for numero in numeros:
    tk.Button(janela, text=numero, command=lambda n=numero: adicionar_caractere(n), padx=20, pady=20, font=("Arial", 16), bg="#d4d4d2", activebackground="#c2c2c0").grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 5:
        col_val = 3
        row_val += 4


numeros = ['0']
row_val = 4
col_val = 1

for numero in numeros:
    tk.Button(janela, text=numero, command=lambda n=numero: adicionar_caractere(n), padx=20, pady=20, font=("Arial", 16), bg="#d4d4d2", activebackground="#c2c2c0").grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 10:
        col_val = 6
        row_val += 4



# Botões de operação
operacoes = ['/', '*', '-', '+']
row_val = 1
col_val = 3

for operacao in operacoes:
    tk.Button(janela, text=operacao, command=lambda o=operacao: adicionar_caractere(o), padx=20, pady=20, font=("Arial", 16), bg="#f5923e", activebackground="#e27c38").grid(row=row_val, column=col_val)
    row_val += 1

# Botões especiais
tk.Button(janela, text=".", command=lambda: adicionar_caractere('.'), padx=20, pady=20, font=("Arial", 16), bg="#d4d4d2", activebackground="#c2c2c0").grid(row=row_val, column=0)
tk.Button(janela, text="=", command=calcular, padx=40, pady=40, font=("Arial", 16), bg="#f5923e", activebackground="#e27c38").grid(row=row_val, column=1, columnspan=2)
tk.Button(janela, text="C", command=limpar, padx=20, pady=20, font=("Arial", 16), bg="#f5923e", activebackground="#e27c38").grid(row=row_val, column=3)

# Histórico
historico_lista = tk.Listbox(janela, width=40, height=10, font=("Arial", 12))
historico_lista.grid(row=row_val+1, column=0, columnspan=4)

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="Resultado: ", font=("Arial", 16))
resultado_label.grid(row=row_val+2, column=0, columnspan=4)

# Ajustar o tamanho da janela
janela.geometry("400x800")

# Executar a janela
janela.mainloop()
