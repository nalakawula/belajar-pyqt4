import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QWidget()

w.resize(500,200)

w.setWindowTitle("Latihan1")

w.show()

sys.exit(a.exec_())
