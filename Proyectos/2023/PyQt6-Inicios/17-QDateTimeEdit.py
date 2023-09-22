import sys
from PyQt6.QtWidgets import QWidget, QApplication, QFormLayout, QLabel

class VentanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('PyQt QDateEdit')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPadre()
    sys.exit(app.exec())