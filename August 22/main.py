import sys
import os
from PyQt5.QtWidgets import QApplication
from calc_main_window import CalcMainWindow
from calc_view import SimpleCalcView

if __name__ == '__main__':
    os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "venv/Lib/site-packages/PyQt5/Qt5/plugins/platforms"

    app = QApplication(sys.argv)

    window = CalcMainWindow('Simple Calculator v1.0')
    view = SimpleCalcView()

    window.set_view(view)
    window.show()
    app.exec()
