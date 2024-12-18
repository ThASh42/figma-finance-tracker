
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Dima\university\2\UX and UI Design 2.1\Figma-finance-tracker\project\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x600")
window.configure(bg = "#FFF6F6")

expenses = 0
income = 5400
balance = income - expenses

def submit_handler():
    global expenses, balance
    new_expense = float(entry_2.get())

    expenses += new_expense
    canvas.itemconfig(tagOrId=expenses_text, text=f"${expenses}")

    balance -= new_expense
    canvas.itemconfig(tagOrId=balance_text, text=f"${balance}")
    

canvas = Canvas(
    window,
    bg = "#FFF6F6",
    height = 600,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    104.0,
    fill="#570064",
    outline="")

canvas.create_text(
    20.0,
    21.0,
    anchor="nw",
    text="Finance Tracker\n",
    fill="#FFFFFF",
    font=("InknutAntiqua Regular", 36 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    172.0,
    152.0,
    image=image_image_1
)

canvas.create_text(
    39.0,
    136.0,
    anchor="nw",
    text=f"${income}",
    fill="#000000",
    font=("Jersey25 Regular", 36 * -1)
)

canvas.create_text(
    39.0,
    114.0,
    anchor="nw",
    text="Income\n",
    fill="#000000",
    font=("InknutAntiqua Regular", 15 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    340.0,
    237.0,
    image=image_image_2
)

balance_text = canvas.create_text(
    39.0,
    221.0,
    anchor="nw",
    text=f"${str(balance)}",
    fill="#000000",
    font=("Jersey25 Regular", 36 * -1)
)

canvas.create_text(
    39.0,
    199.0,
    anchor="nw",
    text="Balance",
    fill="#000000",
    font=("InknutAntiqua Regular", 15 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    509.0,
    155.0,
    image=image_image_3
)

expenses_text = canvas.create_text(
    376.0,
    139.0,
    anchor="nw",
    text="$0",
    fill="#000000",
    font=("Jersey25 Regular", 36 * -1)
)

canvas.create_text(
    376.0,
    117.0,
    anchor="nw",
    text="Expenses\n",
    fill="#000000",
    font=("InknutAntiqua Regular", 15 * -1)
)

canvas.create_text(
    28.0,
    297.0,
    anchor="nw",
    text="Add Expense",
    fill="#000000",
    font=("InknutAntiqua Regular", 32 * -1)
)

canvas.create_text(
    24.0,
    350.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("InknutAntiqua Regular", 24 * -1)
)

canvas.create_text(
    361.0,
    347.0,
    anchor="nw",
    text="Amount ($)",
    fill="#000000",
    font=("InknutAntiqua Regular", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    172.0,
    427.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#DEDEDE",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=34.0,
    y=397.0,
    width=276.0,
    height=59.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    509.0,
    424.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#DEDEDE",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=371.0,
    y=394.0,
    width=276.0,
    height=59.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=submit_handler,
    relief="flat"
)
button_1.place(
    x=191.0,
    y=504.0,
    width=304.0,
    height=69.0
)
window.resizable(False, False)
window.mainloop()
