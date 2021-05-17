from tkinter import *


def temperature_celsius():
    celsius = (float(e2.get()) - 32) * 5/9
    label_text.set(celsius)


def temperature_fahrenheit():
    fahrenheit = (float(e1.get())) * 9/5 + 32
    label_text.set(fahrenheit)


def activate_button_cels():
    e1.config(state="normal")
    return


def activate_button_fahr():
    e2.config(state="normal")
    return


def combinefunc(self, *funcs):
    def combinedfunc(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combinedfunc


def clear_button():
    e1.delete(0, END)
    e2.delete(0, END)


def exit_button():
    return root.destroy()


root = Tk()


root.geometry("1000x1000")
root.title("Temperature Convertor")
root.config(bg="blue")

myframe = Frame(root)
myframe.pack(side=BOTTOM)

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

leftframe = LabelFrame(root, text="Celsius to Fahrenheit")
leftframe.pack(side=LEFT)

rightframe = LabelFrame(root, text="Fahrenheit to Celsius")
rightframe.pack(side=RIGHT)

label_text = StringVar()

answer = Label(myframe, text="", textvariable=label_text, bg="green", padx=50, pady=25)
answer.pack(side=RIGHT)

e1 = Entry(leftframe, state="readonly")
e1.pack()
e2 = Entry(rightframe, state="readonly")
e2.pack()

act_cels = Button(root, text="Activate - Celsius to Fahrenheit", command=activate_button_cels)
act_cels.pack(side=LEFT)
act_fahr = Button(root, text="Activate - Fahrenheit to Celsius", command=activate_button_fahr)
act_fahr.pack(side=RIGHT)
conver1 = Button(myframe, text="Calculate Conversion", command=combinefunc(temperature_celsius, temperature_fahrenheit))
conver1.pack(side=LEFT)
clear = Button(bottomframe, text="Clear", command=clear_button)
clear.pack(side=LEFT)
fin = Button(bottomframe, text="Exit", command=exit_button)
fin.pack(side=RIGHT)

mainloop()
