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
import time

import pymysql
from PySide6 import QtCore
from PySide6.QtCore import QSize, QThread, QObject
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtWidgets import QMessageBox, QDialog, QLabel, QPushButton, QFrame

from app.utils.checkSqlLink import SQLHandler

from types import MethodType

from threading import Thread

def window_init_for_database(self):
    '''
    数据库配置页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
    :return:
    '''
    self.ui.button_get_db_names.clicked.connect(self.get_dbname)
    self.id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # 初始化多线程信号与槽
    self.loadData.sig_load_table.connect(self.loadData.load_tables)
    self.loadData.sig_load_table_comp.connect(self.load_table_comp)
    self.loadData.sig_load_dbname.connect(self.loadData.load_dbname)
    self.loadData.sig_load_dbname_comp.connect(self.load_dbname_comp)

    # 加载用户上一次使用的配置
    user_configfile = "app/config/user_config.conf"
    if os.path.isfile(user_configfile):
        user_conf = configparser.ConfigParser()  # 实例类
        user_conf.read(user_configfile, encoding='UTF-8')  # 读取配置文件
        if user_conf.has_section('DATABASE'):
            self.ui.text_host.setText(user_conf['DATABASE']['host'])
            self.ui.text_port.setText(user_conf['DATABASE']['port'])
            self.ui.text_user.setText(user_conf['DATABASE']['username'])
            self.ui.text_password.setText(user_conf['DATABASE']['password'])
            self.ui.checkBox_re.setChecked(1)


def db_config(self):
    """
    数据库配置页面主要代码，
    """
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    f = open(dir + r"/app/config/config_" + str(self.id) + ".conf", "w")
    f.close()

    # 接收参数
    if len(host := self.ui.text_host.text()) == 0:
        QMessageBox.information(self, '提示', '请填写主机')
        return
    if len(port := self.ui.text_port.text()) == 0:
        QMessageBox.information(self, '提示', '请填写数据库端口')
        return
    if len(username := self.ui.text_user.text()) == 0:
        QMessageBox.information(self, '提示', '请填写账号')
        return
    if len(password := self.ui.text_password.text()) == 0:
        QMessageBox.information(self, '提示', '请填写密码')
        return
    if self.ui.comboBox_database.currentText() == '请先获取数据库名':
        QMessageBox.information(self, '提示', '请先获取数据库名')
        return

    dialect = self.ui.comboBox_db_type.currentText()
    host = host
    port = port
    database = self.ui.comboBox_database.currentText()
    username = username
    password = password

    # 检查数据库链接

    # 这里并不能正常检查数据库连接，该bug难以修复
    result_sql = SQLHandler.connect_sql_link(dialect, username, password, host, port, database)
    if result_sql['code']:
        # 填写配置文件
        configfile = "app/config/config_" + str(self.id) + ".conf"
        configfile = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), configfile)
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

        self.loadData.sig_load_table.emit()

        self.dialog_fault.open()  # 阻塞当前窗口，避免用户违规操作
        return

    else:
        QMessageBox.critical(self, '错误', '数据库读取失败!')
        return


def get_dbname(self):
    """
    获取数据库名
    """
    if len(host := self.ui.text_host.text()) == 0:
        QMessageBox.information(self, '提示', '请填写主机')
        return
    if len(port := self.ui.text_port.text()) == 0:
        QMessageBox.information(self, '提示', '请填写数据库端口')
        return
    if len(username := self.ui.text_user.text()) == 0:
        QMessageBox.information(self, '提示', '请填写账号')
        return
    if len(password := self.ui.text_password.text()) == 0:
        QMessageBox.information(self, '提示', '请填写密码')
        return

    # 清空下拉框
    self.ui.comboBox_database.clear()
    self.ui.comboBox_database.addItem('请先获取数据库名')

    self.loadData.sig_load_dbname.emit(host, username, password, port)  # 开始用多线程获取dbname

    self.dialog_fault.open()  # 阻塞当前窗口，避免用户违规操作


# 获取dbname完成
def load_dbname_comp(self, result):
    self.dialog_fault.close()
    if result.get('code') == 2000:
        # 清空下拉框
        self.ui.comboBox_database.clear()

        dbnames = result.get('data')
        # 将数据库名添加到下拉框中
        for dbname in dbnames:
            self.ui.comboBox_database.addItem(dbname[0])

    else:
        QMessageBox.critical(self, '错误', str(result))
        QMessageBox.critical(self, '错误', '数据库连接失败!')



# 数据处理结束
def load_table_comp(self, tables_info):
    if tables_info.get('code'):
        self.sql_data['table'] = tables_info['data']['table']
        self.next_step()
        self.dialog_fault.close()
    else:
        self.dialog_fault.close()
        QMessageBox.critical(self, '错误', str(tables_info.get('message')))
        QMessageBox.critical(self, '错误', '数据库连接失败!')


# 将函数添加到对象中
def add_func(self):
    '''
    添加该.py文件的方法到对象中
    :param self: 添加函数的对象
    :return:
    '''
    self. window_init_for_database = MethodType( window_init_for_database, self)
    self.db_config = MethodType(db_config, self)
    self.get_dbname = MethodType(get_dbname, self)
    self.load_table_comp = MethodType(load_table_comp, self)
    self.load_dbname_comp = MethodType(load_dbname_comp, self)