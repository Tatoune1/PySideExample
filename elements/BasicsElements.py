# create a QLabel
Label = QLabel("Text")
layout.addWidget(Label) # you must use layout.addWidget(Thing) in order for it to be on the window

# Create a QLineEdit
input = QLineEdit()
input.setPlaceholderText("text") # Hint text for the user
layout.addWidget(input)

# Create a QPushButton with text
button = QPushButton("Text")
layout.addWidget(button)
