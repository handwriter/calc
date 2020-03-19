from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import sys
from design import Ui_Form as Design
from PyQt5.QtCore import QTimer


class DialogGenerator:
    def __init__(self, text, title, types='critical'):
        self.box = QMessageBox()
        if types == 'critical':  # Условие в зависимости от переанного типа сообщения
            self.box.setIcon(QMessageBox.Critical)  # меняющее отображаемуюю иконку
        elif types == 'information':
            self.box.setIcon(QMessageBox.Information)
        elif types == 'text':
            pass
        self.box.setText(text)
        self.box.setWindowTitle(title)

    def get_class(self):  # функция возвращает класс созданного объекта
        return self.box


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.p1)
        self.pushButton_2.clicked.connect(self.p2)
        self.pushButton_3.clicked.connect(self.p3)
        self.pushButton_4.clicked.connect(self.p4)
        self.pushButton_5.clicked.connect(self.p5)
        self.pushButton_6.clicked.connect(self.p6)
        self.pushButton_7.clicked.connect(self.p7)
        self.pushButton_8.clicked.connect(self.p8)
        self.pushButton_9.clicked.connect(self.p9)
        self.pushButton_10.clicked.connect(self.p10)
        self.pushButton_11.clicked.connect(self.p11)
        self.pushButton_12.clicked.connect(self.p12)
        self.pushButton_13.clicked.connect(self.p13)
        self.pushButton_14.clicked.connect(self.p14)
        self.pushButton_15.clicked.connect(self.p15)
        self.pushButton_16.clicked.connect(self.p16)
        self.pushButton_17.clicked.connect(self.p17)
        self.pushButton_18.clicked.connect(self.p18)
        self.prt = ''
        self.timer = QTimer()
        self.timer.timeout.connect(self.updater)
        self.timer.start(1)

    def p1(self):
        self.prt += '1'

    def p2(self):
        self.prt += '2'

    def p3(self):
        self.prt += '3'

    def p4(self):
        self.prt += '4'

    def p5(self):
        self.prt += '5'

    def p6(self):
        self.prt += '6'

    def p7(self):
        self.prt += '7'

    def p8(self):
        self.prt += '8'

    def p9(self):
        self.prt += '9'

    def p10(self):
        self.prt += '0'

    def p11(self):
        self.prt += '/'

    def p12(self):
        self.prt += '+'

    def p13(self):
        self.prt += ' - '

    def p14(self):
        self.prt += '*'

    def p15(self):
        try:
            self.prt = str(eval(self.prt))
        except:
            self.ex = DialogGenerator("Error", "Error", "critical").get_class()
            self.ex.show()

    def p16(self):
        try:
            self.prt = str(self.prt)[:-1]
        except:
            pass

    def p17(self):
        if len(self.prt) == 0:
            self.prt += '-'
        else:
            if self.prt[-1] == '-':
                self.prt = str(self.prt)[:-1]
            else:
                self.prt = str(self.prt) + '-'

    def p18(self):
        if len(self.prt) == 0:
            self.ex = DialogGenerator("Error", "Error", "critical").get_class()
            self.ex.show()
        elif not self.prt[-1].isdigit():
            self.ex = DialogGenerator("Error", "Error", "critical").get_class()
            self.ex.show()
        else:
            self.prt = str(self.prt) + '.'

    def updater(self):
        self.label.setText(str(self.prt))


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())