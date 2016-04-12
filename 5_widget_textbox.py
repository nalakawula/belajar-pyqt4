import sys
from PyQt4.QtGui import  *

a = QApplication(sys.argv)

w = QMainWindow()

w.resize(300, 150)
w.setWindowTitle("textbox widget")

textbox = QLineEdit(w)
textbox.move(10, 10)
textbox.resize(150, 30)

w.show()

sys.exit(a.exec_())
