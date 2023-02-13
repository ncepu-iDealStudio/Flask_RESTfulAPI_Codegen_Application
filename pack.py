# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : pack.py
# @ide    : PyCharm
# @time   : 2023-02-13 17:28:31
'''
this is function description
'''
# import module your need
import os
# nuitka打包
cmd = 'python -m nuitka --follow-imports --standalone --show-progress --enable-plugin=pyside6  --windows-icon-from-ico=E:\MyProject\StudySource\git_pro\ncepu_huadian\api\icon.ico --include-package=sqlalchemy  start.py'

# ui文件转py文件
cmd2 = 'pyside6-uic MainWindow.ui -o MainWindow.py'

os.popen()