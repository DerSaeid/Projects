from tkinter import *
from tkinter.font import BOLD
window = Tk()
window.geometry('200x200')
window.resizable(False, False)
window.title('Mini Game')
#==========================Random=====================
lis_ch = [1, 2, 3, 4, 5, 6, 7, 8]
from random import choice
def rand_start():
    global lis_ch
    cho = choice(lis_ch)
    lis_ch.remove(cho)
    return cho

#==========================Button=====================
one = Button(window, text=rand_start(), command=lambda: one_f())
o_n = 1
x1 = 10
y1 = 10
one.place(x=x1, y=y1, width=60, height=60)

two = Button(window, text=rand_start(), command=lambda: two_f())
tw_n = 2
x2 = 70
y2 = 10
two.place(x=x2, y=y2, width=60, height=60)

three = Button(window, text=rand_start(), command=lambda: three_f())
tr_n = 3
x3 = 130
y3 = 10
three.place(x=x3, y=y3, width=60, height=60)

four = Button(window, text=rand_start(), command=lambda: four_f())
fo_n = 4
x4 = 10
y4 = 70
four.place(x=x4, y=y4, width=60, height=60)

five = Button(window, text=rand_start(), command=lambda: five_f())
fi_n = 5
x5 = 70
y5 = 70
five.place(x=x5, y=y5, width=60, height=60)

six = Button(window, text=rand_start(), command=lambda: six_f())
si_n = 6
x6 = 130
y6 = 70
six.place(x=x6, y=y6, width=60, height=60)

seven = Button(window, text=rand_start(),  command=lambda: seven_f())
se_n = 7
x7 = 10
y7 = 130
seven.place(x=x7, y=y7, width=60, height=60)

eight = Button(window, text=rand_start(), command=lambda: eight_f())
e_n = 8
x8 = 70
y8 = 130
eight.place(x=x8, y=y8, width=60, height=60)

empty = Button(window, text='')
empty_number = 9
x = 130
y = 130
empty.place(x=x, y=y, width=60, height=60)



#=======================================funcs==========================
def one_f():
    global empty_number
    global o_n
    if (o_n == 1 and (empty_number == 2 or 
    empty_number == 4)) or (o_n == 2 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 3)) or (o_n == 3 and (empty_number == 2 or 
    empty_number == 6)) or (o_n == 4 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 7 )) or (o_n == 5 and (empty_number == 2 or 
    empty_number == 4 or empty_number == 6 or empty_number == 8)) or (o_n == 6 and (empty_number == 3 or 
    empty_number == 5 or empty_number == 9)) or (o_n == 7 and (empty_number == 4 or 
    empty_number == 8)) or (o_n == 8 and (empty_number == 5 or 
    empty_number == 7 or empty_number == 9)) or (o_n == 9 and (empty_number == 6 or 
    empty_number == 8)):
        global x
        global y
        global x1
        global y1
        one.place(x=x, y=y)
        empty.place(x=x1, y=y1)
        x, x1 = x1, x
        y, y1 = y1, y
        o_n, empty_number = empty_number, o_n


def two_f():
    global empty_number
    global tw_n
    if (tw_n == 1 and (empty_number == 2 or 
    empty_number == 4)) or (tw_n == 2 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 3)) or (tw_n == 3 and (empty_number == 2 or 
    empty_number == 6)) or (tw_n == 4 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 7 )) or (tw_n == 5 and (empty_number == 2 or 
    empty_number == 4 or empty_number == 6 or empty_number == 8)) or (tw_n == 6 and (empty_number == 3 or 
    empty_number == 5 or empty_number == 9)) or (tw_n == 7 and (empty_number == 4 or 
    empty_number == 8)) or (tw_n == 8 and (empty_number == 5 or 
    empty_number == 7 or empty_number == 9)) or (tw_n == 9 and (empty_number == 6 or 
    empty_number == 8)):
        global x
        global y
        global x2
        global y2
        two.place(x=x, y=y)
        empty.place(x=x2, y=y2)
        x, x2 = x2, x
        y, y2 = y2, y
        tw_n, empty_number = empty_number, tw_n


def three_f():
    global empty_number
    global tr_n
    if (tr_n == 1 and (empty_number == 2 or 
    empty_number == 4)) or (tr_n == 2 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 3)) or (tr_n == 3 and (empty_number == 2 or 
    empty_number == 6)) or (tr_n == 4 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 7 )) or (tr_n == 5 and (empty_number == 2 or 
    empty_number == 4 or empty_number == 6 or empty_number == 8)) or (tr_n == 6 and (empty_number == 3 or 
    empty_number == 5 or empty_number == 9)) or (tr_n == 7 and (empty_number == 4 or 
    empty_number == 8)) or (tr_n == 8 and (empty_number == 5 or 
    empty_number == 7 or empty_number == 9)) or (tr_n == 9 and (empty_number == 6 or 
    empty_number == 8)):
        global x
        global y
        global x3
        global y3
        three.place(x=x, y=y)
        empty.place(x=x3, y=y3)
        x, x3 = x3, x
        y, y3 = y3, y
        tr_n, empty_number = empty_number, tr_n


