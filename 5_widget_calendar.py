import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QMainWindow()
w.resize(600,400)
w.setWindowTitle("Widget Kalendar")

kalender = QCalendarWidget(w)
kalender.setGridVisible(True)
kalender.move(0,0)
kalender.resize(600,400)

w.show()

sys.exit(a.exec_())