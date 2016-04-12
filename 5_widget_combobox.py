import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QMainWindow()
w.resize(400,200)
w.setWindowTitle("widget combobox")

combo = QComboBox(w)
combo.addItem("Python")
combo.addItem("Java")
combo.addItem("C")
combo.addItem("HTML")
combo.move(20,20)

w.show()

sys.exit(a.exec_())