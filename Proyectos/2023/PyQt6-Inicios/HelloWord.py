import sys
from PyQt6.QtWidgets import QApplication, QWidget

# Create the QApplication
app = QApplication(sys.argv)

# Create the main window
window = QWidget(windowTitle='Hola Mundo')
window.show()

# Start the event loop
app.exit(app.exec())