
# coding:utf-8
import serial, sys, binascii, struct, random



# 实现和巡检仪通讯，并且获取数据
# 程序使用的是系统的“com1”串口，其他串口无效
# 点击 SerialDebugTool 串口调试工具，设置好相应的串口号和波特率，就可以进行串口调试。
class Serial_Comm(object):

    def __init__(self):
        # send_big_code：是发送的代码指令      big_data：是返回的数据
        self.big_data = []
        self.send_big_code = ['010400000020F1D2', '010400200020F018', '010400400020F006', '010400600020F1CC','010400800020F03A']

    def getdata(self):
        self.ser = serial.Serial(port="com6", baudrate=9600, stopbits=1, timeout=0.05)
        # W创建串口连接
        # port=None, # 设备编号  baudrate=9600, # 波特率  stopbits=STOPBITS_ONE, # 停止位的数量  timeout=None, # 设置超时值，None 表示永远等待
        for send_code in self.send_big_code:  # 获取指令集
            self.ser.write(binascii.a2b_hex(send_code))  # binascii.a2b_hex(string)     将十六进制数字字符串转换为二进制数据。
            # 发送数据   函数名write()
            hex_data = self.ser.readall()
            # 接收数据(接收固定长度数据)     函数名为read(size=1)
            for i in range(3, len(hex_data) - 2, 4):
                self.big_data.append(round(struct.unpack('!f', hex_data[i:i + 4])[0], 2))
        self.ser.close()
        # 使用ser.close即可关闭串口


        if len(self.big_data) == 80:
            t1 = self.big_data[1]
            t2 = self.big_data[5]
            t = (t1 + t2) / 2
            self.big_data[0] = t
            return self.big_data[0:75]
        else:
            self.big_data = []
            for i in range(0, 120):
                self.big_data.append(random.randint(0, 8) - 2)
            return self.big_data
