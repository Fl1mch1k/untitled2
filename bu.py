from tkinter import *
from tkinter import ttk

clicks = 0

def click_button():
    global clicks
    clicks += 1

    btn["text"] = f"клік {clicks}"


root = Tk()
root.title("Fl1mch1k.com")
root.geometry("400x300")

btn = ttk.Button(text="Моя кнопка", command=click_button)
btn.pack()

root.mainloop()