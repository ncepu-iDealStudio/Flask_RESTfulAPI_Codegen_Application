# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : test.py
# @ide    : PyCharm
# @time   : 2023-01-16 21:56:02
'''
this is function description
'''
# import module your need
#  加载中弹窗
# dialog_fault = QDialog()
import os
import time

from PySide6.QtCore import QSize
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QFrame, QLabel, QPushButton

print(112)

dialog_fault = QLabel()

print(11)
label_loading = QLabel(dialog_fault)  # 弹窗
label_loading.setText('aaaa')
label_loading.setGeometry(110, 10, 230, 230)
print(11)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_path = os.path.join(base_dir, 'app', 'ui', 'static', 'loading.gif')
label_pic = QLabel(label_loading)  # loading动图label
label_pic.setGeometry(55, 10, 120, 120)
pic = QMovie(image_path)  # loading动图
pic.setScaledSize(QSize(label_pic.width(), label_pic.height()))
pic.start()
label_pic.setMovie(pic)

label_text = QLabel(dialog_fault)  # 弹窗提示
label_text.setGeometry(175, 130, 220, 50)
label_text.setText("加载中,请稍候...")

cancel_pbt = QPushButton(dialog_fault)
cancel_pbt.setText("取消")
cancel_pbt.setGeometry(150, 180, 180, 35)
print(2)
dialog_fault.show()
print(1)

time.sleep(5)