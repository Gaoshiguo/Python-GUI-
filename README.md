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
| | | |
| | | |
