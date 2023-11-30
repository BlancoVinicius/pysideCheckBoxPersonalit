from PySide6.QtWidgets import QStackedLayout, QMainWindow, QWidget, QApplication, QPushButton, QHBoxLayout,QVBoxLayout, QTextEdit,QCheckBox, QLayout#
from PySide6.QtGui import QPalette, QColor, QMouseEvent, QFocusEvent, QLinearGradient, QBrush, QIcon
from PySide6.QtCore import Slot
import sys
from pathlib import Path
import rc_icons

ROOT = Path(__file__).parent

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setWindowOpacity(0.9)
        #Cria os layouts
        self.vBoxlayoytParent = QVBoxLayout()
        self.button_layout = QVBoxLayout()
        
        btn2 = QPushButton("adicionar")
        btn2.clicked.connect(self.addItem)
        # self.button_layout.addWidget(btn2)
        self.addItem()

        self.vBoxlayoytParent.addLayout(self.button_layout)
        self.vBoxlayoytParent.addWidget(btn2)

        #Adicona um fundo gradient
        p = QPalette()
        gradient = QLinearGradient(400, 0, 0, 400)
        # gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QColor("#3FF8F5"))
        gradient.setColorAt(1.0, QColor("#A8C0FF"))
        # gradient.setColorAt(0.0, QColor("#59D3FC"))
        # gradient.setColorAt(1.0, QColor("#554DDE"))
        # gradient.setColorAt(0.0, QColor(222, 254, 253))
        # gradient.setColorAt(1.0, QColor(5, 134, 128))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        widget = QWidget()
        widget.setLayout(self.vBoxlayoytParent)
        self.setCentralWidget(widget)

    def addItem(self):
        #cria os widgets
        #cria os dois layouts
        hBoxlayout = QHBoxLayout()
        stacklayout = QStackedLayout()
        #adiciona ao Vbox laytout
        self.button_layout.addLayout(hBoxlayout)

        #cria os controles
        check = checkBox(self, stacklayout)
        text = TextEdit("", self, check, stacklayout)
        btn = botao(self, hBoxlayout, stacklayout, check, text)
        # btn.setText("OK")
        btn.setProperty("class", "buttonEdite")
        btn.setIcon(QIcon(str(Path.joinpath(ROOT, "img\\edit.ico"))))
        check.setText("Digite um texto")

        hBoxlayout.addLayout(stacklayout)
        hBoxlayout.addWidget(btn)
        # self.button_layout.setContentsMargins(50, 50, 50,50)
        #adiciona os wiggets
        stacklayout.addWidget(check)
        stacklayout.addWidget(text)
        # self.setFixedSize(200, 100)

    @Slot()
    def activate_tab_1(self, check: QCheckBox, stacklayout:QStackedLayout, text: QTextEdit):
        check.setText(text.toPlainText())
        stacklayout.setCurrentIndex(0)
    @Slot()
    def activate_tab_2(self,stacklayout:QStackedLayout, text:QTextEdit, check:QCheckBox):
        text.setText(check.text())
        stacklayout.setCurrentIndex(1)
        # btn.setVisible(True)
    @Slot()
    def remover(self, hbox: QLayout,btn: QPushButton,stacklayout:QStackedLayout, text:QTextEdit, check:QCheckBox):
        self.button_layout.removeItem(hbox)
        btn.deleteLater()
        stacklayout.deleteLater()
        text.deleteLater()
        check.deleteLater()


class TextEdit(QTextEdit):
    def __init__(self, text:str, parent:MainWindow, check: QCheckBox, stac: QStackedLayout):
        super().__init__(text, parent=parent)
        self.check = check
        self.sta = stac
        self.paren = parent

    def focusOutEvent(self, event: QFocusEvent):
        self.paren.activate_tab_1(self.check, self.sta, self)

   
class checkBox(QCheckBox):
    def __init__(self, parent:QMainWindow, stack: QStackedLayout):
        super().__init__(parent=parent)
        self.stac = stack
        self.setText("Meu check Box")
        
    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.stac.setCurrentIndex(1)
        if self.isChecked():
            self.setChecked(False)


class botao(QPushButton):
    def __init__(self, parent:MainWindow, hBox:QLayout, stack: QStackedLayout, check: QCheckBox, text: QTextEdit):
        super().__init__(parent=parent)
        self.stac = stack
        self.clicked.connect(lambda: parent.remover(hBox,self, stack,text, check))

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    app.exec()
