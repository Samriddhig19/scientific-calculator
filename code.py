from tkinter import *
from fractions import Fraction
from math import sin, radians, degrees, cos, exp, factorial, log, log10, tan, sqrt, pi, asin, acos, atan

memory = []
deg = True
π = pi

def on_number_click(event):
    temp = event.widget.cget('text')
    s = l.cget('text')
    if temp == 'fac(':
        temp = 'factorial('
    elif temp == 'l10(':
        temp = 'log10('
    elif temp == 'po(':
        temp = 'pow('
    elif (temp == 'sin(' and deg):
        temp = 'sin(radians('
    elif (temp == 'cos(' and deg):
        temp = 'cos(radians('
    elif (temp == 'tan(' and deg):
        temp = 'tan(radians('
    elif (temp == 'asin(' and deg):
        temp = 'degrees(asin('
    elif (temp == 'acos(' and deg):
        temp = 'degrees(acos('
    elif (temp == 'atan(' and deg):
        temp = 'degrees(atan('
        
    if (s == '0'):
        s = temp
    else:
        s += temp
    l.config(text = s)
    
def on_c_click(l):
    s = l.cget('text')
    if (s == 'No more History'):
        l.config(text = '0')
        return
    memory.append(s)
    l.config(text = '0')
    
def key_press(event):
    if ((event.char >= '0' and event.char <= '9') or event.char == '+' or event.char == '-' or event.char == '*' or event.char == '/' or event.char == ','):
        s = l.cget('text')
        if (s == '0'):
            s = event.char
        else:
            s += event.char
        l.config(text = s)
        
def delete(event):
    s = l.cget('text')
    s = s[:len(s) - 1]
    if len(s) == 0:
        s = '0'
    l.config(text = s)
    
def evaluate(event):
    s = l.cget('text')
    s = s.split('\n')
    if s[len(s) - 1].isdigit():
        value = l.cget('text')
    else:
        value = eval(s[len(s) - 1])
    if (type(value) == float):
        value = float("{:.2f}".format(value))
    s = '\n'.join(s)
    s += '\n'
    s += str(value)
    l.config(text = s)
    
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def fract_converter(event):
    s = l.cget('text')
    s = s.split('\n')
    if (len(s) > 1):
        if isfloat(s[1]):
            num = float(s[1])
            s[1] = str(Fraction(num).limit_denominator())
            s = '\n'.join(s)
            l.config(text = s)
    else:
        if isfloat(s[0]):
            num = float(s[0])
            s[0] = str(Fraction(num).limit_denominator())
            s = '\n'.join(s)
            l.config(text = s)
            
def print_prev():
    if len(memory) == 0:
        l.config(text = 'No more History')
        return
    s = memory[len(memory) - 1]
    memory.pop()
    l.config(text = s)
    memory.pop

def degree_sci():
    root.geometry('710x500')
    root.maxsize(710, 500)
    root.minsize(710, 500)
    global deg
    deg = True

def radian_sci():
    root.geometry('710x500')
    root.maxsize(710, 500)
    root.minsize(710, 500)
    global deg
    deg = False
    
def normalise():
    root.geometry('333x500')
    root.maxsize(333, 500)
    root.minsize(333, 500)

root = Tk()
root.title('Scientific Calculator')
root.geometry('333x519')
root.maxsize(333, 519)
root.minsize(333, 519)
root.wm_iconbitmap('Untitled.ico')

fr1 = Frame(root, borderwidth = 5, relief = 'sunken', height = 180)
fr1.pack(side = 'top', fill = 'x')
fr1.pack_propagate(False)

fr2 = Frame(root, borderwidth = 5, height = 320)
fr2.pack(fill = 'x')
fr2.pack_propagate(False)

l = Label(fr1, bg = 'white', height = 180, width = 333, font = 'calibri 28 bold', anchor = 'se', text = '0')
l.pack()

b1 = Button(fr2, text = '7', font = 'calibri 28 bold')
b1.grid(row = 0, column = 0)
b1.bind('<Button-1>', on_number_click)

b2 = Button(fr2, text = '8', font = 'calibri 28 bold')
b2.grid(row = 0, column = 1)
b2.bind('<Button-1>', on_number_click)

b3 = Button(fr2, text = '9', font = 'calibri 28 bold')
b3.grid(row = 0, column = 2)
b3.bind('<Button-1>', on_number_click)

b4 = Button(fr2, text = '4', font = 'calibri 28 bold')
b4.grid(row = 1, column = 0)
b4.bind('<Button-1>', on_number_click)

b5 = Button(fr2, text = '5', font = 'calibri 28 bold')
b5.grid(row = 1, column = 1)
b5.bind('<Button-1>', on_number_click)

b6 = Button(fr2, text = '6', font = 'calibri 28 bold')
b6.grid(row = 1, column = 2)
b6.bind('<Button-1>', on_number_click)

b7 = Button(fr2, text = '1', font = 'calibri 28 bold')
b7.grid(row = 2, column = 0)
b7.bind('<Button-1>', on_number_click)

b8 = Button(fr2, text = '2', font = 'calibri 28 bold')
b8.grid(row = 2, column = 1)
b8.bind('<Button-1>', on_number_click)

b9 = Button(fr2, text = '3', font = 'calibri 28 bold')
b9.grid(row = 2, column = 2)
b9.bind('<Button-1>', on_number_click)

b10 = Button(fr2, text = '0', font = 'calibri 28 bold')
b10.grid(row = 3, column = 1)
b10.bind('<Button-1>', on_number_click)

