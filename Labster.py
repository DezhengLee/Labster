# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox
from PDFgenerator import *
import sys


window = tk.Tk()

window.title('Labster V0.0.2')

screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
dialog_width = 400
dialog_height = 300
window.geometry("%dx%d+%d+%d" % (dialog_width, dialog_height, (screenwidth-dialog_width)/2, (screenheight-dialog_height)/2))

tk.Label(window, text='数据路径:', font=('Arial', 11)).place(x=10, y=80)
tk.Label(window, text='储存路径:', font=('Arial', 11)).place(x=10, y=130)

filename = tk.StringVar()
filename.set(sys.path[0])
entry_filename = tk.Entry(window, textvariable=filename, font=('Arial', 10), width=35)
entry_filename.place(x=120, y=83)

savename = tk.StringVar()
savename.set(sys.path[0])
entry_savename = tk.Entry(window, textvariable=savename, font=('Arial', 10), width=35)
entry_savename.place(x=120, y=133)


def act():
    f = filename.get()
    s = savename.get()
    if len(s) == 0 or len(f) == 0:
        tkinter.messagebox.showerror(title='', message='请正确输入路径.')
    else:
        s = s + r'\ReportResult'
        try:
            PDFgenerator(f, s).generatePDF()
            tkinter.messagebox.showinfo(title='提示', message='报告已生成，储存在' + s + '.pdf中.')
        except:
            tkinter.messagebox.showinfo(title='提示', message='请检查数据路径是否正确.')

btn = tk.Button(window, text='Generate', command=act, width=12, height=3, font=('Arial', 13))
btn.place(x=120, y=200)

window.mainloop()

