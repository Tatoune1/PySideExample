# create a QLabel
Label = QLabel("Text")
layout.addWidget(Label) # you must use layout.addWidget(Thing) in order for it to be on the window

# Create a QLineEdit
city_input = QLineEdit()
city_input.setPlaceholderText("Enter city name...") # Hint text for the user
layout.addWidget(city_input)

# Create a QPushButton with text
button = QPushButton("Text")
layout.addWidget(button)
