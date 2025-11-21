import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# -------- DISPLAY --------
equation = StringVar()
display = Entry(root, textvariable=equation, font=("Arial", 22), bd=8, relief=RIDGE, justify="right")
display.pack(fill="both", ipadx=10, ipady=20, padx=10, pady=10)

# -------- BUTTON FRAME --------
btn_frame = Frame(root, bg="#f0f0f0")
btn_frame.pack()

# Calculator Layout Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Functionality
def click_button(value):
    current = equation.get()
    if value == "=":
        try:
            equation.set(str(eval(current)))
        except:
            equation.set("Error")
    else:
        equation.set(current + value)

# Dynamic Button Creation
row = 0
col = 0

for btn_text in buttons:
    btn = Button(btn_frame, text=btn_text, font=("Arial", 18, "bold"),
                 width=4, height=2, bd=3, relief=RAISED,
                 command=lambda v=btn_text: click_button(v))

    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
