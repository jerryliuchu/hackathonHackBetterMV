import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'My App'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Add a label for the header
        header_label = QLabel('My App Header', self)
        header_label.move(10, 10)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
