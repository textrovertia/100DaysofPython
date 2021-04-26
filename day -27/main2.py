from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


def button_clicked():
    print("Button clicked")
    label["text"] = user_input.get()


label = Label(text="Blue")
label.place(x=100, y=200)

button = Button(text ="Click me", command=button_clicked)
button.grid(column=2, row=2)

user_input = Entry(width=10)
user_input.grid(column=0, row=0)



window.mainloop()