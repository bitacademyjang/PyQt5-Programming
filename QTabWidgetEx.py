import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        tabs = QTabWidget()
        tabs.addTab(FirstTab(), '길이')
        tabs.addTab(SecondTab(), '넓이')

        vbox = QGridLayout()
        vbox.addWidget(tabs)


        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 200, 200)
        self.show()

    def trans_func(self):
        pass

class FirstTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        name = QLabel('변환 길이 선택')
        self.cb_length = QComboBox(self)
        self.cb_length.addItem('단위 선택')
        self.cb_length.addItem('mm')
        self.cb_length.addItem('cm')
        self.cb_length.addItem('m')
        self.cb_length.addItem('km')
        self.length_val = QLineEdit(self)

        self.mm = QLabel()
        self.cm = QLabel()
        self.m = QLabel()
        self.km = QLabel()

        vbox = QGridLayout()
        vbox.addWidget(name, 0,0)
        vbox.addWidget(self.cb_length, 1, 0)
        vbox.addWidget(self.length_val, 2, 0)
        vbox.addWidget(QLabel("mm : "), 3, 0)
        vbox.addWidget(self.mm, 3, 1)
        vbox.addWidget(QLabel("cm : "), 4, 0)
        vbox.addWidget(self.cm, 4, 1)
        vbox.addWidget(QLabel("m : "), 5, 0)
        vbox.addWidget(self.m, 5, 1)
        vbox.addWidget(QLabel("km : "), 6, 0)
        vbox.addWidget(self.km, 6, 1)

        self.cb_length.activated.connect(self.lengthChanged)

        self.setLayout(vbox)

    def lengthChanged(self, index):
        if index == 1:
            self.mm.setNum(int(self.length_val.text()))
            self.cm.setNum(int(self.length_val.text()) / 10)
            self.m.setNum(int(self.length_val.text()) / 1000)
            self.km.setNum(int(self.length_val.text()) / 1000000)
        elif index == 2:
            self.mm.setNum(int(self.length_val.text()) * 10)
            self.cm.setNum(int(self.length_val.text()))
            self.m.setNum(int(self.length_val.text()) / 100)
            self.km.setNum(int(self.length_val.text()) / 100000)
        elif index == 3:
            self.mm.setNum(int(self.length_val.text()) * 1000)
            self.cm.setNum(int(self.length_val.text()) * 100)
            self.m.setNum(int(self.length_val.text()))
            self.km.setNum(int(self.length_val.text()) / 1000)
        elif index == 4:
            self.mm.setNum(int(self.length_val.text()) * 1000000)
            self.cm.setNum(int(self.length_val.text()) * 100000)
            self.m.setNum(int(self.length_val.text()) * 1000)
            self.km.setNum(int(self.length_val.text()))
        elif index == 0:
            self.mm.clear()
            self.cm.clear()
            self.m.clear()
            self.km.clear()

class SecondTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        name = QLabel('변환 넓이 선택')
        self.cb_area = QComboBox(self)
        self.cb_area.addItem('단위 선택')
        self.cb_area.addItem('제곱미터')
        self.cb_area.addItem('아르')
        self.cb_area.addItem('헥타르')
        self.cb_area.addItem('제곱킬로미터')
        self.area_val = QLineEdit(self)
        self.m2 = QLabel()
        self.a = QLabel()
        self.ha = QLabel()
        self.km2 = QLabel()

        vbox = QGridLayout()
        vbox.addWidget(name, 0, 0)
        vbox.addWidget(self.cb_area, 1, 0)
        vbox.addWidget(self.area_val, 2, 0)
        vbox.addWidget(QLabel("제곱미터 : "), 3, 0)
        vbox.addWidget(self.m2, 3, 1)
        vbox.addWidget(QLabel("아르 : "), 4, 0)
        vbox.addWidget(self.a, 4, 1)
        vbox.addWidget(QLabel("헥타르 : "), 5, 0)
        vbox.addWidget(self.ha, 5, 1)
        vbox.addWidget(QLabel("제곱킬로미터 : "), 6, 0)
        vbox.addWidget(self.km2, 6, 1)

        self.cb_area.activated.connect(self.areaChanged)

        self.setLayout(vbox)

    def areaChanged(self, index):
        if index == 1:
            self.m2.setNum(int(self.area_val.text()))
            self.a.setNum(int(self.area_val.text()) / 10)
            self.ha.setNum(int(self.area_val.text()) / 10000)
            self.km2.setNum(int(self.area_val.text()) / 1000000)
        elif index == 2:
            self.m2.setNum(int(self.area_val.text()) * 100)
            self.a.setNum(int(self.area_val.text()))
            self.ha.setNum(int(self.area_val.text()) / 100)
            self.km2.setNum(int(self.area_val.text()) / 10000)
        elif index == 3:
            self.m2.setNum(int(self.area_val.text()) * 10000)
            self.a.setNum(int(self.area_val.text()) * 100)
            self.ha.setNum(int(self.area_val.text()))
            self.km2.setNum(int(self.area_val.text()) / 100)
        elif index == 4:
            self.m2.setNum(int(self.area_val.text()) * 1000000)
            self.a.setNum(int(self.area_val.text()) * 10000)
            self.ha.setNum(int(self.area_val.text()) * 100)
            self.km2.setNum(int(self.area_val.text()))
        elif index == 0:
            self.m2.clear()
            self.a.clear()
            self.ha.clear()
            self.km2.clear()

class ThirdTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lbl = QLabel('Terms and Conditions')
        text_browser = QTextBrowser()
        text_browser.setText('This is the terms and conditions')
        checkbox = QCheckBox('Check the terms and conditions.')

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(text_browser)
        vbox.addWidget(checkbox)

        self.setLayout(vbox)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())