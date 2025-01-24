from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
print(type(Label))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button

def button_clicked():
    my_label["text"] = "I got clicked!"
    #print("I got clicked")
    print(input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

#Input
input = Entry(width=10)
input.pack()








window.mainloop()
