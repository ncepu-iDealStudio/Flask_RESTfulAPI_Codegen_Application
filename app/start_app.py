# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : start_app.py
# @ide    : PyCharm
# @time   : 2023-02-26 23:28:29
'''
开启app窗口
'''
# import module your need
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from app.modules.windows.app_windows import AppWindows


def start_app():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app/ui/ncepu.jpg'))
    app_windows = AppWindows()
    app_windows.main_window.show()
    sys.exit(app.exec())
