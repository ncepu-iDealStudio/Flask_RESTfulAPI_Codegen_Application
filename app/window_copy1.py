# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : window.py
# @ide    : PyCharm
# @time   : 2022-10-06 09:17:22
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


class MainWindow:

    def __init__(self):
        # 从文件中加载UI定义
        qfile_main = QFile('app/ui/MainWindow_copy1.ui')
        qfile_main.open(QFile.ReadOnly)
        qfile_main.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile_main)

        # 对各个页面进行初始化
        self.frame_init()
        self.db_config_init()
        self.table_config_init()
        self.view_config_init()
        self.confirm_config_init()
        self.generate_init()
        import datetime
        import random
        random_number = random.sample('0123456789', 4)
        self.id = datetime.datetime.now().strftime('%Y%m%d%H%M') + ''.join(random_number)

        # 定义主要数据sql_data
        self.sql_data = {
            'table': [],
            'view': []
        }

    def frame_init(self):
        '''
        框架初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
        :return:
        '''
        self.ui.pushButton_next.clicked.connect(self.button_next)
        self.ui.pushButton_last.clicked.connect(self.button_last)

    def db_config_init(self):
        '''
        数据库配置页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
        :return:
        '''
        self.ui.button_get_db_names.clicked.connect(self.get_dbname)

    def table_config_init(self):
        '''
        数据库表页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
        :return:
        '''
        pass

    def view_config_init(self):
        '''
        视图页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
        :return:
        '''
        pass

    def confirm_config_init(self):
        '''
        确认配置页初始化初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
        :return:
        '''
        pass

    def generate_init(self):
        '''
        代码生成页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
        :return:
        '''
        pass

    def button_next(self):
        '''
        下一步按钮点击函数
        :return:
        '''

        # 对不同页面给出不同的操作分支，各自完善相关方法
        if self.ui.stackedWidget.currentIndex() == 0:
            self.db_config()
            return

        if self.ui.stackedWidget.currentIndex() == 4:
            self.table_config()
            return

        if self.ui.stackedWidget.currentIndex() == 3:
            self.view_config()
            return

        if self.ui.stackedWidget.currentIndex() == 1:
            self.confirm_config()
            return

        if self.ui.stackedWidget.currentIndex() == 2:
            self.generate()
            return

    def button_last(self):
        '''
        上一步按钮点击函数
        :return:
        '''

        if self.ui.stackedWidget.currentIndex() == 4:
            self.ui.stackedWidget.setCurrentIndex(0)
            return

        if self.ui.stackedWidget.currentIndex() == 3:
            self.ui.stackedWidget.setCurrentIndex(4)
            return

        if self.ui.stackedWidget.currentIndex() == 1:
            self.ui.stackedWidget.setCurrentIndex(3)
            return

        if self.ui.stackedWidget.currentIndex() == 2:
            self.ui.stackedWidget.setCurrentIndex(1)
            return

    def db_config(self):
        """
        数据库配置页面主要代码，
        """
        id = self.id
        dir = os.getcwd()
        f = open(dir + r"/app/config/config_" + str(id) + ".conf", "w")
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
            configfile = "app/config/config_" + str(id) + ".conf"
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

        # 进入下一步前，完成相关配置并完成对主要数据sql_data的修改
        self.ui.stackedWidget.setCurrentIndex(4)

    def table_config(self):
        '''
        数据库表配置页主要代码
        :return:
        '''

        # 给出一个调试数据，正常情况应该使用self.sql_data数据
        sql_data = {
            'table': [
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': False},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'student', 'businesskeyname': 'Sno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Sname', 'field_type': 'str', 'field_encrypt': False},
                           {'field_name': 'sex', 'field_type': 'str', 'field_encrypt': False},
                           {'field_name': 'age', 'field_type': 'int', 'field_encrypt': False},
                           {'field_name': 'dept', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'sc', 'businesskeyname': '', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'grade', 'field_type': 'int', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': '', 'issave': False}],

            'view': [
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': 'False'},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': 'False'},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': 'False'}],
                 'ischecked': 'False'},
                {'view': 'v_test', 'filter_field': [
                    {'field_name': 'autoID', 'field_type': 'int', 'ischecked': 'False'},
                    {'field_name': 'testID', 'field_type': 'str', 'ischecked': 'False'},
                    {'field_name': 'testName', 'field_type': 'str', 'ischecked': 'False'}], 'ischecked': 'False'}]
        }

        # 进入下一步前，完成相关配置并完成对主要数据sql_data的修改
        self.ui.stackedWidget.setCurrentIndex(3)

    def view_config(self):
        '''
        视图配置页主要代码
        :return:
        '''

        # 给出一个调试数据，正常情况应该使用self.sql_data数据
        sql_data = {
            'table': [
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': False},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'student', 'businesskeyname': 'Sno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Sname', 'field_type': 'str', 'field_encrypt': False},
                           {'field_name': 'sex', 'field_type': 'str', 'field_encrypt': False},
                           {'field_name': 'age', 'field_type': 'int', 'field_encrypt': False},
                           {'field_name': 'dept', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'sc', 'businesskeyname': '', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'grade', 'field_type': 'int', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': '', 'issave': False}],

            'view': [
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': 'False'},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': 'False'},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': 'False'}],
                 'ischecked': 'False'},
                {'view': 'v_test', 'filter_field': [
                    {'field_name': 'autoID', 'field_type': 'int', 'ischecked': 'False'},
                    {'field_name': 'testID', 'field_type': 'str', 'ischecked': 'False'},
                    {'field_name': 'testName', 'field_type': 'str', 'ischecked': 'False'}], 'ischecked': 'False'}]
        }


        # 进入下一步前，完成相关配置并完成对主要数据sql_data的修改
        self.ui.stackedWidget.setCurrentIndex(1)

    def confirm_config(self):
        '''
        确认配置页主要代码
        :return:
        '''

        # 给出一个调试数据，正常情况应该使用self.sql_data数据
        sql_data = {
            'table': [
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': False},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'student', 'businesskeyname': 'Sno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Sname', 'field_type': 'str', 'field_encrypt': False},
                           {'field_name': 'sex', 'field_type': 'str', 'field_encrypt': False},
                           {'field_name': 'age', 'field_type': 'int', 'field_encrypt': False},
                           {'field_name': 'dept', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'sc', 'businesskeyname': '', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'grade', 'field_type': 'int', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': '', 'issave': False}],

            'view': [
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': 'False'},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': 'False'},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': 'False'}],
                 'ischecked': 'False'},
                {'view': 'v_test', 'filter_field': [
                    {'field_name': 'autoID', 'field_type': 'int', 'ischecked': 'False'},
                    {'field_name': 'testID', 'field_type': 'str', 'ischecked': 'False'},
                    {'field_name': 'testName', 'field_type': 'str', 'ischecked': 'False'}], 'ischecked': 'False'}]
        }
        self.ui.stackedWidget.setCurrentIndex(2)

    def generate(self):
        '''
        代码生成页主要代码
        :return:
        '''
        pass

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


def start():

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app/ui/ncepu.jpg'))
    main_window = MainWindow()
    main_window.ui.show()
    sys.exit(app.exec())
