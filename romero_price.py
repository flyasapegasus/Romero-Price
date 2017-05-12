import urllib.request as ur
from bs4 import BeautifulSoup

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, qApp, QAction
from PyQt5.QtCore import QSize

url = "https://www.coinmarketcap.com"
html = ur.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

text = soup.get_text()

price = soup.find_all("a", class_="price", href="/currencies/monero/#markets")

simple_price = str(price)

print("$"+simple_price[49:54])

# Inherit from QMainWindow
class MainWindow(QMainWindow):
    # override the class constructor
    def __init__(self):
        # Invoke the method of super class
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(69, 69))    # Set sizes
        self.setWindowTitle("Romero Price")   # Set title of window
        central_widget = QWidget(self)          # Create a central widget
        self.setCentralWidget(central_widget)   # Set the central widget

        grid_layout = QGridLayout(self)         # Create a QGridLayout
        central_widget.setLayout(grid_layout)   # Set Layout to central widget

        title = QLabel(simple_price, self)    # Create a label
        title.setAlignment(QtCore.Qt.AlignCenter)   # Set alignment of text
        grid_layout.addWidget(title, 0, 0)          # and add it to layout

        exit_action = QAction("&Exit", self)
        exit_action.setShortcut('Ctrl+Q')
        # Connect the signal triggered in the slot quit qApp.
        # Signals and Slots syntax PyQt5 is markedly different from the one used Qt5 C ++
        exit_action.triggered.connect(qApp.quit)
        # Set in the menu bar Action.
        file_menu = self.menuBar()
        file_menu.addAction(exit_action)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())


