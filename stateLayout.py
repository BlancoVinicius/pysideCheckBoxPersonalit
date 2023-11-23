from PySide6.QtWidgets import QStackedLayout, QMainWindow, QWidget, QApplication, QPushButton, QHBoxLayout,QVBoxLayout, QTextEdit,QLineEdit,QCheckBox  #
from PySide6.QtGui import QPalette, QColor, QMouseEvent
import sys

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()
        # self.check = QCheckBox("TExto do Check")
        self.check = checkBox(self)
        self.check.setText("Meu texto")
        self.text = QTextEdit("TEste1")

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        self.btn = QPushButton("Ok")
        self.btn.setVisible(False)
        self.btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(self.btn)
        # self.check.stateChanged.connect(self.activate_tab_2)
        self.stacklayout.addWidget(self.check)
        self.stacklayout.addWidget(self.text)
        self.setFixedSize(200, 100)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.check.setText(self.text.toPlainText())
        self.stacklayout.setCurrentIndex(0)
        self.btn.setVisible(False)

    def activate_tab_2(self):
        self.text.setText(self.check.text())
        self.stacklayout.setCurrentIndex(1)
        self.btn.setVisible(True)

class checkBox(QCheckBox):
    def __init__(self, parent: MainWindow):
        super().__init__(parent=parent)
        self.win = parent
        self.setText("Meu check Box")
        
    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if self.isChecked():
            self.setChecked(False)
        else:
            self.setChecked(True)
        self.win.activate_tab_2()




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()