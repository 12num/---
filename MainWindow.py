from tkinter import *
import datetime
import os
from PIL import Image, ImageTk

from Serial_Communication import Serial_Comm
from testAtals import atals
from xlwt import *
import configparser
import os
from xlrd import *

time1=60000            #定时时间
clock1=1   #定时周期
class MainWindow(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        width = 1800
        height = 800
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (self.screenwidth - width) / 2, (self.screenheight - height) / 2)
        self.root.geometry(alignstr)  # 设置窗口大小
        # 利用StringVar接收用户输入
        self.timeinterval = StringVar()
        #时间关键数据
        global time1
        self.time2 =datetime.datetime.now().strftime('%Y-%m-%d_%H-%M_')  # 此时时间
        #获取模拟数据
        # self.get_data=Serial_Comm()
        self.data=[]
        #实例 生成图片的对象
        self.pictureatals=atals()
        #生成面板函数
        self.createFrame()


    def createFrame(self):

        Label(self.root, text="温度场监控与分析系统", font=('黑体', 20)).place(width=400, height=100, x=900, y=80,anchor="center")
        Label(self.root,text="时间间隔（分）：",font=('宋体', 14)).place(width=200,height=30,x=150,y=200,anchor="center")
        self.entry1=Entry(self.root, textvariable=self.timeinterval)
        self.entry1.place(width=80, height=30, x=300, y=200, anchor="center")
        Label(self.root, text="倒计时（秒）：", font=('宋体', 14)).place(width=200, height=30, x=500, y=200, anchor="center")
        # self.label4 = Label(self.root, fg="red", font=("DBLCDTempBlack", 14))

        #command=self.startrun,command=lambda:[self.startrun,self.update_clock]
        Button(self.root, text="实时云图", command=self.alltime).place(width=100, height=30, x=780, y=200, anchor="center")
        self.button1=Button(self.root, text="开始", command=self.alll)
        self.button1.place(width=100,height=30,x=1000,y=200,anchor="center")
        Button(self.root, text="重置",command=self.run_stop).place(width=100,height=30,x=1200,y=200,anchor="center")
        Button(self.root, text="图形文件夹",command=self.Picture_catalog).place(width=100,height=30,x=1400,y=200,anchor="center")
        Button(self.root, text="表格文件夹",command=self.Form_directory).place(width=100,height=30,x=1600,y=200,anchor="center")

        Label(self.root, text="上层", font=('黑体', 14)).place(width=80,height=30,x=300,y=300,anchor="center")
        Label(self.root, text="中层", font=('黑体', 14)).place(width=80,height=30,x=900,y=300,anchor="center")
        Label(self.root, text="下层", font=('黑体', 14)).place(width=80,height=30,x=1500,y=300,anchor="center")
        # Label(self.root, text="上层图片",bg="red").place(width=400,height=500,x=200,y=650,anchor="center")
        # Label(self.root, text="中层图片",bg="blue").place(width=400,height=500,x=600,y=650,anchor="center")
        # Label(self.root, text="下层图片",bg="green").place(width=400,height=500,x=1000,y=650,anchor="center")

        # Label(self.root, text="版权所有：秦州市沪江特种设备有限公司 江苏大学提供技术支持  地址：江苏省秦州市海陵区吴洲北路88号  电话：0523-66559620传真：0523-66552433邮箱：office@jshujiang.com",
        #       font=('宋体', 10),relief="raised").place(width=1800, height=50, x=900, y=775,anchor="center")

#--------------------------------------------------------------------------------------------------------------------------------------------
    #将所有函数、放到一个button里面
    def alll(self):
        self.update_clock()
        self.creat_execl()
        self.startrun()

    def alltime(self):   #实时
        self.timeexcels()
        self.timerun()


    # 重置按钮
    def run_stop(self):
        self.button1.config(state='normal')  # 开始按钮恢复正常
        self.entry1.config(state='normal')
        # self.button1.config(state=DISABLED)

        #tk.after_cancel(solve)   删除after
        global clock1
        self.time = self.timeinterval.get()
        if len(self.time) == 0:
            self.root.after_cancel(self.clock2)
            # self.root.after_cancel(self.clock3)
            # self.root.after_cancel(self.clock4)
            self.root.after_cancel(self.run1)
            self.root.after_cancel(self.exe1)
        else:
            self.root.after_cancel(self.clock2)
            # self.root.after_cancel(self.clock3)
            self.root.after_cancel(self.clock4)
            self.root.after_cancel(self.run1)
            self.root.after_cancel(self.exe1)
#-------------------------------------------------------------------------------
    #倒计时
    def show_timer(self):
        global time1  # 定时器
        global clock1
        self.clock2=self.root.after(1000,self.show_timer)
        if time1 == 0:
            time1 = 60000*clock1  # 全局变量复原
        else:
            self.label4 = Label(self.root, fg="red", font=("DBLCDTempBlack", 14))
            self.label4.place(width=80, height=30, x=600, y=200, anchor="center")
            self.label4.configure(text=time1 / 1000)
            time1 = time1 - 1000  # 倒计时
    def update_clock(self):
        # 利用StringVar接收用户输入
        global time1
        global clock1
        self.time = self.timeinterval.get()
        # print(type(self.time))
        if len(self.time)==0:
            clock1=1
            self.clock3=self.root.after(1000,self.show_timer)
        else:
            clock1 = float(self.time)
            clock1=int(clock1)
            time1 = 60000 * clock1
            self.clock4=self.root.after(1000, self.show_timer)

