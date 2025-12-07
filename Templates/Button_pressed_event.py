from PySide6.QtWidgets import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__() # copy the parent class attributes and methods (QWidget in our case)
        self.setWindowTitle("Signals & Slots")

        # Create a vertical layout
        layout = QVBoxLayout()
        self.setLayout(layout) # Set the layout for this window

        # Create a button
        self.button = QPushButton("Text")
        layout.addWidget(self.button)

        # Connect the button's 'clicked' signal to our custom 'something' slot
        self.button.clicked.connect(self.something)
        # When the button is clicked, the on_button_clicked method will be called.

        # Create a QSlider
        slider = QSlider()
        layout.addWidget(self.slider)

        # When the slider's value change
        slider.valueChanged.connect(something)
    # This is our custom slot method
    def something(self):
        print("something change") # Print a message to the console
        self.message_label.setText("Text2") # Update the label text

if __name__ == "__main__":  # make sure that the app does not try to run as soon as it's imported by any other program
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
