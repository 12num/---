import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import mainwindow
import show_atlas
import datetime,sys

class show_mainwindow(mainwindow.Ui_MainWindow):
    def __init__(self):
        super(show_mainwindow,self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        # super(show_mainwindow, self).__init__(parent)
        # self.setupUi(self)
        # self.setWindowTitle(u'实时温度监控程序')
        # self.setFixedSize(1000, 700)

        # self.sc=show_atlas.show_picture(self)
        # self.NavigationToolbar = NavigationToolbar(self.sc)
        # self.verticalLayout_2.addWidget(self.sc)
        # self.verticalLayout_2.addWidget(self.NavigationToolbar)

        # # 定义开始按钮（主要实现判断，采集，绘图）
        self.pushButton.clicked.connect(self.start)
        # # 定义重置事件(结束当前的循环)
        # self.pushButton_2.clicked.connect(self.reset)
        #
        # # 设置周期定时器
        # self.period_timer = QtCore.QTimer()
        # # 设置开始定时器
        # self.start_timer = QtCore.QTimer()
        # # 周期次数计数器
        # self.task_times = 1

        def start(self):  # 定义时间
            # 判断，设置定时器，采集，循环，绘图
            # 获取起始、结束和周期的值
            # 判断设置的时间是否正确，要求起始时间和结束时间的时间间隔要在1分钟以上
            start_time = self.start_dateTimeEdit.dateTime()
            end_time = self.end_dateTimeEdit.dateTime()
            # 判断当前设置时间如果小于当前的系统时间则将时间初始化当前系统时间
            if start_time < datetime.datetime.now():
                self.start_dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime().addSecs(1))
                start_time = self.start_dateTimeEdit.dateTime()
            if end_time < datetime.datetime.now():
                self.end_dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime().addSecs(1))
                end_time = self.end_dateTimeEdit.dateTime()
            # 判断结束时间是否大于等于开始时间，如果不是，则提示对话框
            if end_time < start_time:
                message = QtGui.QMessageBox(text=u"您出入的结束时间小于您的起始时间，请重新输入！", parent=self)
                message.show()
                # 将编辑框的时间初始化当前的系统时间
                self.start_dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime().addSecs(1))
                start_time = self.start_dateTimeEdit.dateTime()
                self.end_dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime().addSecs(1))
                end_time = self.end_dateTimeEdit.dateTime()
                return
            period_time = self.spinBox.value()
            # 周期设定，如果周期超过时间间隔，则将周期设置为时间间隔的最大值
            es_time = end_time.toTime_t() - start_time.toTime_t()
            # 1.如果起止时间相同，那么就采集一次2.如果起止时间小于周期时间，则将周期时间设置为起止时间
            if es_time <= period_time * 60:
                self.spinBox.setValue((es_time / 60))
                period_time = es_time / 60
                if es_time == 0:
                    # 设置一个监视器 实时监视系统当前的时间，依据系统当前的时间值
                    self.period_timer = QtCore.QTimer()
                    self.period_timer.timeout.connect(lambda: self.one_task(start_time))
                    # 每隔1秒监测一次
                    self.period_timer.start(1000)
                    # 将起始时间和结束时间以及周期设置设置为不能使用
                    self.start_dateTimeEdit.setEnabled(False)
                    self.end_dateTimeEdit.setEnabled(False)
                    self.spinBox.setEnabled(False)
                    self.start_pushButton.setEnabled(False)
                # 采集起始和结束的时间的数据
                else:
                    self.start_timer = QtCore.QTimer()
                    self.period_timer = QtCore.QTimer()
                    self.start_timer.timeout.connect(lambda: self.two_task(start_time))
                    self.period_timer.timeout.connect(lambda: self.one_task(end_time))
                    self.start_timer.start(1000)
                    self.period_timer.start(1000)
                    # 将起始时间和结束时间以及周期设置设置为不能使用
                    self.start_dateTimeEdit.setEnabled(False)
                    self.end_dateTimeEdit.setEnabled(False)
                    self.spinBox.setEnabled(False)
                    self.start_pushButton.setEnabled(False)
            # 设置正常采集的函数
            else:
                # 三个参数开始时间结束时间和周期
                # 如果周期为0，则默认初始化为15
                if period_time == 0:
                    period_time = 15
                    self.spinBox.setValue(15)
                self.start_timer = QtCore.QTimer()
                self.start_timer.timeout.connect(lambda: self.three_task(start_time, end_time, period_time * 1000 * 60))
                self.start_timer.start(1000)
                self.start_dateTimeEdit.setEnabled(False)
                self.end_dateTimeEdit.setEnabled(False)
                self.spinBox.setEnabled(False)
                self.start_pushButton.setEnabled(False)


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    ui=show_mainwindow()
    ui.show()
sys.exit(app.exec_())