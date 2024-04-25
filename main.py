from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_read:
                data = json.load(data_read)
        except FileNotFoundError:
            with open("data.json", "w") as data_write:
                json.dump(new_data, data_write, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_write:
                json.dump(data, data_write, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_read:
            data = json.load(data_read)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
myimg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=myimg)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(bg="white", width=33)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(bg="white", width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "testov@test.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(bg="white", width=33)
password_entry.grid(column=1, row=3, sticky="W")

generate_password_button = Button(text="Generate Password", width=20, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="E")

search_button = Button(text="Search", width=20, command=find_password)
search_button.grid(column=2, row=1, sticky="E")

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
