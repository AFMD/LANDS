#!/usr/bin/env python3

# written by Grey Christoforo <first name [at] last name [not] net>

import sys

from ui import Ui_landsControl

from PyQt5.QtCore import QSettings, Qt, QSignalMapper, QFileSystemWatcher, QDir, QFileInfo
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QTableWidgetItem, QCheckBox, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_landsControl()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    LANDSControl = MainWindow()
    LANDSControl.show()
    sys.exit(app.exec_())
