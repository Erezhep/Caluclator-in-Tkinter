from tkinter import *

root = Tk()
root.title('GUI Калькулятор')
root.geometry('300x300+200+100')
root.resizable(0, 0)
root['bg'] = 'black'

def result():
    num = str(entry.get())
    if num[0] in '0123456789-':
        try:
            entry.delete(0, END)
            entry.insert(END, eval(num))
        except:
            entry.delete(0, END)
            entry.insert(0, '∞')
    else:
        entry.insert(END, ' = Ошибка')
        

def psms():
    try:
        num = entry.get()
        if num[0] == '-' or len(num) == 0:
            entry.delete(0, END)
            entry.insert(0, num[1:])
        else:
            entry.insert(0, '-')
    except IndexError:
        pass

def delete():
    entry.delete(0, END)

def click():
    num = entry.get()
    if len(num) != 0:
        entry.delete(0, END)
        entry.insert(0, num[:(len(num) - 1)])
    else:
        entry.insert(END, '')

entry = Entry(root, width = 17, bg = '#373636', fg = 'lime', font = 'Arial 20 bold')
entry.grid(ipadx = 13, ipady = 12, padx = 6, pady = 6)

btn_1 =  Button(root, text = 'C', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = delete)
btn_1.place(x = 10, y = 80)

btn_2 =  Button(root, text = '±', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = psms)
btn_2.place(x = 85, y = 80)

btn_3 =  Button(root, text = '←', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = click)
btn_3.place(x = 160, y = 80)

btn_4 =  Button(root, text = '÷', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'orange', font = 'Arial 12 bold', command = lambda: entry.insert(END, '/'))
btn_4.place(x = 235, y = 80)

btn_5 =  Button(root, text = '7', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = lambda: entry.insert(END, '7'))
btn_5.place(x = 10, y = 125)

btn_6 =  Button(root, text = '8', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = lambda: entry.insert(END, '8'))
btn_6.place(x = 85, y = 125)

btn_7 =  Button(root, text = '9', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = lambda: entry.insert(END, '9'))
btn_7.place(x = 160, y = 125)

btn_8 =  Button(root, text = 'x', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'orange', font = 'Arial 12 bold', command = lambda: entry.insert(END, '*'))
btn_8.place(x = 235, y = 125)

btn_9 =  Button(root, text = '4', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = lambda: entry.insert(END, '4'))
btn_9.place(x = 10, y = 170)

btn_10 =  Button(root, text = '5', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = lambda: entry.insert(END, '5'))
btn_10.place(x = 85, y = 170)

btn_11 =  Button(root, text = '6', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = lambda: entry.insert(END, '6'))
btn_11.place(x = 160, y = 170)

btn_12 =  Button(root, text = '-', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'orange', font = 'Arial 12 bold', command = lambda: entry.insert(END, '-'))
btn_12.place(x = 235, y = 170)

btn_13 =  Button(root, text = '1', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = lambda: entry.insert(END, '1'))
btn_13.place(x = 10, y = 215)

btn_14 =  Button(root, text = '2', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = lambda: entry.insert(END, '2'))
btn_14.place(x = 85, y = 215)

btn_15 =  Button(root, text = '3', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = lambda: entry.insert(END, '3'))
btn_15.place(x = 160, y = 215)

btn_16 =  Button(root, text = '+', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'orange', font = 'Arial 12 bold', command = lambda: entry.insert(END, '+'))
btn_16.place(x = 235, y = 215)

btn_17 =  Button(root, text = '0', width = 12, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = lambda: entry.insert(END, '0'))
btn_17.place(x = 10, y = 260)

btn_18 =  Button(root, text = '•', width = 5, height = 1, bg = '#202020', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = lambda: entry.insert(END, '.'))
btn_18.place(x = 160, y = 260)

btn_19 =  Button(root, text = '=', width = 5, height = 1, bg = 'orange', activebackground = '#C1C1C1', fg = 'white', font = 'Arial 12 bold', command = result)
btn_19.place(x = 235, y = 260)

root.mainloop()
