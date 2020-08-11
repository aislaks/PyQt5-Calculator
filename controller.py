from functools import partial

class PyCalcCtrl:
    def __init__(self,modal, view):
        self._evaluate = modal
        self._view = view
        self._connectSignals()
    
    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == 'ERROR_MSG':
            self._view.clearDisplay()
        expression = self._view.displayText() +sub_exp
        self._view.setDisplayText(expression)
    
    def _connectSignals(self):
        for btntext,btn in self._view.buttons.items():
            if btntext not in {"=","C"}:
                btn.clicked.connect(partial(self._buildExpression, btntext))

        self._view.buttons["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons["C"].clicked.connect(self._view.clearDisplay)