b11 = Button(fr2, text = ')', font = 'calibri 28 bold')
b11.grid(row = 3, column = 2)
b11.bind('<Button-1>', on_number_click)

b12 = Button(fr2, text = '(', font = 'calibri 28 bold')
b12.grid(row = 3, column = 0)
b12.bind('<Button-1>', on_number_click)

c = Button(fr2, text = 'C', font = 'calibri 28 bold', command = lambda: on_c_click(l), width = 4)
c.grid(row = 0, column = 3)

b = Button(fr2, text = '<--', font = 'calibri 28 bold', width = 5)
b.grid(row = 0, column = 4)

op1 = Button(fr2, text = '+', font = 'calibri 28 bold', width = 4)
op1.grid(row = 1, column = 3)
op1.bind('<Button-1>', on_number_click)

op2 = Button(fr2, text = '-', font = 'calibri 28 bold', width = 5)
op2.grid(row = 1, column = 4)
op2.bind('<Button-1>', on_number_click)

op3 = Button(fr2, text = '*', font = 'calibri 28 bold', width = 4)
op3.grid(row = 2, column = 3)
op3.bind('<Button-1>', on_number_click)

op4 = Button(fr2, text = '/', font = 'calibri 28 bold', width = 5)
op4.grid(row = 2, column = 4)
op4.bind('<Button-1>', on_number_click)

eq = Button(fr2, text = '=', font = 'calibri 28 bold', width = 4)
eq.grid(row = 3, column = 3)
eq.bind('<Button-1>', evaluate)

util = Button(fr2, text = 'a/b', font = 'calibri 28 bold', width = 5)
util.grid(row = 3, column = 4)
util.bind('<Button-1>', fract_converter)

b13 = Button(fr2, text = '.', font = 'calibri 28 bold', width = 4)
b13.grid(row = 0, column = 5)
b13.bind('<Button-1>', on_number_click)

b.bind('<Button-1>', delete)

root.bind("<Key>", key_press)
root.bind("<BackSpace>", delete)
root.bind('<Return>', evaluate)

main_menu = Menu(root)
m1 = Menu(main_menu, tearoff = 0)
m1.add_command(label = 'Scientific Calculator (radians)', command = radian_sci)
m1.add_command(label = 'Scientific Calculator (degrees)', command = degree_sci)
m1.add_command(label = 'Normal Calculator', command = normalise)

m2 = Menu(main_menu, tearoff = 0)
m2.add_command(label = 'Show Previous', command = print_prev)

main_menu.add_cascade(label = 'Calculators', menu = m1)
main_menu.add_cascade(label = 'History', menu = m2)
root.config(menu = main_menu)

sc_b1 = Button(fr2, text = 'sin(', font = 'calibri 28 bold')
sc_b1.grid(row = 0, column = 6)
sc_b1.bind('<Button-1>', on_number_click)

sc_b2 = Button(fr2, text = 'cos(', font = 'calibri 28 bold')
sc_b2.grid(row = 0, column = 7)
sc_b2.bind('<Button-1>', on_number_click)

sc_b3 = Button(fr2, text = 'tan(', font = 'calibri 28 bold')
sc_b3.grid(row = 0, column = 8)
sc_b3.bind('<Button-1>', on_number_click)

sc_b4 = Button(fr2, text = 'exp(', font = 'calibri 28 bold')
sc_b4.grid(row = 1, column = 5)
sc_b4.bind('<Button-1>', on_number_click)

sc_b5 = Button(fr2, text = 'fac(', font = 'calibri 28 bold')
sc_b5.grid(row = 1, column = 6)
sc_b5.bind('<Button-1>', on_number_click)

sc_b6 = Button(fr2, text = 'log(', font = 'calibri 28 bold')
sc_b6.grid(row = 1, column = 7)
sc_b6.bind('<Button-1>', on_number_click)

sc_b7 = Button(fr2, text = 'l10(', font = 'calibri 28 bold')
sc_b7.grid(row = 1, column = 8)
sc_b7.bind('<Button-1>', on_number_click)

sc_b8 = Button(fr2, text = 'sqrt(', font = 'calibri 28 bold')
sc_b8.grid(row = 2, column = 5)
sc_b8.bind('<Button-1>', on_number_click)

sc_b9 = Button(fr2, text = 'π', font = 'calibri 28 bold', width = 4)
sc_b9.grid(row = 2, column = 6)
sc_b9.bind('<Button-1>', on_number_click)

sc_b10 = Button(fr2, text = 'po(', font = 'calibri 28 bold')
sc_b10.grid(row = 2, column = 7)
sc_b10.bind('<Button-1>', on_number_click)

sc_b11 = Button(fr2, text = 'abs(', font = 'calibri 28 bold')
sc_b11.grid(row = 2, column = 8)
sc_b11.bind('<Button-1>', on_number_click)

sc_b12 = Button(fr2, text = ',', font = 'calibri 28 bold', width = 4)
sc_b12.grid(row = 3, column = 5)
sc_b12.bind('<Button-1>', on_number_click)

sc_b13 = Button(fr2, text = 'asin(', font = 'calibri 28 bold', width = 4)
sc_b13.grid(row = 3, column = 6)
sc_b13.bind('<Button-1>', on_number_click)

sc_b14 = Button(fr2, text = 'acos(', font = 'calibri 28 bold', width = 4)
sc_b14.grid(row = 3, column = 7)
sc_b14.bind('<Button-1>', on_number_click)

sc_b15 = Button(fr2, text = 'atan(', font = 'calibri 28 bold', width = 4)
sc_b15.grid(row = 3, column = 8)
sc_b15.bind('<Button-1>', on_number_click)

root.mainloop()