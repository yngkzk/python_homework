from PyQt5.QtCore import QLibraryInfo
from PyQt5.QtWidgets import *
from PyQt5 import *
import os


def set_qt_plugin_path():
    # qta_path = QLibraryInfo.location(QLibraryInfo.PluginsPath)
    # qta_path = qta_path.encode("latin").decode("utf-8")
    os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "venv/Lib/site-packages/PyQt5/Qt5/plugins/platforms"


set_qt_plugin_path()

app = QApplication([])

window = QWidget()
button1 = QPushButton("One")
button2 = QPushButton("Two")
button3 = QPushButton("Three")
button4 = QPushButton("Four")
button5 = QPushButton("Five")

layout = QGridLayout()

layout.addWidget(button1, 0, 0)
layout.addWidget(button2, 0, 1)
layout.addWidget(button3, 1, 0, 1, 2)
layout.addWidget(button4, 2, 0)
layout.addWidget(button5, 2, 1)

window.setLayout(layout)
window.show()
window.show()
app.exec()
