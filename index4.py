
import sys
from PyQt5 import QtGui, QtCore, QtWidgets


class StartGui (QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(StartGui, self).__init__(parent)
        #QtGui.QWidget.__init__(self, parent)
        #   self.ui = Ui_MainWindow()
        #   self.ui.setupUi(self)

        self.loadButton = QtWidgets.QPushButton()
        self.loadButton.setGeometry(10,10,100,100)
        self.pixmp=QtGui.QPixmap()
      
        self.pixitem = QtWidgets.QGraphicsPixmapItem()
        self.scene = QtWidgets.QGraphicsScene()
        self.grview = QtWidgets.QGraphicsView()
        self.grali=[]
        self.loadButton.clicked.connect(self.addIm)



    def addIm(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,"Open Image", "./", "Image Files (*.png *.jpg*.bmp)"); 
        if fileName:
            self.pixmp.load(fileName)
            klbild=self.pixmp.scaledToHeight(200)
            self.pixitem.setPixmap(klbild)
            self.grali.append(self.pixitem)
            self.scene.addItem(self.grali[-1]) 
            self.grview.setScene(self.scene)
            self.grview.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = StartGui()
    myapp.show()
    sys.exit(app.exec_())
