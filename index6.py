from PyQt5.QtCore import QPoint, QRect, QSize, Qt
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QLayout, QPushButton, QSizePolicy, QWidget, QGridLayout)


class Window(QWidget):
    def __init__(self):
        self.imageheight = 100
        super(Window, self).__init__()
        self.resize(400, 300)
        
        flowLayout = FlowLayout()
        
        highlight_dir = "./"
        self.files_it = iter([os.path.join(highlight_dir, file)
                              for file in os.listdir(highlight_dir)])

        print()
        for file in iter(self.files_it):
            layout = QGridLayout()
            pixmap = QtGui.QPixmap(file)
            if not pixmap.isNull():
                autoWidth = pixmap.width()*self.imageheight/pixmap.height()
                label = QtWidgets.QLabel(pixmap=pixmap)
                label.setScaledContents(True)
                label.setFixedHeight(self.imageheight)
                print(autoWidth)
                label.setFixedWidth(autoWidth)
                #label.setFixedSize(100, 50)
                layout.addWidget(label)
            

                widget = QWidget()
                widget.setLayout(layout)
                flowLayout.addWidget(widget)

        self.setLayout(flowLayout)

        self.setWindowTitle("Flow Layout")


class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)

        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        margin, _, _, _ = self.getContentsMargins()

        size += QSize(2 * margin, 2 * margin)
        return size

    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton,
                                                                QSizePolicy.PushButton, Qt.Horizontal)
            spaceY = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton,
                                                                QSizePolicy.PushButton, Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    mainWin = Window()
    mainWin.show()
    sys.exit(app.exec_())
