# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : window_database.py
# @ide    : PyCharm
# @time   : 2022-10-12 16:13:18
'''
this is function description
'''

import configparser
import datetime
import os
import sys

import pymysql
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from app.utils.checkSqlLink import SQLHandler

from types import MethodType

# 将自己负责的函数复制到此处
def db_config_init(self):
    '''
    数据库配置页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
    :return:
    '''
    self.ui.button_get_db_names.clicked.connect(self.get_dbname)
    self.id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

def db_config(self):
    """
    数据库配置页面主要代码，
    """
    dir = os.getcwd()
    f = open(dir + r"/app/config/config_" + str(self.id) + ".conf", "w")
    f.close()

    # 接收参数
    if len(host := self.ui.text_host.text()) == 0:
        QMessageBox.information(self.ui, '提示', '请填写主机')
        return
    if len(port := self.ui.text_port.text()) == 0:
        QMessageBox.information(self.ui, '提示', '请填写数据库端口')
        return
    if len(username := self.ui.text_user.text()) == 0:
        QMessageBox.information(self.ui, '提示', '请填写账号')
        return
    if len(password := self.ui.text_password.text()) == 0:
        QMessageBox.information(self.ui, '提示', '请填写密码')
        return

    dialect = self.ui.comboBox_db_type.currentText()
    host = host
    port = port
    database = self.ui.comboBox_database.currentText()
    username = username
    password = password

    # 检查数据库链接
    result_sql = SQLHandler.connect_sql_link(dialect, username, password, host, port, database)
    if result_sql['code']:
        # 填写配置文件
        configfile = "app/config/config_" + str(self.id) + ".conf"
        conf = configparser.ConfigParser()  # 实例类
        conf.read(configfile, encoding='UTF-8')  # 读取配置文件

        if not conf.has_section('DATABASE'):
            conf.add_section('DATABASE')

        conf.set("DATABASE", "dialect", dialect)  # 第一个参数为组名，第二个参数为属性名，第三个参数为属性的值
        conf.set("DATABASE", "host", host)
        conf.set("DATABASE", "port", port)
        conf.set("DATABASE", "database", database)
        conf.set("DATABASE", "username", username)
        conf.set("DATABASE", "password", password)
        with open(configfile, "w") as f:
            conf.write(f)

        tables_info = SQLHandler.generate_tables_information()
        if tables_info['code']:
            print(tables_info['data'])
            # self.table_config_show(self, tables_info['data'])
    else:
        QMessageBox.critical(self.ui, '错误', '数据库读取失败!')
        return

    self.sql_data['table'] = tables_info['data']['table']
    # 进入下一步前，完成相关配置并完成对主要数据sql_data的修改
    self.ui.stackedWidget.setCurrentIndex(1)

def get_dbname(self):
    """
    获取数据库名
    """
    if len(host := self.ui.text_host.text()) == 0:
        QMessageBox.information(self.ui, '提示', '请填写主机')
        return
    if len(port := self.ui.text_port.text()) == 0:
        QMessageBox.information(self.ui, '提示', '请填写数据库端口')
        return
    if len(username := self.ui.text_user.text()) == 0:
        QMessageBox.information(self.ui, '提示', '请填写账号')
        return
    if len(password := self.ui.text_password.text()) == 0:
        QMessageBox.information(self.ui, '提示', '请填写密码')
        return

    # 清空下拉框
    self.ui.comboBox_database.clear()
    try:

        conn = pymysql.connect(
            host=host,
            user=username,
            passwd=password,
            port=int(port),
        )
        cur = conn.cursor()
        cur.execute('SHOW DATABASES')
        dbnames = cur.fetchall()

        # 将数据库名添加到下拉框中
        for dbname in dbnames:
            self.ui.comboBox_database.addItem(dbname[0])
    except:
        QMessageBox.critical(self.ui, '错误', '数据库连接失败!')
        return

# 将函数添加到对象中
def add_func(self):
    '''
    添加该.py文件的方法到对象中
    :param self: 添加函数的对象
    :return:
    '''
    self.db_config_init = MethodType(db_config_init, self)
    self.db_config = MethodType(db_config, self)
    self.get_dbname = MethodType(get_dbname, self)