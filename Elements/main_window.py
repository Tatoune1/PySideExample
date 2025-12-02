from PySide6.QtWidgets import *
import sys

app = QApplication(sys.argv) #Central control object for the app and manages vent loop, settings, and general lifecycle. Must create one QApplication instance per app.
window = QWidget()
window.setWindowTitle("Title")

window.show()
sys.exit(app.exec())

#create an empty window of an app, with a title.
