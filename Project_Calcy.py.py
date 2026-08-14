from tkinter import *
import math
expr = ""  # Global expression string

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

def square_root():
    global expr
    try:
        num=float(expr)
        result=math.sqrt(num)
        display.set(str(result))
        expr=str(result)
    except:
        display.set("Error")
        expr=""

def sine():
    global expr
    try:
        angle=float(expr)
        result=math.sin(math.radians(angle))
        display.set(str(result))
    except:
        display.set("Error")
        expr=""

def cose():
    global expr
    try:
        angle=float(expr)
        result=math.cos(math.radians(angle))
        display.set(str(result))
    except:
        display.set("Error")
        expr=""

def tangent():
    global expr
    try:
        result=math.tan(math.radians(float(expr)))
        display.set(str(result))
    except:
        display.set("Error")
        expr=""

def percentage():
    global expr
    try:
        num=float(expr)
        result=num/100
        display.set(str(result))
        expr=str(result)
    except:
        display.set("Error")
        expr=""

def log_e():
    global expr
    try:
        num=float(expr)
        result=math.log(num)
        display.set(str(result))
        expr=str(result)
    except:
        display.set("Error")
        expr=""

def log_e():
    global expr
    try:
        num=float(expr)
        result=math.log(num)
        display.set(str(result))
        expr=str(result)
    except:
        display.set("Error")
        expr=""

def power():
    global expr
    try:
        result=math.eval(expr)
        display.set(str(result))
        expr=str(result)
    except:
        display.set("Error")
        expr=""

def factorial():
    global expr
    try:
        result=math.factorial(int(expr))
        display.set(str(result))
        expr=str(result)
    except:
        display.set("Error")
        expr=""

def pi():
    global expr
    expr+=str(math.pi)
    display.set(expr)


if __name__ == "__main__":
    root = Tk()
    root.configure(bg="light green")
    root.title("Advanced Calculator")
    root.geometry("500x300")

    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=4, ipadx=70)

    # Number buttons
    btn1 = Button(root, text='1', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
    btn1.grid(row=2, column=0)
    btn2 = Button(root, text='2', fg='black', bg='red', command=lambda: press(2), height=1, width=7)
    btn2.grid(row=2, column=1)
    btn3 = Button(root, text='3', fg='black', bg='red', command=lambda: press(3), height=1, width=7)
    btn3.grid(row=2, column=2)
    btn4 = Button(root, text='4', fg='black', bg='red', command=lambda: press(4), height=1, width=7)
    btn4.grid(row=3, column=0)
    btn5 = Button(root, text='5', fg='black', bg='red', command=lambda: press(5), height=1, width=7)
    btn5.grid(row=3, column=1)
    btn6 = Button(root, text='6', fg='black', bg='red', command=lambda: press(6), height=1, width=7)
    btn6.grid(row=3, column=2)
    btn7 = Button(root, text='7', fg='black', bg='red', command=lambda: press(7), height=1, width=7)
    btn7.grid(row=4, column=0)
    btn8 = Button(root, text='8', fg='black', bg='red', command=lambda: press(8), height=1, width=7)
    btn8.grid(row=4, column=1)
    btn9 = Button(root, text='9', fg='black', bg='red', command=lambda: press(9), height=1, width=7)
    btn9.grid(row=4, column=2)
    btn0 = Button(root, text='0', fg='black', bg='red', command=lambda: press(0), height=1, width=7)
    btn0.grid(row=5, column=0)
    btn10= Button(root, text='sqrt', fg='black', bg='red', command=lambda:square_root(), height=1, width=7)
    btn10.grid(row=6, column=1)
    btn11= Button(root, text='sin', fg='black', bg='red', command=lambda:sine(), height=1, width=7)
    btn11.grid(row=6, column=2)
    btn12= Button(root, text='cos', fg='black', bg='red', command=lambda:cose(), height=1, width=7)
    btn12.grid(row=6, column=3)
    btn13= Button(root, text='%', fg='black', bg='red', command=lambda:percentage(), height=1, width=7)
    btn13.grid(row=7, column=0)
    btn14= Button(root, text='log', fg='black', bg='red', command=lambda:log_e(), height=1, width=7)
    btn14.grid(row=7, column=1)
    btn15= Button(root, text='tan', fg='black', bg='red', command=lambda:tangent(), height=1, width=7)
    btn15.grid(row=7, column=2)
    btn16= Button(root, text='^', fg='black', bg='red', command=lambda: press("**"), height=1, width=7)
    btn16.grid(row=7, column=3)
    btn17= Button(root, text='!', fg='black', bg='red', command=lambda:factorial(), height=1, width=7)
    btn17.grid(row=2, column=4)
    btn18= Button(root, text='pi', fg='black', bg='red', command=lambda:pi(), height=1, width=7)
    btn18.grid(row=3,column=4)
    

    # Operator buttons
    plus = Button(root, text='+', fg='black', bg='red', command=lambda: press('+'), height=1, width=7)
    plus.grid(row=2, column=3)
    minus = Button(root, text='-', fg='black', bg='red', command=lambda: press('-'), height=1, width=7)
    minus.grid(row=3, column=3)
    mult = Button(root, text='*', fg='black', bg='red', command=lambda: press('*'), height=1, width=7)
    mult.grid(row=4, column=3)
    div = Button(root, text='/', fg='black', bg='red', command=lambda: press('/'), height=1, width=7)
    div.grid(row=5, column=3)

    # Other buttons
    eq = Button(root, text='=', fg='black', bg='red', command=equal, height=1, width=7)
    eq.grid(row=5, column=2)
    clr = Button(root, text='Clear', fg='black', bg='red', command=clear, height=1, width=7)
    clr.grid(row=5, column=1)
    dot = Button(root, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7)
    dot.grid(row=6, column=0)

    root.mainloop()