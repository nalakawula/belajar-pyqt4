import sys
from PyQt4 import QtGui, QtCore

class contoh(QtGui.QWidget):

    def __init__(self):
        super(contoh, self).__init__()

        self.initUI()
        self.resize(600,400)


    def initUI(self):

        kalender = QtGui.QCalendarWidget(self)
        kalender.setGridVisible(True)
        kalender.move(0, 0)

        kalender.setFirstDayOfWeek(QtCore.Qt.Monday)

        kalender.clicked[QtCore.QDate].connect(self.showDate)

        kalender.resize(600,400)

        self.lbl = QtGui.QLabel(self)

        date = kalender.selectedDate()
        self.lbl.setText(date.toString())

        self.lbl.move(400, 5)
        self.lbl.resize(100,20)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Kalender')
        self.show()


    def showDate(self, date):

        self.lbl.setText(date.toString())


def main():

    app = QtGui.QApplication(sys.argv)
    ex = contoh()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()