import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack() #side="left"

# two ways of changing attributes
my_label["text"] = "New text"
my_label.config(text="New text 2 ")


def button_clicked():
    print("Button clicked")
    my_label["text"] = input.get()


button = tkinter.Button(text ="Click me", command=button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.pack()


window.mainloop()


def add(*args):
    total = 0
    for num in args:
        total += num

    return total


print(add(1, 2, 4))


def calculate(n, **kwargs):
    print(kwargs) # kwargs is a dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]


calculate(3, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car =Car(make="Nissan", model=None)
print(my_car.make)