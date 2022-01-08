#Tkinter Imports
from tkinter import *

#Tkinter window
root = Tk()
root.title("Calculator")

#Global Variables
is_first = True
first_number = 0
sign = ""

#Tkinter Entry. The calculator screen.
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Function of 0-9
def button_click(number):
    global is_first
    if is_first:
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
    else:
        if e.get() == sign: 
            e.delete(0, END)
            e.insert(0, str(number))
        else:
            current = e.get()
            e.delete(0, END)
            e.insert(0, str(current) + str(number))

#Function of clear button
def button_clear():
    e.delete(0, END)
    global first_number, is_first, sign
    first_number = 0
    is_first = True
    sign = ""

#Function of Arithmetic Operators buttons
def button_sign(number):
    global is_first, first_number, sign
    is_first = False
    first_number = e.get()
    print("First number = " , first_number)
    e.delete(0, END)
    sign = number
    e.insert(0, sign)

#Function of equal button that print the results
def button_equal():
    global first_number, sign
    current = e.get()
    e.delete(0, END)
    if sign=="+":
        result = int(first_number) + int(current)
        e.insert(0, "= " + str(result))
    elif sign=="-":
        result = int(first_number) - int(current)
        e.insert(0, "= " + str(result))
    elif sign=="*":
        result = int(first_number) * int(current)
        e.insert(0, "= " + str(result))
    elif sign=="/":
        result = int(first_number) / int(current)
        e.insert(0, "= " + str(result))


#All Buttons settings
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_add = Button(root, text = "+", padx = 25, pady = 20, command = lambda: button_sign("+"))
button_subtract = Button(root, text = "-", padx = 26.50, pady = 20, command = lambda: button_sign("-"))
button_multiply = Button(root, text = "X", padx = 26, pady = 20, command = lambda: button_sign("*"))
button_divide = Button(root, text = "/", padx = 27, pady = 20, command = lambda: button_sign("/"))
button_equal = Button(root, text = "=", padx = 39, pady = 20, command = button_equal)
button_clear = Button(root, text = "Clear", padx = 30, pady = 20, command = button_clear)


#Grid settings
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)
button_add.grid(row=1, column=3)
button_subtract.grid(row= 2, column=3)
button_multiply.grid(row= 3, column=3)
button_divide.grid(row= 4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=0)


root.mainloop()
