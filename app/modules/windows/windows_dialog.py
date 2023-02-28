# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : dialog_loading.py
# @ide    : PyCharm
# @time   : 2023-02-27 16:08:57
'''
this is function description
'''
import os
from PySide6.QtCore import QSize
from PySide6.QtGui import QMovie, Qt
from PySide6.QtWidgets import QDialog, QLabel
from config import setting


class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        # 初始化加载中弹窗
        # self.dialog_loading = QDialog()
        self.label_loading = QLabel(self)  # 弹窗
        self.label_loading.setText('')
        self.label_loading.setGeometry(0, 0, 330, 230)

        base_dir = setting.BASE_DIR
        image_path = os.path.join(
            base_dir, 'app', 'ui', 'static', 'loading.gif')
        label_pic = QLabel(self.label_loading)  # loading动图label
        label_pic.setStyleSheet("background-color:transparent")
        label_pic.setGeometry(0, 0, 330, 230)
        pic = QMovie(image_path)  # loading动图
        pic.setScaledSize(QSize(label_pic.width(), label_pic.height()))
        pic.start()
        label_pic.setMovie(pic)
        # 去除弹窗标题栏
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
