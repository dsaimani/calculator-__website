from tkinter import *

# Button press handler
def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

# Equals (=) button handler
def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

# Clear button handler
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

# Backspace (⌫) button handler
def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

# Initialize main window
window = Tk()
window.title("Calculator Program")
window.geometry("500x600")

equation_text = ""
equation_label = StringVar()

# Display label
label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack()

# Frame for buttons
frame = Frame(window)
frame.pack()

# Number buttons
buttons = [
    (1, 0, 0), (2, 0, 1), (3, 0, 2),
    (4, 1, 0), (5, 1, 1), (6, 1, 2),
    (7, 2, 0), (8, 2, 1), (9, 2, 2),
    (0, 3, 0)
]
for (num, row, col) in buttons:
    Button(frame, text=str(num), height=4, width=9, font=35,
           command=lambda n=num: button_press(n)).grid(row=row, column=col)

# Operator buttons
Button(frame, text='+', height=4, width=9, font=35, command=lambda: button_press('+')).grid(row=0, column=3)
Button(frame, text='-', height=4, width=9, font=35, command=lambda: button_press('-')).grid(row=1, column=3)
Button(frame, text='*', height=4, width=9, font=35, command=lambda: button_press('*')).grid(row=2, column=3)
Button(frame, text='/', height=4, width=9, font=35, command=lambda: button_press('/')).grid(row=3, column=3)

# Other functional buttons
Button(frame, text='.', height=4, width=9, font=35, command=lambda: button_press('.')).grid(row=3, column=1)
Button(frame, text='=', height=4, width=9, font=35, command=equals).grid(row=3, column=2)
Button(frame, text='⌫', height=4, width=9, font=("Consolas", 10), command=backspace).grid(row=4, column=0)

# Clear button below the frame
Button(window, text='Clear', height=2, width=30, font=35, command=clear).pack(pady=10)

window.mainloop()
