from PySide6.QtWidgets import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__() # copy the parent class attributes and methods (QWidget in our case)
        self.setWindowTitle("Signals & Slots Example")

        # Create a vertical layout
        layout = QVBoxLayout()
        self.setLayout(layout) # Set the layout for this window

        # Create a button
        self.button = QPushButton("Text")
        layout.addWidget(self.button)

        # Connect the button's 'clicked' signal to our custom 'on_button_clicked' slot
        self.button.clicked.connect(self.on_button_clicked)
       # When the button is clicked, the on_button_clicked method will be called.

    # This is our custom slot method
    def on_button_clicked(self):
        print("Button was clicked!") # Print a message to the console
        self.message_label.setText("another text") # Update the label text

if __name__ == "__main__":  # make sure that the app does not try to run as soon as it's imported by any other program
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
