from tkinter import *
from MainWindow import *

root = Tk()
root.title('温度监测系统')
MainWindow(root)

all1=root.after(time1,MainWindow.startrun)
root.mainloop()
