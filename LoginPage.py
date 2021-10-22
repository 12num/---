from tkinter import *
from tkinter.messagebox import *
from MainWindow import *


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        width = 500
        height = 300
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)  # 设置窗口大小
        # 利用StringVar接收用户输入
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack(side='top', expand='yes')
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='用户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        if name == '温度系统' and secret == 'wendu123':
            self.page.destroy()
            MainWindow(self.root)
        else:
            showinfo(title='错误', message='账号或密码错误！')
