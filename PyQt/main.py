import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l1.setText("Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit")
    l1.setAlignment()
    w.setFixedHeight(540)
    w.setFixedWidth(960)
    w.setWindowTitle('PyQt5')
    w.show()
    sys.exit(app.exec_())


window()
