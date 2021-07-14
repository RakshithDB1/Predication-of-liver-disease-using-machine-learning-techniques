import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QPixmap
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from fpdf import FPDF

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
        sc=StandardScaler()
        X_train=pd.read_csv('X_train.csv')
        age = int(self.lineEdit.text())
        male=1 if self.radioButton.isChecked() else 0
        female=1 if self.radioButton_2.isChecked() else 0
        TB = float(self.lineEdit_3.text())
        DB = float(self.lineEdit_4.text())
        alkphos = int(self.lineEdit_5.text())
        sgpt = int(self.lineEdit_6.text())
        sgot = int(self.lineEdit_8.text())
        TP = float(self.lineEdit_9.text())
        ALB = float(self.lineEdit_7.text())
        AGratio = float(self.lineEdit_10.text())
        data=np.array([age,TB,DB,alkphos,sgpt,sgot,TP,ALB,AGratio,male+1,female])
        print(data)
        model = joblib.load('svm.pkl')
        print('model loaded')
        sc.fit_transform(X_train)
        r=model.predict(sc.transform(data.reshape(1,-1)))
        if r:
            self.result.setText("NO RISK")
            print(r)
        else:
            self.result.setText("RISK")
            print(r)  
        pdf=FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size = 15)
        pdf.cell(200, 10, txt = "REPORT", ln = 1, align = 'C')
        pdf.cell(200, 10, txt = "Age:    "+str(age),ln = 3, align = 'C')
        if male:
            pdf.cell(200, 10, txt = "Gender:    Male",ln = 4, align = 'C')
        if female:
            pdf.cell(200, 10, txt = "Gender:    Female",ln = 4, align = 'C')
        
        pdf.cell(200, 10, txt = "TB:     "+str(TB),ln = 5, align = 'C')
        pdf.cell(200, 10, txt = "DB:      "+str(DB),ln = 6, align = 'C')
        pdf.cell(200, 10, txt = "alkphos     "+str(alkphos),ln = 7, align = 'C')
        pdf.cell(200, 10, txt = "sgpt:     "+str(sgpt),ln = 8, align = 'C')
        pdf.cell(200, 10, txt = "sgot:     "+str(sgot),ln = 9, align = 'C')
        pdf.cell(200, 10, txt = "TP:     "+str(TP),ln = 10, align = 'C')
        pdf.cell(200, 10, txt = "ALB:     "+str(ALB),ln = 11, align = 'C')
        pdf.cell(200, 10, txt = "AGratio:    "+str(AGratio),ln = 12, align = 'C')
        if r:
            pdf.cell(200, 10, txt = "RESULT : NO RISK",ln = 14, align = 'C')
           
        else:
            pdf.cell(200, 10, txt = "RESULT : RISK",ln = 14, align = 'C')
       
        pdf.output("REPORT.pdf") 
        
        
        
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


