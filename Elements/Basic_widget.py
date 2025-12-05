# 1. Create the QApplication instance
app = QApplication(sys.argv)

# 2. Create a QWidget instance
window = QWidget() 

# 3. Configure the window
window.setWindowTitle("My First PySide6 Window") # Set the title of the window
window.setGeometry(100, 100, 400, 300) # Set position (x, y) and size (width, height)

# 4. Show the window
window.show() 

# 5. Start the application's event loop
sys.exit(app.exec())
