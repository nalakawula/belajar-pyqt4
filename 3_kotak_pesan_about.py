import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QWidget()

tentang = QMessageBox.about(w, "About", "Your daughter is so beautiful")

w.show()
sys.exit(a.exec_())