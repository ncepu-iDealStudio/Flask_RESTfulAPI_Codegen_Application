#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:dbconfig.py
# author:Chen Qinyu
# datetime:2022/8/23 17:22
# software: PyCharm

"""
this is function description
"""
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

from utils.checkSqlLink import connection_check, check_sql_link


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

        self.ui.Button_connect_test.clicked.connect(self.database_connect_test)

    def database_connect_test(self):
        dialect = self.ui.lineEdit_dbtype.text()
        username = self.ui.lineEdit_user.text()
        password = self.ui.lineEdit_password.text()
        host = self.ui.lineEdit_host.text()
        port = self.ui.lineEdit_port.text()
        database = self.ui.lineEdit_database.text()
        print(dialect, username, password, host, port, database)
        res = connection_check(dialect, username, password, host, port, database)
        if res.get('code'):
            print('数据库连接成功')
        else:
            print(res.get('message'), res.get('error'))


app = QApplication([])
stats = Main()
stats.ui.show()
app.exec()
