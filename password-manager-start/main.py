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
canvas.grid(column=1 , row=1 )


#Labels
website_title = Label(text="Website: ")
website_title.grid(column=0 , row=2 )
#Text
website = Entry(width=35)
website.grid(column=1 , row=2 )

#Labels
email_username_title = Label(text="Email/Username: ")
email_username_title.grid(column=0 , row=3 )
#Text
email_username = Entry(width=35)
email_username.grid(column=1 , row=3 )

#Labels
password_title = Label(text="Password: " )
password_title.grid(column=0 , row=4)
#Text
password = Entry(width=21)
password.grid(column=1 , row=4 , columnspan=2)

#Buttons
generate_password = Button(text="Generate Password", width=14)
generate_password.grid(column=2 , row=4)

#Buttons
add = Button(text="Add", width=36)
add.grid(column=1 , row=5, columnspan=2)


window.mainloop()