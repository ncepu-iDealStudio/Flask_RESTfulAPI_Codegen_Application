#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:main.py
# author:Chen Qinyu
# datetime:2022/8/23 17:22
# software: PyCharm

"""
this is function description
"""
import pymysql
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

        self.ui.Button_get_dbnames.clicked.connect(self.get_dbname)

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

        res = connection_check(dialect, username, password, host, port, database)
        if res.get('code'):
            QMessageBox.information(self.ui, '提示', '数据库连接成功!')
        else:
            QMessageBox.critical(self.ui, '错误', '数据库连接失败!')

        # databases = check_sql_link(dialect, username, password, host, port, database)
        # print(databases)


app = QApplication([])
stats = Main()
stats.ui.show()
app.exec()
