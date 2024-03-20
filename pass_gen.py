import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import Scale
import random
import string
import pyperclip

def generate_password():
    length = scale_length.get()
    if var.get() == 0:
        charset = string.ascii_letters + string.digits
    else:
        charset = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(charset) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def copy_to_clipboard():
    password = entry_password.get()
    pyperclip.copy(password)
    messagebox.showinfo("Скопировано", "Пароль скопирован в буфер обмена")

root = tk.Tk()
root.title("Генератор паролей")
root.geometry('400x150')
root.resizable(False, False)

frame_type = tk.Frame(root)
frame_type.pack(fill=tk.X, padx=5, pady=5)

var = tk.IntVar()
rad1 = ttk.Radiobutton(frame_type, text="Буквы и числа", variable=var, value=0)
rad2 = ttk.Radiobutton(frame_type, text="Буквы, числа и символы", variable=var, value=1)
rad1.pack(side=tk.LEFT)
rad2.pack(side=tk.LEFT)

frame_length = tk.Frame(root)
frame_length.pack(fill=tk.X, padx=5, pady=5)

tk.Label(frame_length, text="Длина пароля:").pack(side=tk.LEFT)
scale_length = Scale(frame_length, from_=6, to_=128, orient=tk.HORIZONTAL, command=lambda x: generate_password())
scale_length.set(12)
scale_length.pack(side=tk.LEFT, fill=tk.X, expand=True)

entry_password = tk.Entry(root, width=400)
entry_password.pack(fill=tk.X, padx=5, pady=5)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=5)

button_generate = tk.Button(buttons_frame, text="Сгенерировать пароль", command=generate_password)
button_generate.pack(side=tk.LEFT, padx=14)

button_copy = tk.Button(buttons_frame, text="Копировать", command=copy_to_clipboard)
button_copy.pack(side=tk.LEFT)

generate_password()  # Генерация начального пароля при запуске
root.mainloop()
