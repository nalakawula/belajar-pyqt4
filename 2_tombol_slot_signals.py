import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Tombol slot signal')

tbl = QPushButton('Klik', w)

@pyqtSlot()
def on_click():
    print ('clicked')

@pyqtSlot()
def on_pressed():
    print('pressed')

@pyqtSlot()
def on_release():
    print('released')

tbl.clicked.connect(on_click)
tbl.pressed.connect(on_pressed)
tbl.released.connect(on_release)

w.show()
app.exec_()