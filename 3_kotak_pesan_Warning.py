import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QWidget()

warning = QMessageBox.warning(w, "Message", "Mau lanjut?")

w.show()
sys.exit(a.exec_())