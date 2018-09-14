#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget)


class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(parent=None, flags=0)


app = QApplication(sys.argv)
w = MainWidget()
app.exec()
