from PySide6.QtWidgets import *
import sys

app = QApplication(sys.argv) #Central control object for the app and manages vent loop, settings, and general lifecycle. Must create one QApplication instance per app.
window = QWidget()
window.setWindowTitle("Title")

# Create a layout
layout = QHBoxLayout() 
"""QHBoxLayout() for an horizontal layout : element1   element2   element3
   QVBoxLayout() for a vertical layout    : element1
                                            element2
                                            element3"""
# Create some widgets
Item1 = QLabel("Item1")
Item2 = QLabel("Item2")
Item3 = QLabel("Item3")

# Add widgets to the vertical layout. They will stack and the order determine the placement 
layout.addWidget(Item1)
layout.addWidget(Item2)
layout.addWidget(Item3)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