#-------------------------------------------------------------------------------------
    #生成图片
    def startrun(self):
        global time1   #定时器时间参数
        #利用StringVar接收用户输入
        self.time=self.timeinterval.get()
        #时间文件
        time2 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')       # 此时时间
        data1, data2 = time2.split("_", 1)
        data_floder = 'Picture' + '/' + data1
        if os.path.isdir(data_floder) == False | os.path.exists(data_floder) == False:
            os.makedirs(data_floder)
        self.file1 = data_floder + '/' + data2 + '上层.jpg'
        self.file2 = data_floder + '/' + data2 + '中层.jpg'
        self.file3 = data_floder + '/' + data2 + '下层.jpg'
        #数据
        self.get_data = Serial_Comm()
        self.data=self.get_data.getdata()
        # print(self.data)
        # 对“self.data”进行参数调整 -----------------------
        curpath = os.path.dirname(os.path.realpath(__file__))
        cfgpath = os.path.join(curpath, "config.ini")
        conf = configparser.ConfigParser()
        conf.read(cfgpath, encoding="utf-8")  # python3
        value0 = conf.getfloat('test1', 'node0')
        value1 = conf.getfloat('test1', 'node1')
        value2 = conf.getfloat('test1', 'node2')
        value3 = conf.getfloat('test1', 'node3')
        value4 = conf.getfloat('test1', 'node4')
        value5 = conf.getfloat('test1', 'node5')
        value6 = conf.getfloat('test1', 'node6')
        value7 = conf.getfloat('test1', 'node7')
        value8 = conf.getfloat('test1', 'node8')
        value9 = conf.getfloat('test1', 'node9')
        value10 = conf.getfloat('test1', 'node10')
        value11 = conf.getfloat('test1', 'node11')
        value12 = conf.getfloat('test1', 'node12')
        value13 = conf.getfloat('test1', 'node13')
        value14 = conf.getfloat('test1', 'node14')
        value15 = conf.getfloat('test1', 'node15')
        value16 = conf.getfloat('test1', 'node16')
        value17 = conf.getfloat('test1', 'node17')
        value18 = conf.getfloat('test1', 'node18')
        value19 = conf.getfloat('test1', 'node19')
        value20 = conf.getfloat('test1', 'node20')
        value21 = conf.getfloat('test1', 'node21')
        value22 = conf.getfloat('test1', 'node22')
        value23 = conf.getfloat('test1', 'node23')
        value24 = conf.getfloat('test1', 'node24')
        value25 = conf.getfloat('test1', 'node25')
        value26 = conf.getfloat('test1', 'node26')
        value27 = conf.getfloat('test1', 'node27')
        value28 = conf.getfloat('test1', 'node28')
        value29 = conf.getfloat('test1', 'node29')
        value30 = conf.getfloat('test1', 'node30')
        value31 = conf.getfloat('test1', 'node31')
        value32 = conf.getfloat('test1', 'node32')
        value33 = conf.getfloat('test1', 'node33')
        value34 = conf.getfloat('test1', 'node34')
        value35 = conf.getfloat('test1', 'node35')
        value36 = conf.getfloat('test1', 'node36')
        value37 = conf.getfloat('test1', 'node37')
        value38 = conf.getfloat('test1', 'node38')
        value39 = conf.getfloat('test1', 'node39')
        value40 = conf.getfloat('test1', 'node40')
        value41 = conf.getfloat('test1', 'node41')
        value42 = conf.getfloat('test1', 'node42')
        value43 = conf.getfloat('test1', 'node43')
        value44 = conf.getfloat('test1', 'node44')
        value45 = conf.getfloat('test1', 'node45')
        value46 = conf.getfloat('test1', 'node46')
        value47 = conf.getfloat('test1', 'node47')
        value48 = conf.getfloat('test1', 'node48')
        value49 = conf.getfloat('test1', 'node49')
        value50 = conf.getfloat('test1', 'node50')
        value51 = conf.getfloat('test1', 'node51')
        value52 = conf.getfloat('test1', 'node52')
        value53 = conf.getfloat('test1', 'node53')
        value54 = conf.getfloat('test1', 'node54')
        value55 = conf.getfloat('test1', 'node55')
        value56 = conf.getfloat('test1', 'node56')
        value57 = conf.getfloat('test1', 'node57')
        value58 = conf.getfloat('test1', 'node58')
        value59 = conf.getfloat('test1', 'node59')
        value60 = conf.getfloat('test1', 'node60')
        value61 = conf.getfloat('test1', 'node61')
        value62 = conf.getfloat('test1', 'node62')
        value63 = conf.getfloat('test1', 'node63')
        value64 = conf.getfloat('test1', 'node64')
        value65 = conf.getfloat('test1', 'node65')
        value66 = conf.getfloat('test1', 'node66')
        value67 = conf.getfloat('test1', 'node67')
        value68 = conf.getfloat('test1', 'node68')
        value69 = conf.getfloat('test1', 'node69')
        value70 = conf.getfloat('test1', 'node70')
        value71 = conf.getfloat('test1', 'node71')
        value72 = conf.getfloat('test1', 'node72')
        value73 = conf.getfloat('test1', 'node73')
        value74 = conf.getfloat('test1', 'node74')
        self.data[0] = self.data[0] + value0
        self.data[1] = self.data[1] + value1
        self.data[2] = self.data[2] + value2
        self.data[3] = self.data[3] + value3
        self.data[4] = self.data[4] + value4
        self.data[5] = self.data[5] + value5
        self.data[6] = self.data[6] + value6
        self.data[7] = self.data[7] + value7
        self.data[8] = self.data[8] + value8
        self.data[9] = self.data[9] + value9
        self.data[10] = self.data[10] + value10
        self.data[11] = self.data[11] + value11
        self.data[12] = self.data[12] + value12
        self.data[13] = self.data[13] + value13
        self.data[14] = self.data[14] + value14
        self.data[15] = self.data[15] + value15
        self.data[16] = self.data[16] + value16
        self.data[17] = self.data[17] + value17
        self.data[18] = self.data[18] + value18
        self.data[19] = self.data[19] + value19
        self.data[20] = self.data[20] + value20
        self.data[21] = self.data[21] + value21
        self.data[22] = self.data[22] + value22
        self.data[23] = self.data[23] + value23
        self.data[24] = self.data[24] + value24
        self.data[25] = self.data[25] + value25
        self.data[26] = self.data[26] + value26
        self.data[27] = self.data[27] + value27
        self.data[28] = self.data[28] + value28
        self.data[29] = self.data[29] + value29
        self.data[30] = self.data[30] + value30
        self.data[31] = self.data[31] + value31
        self.data[32] = self.data[32] + value32
        self.data[33] = self.data[33] + value33
        self.data[34] = self.data[34] + value34
        self.data[35] = self.data[35] + value35
        self.data[36] = self.data[36] + value36
        self.data[37] = self.data[37] + value37
        self.data[38] = self.data[38] + value38
        self.data[39] = self.data[39] + value39
        self.data[40] = self.data[40] + value40
        self.data[41] = self.data[41] + value41
        self.data[42] = self.data[42] + value42
        self.data[43] = self.data[43] + value43
        self.data[44] = self.data[44] + value44
        self.data[45] = self.data[45] + value45
        self.data[46] = self.data[46] + value46
        self.data[47] = self.data[47] + value47
        self.data[48] = self.data[48] + value48
        self.data[49] = self.data[49] + value49
        self.data[50] = self.data[50] + value50
        self.data[51] = self.data[51] + value51
        self.data[52] = self.data[52] + value52
        self.data[53] = self.data[53] + value53
        self.data[54] = self.data[54] + value54
        self.data[55] = self.data[55] + value55
        self.data[56] = self.data[56] + value56
        self.data[57] = self.data[57] + value57
        self.data[58] = self.data[58] + value58
        self.data[59] = self.data[59] + value59
        self.data[60] = self.data[60] + value60
        self.data[61] = self.data[61] + value61
        self.data[62] = self.data[62] + value62
        self.data[63] = self.data[63] + value63
        self.data[64] = self.data[64] + value64
        self.data[65] = self.data[65] + value65
        self.data[66] = self.data[66] + value66
        self.data[67] = self.data[67] + value67
        self.data[68] = self.data[68] + value68
        self.data[69] = self.data[69] + value69
        self.data[70] = self.data[70] + value70
        self.data[71] = self.data[71] + value71
        self.data[72] = self.data[72] + value72
        self.data[73] = self.data[73] + value73
        self.data[74] = self.data[74] + value74
        #self.data调整完毕                  -------------------
        self.data1=self.data[0:25]
        self.data2=self.data[25:50]
        self.data3=self.data[50:75]
        # print(type(self.data),type(self.data1))
        #展现图片
        self.pictureatals.showatals1(self.data1,time2)
        self.pictureatals.showatals2(self.data2,time2)
        self.pictureatals.showatals3(self.data3,time2)
        #读取文件夹的图片
        self.pilImage1 = Image.open(self.file1)
        self.tkImage1 = ImageTk.PhotoImage(image=self.pilImage1)
        Label(self.root, image=self.tkImage1,relief="raised").place(width=580,height=400,x=300,y=550,anchor="center")
        self.pilImage2 = Image.open(self.file2)
        self.tkImage2 = ImageTk.PhotoImage(image=self.pilImage2)
        Label(self.root, image=self.tkImage2,relief="raised").place(width=580, height=400, x=900, y=550, anchor="center")
        self.pilImage3 = Image.open(self.file3)
        self.tkImage3 = ImageTk.PhotoImage(image=self.pilImage3)
        Label(self.root, image=self.tkImage3,relief="raised").place(width=580, height=400, x=1500, y=550, anchor="center")
        #禁止按钮
        self.button1.config(state=DISABLED)
        self.entry1.config(state=DISABLED)

        #after循环函数
        self.run1=self.root.after(time1,self.startrun)
        # self.root.after(1000, self.update_clock)


    #保存在xlsx文件中
    def creat_execl(self):
        global time1  # 定时器时间参数
        # 数据
        self.get_data = Serial_Comm()
        self.data = self.get_data.getdata()
        # print(self.data)
        # 对“self.data”进行参数调整 -----------------------
        curpath = os.path.dirname(os.path.realpath(__file__))
        cfgpath = os.path.join(curpath, "config.ini")
        conf = configparser.ConfigParser()
        conf.read(cfgpath, encoding="utf-8")  # python3
        value0 = conf.getfloat('test1', 'node0')
        value1 = conf.getfloat('test1', 'node1')
        value2 = conf.getfloat('test1', 'node2')
        value3 = conf.getfloat('test1', 'node3')
        value4 = conf.getfloat('test1', 'node4')
        value5 = conf.getfloat('test1', 'node5')
        value6 = conf.getfloat('test1', 'node6')
        value7 = conf.getfloat('test1', 'node7')
        value8 = conf.getfloat('test1', 'node8')
        value9 = conf.getfloat('test1', 'node9')
        value10 = conf.getfloat('test1', 'node10')
        value11 = conf.getfloat('test1', 'node11')
        value12 = conf.getfloat('test1', 'node12')
        value13 = conf.getfloat('test1', 'node13')
        value14 = conf.getfloat('test1', 'node14')
        value15 = conf.getfloat('test1', 'node15')
        value16 = conf.getfloat('test1', 'node16')
        value17 = conf.getfloat('test1', 'node17')
        value18 = conf.getfloat('test1', 'node18')
        value19 = conf.getfloat('test1', 'node19')
        value20 = conf.getfloat('test1', 'node20')
        value21 = conf.getfloat('test1', 'node21')
        value22 = conf.getfloat('test1', 'node22')
        value23 = conf.getfloat('test1', 'node23')
        value24 = conf.getfloat('test1', 'node24')
        value25 = conf.getfloat('test1', 'node25')
        value26 = conf.getfloat('test1', 'node26')
        value27 = conf.getfloat('test1', 'node27')
        value28 = conf.getfloat('test1', 'node28')
        value29 = conf.getfloat('test1', 'node29')
        value30 = conf.getfloat('test1', 'node30')
        value31 = conf.getfloat('test1', 'node31')
        value32 = conf.getfloat('test1', 'node32')
        value33 = conf.getfloat('test1', 'node33')
        value34 = conf.getfloat('test1', 'node34')
        value35 = conf.getfloat('test1', 'node35')
        value36 = conf.getfloat('test1', 'node36')
        value37 = conf.getfloat('test1', 'node37')
        value38 = conf.getfloat('test1', 'node38')
        value39 = conf.getfloat('test1', 'node39')
        value40 = conf.getfloat('test1', 'node40')
        value41 = conf.getfloat('test1', 'node41')
        value42 = conf.getfloat('test1', 'node42')
        value43 = conf.getfloat('test1', 'node43')
        value44 = conf.getfloat('test1', 'node44')
        value45 = conf.getfloat('test1', 'node45')
        value46 = conf.getfloat('test1', 'node46')
        value47 = conf.getfloat('test1', 'node47')
        value48 = conf.getfloat('test1', 'node48')
        value49 = conf.getfloat('test1', 'node49')
        value50 = conf.getfloat('test1', 'node50')
        value51 = conf.getfloat('test1', 'node51')
        value52 = conf.getfloat('test1', 'node52')
        value53 = conf.getfloat('test1', 'node53')
        value54 = conf.getfloat('test1', 'node54')
        value55 = conf.getfloat('test1', 'node55')
        value56 = conf.getfloat('test1', 'node56')
        value57 = conf.getfloat('test1', 'node57')
        value58 = conf.getfloat('test1', 'node58')
        value59 = conf.getfloat('test1', 'node59')
        value60 = conf.getfloat('test1', 'node60')
        value61 = conf.getfloat('test1', 'node61')
        value62 = conf.getfloat('test1', 'node62')
        value63 = conf.getfloat('test1', 'node63')
        value64 = conf.getfloat('test1', 'node64')
        value65 = conf.getfloat('test1', 'node65')
        value66 = conf.getfloat('test1', 'node66')
        value67 = conf.getfloat('test1', 'node67')
        value68 = conf.getfloat('test1', 'node68')
        value69 = conf.getfloat('test1', 'node69')
        value70 = conf.getfloat('test1', 'node70')
        value71 = conf.getfloat('test1', 'node71')
        value72 = conf.getfloat('test1', 'node72')
        value73 = conf.getfloat('test1', 'node73')
        value74 = conf.getfloat('test1', 'node74')
        self.data[0] = self.data[0] + value0
        self.data[1] = self.data[1] + value1
        self.data[2] = self.data[2] + value2
        self.data[3] = self.data[3] + value3
        self.data[4] = self.data[4] + value4
        self.data[5] = self.data[5] + value5
        self.data[6] = self.data[6] + value6
        self.data[7] = self.data[7] + value7
        self.data[8] = self.data[8] + value8
        self.data[9] = self.data[9] + value9
        self.data[10] = self.data[10] + value10
        self.data[11] = self.data[11] + value11
        self.data[12] = self.data[12] + value12
        self.data[13] = self.data[13] + value13
        self.data[14] = self.data[14] + value14
        self.data[15] = self.data[15] + value15
        self.data[16] = self.data[16] + value16
        self.data[17] = self.data[17] + value17
        self.data[18] = self.data[18] + value18
        self.data[19] = self.data[19] + value19
        self.data[20] = self.data[20] + value20
        self.data[21] = self.data[21] + value21
        self.data[22] = self.data[22] + value22
        self.data[23] = self.data[23] + value23
        self.data[24] = self.data[24] + value24
        self.data[25] = self.data[25] + value25
        self.data[26] = self.data[26] + value26
        self.data[27] = self.data[27] + value27
        self.data[28] = self.data[28] + value28
        self.data[29] = self.data[29] + value29
        self.data[30] = self.data[30] + value30
        self.data[31] = self.data[31] + value31
        self.data[32] = self.data[32] + value32
        self.data[33] = self.data[33] + value33
        self.data[34] = self.data[34] + value34
        self.data[35] = self.data[35] + value35
        self.data[36] = self.data[36] + value36
        self.data[37] = self.data[37] + value37
        self.data[38] = self.data[38] + value38
        self.data[39] = self.data[39] + value39
        self.data[40] = self.data[40] + value40
        self.data[41] = self.data[41] + value41
        self.data[42] = self.data[42] + value42
        self.data[43] = self.data[43] + value43
        self.data[44] = self.data[44] + value44
        self.data[45] = self.data[45] + value45
        self.data[46] = self.data[46] + value46
        self.data[47] = self.data[47] + value47
        self.data[48] = self.data[48] + value48
        self.data[49] = self.data[49] + value49
        self.data[50] = self.data[50] + value50
        self.data[51] = self.data[51] + value51
        self.data[52] = self.data[52] + value52
        self.data[53] = self.data[53] + value53
        self.data[54] = self.data[54] + value54
        self.data[55] = self.data[55] + value55
        self.data[56] = self.data[56] + value56
        self.data[57] = self.data[57] + value57
        self.data[58] = self.data[58] + value58
        self.data[59] = self.data[59] + value59
        self.data[60] = self.data[60] + value60
        self.data[61] = self.data[61] + value61
        self.data[62] = self.data[62] + value62
        self.data[63] = self.data[63] + value63
        self.data[64] = self.data[64] + value64
        self.data[65] = self.data[65] + value65
        self.data[66] = self.data[66] + value66
        self.data[67] = self.data[67] + value67
        self.data[68] = self.data[68] + value68
        self.data[69] = self.data[69] + value69
        self.data[70] = self.data[70] + value70
        self.data[71] = self.data[71] + value71
        self.data[72] = self.data[72] + value72
        self.data[73] = self.data[73] + value73
        self.data[74] = self.data[74] + value74
        print(self.data)
        # self.data调整完毕                  -------------------
        # self.data = self.data.tolist()   #numpy转list
        # 将数据以xls形式保存在日期文件夹中
        time2 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')  # 此时时间
        # 颜色
        styleBlueBkg = easyxf('pattern: pattern solid, fore_colour ice_blue');  # 80% like
        styleBold = easyxf('pattern: pattern solid, fore_colour gray25');
        #坐标信息
        self.small_x_y = [[20, 0], [20, 832.5], [20, 1665], [20, 2497.5], [20, 3330], [692.5, 0], [692.5, 832.5],
                          [692.5, 1665], [692.5, 2497.5], [692.5, 3330], [1365, 0], [1365, 832.5], [1365, 1665],
                          [1365, 2497.5], [1365, 3330], [2037.5, 0], [2037.5, 832.5], [2037.5, 1665], [2037.5, 2497.5],
                          [2037.5, 3330], [2710, 0], [2710, 832.5], [2710, 1665], [2710, 2497.5], [2710, 3330]]
        #生成文件夹
        data1, data2 = time2.split("_", 1)
        data_floder = 'Excell' + '/' + data1
        if os.path.isdir(data_floder) == False | os.path.exists(data_floder) == False:
            os.makedirs(data_floder)
        # 写入excel
        tilte = ['Time', 'X', 'Y', 'Number', 'Temperature']
        wx = Workbook()
        ws = wx.add_sheet('sheet1')
        ws.col(0).width = 256 * 20
        ws.col(4).width = 256 * 12
        for i in range(0, 5):
            ws.write(0, i, tilte[i])
        # 批量写数据
        for i in range(0, 25):
            ws.write(i + 1, 0, str(time2), styleBlueBkg)
            ws.write(i + 1, 1, self.small_x_y[i % 25][0], styleBlueBkg)
            ws.write(i + 1, 2, self.small_x_y[i % 25][1], styleBlueBkg)
            ws.write(i + 1, 3, i + 1, styleBlueBkg)
            ws.write(i + 1, 4, self.data[i], styleBlueBkg)
        for i in range(25, 50):
            ws.write(i + 1, 0, str(time2), styleBold)
            ws.write(i + 1, 1, self.small_x_y[i % 25][0], styleBold)
            ws.write(i + 1, 2, self.small_x_y[i % 25][1], styleBold)
            ws.write(i + 1, 3, i + 1, styleBold)
            ws.write(i + 1, 4, self.data[i], styleBold)
        for i in range(50, 75):
            ws.write(i + 1, 0, str(time2))
            ws.write(i + 1, 1, self.small_x_y[i % 25][0])
            ws.write(i + 1, 2, self.small_x_y[i % 25][1])
            ws.write(i + 1, 3, i + 1)
            ws.write(i + 1, 4, self.data[i])
        #excels文件路径   xls！！!
        self.file1 = data_floder + '/' + data2 + '.xls'
        wx.save(self.file1)
        # after循环函数
        self.exe1=self.root.after(time1, self.creat_execl)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Picture_catalog(self):
        data_floder = 'Picture'
        os.startfile(data_floder)
    def Form_directory(self):
        data_floder='Excell'
        os.startfile(data_floder)

    # -------------------------------------------------------------------------------------------------------------------------------------------------
    # 实时云图

    def timerun(self):
        global time1  # 定时器时间参数
        # 利用StringVar接收用户输入
        # self.time = self.timeinterval.get()
        # 时间文件
        time2 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')  # 此时时间
        data1, data2 = time2.split("_", 1)
        data_floder = 'Picture' + '/' + time2 + 'Time'
        if os.path.isdir(data_floder) == False | os.path.exists(data_floder) == False:
            os.makedirs(data_floder)
        # 数据
        self.get_data = Serial_Comm()
        self.data = self.get_data.getdata()
        # print(self.data)
        # 对“self.data”进行参数调整 -----------------------
        curpath = os.path.dirname(os.path.realpath(__file__))
        cfgpath = os.path.join(curpath, "config.ini")
        conf = configparser.ConfigParser()
        conf.read(cfgpath, encoding="utf-8")  # python3
        value0 = conf.getfloat('test1', 'node0')
        value1 = conf.getfloat('test1', 'node1')
        value2 = conf.getfloat('test1', 'node2')
        value3 = conf.getfloat('test1', 'node3')
        value4 = conf.getfloat('test1', 'node4')
        value5 = conf.getfloat('test1', 'node5')
        value6 = conf.getfloat('test1', 'node6')
        value7 = conf.getfloat('test1', 'node7')
        value8 = conf.getfloat('test1', 'node8')
        value9 = conf.getfloat('test1', 'node9')
        value10 = conf.getfloat('test1', 'node10')
        value11 = conf.getfloat('test1', 'node11')
        value12 = conf.getfloat('test1', 'node12')
        value13 = conf.getfloat('test1', 'node13')
        value14 = conf.getfloat('test1', 'node14')
        value15 = conf.getfloat('test1', 'node15')
        value16 = conf.getfloat('test1', 'node16')
        value17 = conf.getfloat('test1', 'node17')
        value18 = conf.getfloat('test1', 'node18')
        value19 = conf.getfloat('test1', 'node19')
        value20 = conf.getfloat('test1', 'node20')
        value21 = conf.getfloat('test1', 'node21')
        value22 = conf.getfloat('test1', 'node22')
        value23 = conf.getfloat('test1', 'node23')
        value24 = conf.getfloat('test1', 'node24')
        value25 = conf.getfloat('test1', 'node25')
        value26 = conf.getfloat('test1', 'node26')
        value27 = conf.getfloat('test1', 'node27')
        value28 = conf.getfloat('test1', 'node28')
        value29 = conf.getfloat('test1', 'node29')
        value30 = conf.getfloat('test1', 'node30')
        value31 = conf.getfloat('test1', 'node31')
        value32 = conf.getfloat('test1', 'node32')
        value33 = conf.getfloat('test1', 'node33')
        value34 = conf.getfloat('test1', 'node34')
        value35 = conf.getfloat('test1', 'node35')
        value36 = conf.getfloat('test1', 'node36')
        value37 = conf.getfloat('test1', 'node37')
        value38 = conf.getfloat('test1', 'node38')
        value39 = conf.getfloat('test1', 'node39')
        value40 = conf.getfloat('test1', 'node40')
        value41 = conf.getfloat('test1', 'node41')
        value42 = conf.getfloat('test1', 'node42')
        value43 = conf.getfloat('test1', 'node43')
        value44 = conf.getfloat('test1', 'node44')
        value45 = conf.getfloat('test1', 'node45')
        value46 = conf.getfloat('test1', 'node46')
        value47 = conf.getfloat('test1', 'node47')
        value48 = conf.getfloat('test1', 'node48')
        value49 = conf.getfloat('test1', 'node49')
        value50 = conf.getfloat('test1', 'node50')
        value51 = conf.getfloat('test1', 'node51')
        value52 = conf.getfloat('test1', 'node52')
        value53 = conf.getfloat('test1', 'node53')
        value54 = conf.getfloat('test1', 'node54')
        value55 = conf.getfloat('test1', 'node55')
        value56 = conf.getfloat('test1', 'node56')
        value57 = conf.getfloat('test1', 'node57')
        value58 = conf.getfloat('test1', 'node58')
        value59 = conf.getfloat('test1', 'node59')
        value60 = conf.getfloat('test1', 'node60')
        value61 = conf.getfloat('test1', 'node61')
        value62 = conf.getfloat('test1', 'node62')
        value63 = conf.getfloat('test1', 'node63')
        value64 = conf.getfloat('test1', 'node64')
        value65 = conf.getfloat('test1', 'node65')
        value66 = conf.getfloat('test1', 'node66')
        value67 = conf.getfloat('test1', 'node67')
        value68 = conf.getfloat('test1', 'node68')
        value69 = conf.getfloat('test1', 'node69')
        value70 = conf.getfloat('test1', 'node70')
        value71 = conf.getfloat('test1', 'node71')
        value72 = conf.getfloat('test1', 'node72')
        value73 = conf.getfloat('test1', 'node73')
        value74 = conf.getfloat('test1', 'node74')
        self.data[0] = self.data[0] + value0
        self.data[1] = self.data[1] + value1
        self.data[2] = self.data[2] + value2
        self.data[3] = self.data[3] + value3
        self.data[4] = self.data[4] + value4
        self.data[5] = self.data[5] + value5
        self.data[6] = self.data[6] + value6
        self.data[7] = self.data[7] + value7
        self.data[8] = self.data[8] + value8
        self.data[9] = self.data[9] + value9
        self.data[10] = self.data[10] + value10
        self.data[11] = self.data[11] + value11
        self.data[12] = self.data[12] + value12
        self.data[13] = self.data[13] + value13
        self.data[14] = self.data[14] + value14
        self.data[15] = self.data[15] + value15
        self.data[16] = self.data[16] + value16
        self.data[17] = self.data[17] + value17
        self.data[18] = self.data[18] + value18
        self.data[19] = self.data[19] + value19
        self.data[20] = self.data[20] + value20
        self.data[21] = self.data[21] + value21
        self.data[22] = self.data[22] + value22
        self.data[23] = self.data[23] + value23
        self.data[24] = self.data[24] + value24
        self.data[25] = self.data[25] + value25
        self.data[26] = self.data[26] + value26
        self.data[27] = self.data[27] + value27
        self.data[28] = self.data[28] + value28
        self.data[29] = self.data[29] + value29
        self.data[30] = self.data[30] + value30
        self.data[31] = self.data[31] + value31
        self.data[32] = self.data[32] + value32
        self.data[33] = self.data[33] + value33
        self.data[34] = self.data[34] + value34
        self.data[35] = self.data[35] + value35
        self.data[36] = self.data[36] + value36
        self.data[37] = self.data[37] + value37
        self.data[38] = self.data[38] + value38
        self.data[39] = self.data[39] + value39
        self.data[40] = self.data[40] + value40
        self.data[41] = self.data[41] + value41
        self.data[42] = self.data[42] + value42
        self.data[43] = self.data[43] + value43
        self.data[44] = self.data[44] + value44
        self.data[45] = self.data[45] + value45
        self.data[46] = self.data[46] + value46
        self.data[47] = self.data[47] + value47
        self.data[48] = self.data[48] + value48
        self.data[49] = self.data[49] + value49
        self.data[50] = self.data[50] + value50
        self.data[51] = self.data[51] + value51
        self.data[52] = self.data[52] + value52
        self.data[53] = self.data[53] + value53
        self.data[54] = self.data[54] + value54
        self.data[55] = self.data[55] + value55
        self.data[56] = self.data[56] + value56
        self.data[57] = self.data[57] + value57
        self.data[58] = self.data[58] + value58
        self.data[59] = self.data[59] + value59
        self.data[60] = self.data[60] + value60
        self.data[61] = self.data[61] + value61
        self.data[62] = self.data[62] + value62
        self.data[63] = self.data[63] + value63
        self.data[64] = self.data[64] + value64
        self.data[65] = self.data[65] + value65
        self.data[66] = self.data[66] + value66
        self.data[67] = self.data[67] + value67
        self.data[68] = self.data[68] + value68
        self.data[69] = self.data[69] + value69
        self.data[70] = self.data[70] + value70
        self.data[71] = self.data[71] + value71
        self.data[72] = self.data[72] + value72
        self.data[73] = self.data[73] + value73
        self.data[74] = self.data[74] + value74
        # self.data调整完毕                  -------------------
        self.data1 = self.data[0:25]
        self.data2 = self.data[25:50]
        self.data3 = self.data[50:75]
        # 生成图片
        self.pictureatals.showatals4(self.data1, time2)
        self.pictureatals.showatals5(self.data2, time2)
        self.pictureatals.showatals6(self.data3, time2)
        # 读取文件夹的图片
        self.file1 = data_floder + '/' + data2 + '上层.jpg'
        self.file2 = data_floder + '/' + data2 + '中层.jpg'
        self.file3 = data_floder + '/' + data2 + '下层.jpg'
        self.pilImage1 = Image.open(self.file1)
        self.tkImage1 = ImageTk.PhotoImage(image=self.pilImage1)
        Label(self.root, image=self.tkImage1, relief="raised").place(width=580, height=400, x=300, y=550,
                                                                     anchor="center")
        self.pilImage2 = Image.open(self.file2)
        self.tkImage2 = ImageTk.PhotoImage(image=self.pilImage2)
        Label(self.root, image=self.tkImage2, relief="raised").place(width=580, height=400, x=900, y=550,
                                                                     anchor="center")
        self.pilImage3 = Image.open(self.file3)
        self.tkImage3 = ImageTk.PhotoImage(image=self.pilImage3)
        Label(self.root, image=self.tkImage3, relief="raised").place(width=580, height=400, x=1500, y=550,
                                                                     anchor="center")

    def timeexcels(self):
        global time1  # 定时器时间参数
        # 数据  将nupy转换成列表
        self.get_data = Serial_Comm()
        self.data = self.get_data.getdata()
        # print(self.data)
        # self.data = self.data.tolist()
        # 对“self.data”进行参数调整 -----------------------
        curpath = os.path.dirname(os.path.realpath(__file__))
        cfgpath = os.path.join(curpath, "config.ini")
        conf = configparser.ConfigParser()
        conf.read(cfgpath, encoding="utf-8")  # python3
        value0 = conf.getfloat('test1', 'node0')
        value1 = conf.getfloat('test1', 'node1')
        value2 = conf.getfloat('test1', 'node2')
        value3 = conf.getfloat('test1', 'node3')
        value4 = conf.getfloat('test1', 'node4')
        value5 = conf.getfloat('test1', 'node5')
        value6 = conf.getfloat('test1', 'node6')
        value7 = conf.getfloat('test1', 'node7')
        value8 = conf.getfloat('test1', 'node8')
        value9 = conf.getfloat('test1', 'node9')
        value10 = conf.getfloat('test1', 'node10')
        value11 = conf.getfloat('test1', 'node11')
        value12 = conf.getfloat('test1', 'node12')
        value13 = conf.getfloat('test1', 'node13')
        value14 = conf.getfloat('test1', 'node14')
        value15 = conf.getfloat('test1', 'node15')
        value16 = conf.getfloat('test1', 'node16')
        value17 = conf.getfloat('test1', 'node17')
        value18 = conf.getfloat('test1', 'node18')
        value19 = conf.getfloat('test1', 'node19')
        value20 = conf.getfloat('test1', 'node20')
        value21 = conf.getfloat('test1', 'node21')
        value22 = conf.getfloat('test1', 'node22')
        value23 = conf.getfloat('test1', 'node23')
        value24 = conf.getfloat('test1', 'node24')
        value25 = conf.getfloat('test1', 'node25')
        value26 = conf.getfloat('test1', 'node26')
        value27 = conf.getfloat('test1', 'node27')
        value28 = conf.getfloat('test1', 'node28')
        value29 = conf.getfloat('test1', 'node29')
        value30 = conf.getfloat('test1', 'node30')
        value31 = conf.getfloat('test1', 'node31')
        value32 = conf.getfloat('test1', 'node32')
        value33 = conf.getfloat('test1', 'node33')
        value34 = conf.getfloat('test1', 'node34')
        value35 = conf.getfloat('test1', 'node35')
        value36 = conf.getfloat('test1', 'node36')
        value37 = conf.getfloat('test1', 'node37')
        value38 = conf.getfloat('test1', 'node38')
        value39 = conf.getfloat('test1', 'node39')
        value40 = conf.getfloat('test1', 'node40')
        value41 = conf.getfloat('test1', 'node41')
        value42 = conf.getfloat('test1', 'node42')
        value43 = conf.getfloat('test1', 'node43')
        value44 = conf.getfloat('test1', 'node44')
        value45 = conf.getfloat('test1', 'node45')
        value46 = conf.getfloat('test1', 'node46')
        value47 = conf.getfloat('test1', 'node47')
        value48 = conf.getfloat('test1', 'node48')
        value49 = conf.getfloat('test1', 'node49')
        value50 = conf.getfloat('test1', 'node50')
        value51 = conf.getfloat('test1', 'node51')
        value52 = conf.getfloat('test1', 'node52')
        value53 = conf.getfloat('test1', 'node53')
        value54 = conf.getfloat('test1', 'node54')
        value55 = conf.getfloat('test1', 'node55')
        value56 = conf.getfloat('test1', 'node56')
        value57 = conf.getfloat('test1', 'node57')
        value58 = conf.getfloat('test1', 'node58')
        value59 = conf.getfloat('test1', 'node59')
        value60 = conf.getfloat('test1', 'node60')
        value61 = conf.getfloat('test1', 'node61')
        value62 = conf.getfloat('test1', 'node62')
        value63 = conf.getfloat('test1', 'node63')
        value64 = conf.getfloat('test1', 'node64')
        value65 = conf.getfloat('test1', 'node65')
        value66 = conf.getfloat('test1', 'node66')
        value67 = conf.getfloat('test1', 'node67')
        value68 = conf.getfloat('test1', 'node68')
        value69 = conf.getfloat('test1', 'node69')
        value70 = conf.getfloat('test1', 'node70')
        value71 = conf.getfloat('test1', 'node71')
        value72 = conf.getfloat('test1', 'node72')
        value73 = conf.getfloat('test1', 'node73')
        value74 = conf.getfloat('test1', 'node74')
        self.data[0] = self.data[0] + value0
        self.data[1] = self.data[1] + value1
        self.data[2] = self.data[2] + value2
        self.data[3] = self.data[3] + value3
        self.data[4] = self.data[4] + value4
        self.data[5] = self.data[5] + value5
        self.data[6] = self.data[6] + value6
        self.data[7] = self.data[7] + value7
        self.data[8] = self.data[8] + value8
        self.data[9] = self.data[9] + value9
        self.data[10] = self.data[10] + value10
        self.data[11] = self.data[11] + value11
        self.data[12] = self.data[12] + value12
        self.data[13] = self.data[13] + value13
        self.data[14] = self.data[14] + value14
        self.data[15] = self.data[15] + value15
        self.data[16] = self.data[16] + value16
        self.data[17] = self.data[17] + value17
        self.data[18] = self.data[18] + value18
        self.data[19] = self.data[19] + value19
        self.data[20] = self.data[20] + value20
        self.data[21] = self.data[21] + value21
        self.data[22] = self.data[22] + value22
        self.data[23] = self.data[23] + value23
        self.data[24] = self.data[24] + value24
        self.data[25] = self.data[25] + value25
        self.data[26] = self.data[26] + value26
        self.data[27] = self.data[27] + value27
        self.data[28] = self.data[28] + value28
        self.data[29] = self.data[29] + value29
        self.data[30] = self.data[30] + value30
        self.data[31] = self.data[31] + value31
        self.data[32] = self.data[32] + value32
        self.data[33] = self.data[33] + value33
        self.data[34] = self.data[34] + value34
        self.data[35] = self.data[35] + value35
        self.data[36] = self.data[36] + value36
        self.data[37] = self.data[37] + value37
        self.data[38] = self.data[38] + value38
        self.data[39] = self.data[39] + value39
        self.data[40] = self.data[40] + value40
        self.data[41] = self.data[41] + value41
        self.data[42] = self.data[42] + value42
        self.data[43] = self.data[43] + value43
        self.data[44] = self.data[44] + value44
        self.data[45] = self.data[45] + value45
        self.data[46] = self.data[46] + value46
        self.data[47] = self.data[47] + value47
        self.data[48] = self.data[48] + value48
        self.data[49] = self.data[49] + value49
        self.data[50] = self.data[50] + value50
        self.data[51] = self.data[51] + value51
        self.data[52] = self.data[52] + value52
        self.data[53] = self.data[53] + value53
        self.data[54] = self.data[54] + value54
        self.data[55] = self.data[55] + value55
        self.data[56] = self.data[56] + value56
        self.data[57] = self.data[57] + value57
        self.data[58] = self.data[58] + value58
        self.data[59] = self.data[59] + value59
        self.data[60] = self.data[60] + value60
        self.data[61] = self.data[61] + value61
        self.data[62] = self.data[62] + value62
        self.data[63] = self.data[63] + value63
        self.data[64] = self.data[64] + value64
        self.data[65] = self.data[65] + value65
        self.data[66] = self.data[66] + value66
        self.data[67] = self.data[67] + value67
        self.data[68] = self.data[68] + value68
        self.data[69] = self.data[69] + value69
        self.data[70] = self.data[70] + value70
        self.data[71] = self.data[71] + value71
        self.data[72] = self.data[72] + value72
        self.data[73] = self.data[73] + value73
        self.data[74] = self.data[74] + value74
        # self.data调整完毕                  -------------------
        # 将数据以xls形式保存在日期文件夹中
        time2 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')  # 此时时间
        data1, data2 = time2.split("_", 1)
        # 颜色
        styleBlueBkg = easyxf('pattern: pattern solid, fore_colour ice_blue');  # 80% like
        styleBold = easyxf('pattern: pattern solid, fore_colour gray25');
        # 坐标信息
        self.small_x_y = [[20, 0], [20, 832.5], [20, 1665], [20, 2497.5], [20, 3330], [692.5, 0], [692.5, 832.5],
                          [692.5, 1665], [692.5, 2497.5], [692.5, 3330], [1365, 0], [1365, 832.5], [1365, 1665],
                          [1365, 2497.5], [1365, 3330], [2037.5, 0], [2037.5, 832.5], [2037.5, 1665],
                          [2037.5, 2497.5],
                          [2037.5, 3330], [2710, 0], [2710, 832.5], [2710, 1665], [2710, 2497.5], [2710, 3330]]
        # 生成文件夹
        data_floder = 'Excell' + '/' + time2 + 'Time'
        if os.path.isdir(data_floder) == False | os.path.exists(data_floder) == False:
            os.makedirs(data_floder)
        # 写入excel
        tilte = ['Time', 'X', 'Y', 'Number', 'Temperature']
        wx = Workbook()
        ws = wx.add_sheet('sheet1')
        ws.col(0).width = 256 * 20
        ws.col(4).width = 256 * 12
        for i in range(0, 5):
            ws.write(0, i, tilte[i])
        # 批量写数据
        for i in range(0, 25):
            ws.write(i + 1, 0, str(time2), styleBlueBkg)
            ws.write(i + 1, 1, self.small_x_y[i % 25][0], styleBlueBkg)
            ws.write(i + 1, 2, self.small_x_y[i % 25][1], styleBlueBkg)
            ws.write(i + 1, 3, i + 1, styleBlueBkg)
            ws.write(i + 1, 4, self.data[i], styleBlueBkg)
        for i in range(25, 50):
            ws.write(i + 1, 0, str(time2), styleBold)
            ws.write(i + 1, 1, self.small_x_y[i % 25][0], styleBold)
            ws.write(i + 1, 2, self.small_x_y[i % 25][1], styleBold)
            ws.write(i + 1, 3, i + 1, styleBold)
            ws.write(i + 1, 4, self.data[i], styleBold)
        for i in range(50, 75):
            ws.write(i + 1, 0, str(time2))
            ws.write(i + 1, 1, self.small_x_y[i % 25][0])
            ws.write(i + 1, 2, self.small_x_y[i % 25][1])
            ws.write(i + 1, 3, i + 1)
            ws.write(i + 1, 4, self.data[i])
        # excels文件路径   xls！！!
        self.file1 = data_floder + '/' + data2 + '.xls'
        wx.save(self.file1)



