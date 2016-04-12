import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QWidget()

tanya = QMessageBox.question(w, 'Message', 'Kamu suka aku?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

if tanya == QMessageBox.Yes:
    print('Yes.')

else:
    print('No.')

w.show()
sys.exit(a.exec_())