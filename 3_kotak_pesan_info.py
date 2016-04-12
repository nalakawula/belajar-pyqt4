import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QWidget()

Info = QMessageBox.information(w, "Message", "I Love U so much")

w.show()
sys.exit(a.exec_())