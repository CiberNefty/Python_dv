import sys
from PyQt6.QtWidgets import QWidget, QApplication, QFormLayout, QLabel, QSlider
from PyQt6.QtCore import Qt

class VentanaPadre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('QSlider')
        #self.setGeometry(100,100,200,100)
        self.setMinimumHeight(200)

        layoutPadre = QFormLayout()
        self.setLayout(layoutPadre)

        # Creamos el objeto QSlider
        sliderHorizontal = QSlider(Qt.Orientation.Horizontal, self)
        sliderHorizontal.setRange(0, 100) # Aqui podemos brindarle un rango de recorrido.
        sliderHorizontal.setValue(50) # Este metodo nos ayuda a poder colocar el posicioamiento inicial del slider.
        sliderHorizontal.setSingleStep(5) # Este metodo nos ayuda a que el slider corrara de tanto a tanto.
        sliderHorizontal.setPageStep(2) # Paso de pagina
        sliderHorizontal.setTickPosition(QSlider.TickPosition.TicksAbove) # Estos son marcas de graduacion arriba del slider

        sliderHorizontal.valueChanged.connect(self.slideractualizado) # Esta bandera (valueChanged)  emite la señal cada vez que cambia el valor del control deslizante

        self.resultadoSliderHorizal = QLabel('', self)

        layoutPadre.addRow(sliderHorizontal)
        layoutPadre.addRow(self.resultadoSliderHorizal)

        self.show()
    
    def slideractualizado(self ,value):
        self.resultadoSliderHorizal.setText(f'Valor actual: {value}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPadre()
    sys.exit(app.exec())