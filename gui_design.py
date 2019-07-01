from tkinter import *
root= Tk()
lb_1 = Label(root,text="这是第一个标签", \
                #设置label背景颜色
                bg = 'WHITE', \
                #设置前景颜色
                fg = 'black', \
                #设置字体型号和大小
                font = ('华文新魏', 12), \
                #设置标签长度
                width = 48, \
                #设置标签高度
                height = 5, \
                #reliefrelief 为控件呈现出来的3D浮雕样式，有 FLAT(平的)、RAISED(凸起的)、SUNKEN(凹陷的)、GROOVE(沟槽状边缘)和 RIDGE(脊状边缘) 5种
                relief = RIDGE)
lb_1.pack()
lb_2 = Label(root,text="这是第二个标签", \
                #设置label背景颜色
                bg = 'gray', \
                #设置前景颜色
                fg = 'black', \
                #设置字体型号和大小
                font = ('华文新魏', 14), \
                #设置标签长度
                width = 15, \
                #设置标签高度
                height = 4, \
                #reliefrelief 为控件呈现出来的3D浮雕样式，有 FLAT(平的)、RAISED(凸起的)、SUNKEN(凹陷的)、GROOVE(沟槽状边缘)和 RIDGE(脊状边缘) 5种
                relief = RIDGE)
lb_2.pack(side=RIGHT)
lb_3 = Label(root,text="这是第三个标签", \
                #设置label背景颜色
                bg = 'pink', \
                #设置前景颜色
                fg = 'black', \
                #设置字体型号和大小
                font = ('华文新魏', 14), \
                #设置标签长度
                width = 10, \
                #设置标签高度
                height = 4, \
                #reliefrelief 为控件呈现出来的3D浮雕样式，有 FLAT(平的)、RAISED(凸起的)、SUNKEN(凹陷的)、GROOVE(沟槽状边缘)和 RIDGE(脊状边缘) 5种
                relief = RIDGE)
lb_3.pack(fill=X)
#pack()不带参数，代表将按布局语句的先后，以最小占用空间的方式自上而下地排列控件实例，并且保持控件本身的最小尺寸
#pack()如果带参数，可以设置为fill、side等参数，fill的取值可以为fill=X,fill=Y或fill=BOTH，
# 分别表示允许控件向水平方向、垂直方向或二维伸展填充未被占用控件。参数 side 可取值：side=TOP(默认)，side=LEFT,side=RIGHT,side=BOTTOM,分别表示本控件实例的布局相对于下一个控件实例的方位
root.title('我的第一个Python窗体')
root.geometry('480x480') # 这里的乘号不是 * ，而是小写英文字母 x
root.mainloop()