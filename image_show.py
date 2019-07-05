import tkinter
from tkinter.filedialog import *
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
root = tkinter.Tk()

def callback():

    #filename=ImageTk.PhotoImage(Image.open(file))
    #cv.image = filename  # <--- keep reference of your image
    #cv.create_image(20, 20, anchor='nw', image=file)
    file = tkinter.filedialog.askopenfilename(
    filetypes=[("jpg", ".jpg"),("png", ".png"), ("gpf", ".gpf"),  ("gif", ".gif")])
    image_open = Image.open(file)
    image_png = ImageTk.PhotoImage(image_open)
    label_img = tkinter.Label(root, image=image_png)
    label_img.place(relx=0.1,rely=0.2,relwidth=0.3,relheight=0.3)
    label_context=tkinter.Label(root,text="您想要识别的图片为：")
    label_context.place(relx=0.1,rely=0.15,relwidth=0.3,relheight=0.1)
    root.mainloop()

label=Label(root,text="图片识别：")
label.place(relx=0.3,rely=0.01,relwidth=0.3,relheight=0.2)
button=Button(root,text="选择想要识别的图片",command=callback)
button.place(relx=0.15,rely=0.7)

def pca_face_recongize():
    tkinter.messagebox.showinfo('提示', '急个几把，函数函数还没写好呢！再等等吧！')

button_1=Button(root,text="开始识别",command=pca_face_recongize)
button_1.place(relx=0.5,rely=0.7)
root.title = ('记事本')
root.geometry('640x480')
root.mainloop()