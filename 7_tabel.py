import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

def main():
    app = QApplication(sys.argv)
    tabel = QTableWidget()


    tabel.setWindowTitle('Tabel')
    tabel.resize(800,600)
    tabel.setRowCount(4)
    tabel.setColumnCount(2)

    tabel.setItem(0,0, QTableWidgetItem("A"))
    tabel.setItem(0,1, QTableWidgetItem("B"))
    tabel.setItem(1,0, QTableWidgetItem("C"))
    tabel.setItem(1,1, QTableWidgetItem("D"))
    tabel.setItem(2,0, QTableWidgetItem("E"))
    tabel.setItem(2,1, QTableWidgetItem("F"))
    tabel.setItem(3,0, QTableWidgetItem("G"))
    tabel.setItem(3,1, QTableWidgetItem("H"))



    tabel.show()
    return app.exec_()

if __name__ == '__main__':
    main()