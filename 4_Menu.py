import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QMainWindow()

w.resize(500,200)

w.setWindowTitle("menu")

mainMenu = w.menuBar()
mainMenu.setNativeMenuBar(False)
fileMenu = mainMenu.addMenu('File')

exitButton = QAction(QIcon('exit24.png'), 'Exit', w)
exitButton.setShortcut('Ctrl+Q')
exitButton.setStatusTip('Exit App')
exitButton.triggered.connect(w.close)
fileMenu.addAction(exitButton)

w.show()

sys.exit(a.exec_())