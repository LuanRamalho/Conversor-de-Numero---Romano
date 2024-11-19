import tkinter as tk
from tkinter import messagebox

# Função para converter um número inteiro em número romano
def int_to_roman(num):
    if num < 1 or num > 3999:
        return "Número inválido. Digite um número entre 1 e 3999."
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

# Função para realizar a conversão e atualizar a interface
def convert_to_roman():
    try:
        num = int(entry.get())
        roman = int_to_roman(num)
        result_label.config(text=f"Resultado: {roman}", fg="green")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número inteiro válido!")

# Configuração da janela principal
window = tk.Tk()
window.title("Conversor de Números Romanos")
window.geometry("450x300")
window.configure(bg="#f7d7da")

# Elementos da interface
title_label = tk.Label(
    window, text="Conversor de Números Inteiros para Romanos",
    font=("Helvetica", 14, "bold"), bg="#f7d7da", fg="#2c2b2b"
)
title_label.pack(pady=10)

entry_label = tk.Label(
    window, text="Digite um número inteiro (1-3999):",
    font=("Helvetica", 10), bg="#f7d7da", fg="#2c2b2b"
)
entry_label.pack()

entry = tk.Entry(window, font=("Helvetica", 12), justify="center", width=10)
entry.pack(pady=5)

convert_button = tk.Button(
    window, text="Converter", command=convert_to_roman,
    font=("Helvetica", 12), bg="#ff6f61", fg="white", activebackground="#ff847c", activeforeground="white"
)
convert_button.pack(pady=10)

result_label = tk.Label(
    window, text="", font=("Helvetica", 12, "bold"),
    bg="#f7d7da"
)
result_label.pack(pady=20)

# Rodando o programa
window.mainloop()
