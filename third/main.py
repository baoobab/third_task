import sys
from random import randint
from UI import Ui_MainWindow
from PyQt5.QtCore import Qt, QPoint, QPointF
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('second task')
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)


    def paint(self):
        self.do_paint = True
        self.repaint()


    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_figure(qp)
            qp.end()

    def draw_figure(self, qp):
        for i in range(randint(1, 10)):
            qp.setBrush(
                QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            a = randint(10, 50)
            qp.drawEllipse(randint(50, 250), randint(60, 250), a, a)
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
