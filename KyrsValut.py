import os, sys
from tkinter import *
import requests
from tkinter.messagebox import showerror

response = requests.get(f"https://www.cbr-xml-daily.ru/daily_json.js").json()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def exchange_rates():
    rates = rates_entry.get().upper()
    if not rates:
        rates_info.config(text="")
        showerror("Ошибка", "Строка не может быть пустой")
    else:
        if rates not in response["Valute"].keys():
            rates_info.config(text="")
            showerror("Ошибка", "Код валюты не найден!")
        else:
            rates_info.config(text=f"Курс: {round(response["Valute"][rates]["Value"], 2)} ₽\n"
                                   f"Валюта: {response["Valute"][rates]["Name"]}")


window = Tk()
window.geometry("400x200")
window.title("Курс валют")
window.iconbitmap("finance-saving.ico")
window.resizable(False, False)

welcome_text = Label(window, text="Курсы валют", font=("Time New Roman", 12, "bold"))
welcome_text.pack(expand=True, anchor=CENTER)

rates_entry = Entry(window)
rates_entry.pack(expand=True, anchor=CENTER)
rates_entry.focus()

btn = Button(window, text="Показать результат", command=exchange_rates)
btn.pack(expand=True, anchor=CENTER)

rates_info = Label(window, font=("Time New Roman", 20))
rates_info.pack(expand=True, anchor=CENTER)

window.mainloop()
