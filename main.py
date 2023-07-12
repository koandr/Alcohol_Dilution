import sys
from PyQt5.QtWidgets import *


class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.btn = None
        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Розпочнемо ?', self)
        self.btn.move(120, 20)
        self.btn.clicked.connect(self.start)

        self.setGeometry(0, 0, 320, 320)
        self.setWindowTitle('Від спирту до горілки')
        self.show()

    def start(self):

        alcohol_strength, ok = QInputDialog.getInt(self, 'Від спирту до горілки', 'введіть міцність спирту, %',
                                                   96, 1, 100, 1)
        alcohol_volume, ok = QInputDialog.getInt(self, 'Від спирту до горілки', 'введіть кількість спирту, мл',
                                                 100, 1, 1000, 1)
        vodka_strength, ok = QInputDialog.getInt(self, 'Від спирту до горілки', 'введіть потрібну міцність горілки, %',
                                                 40, 1, alcohol_strength, 1)

        if ok and alcohol_strength and alcohol_volume and vodka_strength:
            water_volume = str(alcohol_strength * alcohol_volume / vodka_strength - alcohol_volume)
            output_text = 'Вам потрібно ' + water_volume + 'мл води'
            QMessageBox.information(self, ' ', output_text)

    def closeEvent(self, event):
        msg = QMessageBox(self)
        msg.setWindowTitle("Вихід")
        msg.setIcon(QMessageBox.Question)
        msg.setText("А може ще по одній?")

        button_accept = msg.addButton("Ні, на сьогодні досить", QMessageBox.YesRole)
        button_cancel = msg.addButton("Так", QMessageBox.RejectRole)
        msg.setDefaultButton(button_accept)
        msg.exec_()

        if msg.clickedButton() == button_accept:
            event.accept()
        elif msg.clickedButton() == button_cancel:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
