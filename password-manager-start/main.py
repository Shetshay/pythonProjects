from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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


website.grid(column=1 , row=1, columnspan=2, sticky="w")

#Email/Username Label
email_username_title = Label(text="Email/Username: ")
email_username_title.grid(column=0 , row=2 )
#Email/Username Text
email_username = Entry(width=35)


email_username.grid(column=1 , row=2, columnspan=2, sticky="w")

#Password Label
password_title = Label(text="Password: " )


password_title.grid(column=0 , row=3, sticky="w")

#Password Text
password_text = Entry(width=21)
password_text.grid(column=1 , row=3, sticky="w")
#Generate Password Button
generate_password = Button(text="Generate Password")


generate_password.grid(column=1 , row=3, sticky="e")

#Add Button
add = Button(text="Add", width=30)
add.grid(column=1 , row=4, columnspan=2, sticky="w")


window.mainloop()