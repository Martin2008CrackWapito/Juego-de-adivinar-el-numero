import tkinter as tk
from tkinter import messagebox
from random import randint

num = randint(1, 10)

def verificar_numero(event=None):
    global num
    try:
        play = int(entry.get())
        if play == num:
            messagebox.showinfo("Resultado", "¡Lo has adivinado!")
        elif play < 1 or play > 10:
            messagebox.showwarning("Advertencia", "El número tiene que estar entre 1 y 10")
        elif abs(play - num) <= 2:
            messagebox.showinfo("!Casi!", "Te has quedado a nada de adivinarlo")
        else:
            messagebox.showinfo("¿¡Donde vas!?", "Te has pasado, vuelve a intentarlo")

    except ValueError:
        messagebox.showerror("Error", "Por favor, mete un número que sirva.")

# Ventana principal
root = tk.Tk()
root.title("Juego de adivinar el número")

window_size = 350
root.geometry(f"{window_size}x{window_size}")

root.configure(bg="blue")
root.bind("<Return>", verificar_numero)

entry = tk.Entry(root)
entry.pack(pady=20)

button = tk.Button(root, text="Verificar", command=verificar_numero)
button.pack(pady=10)

root.mainloop()
