from tkinter import *

def button_clicked():
    my_label["text"] = "I got clicked!"
    #print("I got clicked")
    print(input.get())


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50,pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

#Button
button2 = Button(text="New Button", command=button_clicked)
#button.pack()
button2.grid(column=2, row=0)


#Input
input = Entry(width=10)
#input.pack()
input.grid(column=3, row=3)








window.mainloop()
