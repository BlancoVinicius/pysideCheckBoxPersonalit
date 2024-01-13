from PySide6.QtWidgets import QMenu, QMenuBar
from PySide6.QtGui import QAction
# from PySide6.QtCore import Slot, Qt
# import sys


class MenuBar(QMenuBar):
    def __init__(self, parent) -> None:
        super().__init__()
        self.paren = parent
        self.menuFile = self.addMenu("&File")
        self.menuItem = self.addMenu("Tamplayts")
        
        # self.addMenuItemTemplayts("Menu1")
        self.addMenuItemFile("SaveAs")
        
    def addMenuItemTemplayts(self, name:str):
        
        def onMyToolBarButtonClick(action:QAction):
            print(action.text())
        
        button_action = QAction(name, self)
        button_action.triggered.connect(lambda: onMyToolBarButtonClick(button_action))
                    
        self.menuItem.addAction(button_action)

    def addMenuItemFile(self, name:str):
    
        def onMyToolBarButtonClick(s):
            self.paren.saveTemplat()    
        
        button_action = QAction(name, self)
        button_action.triggered.connect(onMyToolBarButtonClick)
        self.menuFile.addAction(button_action)

