import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.generateButton.clicked.connect(self.printCircle)

    def printCircle(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
