from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
from typing import TextIO

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6,8)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(1, 3)

    password_list = []

    letters = [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    symbols = [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    numbers = [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""

    password = "".join(password_list)

    password_text.delete(0, END)
    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #



def export_data():
    email = Entry.get(email_username)
    password = Entry.get(password_text)
    website_text = Entry.get(website)
    new_data = {
        website_text: {
            "email": email,
            "password": password,
        }
    }



    if len(website_text) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message= "Please don't leave any fields empty!")
    else:
        with open("data.json", "w") as data_file: # type: ignore
            # Reading old data
            data = json.load(data_file)
            # Updating old data with new data
            data.update(new_data)

        with open("data.json", "w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)
            email_username.delete(0,END) #from https://www.tutorialspoint.com/how-to-clear-the-contents-of-a-tkinter-text-widget
            password_text.delete(0,END)
            website.delete(0,END)
            email_username.insert(0, "default@email.com")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1 , row=0 )


#Website Label
website_title = Label(text="Website: ")
website_title.grid(column=0 , row=1 )
#Website Text
website = Entry(width=35)
website.focus()

website.grid(column=1 , row=1, columnspan=2, sticky="w")

#Email/Username Label
email_username_title = Label(text="Email/Username: ")
email_username_title.grid(column=0 , row=2 )
#Email/Username Text
email_username = Entry(width=35)
email_username.insert(0, "changeme@email.com")
email_username.grid(column=1 , row=2, columnspan=2, sticky="w")

#Password Label
password_title = Label(text="Password: " )
password_title.grid(column=0 , row=3, sticky="w")

#Password Text
password_text = Entry(width=22)
password_text.grid(column=1 , row=3, sticky="w")
#Generate Password Button
generate_password = Button(text="Generate Password", command=generate_password, width=14)
generate_password.grid(column=1 , row=3, sticky="e")

#Add Button
add = Button(text="Add", width=30, command=export_data)
add.grid(column=1 , row=4, columnspan=2, sticky="w")


window.mainloop()