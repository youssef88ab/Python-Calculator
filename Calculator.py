from tkinter import * 

# -----------------------------------------------------

# Basic Customize 

# -----------------------------------------------------

calculator = Tk()
calculator.title("Caclculator")
calculator.geometry("435x507")

# -----------------------------------------------------

# Functions 

# -----------------------------------------------------

def button_press(number):

    global result_text

    result_text += str(number)
    label.set(result_text)


def equals():

    global result_text 

    try :

        total = str(eval(result_text))

        label.set(total)

        result_text = total

    except ZeroDivisionError:

        label.set("Arithmetic Error")

        result_text = ""

    except SyntaxError:

        label.set("Syntax Error")


# -----------------------------------------------------

# Result Outpout 

# -----------------------------------------------------

result_text  = ""

label = StringVar()

result_label = Label(calculator , textvariable=label)
result_label.config(bg="white" , fg="black")
result_label.config(font=('Arial' , 20 , 'bold'))
result_label.config(width=25 , height=2)
result_label.pack()

# -----------------------------------------------------

# Create Numbers Buttons

# -----------------------------------------------------

frame = Frame(calculator)
frame.pack()

button1 = Button(frame , text="1" , height=4 , width=9 , font=35 , command=lambda:button_press(1))
button1.grid(row=0 , column=0)

button2 = Button(frame , text="2" , height=4 , width=9 , font=35 , command=lambda:button_press(2))
button2.grid(row=0 , column=1)

button3 = Button(frame , text="3" , height=4 , width=9 , font=35 , command=lambda:button_press(3))
button3.grid(row=0 , column=2)

button4 = Button(frame , text="4" , height=4 , width=9 , font=35 , command=lambda:button_press(4))
button4.grid(row=1 , column=0)

button5 = Button(frame , text="5" , height=4 , width=9 , font=35 , command=lambda:button_press(5))
button5.grid(row=1 , column=1)

button6 = Button(frame , text="6" , height=4 , width=9 , font=35 , command=lambda:button_press(6))
button6.grid(row=1 , column=2)

button7 = Button(frame , text="7" , height=4 , width=9 , font=35 , command=lambda:button_press(7))
button7.grid(row=2 , column=0)

button8 = Button(frame , text="8" , height=4 , width=9 , font=35 , command=lambda:button_press(8))
button8.grid(row=2 , column=1)

button9 = Button(frame , text="9" , height=4 , width=9 , font=35 , command=lambda:button_press(9))
button9.grid(row=2 , column=2)

button0 = Button(frame , text="0" , height=4 , width=9 , font=35 , command=lambda:button_press(0))
button0.grid(row=3 , column=0)

# -----------------------------------------------------

# Create Operators Buttons

# -----------------------------------------------------

add = Button(frame , text="+" , height=4 , width=9 , font=35 , command=lambda:button_press("+"))
add.grid(row=0 , column=3)

minus = Button(frame , text="-" , height=4 , width=9 , font=35 , command=lambda:button_press("-"))
minus.grid(row=1 , column=3)

divide = Button(frame , text="/" , height=4 , width=9 , font=35 , command=lambda:button_press("/"))
divide.grid(row=2 , column=3)

multiply = Button(frame , text="*" , height=4 , width=9 , font=35 , command=lambda:button_press("*"))
multiply.grid(row=3 , column=3)

# -----------------------------------------------------

# Other Buttons Buttons

# -----------------------------------------------------

point = Button(frame , text="." , height=4 , width=9 , font=35 , command=lambda:button_press("."))
point.grid(row=3 , column=1)

equals = Button(frame , text="=" , height=4 , width=9 , font=35 , command=equals)
equals.grid(row=3 , column=2)

# -----------------------------------------------------

# Other Functionalities 

# -----------------------------------------------------

def BackSpace(event) :

    global result_text

    result_text = result_text[:len(result_text) - 1]
    label.set(result_text)


calculator.bind("<BackSpace>" , BackSpace)

# -----------------------------------------------------


calculator.mainloop()