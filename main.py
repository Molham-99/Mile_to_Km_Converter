from tkinter import *

window = Tk()
window.minsize(width=200, height=100)
window.title("Mile to Kilometer Converter")
window.config(padx=10, pady=30)

is_equal_to = Label(text="Is equal to", font=("Arial", 10, "bold"))
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10, pady=10)

inter = Entry(width=8, textvariable=IntVar())
inter.grid(column=1, row=0)

mile = Label(text="Miles", font=("Arial", 10, "bold"))
mile.grid(column=2, row=0)

k_m = Label(text="KM", font=("Arial", 10, "bold"))
k_m.grid(column=2, row=1)

result = Label(text="0")
result.grid(column=1, row=1)


def the_result():
    mile.grid(column=2, row=0)
    k_m.grid(column=2, row=1)
    hold = float(inter.get())
    formula = round(hold * 1.60934, 4)
    result.config(text=formula)


def opposite():
    k_m.grid(column=2, row=0)
    mile.grid(column=2, row=1)
    hold = float(inter.get())
    formula = round(hold / 1.60934, 4)
    result.config(text=formula)


def checkbutton_used():
    if checked_state.get() == 1:
        k_m.grid(column=2, row=0)
        mile.grid(column=2, row=1)
        hold = float(inter.get())
        formula = round(hold / 1.60934, 4)
        result.config(text=formula)
    else:
        the_result()


checked_state = IntVar()
checkbutton = Checkbutton(text="Switch", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=3, row=1)
button = Button(text="Calculate", command=checkbutton_used)
button.grid(column=1, row=3)

window.mainloop()
