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
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog
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


def code_generate(self):
    """
    代码生成页主要代码
    :return:
    """

    session_id = self.id

    # 获取用户填写的数据，并将其赋值给变量
    path = self.ui.lineEdit.text()
    name = self.ui.lineEdit_2.text()
    version = self.ui.lineEdit_3.text()

    # 检查用户填写的数据是否正确
    if len(path) == 0:
        QMessageBox.information(self.ui, '提示', '生成路径不能为空')
        return
    if not os.path.isdir(path):
        QMessageBox.information(self.ui, '提示', '生成路径有误,该路径不是一个文件夹')
        return
    if len(name) == 0:
        QMessageBox.information(self.ui, '提示', '项目名不能为空')
        return
    if len(version) == 0:
        QMessageBox.information(self.ui, '提示', '版本号不能为空')
        return

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

    # 过滤掉未勾选的表和视图
    table_config = {
        'table': [],
        'view': []
    }
    for table in self.sql_data.get('table'):
        if table.get('ischecked'):
            table_config['table'].append(table)

    for view in self.sql_data.get('view'):
        if view.get('ischecked'):
            table_config['view'].append(view)

    # 开始生成代码
    generate.start(table_config, session_id, "127.0.0.1")


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
    self.generate = MethodType(code_generate, self)
    self.button_show_file = MethodType(button_show_file, self)
