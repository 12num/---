# 载入模块
import numpy as np
import matplotlib
#！！！如果不加上，则plt就会展现出来（前端看不见但是后端是打开的），后续plt.close时候就会关闭GUI界面
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import pandas as pd
import seaborn as sns
from scipy import interpolate
import datetime as time
import os


class atals():
    def __init__(self):
        a=1

    def showatals1(self,data1,time2):
        self.x = np.linspace(0, 330, 5)
        self.y = np.linspace(0, 330, 5)
        self.z=data1
        # print(type(self.z))
        self.f = interpolate.interp2d(self.x, self.y, self.z, kind='cubic')
        self.xnew = np.arange(0, 330, 10)
        self.ynew = np.arange(0, 330, 10)
        self.znew = self.f(self.xnew, self.ynew)
        self.xx1, self.yy1 = np.meshgrid(self.xnew, self.ynew)
        self.newshape = (self.xx1.shape[0]) * (self.xx1.shape[0])
        self.y_input = self.xx1.reshape(self.newshape)
        self.x_input = self.yy1.reshape(self.newshape)
        self.z_input = self.znew.reshape(self.newshape)

        sns.set(style='white')
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(self.xx1, self.yy1, self.znew, rstride=1, cstride=1, linewidth=0.0001, cmap=plt.get_cmap('rainbow'))
        fig.colorbar(surf, shrink=0.5, aspect=5)
        # ax.plot_trisurf(x_input,y_input,z_input,cmap=plt.get_cmap('rainbow'))
        #时间文件创建
        time2 = time.datetime.now().strftime('%Y-%m-%d_%H-%M')  # 此时时间
        data1, data2 = time2.split("_", 1)
        data_floder = 'Picture' + '/' + data1
        if os.path.isdir(data_floder) == False | os.path.exists(data_floder) == False:
            os.makedirs(data_floder)
        self.file1 = data_floder + '/' + data2 +  '上层.jpg'
        plt.savefig(self.file1)
        # plt.show()
        plt.close(fig)

    def showatals2(self,data2,time2):
        self.x = np.linspace(0, 330, 5)
        self.y = np.linspace(0, 330, 5)
        self.z=data2
        self.f = interpolate.interp2d(self.x, self.y, self.z, kind='cubic')
        self.xnew = np.arange(0, 330, 10)
        self.ynew = np.arange(0, 330, 10)
        self.znew = self.f(self.xnew, self.ynew)
        self.xx1, self.yy1 = np.meshgrid(self.xnew, self.ynew)
        self.newshape = (self.xx1.shape[0]) * (self.xx1.shape[0])
        self.y_input = self.xx1.reshape(self.newshape)
        self.x_input = self.yy1.reshape(self.newshape)
        self.z_input = self.znew.reshape(self.newshape)

        sns.set(style='white')
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(self.xx1, self.yy1, self.znew, rstride=1, cstride=1, linewidth=0.0001, cmap=plt.get_cmap('rainbow'))
        fig.colorbar(surf, shrink=0.5, aspect=5)
        # ax.plot_trisurf(x_input,y_input,z_input,cmap=plt.get_cmap('rainbow'))
        # 时间文件创建
        time2 = time.datetime.now().strftime('%Y-%m-%d_%H-%M')  # 此时时间
        data1, data2 = time2.split("_", 1)
        data_floder = 'Picture' + '/' + data1
        if os.path.isdir(data_floder) == False | os.path.exists(data_floder) == False:
            os.makedirs(data_floder)
        self.file2 = data_floder + '/' + data2 + '中层.jpg'
        plt.savefig(self.file2)
        # plt.show()
        plt.close(fig)

    def showatals3(self,data3,time2):
        self.x = np.linspace(0, 330, 5)
        self.y = np.linspace(0, 330, 5)
        self.z=data3
        self.f = interpolate.interp2d(self.x, self.y, self.z, kind='cubic')
        self.xnew = np.arange(0, 330, 10)
        self.ynew = np.arange(0, 330, 10)
        self.znew = self.f(self.xnew, self.ynew)
        self.xx1, self.yy1 = np.meshgrid(self.xnew, self.ynew)
        self.newshape = (self.xx1.shape[0]) * (self.xx1.shape[0])
        self.y_input = self.xx1.reshape(self.newshape)
        self.x_input = self.yy1.reshape(self.newshape)
        self.z_input = self.znew.reshape(self.newshape)

        sns.set(style='white')
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(self.xx1, self.yy1, self.znew, rstride=1, cstride=1, linewidth=0.0001, cmap=plt.get_cmap('rainbow'))
        fig.colorbar(surf, shrink=0.5, aspect=5)
        # ax.plot_trisurf(x_input,y_input,z_input,cmap=plt.get_cmap('rainbow'))
        # 时间文件创建
        time2 = time.datetime.now().strftime('%Y-%m-%d_%H-%M')  # 此时时间
        data1, data2 = time2.split("_", 1)
        data_floder = 'Picture' + '/' + data1
        if os.path.isdir(data_floder) == False | os.path.exists(data_floder) == False:
            os.makedirs(data_floder)
        self.file3 = data_floder + '/' + data2 + '下层.jpg'
        plt.savefig(self.file3)
        # plt.show()
        plt.close(fig)


    def showatals4(self,data1,time2):
        self.x = np.linspace(0, 330, 5)
        self.y = np.linspace(0, 330, 5)
        self.z=data1
        self.f = interpolate.interp2d(self.x, self.y, self.z, kind='cubic')
        self.xnew = np.arange(0, 330, 10)
        self.ynew = np.arange(0, 330, 10)
        self.znew = self.f(self.xnew, self.ynew)
        self.xx1, self.yy1 = np.meshgrid(self.xnew, self.ynew)
        self.newshape = (self.xx1.shape[0]) * (self.xx1.shape[0])
        self.y_input = self.xx1.reshape(self.newshape)
        self.x_input = self.yy1.reshape(self.newshape)
        self.z_input = self.znew.reshape(self.newshape)

        sns.set(style='white')
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(self.xx1, self.yy1, self.znew, rstride=1, cstride=1, linewidth=0.0001, cmap=plt.get_cmap('rainbow'))
        fig.colorbar(surf, shrink=0.5, aspect=5)
        # ax.plot_trisurf(x_input,y_input,z_input,cmap=plt.get_cmap('rainbow'))
        #时间文件创建
        time2 = time.datetime.now().strftime('%Y-%m-%d_%H-%M')  # 此时时间
        data1, data2 = time2.split("_", 1)
        data_floder = 'Picture' + '/' + time2+'Time'
        if os.path.isdir(data_floder) == False | os.path.exists(data_floder) == False:
            os.makedirs(data_floder)
        self.file1 = data_floder + '/' + data2 +  '上层.jpg'
        plt.savefig(self.file1)
        # plt.show()
        plt.close(fig)

    def showatals5(self,data2,time2):
        self.x = np.linspace(0, 330, 5)
        self.y = np.linspace(0, 330, 5)
        self.z=data2
        self.f = interpolate.interp2d(self.x, self.y, self.z, kind='cubic')
        self.xnew = np.arange(0, 330, 10)
        self.ynew = np.arange(0, 330, 10)
        self.znew = self.f(self.xnew, self.ynew)
        self.xx1, self.yy1 = np.meshgrid(self.xnew, self.ynew)
        self.newshape = (self.xx1.shape[0]) * (self.xx1.shape[0])
        self.y_input = self.xx1.reshape(self.newshape)
        self.x_input = self.yy1.reshape(self.newshape)
        self.z_input = self.znew.reshape(self.newshape)

        sns.set(style='white')
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(self.xx1, self.yy1, self.znew, rstride=1, cstride=1, linewidth=0.0001, cmap=plt.get_cmap('rainbow'))
        fig.colorbar(surf, shrink=0.5, aspect=5)
        # ax.plot_trisurf(x_input,y_input,z_input,cmap=plt.get_cmap('rainbow'))
        # 时间文件创建
        time2 = time.datetime.now().strftime('%Y-%m-%d_%H-%M')  # 此时时间
        data1, data2 = time2.split("_", 1)
        data_floder = 'Picture' + '/' + time2+'Time'
        if os.path.isdir(data_floder) == False | os.path.exists(data_floder) == False:
            os.makedirs(data_floder)
        self.file2 = data_floder + '/' + data2 + '中层.jpg'
        plt.savefig(self.file2)
        # plt.show()
        plt.close(fig)

    def showatals6(self,data3,time2):
        self.x = np.linspace(0, 330, 5)
        self.y = np.linspace(0, 330, 5)
        self.z=data3
        self.f = interpolate.interp2d(self.x, self.y, self.z, kind='cubic')
        self.xnew = np.arange(0, 330, 10)
        self.ynew = np.arange(0, 330, 10)
        self.znew = self.f(self.xnew, self.ynew)
        self.xx1, self.yy1 = np.meshgrid(self.xnew, self.ynew)
        self.newshape = (self.xx1.shape[0]) * (self.xx1.shape[0])
        self.y_input = self.xx1.reshape(self.newshape)
        self.x_input = self.yy1.reshape(self.newshape)
        self.z_input = self.znew.reshape(self.newshape)

        sns.set(style='white')
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(self.xx1, self.yy1, self.znew, rstride=1, cstride=1, linewidth=0.0001, cmap=plt.get_cmap('rainbow'))
        fig.colorbar(surf, shrink=0.5, aspect=5)
        # ax.plot_trisurf(x_input,y_input,z_input,cmap=plt.get_cmap('rainbow'))
        # 时间文件创建
        time2 = time.datetime.now().strftime('%Y-%m-%d_%H-%M')  # 此时时间
        data1, data2 = time2.split("_", 1)
        data_floder = 'Picture' + '/' + time2+'Time'
        if os.path.isdir(data_floder) == False | os.path.exists(data_floder) == False:
            os.makedirs(data_floder)
        self.file3 = data_floder + '/' + data2 + '下层.jpg'
        plt.savefig(self.file3)
        # plt.show()
        plt.close(fig)
