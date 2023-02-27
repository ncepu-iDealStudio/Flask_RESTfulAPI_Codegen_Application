# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : app_windows.py
# @ide    : PyCharm
# @time   : 2023-02-27 11:10:42
'''
this is function description
'''
# import module your need
from PySide6.QtWidgets import QMainWindow

from .window_main import MainWindow

class AppWindows(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_window = MainWindow()
        self.main_window.window_init()
