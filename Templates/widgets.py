# create a QLabel
Label = QLabel("Text")

# Create a QLineEdit
input = QLineEdit()
input.setPlaceholderText("text") # Hint text for the user

# Create a QPushButton with text
button = QPushButton("Text")

# Create a QSlider
slider = QSlider(tickIntervall = 0, tickPosition = 0) 
# tickIntervall : spacing between tick marks, measured in slider value units, 0 and the slider will choose between singleStep and pageStep
# tickPosition : holds the tickmark position for this slider, the default value is 0
slider.setMinimum(1)
slider.setMaximum(50)
slider.setValue(10) #set the value of the slider to an integer between 0 and 100
