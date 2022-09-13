#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:main.py
# author:Chen Qinyu
# datetime:2022/8/23 17:22
# software: PyCharm

"""
this is function description
"""
import configparser
import datetime
import os

import pymysql
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

from app.utils.checkSqlLink import SQLHandler


class Main:

    def __init__(self):
        # 从文件中加载UI定义
        qfile_main = QFile('ui/database_config.ui')
        qfile_main.open(QFile.ReadOnly)
        qfile_main.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile_main)

        self.ui.Button_get_dbnames.clicked.connect(self.get_dbname)

        self.ui.Button_next.clicked.connect(self.next)

    def get_dbname(self):
        """
        获取数据库名
        """
        if len(host := self.ui.lineEdit_host.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写主机')
            return
        if len(port := self.ui.lineEdit_port.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写数据库端口')
            return
        if len(username := self.ui.lineEdit_user.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写账号')
            return
        if len(password := self.ui.lineEdit_password.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写密码')
            return

        # 清空下拉框
        self.ui.comboBox_databases.clear()
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
            self.ui.comboBox_databases.addItem(dbname[0])

    def database_connect_test(self):
        """
        数据库连接测试
        """
        dialect = self.ui.comboBox_dbtype.currentText()
        if len(host := self.ui.lineEdit_host.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写主机')
            return
        if len(port := self.ui.lineEdit_port.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写数据库端口')
            return
        if len(username := self.ui.lineEdit_user.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写账号')
            return
        if len(password := self.ui.lineEdit_password.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写密码')
            return
        if len(database := self.ui.comboBox_databases.currentText()) == 0:
            QMessageBox.information(self.ui, '提示', '请选择数据库名')
            return

        res = SQLHandler.connection_check(dialect, username, password, host, port, database)
        if res.get('code'):
            QMessageBox.information(self.ui, '提示', '数据库连接成功!')
        else:
            QMessageBox.critical(self.ui, '错误', '数据库连接失败!')

        # databases = check_sql_link(dialect, username, password, host, port, database)
        # print(databases)

    def next(self):
        id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        dir = os.getcwd()
        f = open(dir + "/config/config_" + str(id) + ".conf", "w")
        f.close()
        # 接收参数
        if len(host := self.ui.lineEdit_host.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写主机')
            return
        if len(port := self.ui.lineEdit_port.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写数据库端口')
            return
        if len(username := self.ui.lineEdit_user.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写账号')
            return
        if len(password := self.ui.lineEdit_password.text()) == 0:
            QMessageBox.information(self.ui, '提示', '请填写密码')
            return

        dialect = self.ui.comboBox_dbtype.currentText()
        host = host
        port = port
        database = self.ui.comboBox_databases.currentText()
        username = username
        password = password
        # 检查数据库链接
        result_sql = SQLHandler.connect_sql_link(dialect, username, password, host, port, database)
        if result_sql['code']:
            # 填写配置文件
            configfile = "config/config_" + str(id) + ".conf"
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
            result_sql = SQLHandler.generate_tables_information()
            print(result_sql)
            if result_sql['code']:
                return {'code': '2000', 'data': result_sql['data'], 'message': '数据库连接成功',
                        'invalid': result_sql['invalid']}
            else:
                return {'code': '4000', 'data': [], 'message': result_sql['message']}
        else:
            QMessageBox.critical(self.ui, '错误', '数据库读取失败!')
            return


app = QApplication([])
stats = Main()
stats.ui.show()
app.exec()
