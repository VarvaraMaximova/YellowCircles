import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.doPaint = False
        self.generateButton.clicked.connect(self.changeDoPaint)

    def changeDoPaint(self):
        self.doPaint = True
        self.update()

    def paintEvent(self, event):
        if self.doPaint:
            qp = QPainter()
            qp.begin(self)
            n = randint(2, 30)
            for i in range(n):
                self.drawCircle(qp)
            qp.end()
        self.doPaint = False

    def drawCircle(self, qp):
        qp.setBrush(QColor(255, 216, 0))
        try:
            x = randint(20, self.size().width() - 20)
        except ValueError:
            x = self.size().width() // 2
        try:
            y = randint(20, self.size().height() - 20)
        except ValueError:
            y = self.size().height() // 2
        r = randint(20, 100)
        qp.drawEllipse(x, y, r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
