# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : pack.py
# @ide    : PyCharm
# @time   : 2023-02-13 17:28:31

'''
打包以及功能程序  
'''

import os


def nuitaka_pack():
    # nuitka打包
<<<<<<< HEAD
<<<<<<< HEAD
    cmd = 'python -m nuitka --follow-imports --standalone --show-progress --enable-plugin=pyside6 --windows-icon-from-ico=icon.ico --include-package=sqlalchemy  start.py'
=======
    cmd = 'python -m nuitka --follow-imports --standalone --show-progress --enable-plugin=pyside6 --windows-disable-console --windows-icon-from-ico=icon.ico --include-package=sqlalchemy  start.py'
>>>>>>> 1e4cc9842fb4b747de3fb7d4d0ae9ab44cbf9ffb
=======
    cmd = 'python -m nuitka --follow-imports --standalone --show-progress --enable-plugin=pyside6 --windows-icon-from-ico=icon.ico --include-package=sqlalchemy  start.py'
>>>>>>> 3fafd1d9eae4804bfa93342a5080a3546817eba3
    os.system(cmd)


def cx_Freeze_pack():
    # cx_Freeze方式打包
    cmd1 = 'pip install cx_Freeze idna'
    cmd2 = 'python setup.py build'
    os.system(cmd1)
    os.system(cmd2)


def convert_ui_to_py():
    # ui文件转py文件
    cmd = 'pyside6-uic app/ui/MainWindow.ui -o app/ui/MainWindow.py'
    os.system(cmd)


if __name__ == "__main__":
    pass
    nuitaka_pack()
