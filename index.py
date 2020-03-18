import sys

from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def show_image(image_path='demo1.jpg'):
    app = QtWidgets.QApplication(sys.argv)
    w = QWidget()
    w.label = QLabel(w)
    w.label.setText("   显示图片")
    w.label.setFixedSize(300, 200)
    w.label.move(160, 160)
    w.label.setStyleSheet("QLabel{background:white;}"
                             "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                             )
    #resize()方法调整窗口的大小。这离是250px宽150px高
    w.resize(600, 400)
    #move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
#    w.move(300, 300)
    #设置窗口的标题
    w.setWindowTitle('Simple')
    jpg = QtGui.QPixmap(image_path).scaled(w.label.width(), w.label.height())
    w.label.setPixmap(jpg)
    #显示在屏幕上
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    show_image()
