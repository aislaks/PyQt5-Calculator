import sys
from view import PyCalcUI
from controller import PyCalcCtrl
from modal import evaluateExpression

def main():
    pycalc = QApplication(sys.argv)
    pycalc.setStyle('Fusion')
    view = PyCalcUI()
    view.show()
    modal = evaluateExpression
    PyCalcCtrl(modal, view)
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()