# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : window_generate.py
# @ide    : PyCharm
# @time   : 2022-10-12 16:15:38
'''
this is function description
'''
# import module your need
import configparser
import os
import sys

import pymysql
from PySide6 import QtWidgets
from PySide6.QtCore import QFile, QDir
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow,QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon

from types import MethodType

import app.generate
from app import generate


# 将自己负责的函数复制到此处
def generate_init(self):
    '''
    代码生成页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
    :return:
    '''
    self.ui.dig = QFileDialog()
    self.ui.dig.setFileMode(QFileDialog.AnyFile)
    self.ui.dig.setFilter(QDir.Files)
    self.ui.toolButton_file.clicked.connect(self.button_show_file)


def generate(self):
    '''
    代码生成页主要代码
    :return:
    '''
    # file_name = QFileDialog.getOpenFileName(self, "open file dialog", "C:","Txt files(*.txt)")
    # ##"open file Dialog "为文件对话框的标题，第三个是打开的默认路径，第四个是文件类型过滤器
    # self.ui.dig = QFileDialog()
    # self.ui.dig.setFileMode(QFileDialog.AnyFile)
    # self.ui.dig.setFilter(QDir.Files)

    # codegen.start(self.sql_data, 1, "127.0.0.1")
    self.ui.stackedWidget.setCurrentIndex(3)

    session_id = '123'
    # session_id = self.id
    # 获取用户填写的数据，并将其赋值给变量
    path = self.ui.lineEdit.text()
    name = self.ui.lineEdit_2.text()
    version = self.ui.lineEdit_3.text()

    project_path = path
    project_name = name
    interface_version = version

    configfile = "app/config/config_" + str(session_id) + ".conf"
    conf = configparser.ConfigParser()  # 实例类
    conf.read(configfile, encoding='UTF-8')  # 读取配置文件

    if not conf.has_section('PARAMETER'):
        conf.add_section('PARAMETER')

    conf.set("PARAMETER", "target_dir", project_path)  # 第一个参数为组名，第二个参数为属性名，第三个参数为属性的值
    conf.set("PARAMETER", "project_name", project_name)
    conf.set("PARAMETER", "api_version", interface_version)
    with open(configfile, "w") as f:
        conf.write(f)

    app.generate.start(self.sql_data, session_id, project_path, "127.0.0.1")


def button_show_file(self):
    dialog = QtWidgets.QFileDialog
    # dialog.setFileMode(dialog.AnyFile)
    # fileName, fileType = dialog.getOpenFileName(self.ui, "选取文件", os.getcwd(),
    #                                                            "All Files(*);;Text Files(*.txt)")
    fileName = dialog.getExistingDirectory(self.ui, "选取文件", os.getcwd())
    self.ui.lineEdit.setText(fileName)

# 将函数添加到对象中
def add_func(self):
    '''
    添加该.py文件的方法到对象中
    :param self: 添加函数的对象
    :return:
    '''
    self.generate_init = MethodType(generate_init, self)
    self.generate = MethodType(generate, self)
    self.button_show_file = MethodType(button_show_file, self)