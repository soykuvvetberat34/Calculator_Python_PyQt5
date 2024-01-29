import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("Berat SOYKUVVET")
        self.setGeometry(750,400,500,350)
        self.setToolTip("My tooltip")
        self.initUI()
        self.setWindowIcon(QIcon("sketch.png"))
    
    def initUI(self):
        font=QFont("Arial",12)
        font_title=QFont("Arial",20)

        
        self.title=QLabel(self)
        self.title.setText("Calculator")
        self.title.resize(200,40)
        self.title.move(100,10)
        self.title.setFont(font_title)
        
        self.num1=QLabel(self)
        self.num1.setText("Enter num:")
        self.num1.move(80,70)
        self.num1.setFont(font)

        self.num1_txt=QLineEdit(self)
        self.num1_txt.move(190,70)
        self.num1_txt.resize(100,32)
        self.num1_txt.setFont(font)

        
        self.num2=QLabel(self)
        self.num2.move(80,130)
        self.num2.setText("Enter num:")
        self.num2.setFont(font)
        
        self.num2_txt=QLineEdit(self)
        self.num2_txt.move(190,130)
        self.num2_txt.resize(100,32)
        self.num2_txt.setFont(font)

        
        self.btn_add=QPushButton(self)
        self.btn_subt=QPushButton(self)
        self.btn_divi=QPushButton(self)
        self.btn_multip=QPushButton(self)
        self.btn_add.setText("Addition")
        self.btn_add.move(10,200)
        self.btn_add.setFont(font)
        self.btn_add.clicked.connect(self.process)
        
        self.btn_subt.setText("subtraction")
        self.btn_subt.move(120,200)
        self.btn_subt.resize(120,30)
        self.btn_subt.setFont(font)   
        self.btn_subt.clicked.connect(self.process)
             
        self.btn_divi.setText("Divide")
        self.btn_divi.move(250,200)
        self.btn_divi.resize(100,30)
        self.btn_divi.setFont(font)  
        self.btn_divi.clicked.connect(self.process)
             
        self.btn_multip.setText("multiplication")
        self.btn_multip.resize(130,30)
        self.btn_multip.move(360,200)
        self.btn_multip.setFont(font) 
        self.btn_multip.clicked.connect(self.process)
          
        self.result=QLabel(self) 
        self.result.setText("Result:")
        self.result.setFont(font)
        self.result.move(50,250)
        self.result.resize(400,60)
           
        
    def process(self):
        sender = self.sender()
        result = 0
                
        if sender == self.btn_add:
            result = int(self.num1_txt.text()) + int(self.num2_txt.text())
            self.result.setText(f"Result: {str(result)}")
        elif sender == self.btn_subt:
            result = int(self.num1_txt.text()) - int(self.num2_txt.text())
            self.result.setText(f"Result: {str(result)}")
        elif sender == self.btn_divi:
            result = int(self.num1_txt.text()) / int(self.num2_txt.text())
            self.result.setText(f"Result: {str(result)}")
        elif sender == self.btn_multip:  
            result = int(self.num1_txt.text()) * int(self.num2_txt.text())
            self.result.setText(f"Result: {str(result)}")

        
if __name__=='__main__':
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())
    




