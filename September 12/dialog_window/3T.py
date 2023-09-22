import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QTextEdit, QWidget, QVBoxLayout, QFileDialog
from PyQt6.QtCore import pyqtSignal
from threading import Thread, Lock


class MainWindow(QWidget):
    send_message = pyqtSignal(str)
    lock = Lock()

    def __init__(self):
        super().__init__()
        self.resize(600, 400)

        self.button = QPushButton('Send')
        self.button.clicked.connect(self.send_button)
        self.buttonQfile = QPushButton('Import text')
        self.buttonQfile.clicked.connect(self.get_text_file)

        self.textEditor = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.buttonQfile)
        layout.addWidget(self.textEditor)

        self.setLayout(layout)

    def get_text_file(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialog.setNameFilter('Files (*.*)')

        if dialog.exec():
            file_name = dialog.selectedFiles()

            if file_name[0].endswith('.txt') or file_name[0].endswith('.py'):
                with open(file_name[0]) as open_file:
                    data = open_file.read()
                    self.textEditor.setPlainText(data)
                    open_file.close()
            else:
                pass

    def send_button(self):
        thread = Thread(target=self.send_signal)
        thread.start()
        thread.join()

    def send_signal(self):
        self.lock.acquire()
        print("Кнопка нажата!")
        message = self.textEditor.toPlainText()
        self.send_message.emit(message)
        self.lock.release()  # Не знаю как правильнее реализовать этот метод


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = MainWindow()
    demo.show()

    sys.exit(app.exec())