def four_f():
    global empty_number
    global fo_n
    if (fo_n == 1 and (empty_number == 2 or 
    empty_number == 4)) or (fo_n == 2 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 3)) or (fo_n == 3 and (empty_number == 2 or 
    empty_number == 6)) or (fo_n == 4 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 7 )) or (fo_n == 5 and (empty_number == 2 or 
    empty_number == 4 or empty_number == 6 or empty_number == 8)) or (fo_n == 6 and (empty_number == 3 or 
    empty_number == 5 or empty_number == 9)) or (fo_n == 7 and (empty_number == 4 or 
    empty_number == 8)) or (fo_n == 8 and (empty_number == 5 or 
    empty_number == 7 or empty_number == 9)) or (fo_n == 9 and (empty_number == 6 or 
    empty_number == 8)):
        global x
        global y
        global x4
        global y4
        four.place(x=x, y=y)
        empty.place(x=x4, y=y4)
        x, x4 = x4, x
        y, y4 = y4, y
        fo_n, empty_number = empty_number, fo_n


def five_f():
    global empty_number
    global fi_n
    if (fi_n == 1 and (empty_number == 2 or 
    empty_number == 4)) or (fi_n == 2 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 3)) or (fi_n == 3 and (empty_number == 2 or 
    empty_number == 6)) or (fi_n == 4 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 7 )) or (fi_n == 5 and (empty_number == 2 or 
    empty_number == 4 or empty_number == 6 or empty_number == 8)) or (fi_n == 6 and (empty_number == 3 or 
    empty_number == 5 or empty_number == 9)) or (fi_n == 7 and (empty_number == 4 or 
    empty_number == 8)) or (fi_n == 8 and (empty_number == 5 or 
    empty_number == 7 or empty_number == 9)) or (fi_n == 9 and (empty_number == 6 or 
    empty_number == 8)):
        global x
        global y
        global x5
        global y5
        five.place(x=x, y=y)
        empty.place(x=x5, y=y5)
        x, x5 = x5, x
        y, y5 = y5, y
        fi_n, empty_number = empty_number, fi_n


def six_f():
    global empty_number
    global si_n
    if (si_n == 1 and (empty_number == 2 or 
    empty_number == 4)) or (si_n == 2 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 3)) or (si_n == 3 and (empty_number == 2 or 
    empty_number == 6)) or (si_n == 4 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 7 )) or (si_n == 5 and (empty_number == 2 or 
    empty_number == 4 or empty_number == 6 or empty_number == 8)) or (si_n == 6 and (empty_number == 3 or 
    empty_number == 5 or empty_number == 9)) or (si_n == 7 and (empty_number == 4 or 
    empty_number == 8)) or (si_n == 8 and (empty_number == 5 or 
    empty_number == 7 or empty_number == 9)) or (si_n == 9 and (empty_number == 6 or 
    empty_number == 8)):
        global x
        global y
        global x6
        global y6
        six.place(x=x, y=y)
        empty.place(x=x6, y=y6)
        x, x6 = x6, x
        y, y6 = y6, y
        si_n, empty_number = empty_number, si_n


def seven_f():
    global empty_number
    global se_n
    if (se_n == 1 and (empty_number == 2 or 
    empty_number == 4)) or (se_n == 2 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 3)) or (se_n == 3 and (empty_number == 2 or 
    empty_number == 6)) or (se_n == 4 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 7 )) or (se_n == 5 and (empty_number == 2 or 
    empty_number == 4 or empty_number == 6 or empty_number == 8)) or (se_n == 6 and (empty_number == 3 or 
    empty_number == 5 or empty_number == 9)) or (se_n == 7 and (empty_number == 4 or 
    empty_number == 8)) or (se_n == 8 and (empty_number == 5 or 
    empty_number == 7 or empty_number == 9)) or (se_n == 9 and (empty_number == 6 or 
    empty_number == 8)):
        global x
        global y
        global x7
        global y7
        seven.place(x=x, y=y)
        empty.place(x=x7, y=y7)
        x, x7 = x7, x
        y, y7 = y7, y
        se_n, empty_number = empty_number, se_n


def eight_f():
    global empty_number
    global e_n
    if (e_n == 1 and (empty_number == 2 or 
    empty_number == 4)) or (e_n == 2 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 3)) or (e_n == 3 and (empty_number == 2 or 
    empty_number == 6)) or (e_n == 4 and (empty_number == 1 or 
    empty_number == 5 or empty_number == 7 )) or (e_n == 5 and (empty_number == 2 or 
    empty_number == 4 or empty_number == 6 or empty_number == 8)) or (e_n == 6 and (empty_number == 3 or 
    empty_number == 5 or empty_number == 9)) or (e_n == 7 and (empty_number == 4 or 
    empty_number == 8)) or (e_n == 8 and (empty_number == 5 or 
    empty_number == 7 or empty_number == 9)) or (e_n == 9 and (empty_number == 6 or 
    empty_number == 8)):
        global x
        global y
        global x8
        global y8
        eight.place(x=x, y=y)
        empty.place(x=x8, y=y8)
        x, x8 = x8, x
        y, y8 = y8, y
        e_n, empty_number = empty_number, e_n


window.mainloop()
