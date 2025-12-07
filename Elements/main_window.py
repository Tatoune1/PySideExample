from PySide6.QtWidgets import *

import sys

#Basic templates of a window with Qt
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My window")
        #add Qwidget


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()
