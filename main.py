from PySide6.QtWidgets import QStackedLayout, QMainWindow, QWidget, QApplication, QPushButton, QHBoxLayout,QVBoxLayout, QTextEdit,QCheckBox, QLayout, QMessageBox, QInputDialog
from PySide6.QtGui import QCursor, QPalette, QColor, QMouseEvent, QFocusEvent, QLinearGradient, QBrush, QIcon
from PySide6.QtCore import Slot, Qt
import sys
from pathlib import Path
from modulos import rc_icons
from modulos.templat import Templat

ROOT = Path(__file__).parent

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Janela de tarefas")
        self.setWindowOpacity(0.9)
        #Cria os layouts
        self.vBoxlayoytParent = QVBoxLayout()
        self.button_layout = QVBoxLayout()
        
        btn2 = QPushButton("adicionar")
        btn2.setProperty("class", "add-item")
        btn2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn2.clicked.connect(self.addItem)

        self.vBoxlayoytParent.addLayout(self.button_layout)
        self.vBoxlayoytParent.addWidget(btn2)

        #Adicona um fundo gradient
        p = QPalette()
        gradient = QLinearGradient(400, 0, 0, 400)
        gradient.setColorAt(0.0, QColor("#3FF8F5"))
        gradient.setColorAt(1.0, QColor("#A8C0FF"))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        widget = QWidget()
        widget.setLayout(self.vBoxlayoytParent)
        self.setCentralWidget(widget)

        

    def addItem(self):
        #cria os dois layouts
        hBoxlayout = QHBoxLayout()
        stacklayout = QStackedLayout()
        #adiciona ao Vbox laytout
        self.button_layout.addLayout(hBoxlayout)

        #cria os controles
        check = checkBox(self, stacklayout)
        text = TextEdit("", self, check, stacklayout)
        btn = botao(self, hBoxlayout, stacklayout, check, text)
        btn.setProperty("class", "buttonExclud")
        btn.setIcon(QIcon(str(Path.joinpath(ROOT, "modulos\\img\\excluir.ico"))))
        check.setText("Digite um texto")

        hBoxlayout.addLayout(stacklayout)
        hBoxlayout.addWidget(btn)
        #adiciona os wiggets
        stacklayout.addWidget(check)
        stacklayout.addWidget(text)

        self.saveTemplat()
    
    @Slot()
    def activate_tab_1(self, check: QCheckBox, stacklayout:QStackedLayout, text: QTextEdit):
        check.setText(text.toPlainText())
        stacklayout.setCurrentIndex(0)
 
    @Slot()
    def activate_tab_2(self,stacklayout:QStackedLayout, text:QTextEdit, check:QCheckBox):
        text.setText(check.text())
        stacklayout.setCurrentIndex(1)
 
    @Slot()
    def remover(self, hbox: QLayout,btn: QPushButton,stacklayout:QStackedLayout, text:QTextEdit, check:QCheckBox):
        msg = QMessageBox(QMessageBox.Icon.Critical, "EXCLUIR!", "Tem certeza que deseja excluir o item?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, self)
        respMsg = msg.exec()

        if respMsg == QMessageBox.StandardButton.Yes:
            self.button_layout.removeItem(hbox)
            btn.deleteLater()
            stacklayout.deleteLater()
            text.deleteLater()
            check.deleteLater()

    def saveTemplat(self):
        modelo = {"templats": [ 
            {"name": "conferencia", "mensages": ["Mensage1", "item1", "item2", "item3"]},
        ]}

        imput = QInputDialog(self)
        t = imput.getText(self, "Nome", "Preencha um nome.")
        if not t[1]:
            return    
            
        templat = Templat(t[0])
        templat.mensagens.clear()
        
        for i in range(self.button_layout.count()):
            r:QHBoxLayout
            stack: QStackedLayout
            c:QCheckBox
            
            hLayout =self.button_layout.itemAt(i)
            stack = hLayout.itemAt(0)
            cBox = stack.itemAt(0).widget()
            text = cBox.text()
            templat.mensagens.append(text)    
        
        print(templat.mensagens)

class TextEdit(QTextEdit):
    def __init__(self, text:str, parent:MainWindow, check: QCheckBox, stac: QStackedLayout):
        super().__init__(text, parent=parent)
        self.setMinimumSize(300, 100)
        self.check = check
        self.sta = stac
        self.paren = parent

    def focusOutEvent(self, event: QFocusEvent):
        self.paren.activate_tab_1(self.check, self.sta, self)

   
class checkBox(QCheckBox):
    def __init__(self, parent:QMainWindow, stack: QStackedLayout):
        super().__init__(parent=parent)
        self.stac = stack
        self.stateChanged.connect(self.__stateChenge)
    
    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.stac.setCurrentIndex(1)
        if self.isChecked():
            self.setChecked(False)

    def __stateChenge(self):
        if self.isChecked():
            self.setStyleSheet("text-decoration: line-through; color: #757575")
        else:
            self.setStyleSheet("text-decoration: none; color: #101010")
            
class botao(QPushButton):
    def __init__(self, parent:MainWindow, hBox:QLayout, stack: QStackedLayout, check: QCheckBox, text: QTextEdit):
        super().__init__(parent=parent)
        self.stac = stack
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clicked.connect(lambda: parent.remover(hBox,self, stack,text, check))

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    with open("pysideCheckBoxPersonalit\\modulos\\style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    app.exec()
