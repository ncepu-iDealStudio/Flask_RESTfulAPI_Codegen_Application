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
from PySide6.QtCore import QFile, Qt
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidgetItem, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from app.utils.checkSqlLink import SQLHandler


class MainWindow:

    def __init__(self):
        # 从文件中加载UI定义
        qfile_main = QFile('app/ui/MainWindow_copy4.ui')
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
        pass

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
        '''
        数据库配置页面主要代码，
        :return:
        '''

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
        self.sql_data = {
            'table': [
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},{'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},{'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},{'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},{'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},{'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},






                {'table': 'student', 'businesskeyname': 'Sno', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'Sname', 'field_type': 'str', 'field_encrypt': False},
                           {'field_name': 'sex', 'field_type': 'str', 'field_encrypt': True},
                           {'field_name': 'age', 'field_type': 'int', 'field_encrypt': True},
                           {'field_name': 'dept', 'field_type': 'str', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False},
                {'table': 'sc', 'businesskeyname': '', 'businesskeyrule': '', 'logicaldeletemark': '',
                 'field': [{'field_name': 'grade', 'field_type': 'int', 'field_encrypt': False}],
                 'businesskeyuneditable': True, 'businesskeytype': '', 'issave': False}],

            'view': [
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},{'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_student_course_score',
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': True},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},


                {'view': 'v_test', 'filter_field': [
                    {'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                    {'field_name': 'testID', 'field_type': 'str', 'ischecked': True},
                    {'field_name': 'testName', 'field_type': 'str', 'ischecked': False}], 'ischecked': False}]
        }
        # 数据表
        self.ui.tableWidget_DB.setRowCount(len(self.sql_data['table']))
        self.ui.tableWidget_DB.setColumnCount(5)
        for i in range(len(self.sql_data['table'])):
            item_name_1 = QTableWidgetItem(self.sql_data['table'][i]['table'])
            item_name_1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            str1 = ''
            for x in self.sql_data['table'][i]['field']:
                if x["field_encrypt"] == True:
                    str1 = str1 + x["field_name"] + ","
            if str1 == '':
                str1='/'
            str2 =self.sql_data['table'][i]['logicaldeletemark']
            if self.sql_data['table'][i]['logicaldeletemark'] == '':
                str2 ="/"
            str3 = self.sql_data['table'][i]['businesskeyname']
            if self.sql_data['table'][i]['businesskeyname'] == '':
                str3 = "/"
            str4 = self.sql_data['table'][i]['businesskeyrule']
            if self.sql_data['table'][i]['businesskeyrule'] == '':
                str4 = "/"
            item_name_2 = QTableWidgetItem(str1)
            item_name_2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item_name_3 = QTableWidgetItem(str2)
            item_name_3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item_name_4 = QTableWidgetItem(str3)
            item_name_4.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item_name_5 = QTableWidgetItem(str4)
            item_name_5.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget_DB.setItem(i, 0, item_name_1)
            self.ui.tableWidget_DB.setItem(i, 1, item_name_2)
            self.ui.tableWidget_DB.setItem(i, 2, item_name_3)
            self.ui.tableWidget_DB.setItem(i, 3, item_name_4)
            self.ui.tableWidget_DB.setItem(i, 4, item_name_5)
            self.ui.tableWidget_DB.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 视图
        self.ui.tableWidget_View.setRowCount(len(self.sql_data['view']))
        self.ui.tableWidget_View.setColumnCount(2)
        for i in range(len(self.sql_data['view'])):
            item_name_1 = QTableWidgetItem(self.sql_data['view'][i]['view'])
            item_name_1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            str2 = ' '
            for x in self.sql_data['view'][i]['filter_field']:
                if x["ischecked"] == True:
                    str2 = str2 + x["field_name"] + ","
            if str2 == '':
                str2= '/'
            item_name_2 = QTableWidgetItem(str2)
            item_name_2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.tableWidget_View.setItem(i, 0, item_name_1)
            self.ui.tableWidget_View.setItem(i, 1, item_name_2)
        self.ui.tableWidget_View.setEditTriggers(QAbstractItemView.NoEditTriggers)


        # 给出一个调试数据，正常情况应该使用self.sql_data数据

        self.ui.stackedWidget.setCurrentIndex(2)

    def generate(self):
        '''
        代码生成页主要代码
        :return:
        '''
        pass


def start():

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app/ui/ncepu.jpg'))
    main_window = MainWindow()
    main_window.confirm_config()
    main_window.ui.show()
    sys.exit(app.exec())
