from tkinter import *
def add_nonpar():
    a = float(inp1.get())
    b = float(inp2.get())
    s = '%0.2f+%0.2f=%0.2f\n' % (a, b, a + b)
    txt.insert(END, s)  # 追加显示运算结果
    inp1.delete(0, END)  # 清空输入
    inp2.delete(0, END)  # 清空输入

def add_havepar(x,y):
    a = float(x)
    b = float(y)
    s = '%0.2f+%0.2f=%0.2f\n' % (a, b, a + b)
    txt.insert(END, s)  # 追加显示运算结果
    inp1.delete(0, END)  # 清空输入
    inp2.delete(0, END)  # 清空输入

def mlu():
    a = float(inp1.get())
    b = float(inp2.get())
    s = '%0.2f-%0.2f=%0.2f\n' % (a, b, a - b)
    txt.insert(END, s)  # 追加显示运算结果
    inp1.delete(0, END)  # 清空输入
    inp2.delete(0, END)  # 清空输入

def cheng():
    a = float(inp1.get())
    b = float(inp2.get())
    s = '%0.2f*%0.2f=%0.2f\n' % (a, b, a * b)
    txt.insert(END, s)  # 追加显示运算结果
    inp1.delete(0, END)  # 清空输入
    inp2.delete(0, END)  # 清空输入

def chu():
    a = float(inp1.get())
    b = float(inp2.get())
    s = '%0.2f÷%0.2f=%0.2f\n' % (a, b, a / b)
    txt.insert(END, s)  # 追加显示运算结果
    inp1.delete(0, END)  # 清空输入
    inp2.delete(0, END)  # 清空输入

root = Tk()
lb_1=Label(root,text="请输入您想要计算的两个数字：")
#place中参数的意思是，relx代表相对于窗体的相对水平起始位置，
#rely代表相对于窗体的垂直起始位置。relwidth意思是相对于窗体的宽度为0.8
#relheight代表相对于窗体高度为0.1
#相对应的这些参数如果是x,y,width,heigh代表的意思是绝对位置和绝对高度和宽度。
lb_1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
#创建两个输入框
inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)
inp2 = Entry(root)
inp2.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.1)
#创建加法按钮组件.当回到函数无参数传入的时候
btn1 = Button(root, text='无参数传入的加法运算', command=add_nonpar)
btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

#创建加法按钮组件.当回到函数有参数传入的时候
btn2 = Button(root, text='有参数传入的加法运算', command=lambda:add_havepar(inp1.get(),inp2.get()))
btn2.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)

#创建减法按钮组件.
btn3 = Button(root, text='减法运算', command=mlu)
btn3.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.1)

#创建乘法按钮组件.
btn3 = Button(root, text='乘法运算',command=cheng )
btn3.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.1)

#创建除法按钮组件.
btn3 = Button(root, text='除法运算', command=chu)
btn3.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.1)

#创建一个文本框用来显示计算得到的结果
txt = Text(root)
txt.place(relx=0.1,rely=0.8, relheight=0.3)


root.geometry('800x400')
root.title('四则运算计算器')
root.mainloop()