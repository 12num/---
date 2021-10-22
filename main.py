from tkinter import *
from LoginPage import *
import sys
sys.path.append(r"C:\Users\ljt\AppData\Local\Programs\Python\Python38\Lib\site-packages\pyzmq.libs") #添加自定义模块的路径


root = Tk()
root.title('温度监测系统')
LoginPage(root)
root.mainloop()

