import tkinter

from palindromic_number import pnum
from Armstrong import arm
from ZONE import print_patten
def palindrom():

    given_num = entry.get()
    if given_num.isdigit():
        label.config(text=str(pnum(int(given_num))))

    else:
        label.config(text="please enter a valid number")


def armstong():

    given_num = entry.get()
    if given_num.isdigit():
        label.config(text=str(arm(int(given_num))))

    else:
        label.config(text="enter a valid number")


def Z_one():

    given_num = entry.get()
    if given_num.isdigit():
        label.config(text=str(print_patten(int(given_num))))

    else:
        label.config(text="please enter a valid number")

window = tkinter.Tk()
window.title("Combination_of_3")
window.geometry("300x200")

entry = tkinter.Entry(window, width=20)
entry.pack(pady=20)

label = tkinter.Label(window, text="Enter a number")
label.pack(pady=20)


button1 = tkinter.Button(window, text="Palindromic_number", command=palindrom)
button2 = tkinter.Button(window, text="Armstrong_number", command=armstong)
button3 = tkinter.Button(window, text="Z_one", command=Z_one)

button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)


window.mainloop()




