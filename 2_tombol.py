import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QWidget()

w.resize(500,200)

w.setWindowTitle('Latihan2')

tbl = QPushButton('Klik', w)
tbl.setToolTip('Klik tombol ini')
tbl.clicked.connect(exit)
tbl.resize(tbl.sizeHint())
tbl.move(400,150)

w.show()

sys.exit(a.exec_())