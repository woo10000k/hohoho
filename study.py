import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.make_button()
   
   
#부모 클래스 메소드 호출하기    
    def make_button(self):
        btn = QPushButton(str(self), self)
        btn.setCheckable(True)
        btn.toggle()
        


    def initUI(self):
        label2 = QLabel('Face', self)
        label2.setAlignment(Qt.AlignVCenter)

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        label2.setFont(font2)

        

        btn2 = QPushButton('Rear', self)
        btn2.setCheckable(True)
        btn2.toggle()

        btn3 = QPushButton('Left', self)
        btn3.setCheckable(True)
        btn3.toggle()

        btn4 = QPushButton('Right', self)
        btn4.setCheckable(True)
        btn2.toggle()


        hbox = QGridLayout()
        hbox.addWidget(label2)
        hbox.addWidget(btn1, 0, 1)
        hbox.addWidget(btn2, 0, 2)
        hbox.addWidget(btn3, 0, 3)
        hbox.addWidget(btn4, 0, 4)


        self.setLayout(hbox)
        self.setWindowTitle('Properties')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
