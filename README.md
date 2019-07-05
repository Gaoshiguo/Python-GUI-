# Python-GUI-
这个醒目主要记录使用Python来完成一些图形化界面的设计和实现
# 一、使用python自带的tkinter库完成一些简单的图形化界面
*首先来写一个最简单的图形化界面的代码看看效果

```python
from tkinter import *
root= Tk()
root.title('我的第一个Python窗体')
root.geometry('240x240') # 这里的乘号不是 * ，而是小写英文字母 x
root.mainloop()
```
生成的第一个图形化的界面如下图所示：

![image](https://github.com/Gaoshiguo/Python-GUI-/blob/master/image/1.png)

## 1.1 介绍一下tkinter的常用控件

| 控件 |名称|作用|
|-----|------|-----|
|Button|按钮|单击可以触发相应的事件|
| Canvas| 画布|绘制图形或绘制特殊控件|
|Checkbutton | 复选框|多项选择 |
| Entry|输入框 |接收单行文本输入 |
|Frame | 框架|用于控件分组 |
|Label |标签 |单行文本显示 |
| Lisbox|列表框 |显示文本列表 |
| Menu|菜单 |创建菜单命令 |
|Message |消息 |多行文本标签，与Label 用法类似 |
|Radiobutton |单选按钮 |从互斥的多个选项中做单项选择 |
|Scale |滑块 | 默认垂直方向，鼠标拖动改变数值形成可视化交互|
|Scrollbar |滑动条 |默认垂直方向，课鼠标拖动改变数值，可与 Text、Lisbox、Canvas等控件配合移动可视化空间 |
|Text |文本框 |接收或输出显示多行文本 |
|Toplevel |新建窗体容器 | 在顶层创建新窗体|

### 1.1.1 Button控件的使用方法
* 将一个 Python 函数或方法绑定到一个 Button 控件. 这个函数或方法将在按钮被点击时执行，这样我们就可以实现交互

button控件的一些参数代表的意思及用法。activebackground, activeforeground:{类型：颜色；说明：当按钮被激活时所使用的颜色}，background (bg), foreground (fg):{类型：颜色；说明：按钮的颜色。默认值与特定平台相关},borderwidth (bd)：{类型：整数；说明：按钮边框的宽度。默认值与特定平台相关。但通常是1或2象素}，command：{类型：回调；说明：当按钮被按下时所调用的一个函数或方法。所回调的可以是一个函数、方法或别的可调用的Python对象}

通常button控件都是与某些回调函数连用，以实现交互的效果。
假设我们需要当用户点击按钮后弹出一个对话框的需求

```python
from tkinter import *
from tkinter.messagebox import *
root= Tk()
def printmessagr():
    showinfo(title='提示', message='您点击了按钮')
    
bt=Button(root,text="点击我",command=printmessagr)
bt.pack()
root.title('我的第一个Python窗体')
root.geometry('240x240') # 这里的乘号不是 * ，而是小写英文字母 x
root.mainloop()
```
此段代码生成后的效果图如下所示：

![image](https://github.com/Gaoshiguo/Python-GUI-/blob/master/image/2.png)

同样的我们还可以设置一些更加复杂的回调函数。

我们可以写一个简单的计算器小程序。

```python
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
```
最后的效果图如下所示：

![image](https://github.com/Gaoshiguo/Python-GUI-/blob/master/image/3.png)

假如我想要使用text控件来实现将文本框中的内容作为文件保存到指定文件夹中。实现的功能类似于notepad

[代码链接](https://github.com/Gaoshiguo/Python-GUI-/blob/master/notepad.py)

效果图如下图所示：

![image](https://github.com/Gaoshiguo/Python-GUI-/blob/master/image/4.png)

![image](https://github.com/Gaoshiguo/Python-GUI-/blob/master/image/5.png)

制作一个文件选择对话框，并将选择的图片显示在图形化界面中

生成的效果如下图所示：

![image](https://github.com/Gaoshiguo/Python-GUI-/blob/master/image/6.png)

![image](https://github.com/Gaoshiguo/Python-GUI-/blob/master/image/7.png)

![image](https://github.com/Gaoshiguo/Python-GUI-/blob/master/image/8.png)


