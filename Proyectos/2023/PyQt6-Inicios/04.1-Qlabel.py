import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt6.QtGui import QMovie, QPixmap

class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QLabel con Imagen')
        self.setGeometry(100, 100, 320, 210)

        # No me mostro la imagen
        """label= QLabel()
        # Creamos un widget con una ruta de una imagen
        pixmap = QPixmap('python-logo.png') # Ruta de acceso a la imagen
        label.setPixmap(pixmap)

        # Colocamos el Widget en la ventana
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)"""

        labelGIf = QLabel()
        movie = QMovie('\PyQt6-Inicios\giphy.gif') # La ruta de acceso a la imagen NO ME DEJA.
        labelGIf.setMovie(movie)
        movie.start() # Iniciamos la animacion

        layoutGif = QVBoxLayout()
        layoutGif.addWidget(labelGIf)
        self.setLayout(layoutGif)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())
