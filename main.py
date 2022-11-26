import tkinter
import random
import pyperclip
import json

from tkinter import messagebox
from string import ascii_lowercase


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    # password_input.delete(0, tkinter.END)
    base_list = ascii_lowercase
    length = int(spinbox.get())

    if digits.get():
        base_list += '0123456789'

    if uppers.get():
        base_list += ascii_lowercase.upper()

    if specials.get():
        base_list += '!#$%&*+-/=?^_{|}~'

    password = ''.join(random.choice(base_list) for _ in range(length))
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        pass
    else:
        website = website_input.get()
        if data.get(website, 0):
            messagebox.showinfo(title=website,
                                message=f"Login: {data[website]['login']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(message='No such website')


def save_to_file():
    my_website = website_input.get()
    my_email = email_input.get()
    my_password = password_input.get()
    new_data = {
        my_website: {
            'login': my_email,
            'password': my_password
        }
    }

    if not all((my_website, my_email, my_password)):
        messagebox.showinfo(message="Пожалуйста, введите данные")
    else:
        is_ok = messagebox.askokcancel(title=my_website, message=f"Введены следующие значения:\nсайт {my_website},"
                                                                 f"\nимя {my_email},\nпароль {my_password}")
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}
            finally:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
                website_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)
                email_input.delete(0, tkinter.END)
                email_input.insert(0, 'Maura Henriette Franklin')


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
bg_image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text='Email/username:')
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_input = tkinter.Entry(width=32)
website_input.grid(column=1, row=1)

email_input = tkinter.Entry(width=50)
email_input.insert(0, 'Maura Henriette Franklin')
email_input.grid(column=1, row=2, columnspan=2)

password_input = tkinter.Entry(width=32)
password_input.grid(column=1, row=3)

# Buttons
password_button = tkinter.Button(text='Generate Password', command=generator)
password_button.grid(column=2, row=3)

add_button = tkinter.Button(text='Add', command=save_to_file, width=43)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tkinter.Button(text='Search', width=15, command=find_password)
search_button.grid(column=2, row=1)

# CheckButtons
digits = tkinter.BooleanVar()
digits.set(False)
check_digits = tkinter.Checkbutton(text='Цифры', variable=digits)
check_digits.grid(column=1, row=6)

uppers = tkinter.BooleanVar()
uppers.set(False)
check_upper = tkinter.Checkbutton(text='Заглавные', variable=uppers)
check_upper.grid(column=1, row=7)

specials = tkinter.BooleanVar()
specials.set(False)
specials_upper = tkinter.Checkbutton(text='Спецсимволы', variable=specials)
specials_upper.grid(column=1, row=8)

spinbox = tkinter.Spinbox(from_=6, to=15, width=5)
spinbox.grid(column=1, row=5)
spinbox.delete(0, tkinter.END)
spinbox.insert(0, 10)

window.mainloop()
