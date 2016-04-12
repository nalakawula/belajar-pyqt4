import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

#window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("tombol dan textbox")
w.resize(600,400)

#textbox
textbox = QLineEdit(w)
textbox.move(20,20)
textbox.resize(280,40)

#tombol
tombol = QPushButton('Klik', w)
tombol.move(20,80)

#aksi
@pyqtSlot()
def klik():
    textbox.setText("tombol diklik")

@pyqtSlot()
def tekan():
    textbox.setText("tombol ditahan")

@pyqtSlot()
def lepas():
    textbox.setText("tombol dilepas")

#konek
tombol.clicked.connect(klik)
tombol.pressed.connect(tekan)
tombol.released.connect(lepas)

w.show()
app.exec_()