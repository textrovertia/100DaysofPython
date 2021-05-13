
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_info():
    website = website_entry.get()
    email = email_entry.get()
    user_password = password_entry.get()

    if len(website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Not all fields are filled")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n \nEmail: {email}\n"
                                                              f"Password: {user_password}\n"
                                                              f"Is it okay to save?")
        if is_ok:
            with open("passwords.txt", 'a') as file:
                file.write(f"{website} | {email} | {user_password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_entry = Entry(width=35)
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_entry = Entry(width=35)
email_label.grid(column=0, row=2)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "adwoaasante91@gmail.com")

password_label = Label(text="Password:")
password_entry = Entry(width=35)
password_button = Button(width=15, text="Generate Password", command=generate_password)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3, columnspan=2)
password_button.grid(column=3, row=3)


add_button = Button(width=20, text="Add", command=save_info)
add_button.grid(column=1, row=4)






window.mainloop()