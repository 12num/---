import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import pandas as pd
import seaborn as sns
from scipy import interpolate
from PyQt5 import QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class show_picture(FigureCanvas):
    def __init__(self):
        # self.width = width
        # self.height=height
        # self.dpi=dpi
        # self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        # self.axes.hold(False)
        self.init_figure()
        self.FigureCanvas = FigureCanvas.__init__(self, self.fig)
        # self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def input_picture(self):
        # 生成数据
        x = np.linspace(0, 330, 5)
        y = np.linspace(0, 330, 5)
        z = np.array([np.random.randint(0, 30) for i in range(25)])
        # print(len(x))
        # print(len(y))
        # print(type(z))
        # 插值
        # xx, yy = np.meshgrid(x, y)

        f = interpolate.interp2d(x, y, z, kind='cubic')
        # print(type(f))

        xnew = np.arange(0, 330, 10)
        ynew = np.arange(0, 330, 10)
        znew = f(xnew, ynew)
        print(z)

        # 修改x,y，z输入画图函数前的shape
        xx1, yy1 = np.meshgrid(xnew, ynew)
        newshape = (xx1.shape[0]) * (xx1.shape[0])
        y_input = xx1.reshape(newshape)
        x_input = yy1.reshape(newshape)
        z_input = znew.reshape(newshape)

        # 画图
        sns.set(style='white')
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        surf = ax.plot_surface(xx1, yy1, znew, rstride=1, cstride=1, linewidth=0.0001, cmap=plt.get_cmap('rainbow'))
        fig.colorbar(surf, shrink=0.5, aspect=5)

        # ax.plot_trisurf(x_input,y_input,z_input,cmap=plt.get_cmap('rainbow'))
        plt.show()