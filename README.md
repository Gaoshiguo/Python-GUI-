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
