import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow
from PyQt5.QtGui import QPixmap
import joblib
from sklearn.preprocessing import StandardScaler

class Welcomepage(QMainWindow):
    def __init__(self):
        super(Welcomepage, self).__init__()
        loadUi("welcomepage.ui",self)
        self.pushButton.clicked.connect(self.detailspage)
        self.pushButton_2.clicked.connect(self.endscreen)
        self.label_2.setPixmap(QPixmap('liver_smaller.jpg'))
    def endscreen(self):
        sys.exit(app.exec_())
    def detailspage(self):
        details = detailspage()
        widget.addWidget(details)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class detailspage(QMainWindow):
    def __init__(self):
        super(detailspage,self).__init__()
        loadUi("GUI.UI",self)
        self.pushButton.clicked.connect(self.prediction)
    def prediction(self):
        model = joblib.load('svm.pkl')
        print('model loaded')
        age = self.lineEdit.text()
        
if __name__ == "__main__":
        app = QApplication(sys.argv)
        welcome = Welcomepage()
        widget = QtWidgets.QStackedWidget()
        widget.addWidget(welcome)
        widget.show()
        widget.setFixedHeight(800)
        widget.setFixedWidth(800)
        try:
            sys.exit(app.exec_())
        except:
            print("Exiting")


