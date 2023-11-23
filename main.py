from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
import sys

class SegundaJanela(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("MEu titulo")
        l = QLabel("Segunda Janela")
        self.layout = QVBoxLayout()
        self.layout.addWidget(l)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.janela2 = SegundaJanela()
        self.janela3 = SegundaJanela()

        self.setWindowTitle("MEu titulo")
        l = QLabel("Primeira janela")
        b = QPushButton("Botao")
        b.clicked.connect(lambda c: self.openJanela2(self.janela3))
        self.layout = QVBoxLayout()
        self.layout.addWidget(l)
        self.layout.addWidget(b)
        
        self.wid = QWidget()
        self.wid.setLayout(self.layout)
        self.setCentralWidget(self.wid)

    def openJanela2(self, window3:SegundaJanela):
        self.janela2.setWindowTitle("Janela 2")
        self.janela2.show()
        window3.setWindowTitle("Janela  3")
        window3.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    app.exec()