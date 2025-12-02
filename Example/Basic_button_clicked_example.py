from PySide6.QtWidgets import *
import sys

class InputDisplayApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Display App")
        self.setGeometry(100, 100, 400, 150) # x, y, width, height

        # Create the main vertical layout for the entire window
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # --- Input Section (Horizontal Layout) ---
        input_layout = QHBoxLayout()

        # Label for the input field
        input_label = QLabel("Input:")
        input_layout.addWidget(input_label)

        # Line edit for current input
        self.current_input = QLineEdit()
        self.current_input.setPlaceholderText("Enter input...")
        input_layout.addWidget(self.current_input)

        # Button to display the city
        self.display_button = QPushButton("Display Input")
        input_layout.addWidget(self.display_button)

        # Add the input_layout to the main_layout
        main_layout.addLayout(input_layout)

        # --- Output Section (Label) ---
        self.output_label = QLabel("Input will appear here.")
        # Ensure text wraps if it's too long
        self.output_label.setWordWrap(True)
        # Add the output_label to the main_layout
        main_layout.addWidget(self.output_label)

        # --- Connect Signals and Slots ---
        # When the 'display_button' is clicked, call the 'update_city_display' method
        self.display_button.clicked.connect(self.update_input_display)
        # You can also connect the QLineEdit's 'returnPressed' signal (when user presses Enter)
        # to the same slot for convenience.
        self.current_input.returnPressed.connect(self.update_input_display)


    # This is our slot method that will update the label with the city name
    def update_input_display(self):
        input = self.current_input.text() # Get the text from the QLineEdit
        if input: # Only update if the text isn't empty
            self.output_label.setText(f"You entered: <b>{input}</b>")
            print(f"City entered: {input}") # For console debugging
        else:
            self.output_label.setText("Please enter a city name.")
            print("No city entered.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputDisplayApp()
    window.show()
    sys.exit(app.exec())
