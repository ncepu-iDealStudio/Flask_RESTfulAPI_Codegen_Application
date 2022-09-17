# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : table_ui_perfect.py
# @ide    : PyCharm
# @time   : 2022-09-16 11:08:56
'''
this is function description
'''
# import module your need
import sys

from app.ui.data_table_config import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class table_ui(Ui_MainWindow):
    def __init__(self):
        pass
    def object_perfect(self):
        self.horizontalLayout_1 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_all.setContentsMargins(0, 0, 0, 0)
        self.checkBox_1 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_1.setObjectName(u"checkBox_1")

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_1.sizePolicy().hasHeightForWidth())

        self.checkBox_1.setSizePolicy(sizePolicy)
        self.checkBox_1.setMinimumSize(QSize(0, 0))
        print(self.centralwidget.findChild(QCheckBox, 'checkBox_1'))

        self.horizontalLayout_1.addWidget(self.checkBox_1)

        self.label_select_1 = QLabel(self.horizontalLayoutWidget)
        self.label_select_1.setObjectName(u"label_select_1")

        self.horizontalLayout_1.addWidget(self.label_select_1)

        self.horizontalLayout_all.setStretch(0, 1)
        self.horizontalLayout_all.setStretch(1, 5)

    def signal_perfect(self):
        pass



if __name__ == '__main__':

    app = QApplication([])
    window = QMainWindow()
    config1 = table_ui()
    config1.setupUi(window)
    config1.retranslateUi(window)
    config1.object_perfect()
    window.show()
    app.exec_()