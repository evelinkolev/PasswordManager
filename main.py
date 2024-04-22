from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

website_entry = Entry(bg="white", width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(bg="white", width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(bg="white")
password_entry.grid(column=1, row=3, sticky="W")

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="E")

add_button = Button(text="Add", width=30)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()