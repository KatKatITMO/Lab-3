import tkinter as tk
from tkinter import ttk
import random
import string


def key_gen():
    key = ""
    key1 = generate_4code()
    key2 = generate_4code()
    key3 = generate_4code()
    key = key1 + "-" + key2 + "-" + key3
    lbl_result['text'] = key


def generate_4code():
    while True:
        code = ''.join(random.choice(string.ascii_uppercase) for _ in range(4))
        code_sum = sum(ord(char) - ord('A') + 1 for char in code)
        if 30 <= code_sum <= 35:
            return code

root = tk.Tk()
root.geometry('568x800')
root.title('Bill Cipher')

bg_image = tk.PhotoImage(file='svin.png')
lbl_bg = tk.Label(root, image=bg_image)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

lbl_welcome = ttk.Label(text='CLICK THE BUTTON')
lbl_welcome.place(y=300)
lbl_welcome.pack(anchor='center', pady=10)

lbl_result = ttk.Label()
lbl_result.pack(anchor="s", pady=10)

btn = ttk.Button(text="Click", command=key_gen)
btn.pack(anchor='s', pady=10)

root.mainloop()
