from tkinter import *

def button_clicked():
    x = float(input.get())
    return label4.config(text=round((x * 1.609), 1)) # edit the lab4.config to output km from miles integer

window = Tk() # setup Tk
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

#Label 1
label = Label(text="Miles")
label.grid(column=3, row=0) # right 3 down 0

#Label 2
label2 = Label(text="Km")
label2.grid(column=3, row=1) # right 3 down 1

#Label 3
label3 = Label(text="is equal to")
label3.grid(column=1, row=1) # right 1 down 1

#Label 4
label4 = Label(text=0) # set the label = to 0
label4.grid(column=2, row=1) # right 2 down 1

# USER Input
input = Entry(width=10)
input.grid(column=2, row=0) # right 2 down 0

#Button
button = Button(text="Calculate", command=button_clicked) # start the calculation from USER Input convert to float
button.grid(column=2, row=2) # right 2 down 2









window.mainloop()
