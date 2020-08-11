from PyQt5.QtWidgets import (QApplication,QMainWindow,QWidget,QGridLayout,QLineEdit, QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt

class PyCalcUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(240,240)
        
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {
            '(':(0,0),
            ')':(0,1),
            'C':(0,2),
            '/':(0,3),
            '7':(1,0), 
            '8':(1,1), 
            '9':(1,2),
            '*':(1,3),
            '4':(2,0),
            '5':(2,1),
            '6':(2,2),
            '-':(2,3),
            '1':(3,0),
            '2':(3,1),
            '3':(3,2),
            '+':(3,3),
            '00':(4,0),
            '0':(4,1),
            '.':(4,2),
            '=':(4,3)
            }

        for btntext, pos in buttons.items():
            self.buttons[btntext] = QPushButton(btntext)
            self.buttons[btntext].setFixedSize(50,35)
            buttonsLayout.addWidget(self.buttons[btntext], pos[0], pos[1])

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self,text):
        self.display.setText(text)
        self.display.setFocus()
    
    def displayText(self):
        return self.display.text()
    
    def clearDisplay(self):
        self.setDisplayText('')