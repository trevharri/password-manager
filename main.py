from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json

FONT = ("Courier", 12)
DEFAULT_EMAIL = "trevor.harri94@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pass_input.delete(0, END)
    pass_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_fields():
    web_input.delete(0, END)
    user_input.delete(0, END)
    user_input.insert(0, DEFAULT_EMAIL)
    pass_input.delete(0, END)


def write_to_file(data):
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)


def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            password = data[web_input.get()]["password"]
            email = data[web_input.get()]["email"]
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No password found for {web_input.get()}.")
    else:
        if web_input.get() in data:
            pyperclip.copy(password)
            messagebox.showinfo(title=web_input.get(), message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No password found for {web_input.get()}.")

def add_pass():
    web_site = web_input.get()
    user = user_input.get()
    password = pass_input.get()
    new_data = {
        web_site: {
            "email": user,
            "password": password
        }
    }

    if len(web_site) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields blank.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            write_to_file(new_data)
        else:
            # updating old data with new data
            data.update(new_data)
            write_to_file(data)
        finally:
            clear_fields()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(pady=20, padx=20, bg="white")
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg="white", highlightbackground="white")
padlock_logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_logo)
canvas.grid(row=0, column=1)

web_label = Label(text="Website: ", bg="white", fg="black", font=FONT)
web_label.grid(row=1, column=0)
web_input = Entry(width=20, bg="white", fg="black", highlightbackground="white")
web_input.focus()
web_input.grid(row=1, column=1)

user_label = Label(text="Email/Username: ", bg="white", fg="black", font=FONT)
user_label.grid(row=2, column=0)
user_input = Entry(width=35, bg="white", fg="black", highlightbackground="white")
user_input.insert(0, DEFAULT_EMAIL)
user_input.grid(row=2, column=1, columnspan=2)



pass_label = Label(text="Password: ", bg="white", fg="black", font=FONT)
pass_label.grid(row=3, column=0)
pass_input = Entry(width=20, bg="white", fg="black", highlightbackground="white")
pass_input.grid(row=3, column=1)

gen_button = Button(command=gen_password, width=14, text="Generate Password", bg="white",
                    fg="black", font=FONT, highlightbackground="white")
gen_button.grid(row=3, column=2)

add_button = Button(command=add_pass, width=42, text="Add", bg="white",
                    fg="black", font=FONT, highlightbackground="white")
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(command=search, width=13, text="Search", bg="white",
                    fg="black", font=FONT, highlightbackground="white")
search_button.grid(row=1, column=2)

window.mainloop()
