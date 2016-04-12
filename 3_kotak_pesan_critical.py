import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QWidget()

critical = QMessageBox.information(w, "Message", "I will marry u")

w.show()
sys.exit(a.exec_())