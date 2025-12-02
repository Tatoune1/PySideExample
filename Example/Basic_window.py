from PySide6.QtWidgets import *
import sys


app = QApplication(sys.argv) 
window = QWidget()
window.setWindowTitle("Example")

layout = QVBoxLayout() # Create a vertical layout

# Create some widgets
Item1 = QLabel("Item1")
Item2 = QLabel("Item2")
Item3 = QLabel("Item3")


# Create a QPushButton with text "Click Me!"
button = QPushButton("Click Me!")
layout.addWidget(button) # Add the button to the layout

# Create a QLineEdit
city_input = QLineEdit()
city_input.setPlaceholderText("Enter something") # Hint text for the user
layout.addWidget(city_input)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
