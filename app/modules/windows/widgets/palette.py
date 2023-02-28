# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : palette.py
# @ide    : PyCharm
# @time   : 2023-02-28 13:04:19
'''
this is function description
'''
# import module your need
from PySide6.QtGui import QPalette, QColor


class Palette(QPalette):
    def __init__(self):
        QPalette.__init__(self)

    def set_placeholder_color(self, color):
        self.setColor(QPalette.Normal, QPalette.PlaceholderText, color)