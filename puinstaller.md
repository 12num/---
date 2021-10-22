76731 WARNING: Hidden import "pkg_resources.py2_warn" not found!
加入--hidden-import pkg_resources.py2_warn 即可解决。
76732 WARNING: Hidden import "pkg_resources.markers" not found!


lib not found:


1.python2 -m PyInstaller -F -c main.py -p C:\Users\ljt\AppData\Local\Programs\Python\Python27\Lib\site-packages\PyQt4
2.python2 -m pyinstaller -F -c main.py --hidden-import=C:\Users\ljt\AppData\Local\Programs\Python\Python27\Lib\site-packages\PyQt4
-p C:\Users\ljt\AppData\Local\Programs\Python\Python27\Lib\site-packages\PyQt4;C:\Python27\Lib\site-packages\matplotlib\backends --hidden-import matplotlib.backends.backend_tkagg


python3 -m PyInstaller -F -c main.py       #指定使用命令行窗口运行程序（仅对 Windows 有效）
python3 -m PyInstaller -F -w main.py            #指定程序运行时不显示命令行窗口

python3 -m PyInstaller -D -c main.py
python3 -m PyInstaller -D -w main.py


main.spec
datas=[('C:\\Users\\ljt\\AppData\\Local\\Programs\\Python\\Python38\\Lib\site-packages\\pyzmq.libs','')],