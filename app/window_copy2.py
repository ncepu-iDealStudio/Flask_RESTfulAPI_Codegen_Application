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

# 表配置页导入的包
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from functools import partial


class MainWindow:

    def __init__(self):
        # 从文件中加载UI定义
        qfile_main = QFile('app/ui/MainWindow_copy2.ui')
        qfile_main.open(QFile.ReadOnly)
        qfile_main.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile_main)

        # 定义主要数据sql_data
        self.sql_data = {
            'table': [],
            'view': []
        }

        # 对各个页面进行初始化
        self.frame_init()
        self.db_config_init()
        self.table_config_init()
        self.view_config_init()
        self.confirm_config_init()
        self.generate_init()

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
        # 通过table_data创建按钮组

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
        self.sql_data = sql_data

        self.table_number = 0   # 记录拿到表的序号
        self.selected_table = {}  # 被选中的表缓存数据

        # 给全选按钮命名
        self.ui.pushButton_all_6.setText('全选')

        # 添加表按钮等组件
        for table in self.sql_data['table']:
            self.add_table_button_group(table.get('table'))

        # 测试用，添加组件
        # for x in range(17):
        #     self.add_table_button_group(str(x))

        #  事件初始化

        # 全选CheckBox事件添加
        self.ui.centralwidget.findChild(QCheckBox, u"checkBox_all_6").clicked.connect(self.checkBox_all_select_clicked)

        # 表对应的pushButton事件添加
        for pushButton in self.ui.scrollArea_left_6.findChildren(QPushButton):
            pushButton.clicked.connect(partial(self.table_pushButton_clicked, pushButton.text()))

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

    def add_table_button_group(self, table_name):
        '''
        添加单个按钮组件组，用于表配置页面
        :param table_name: 表名
        :return:
        '''

        self.ui.horizontalLayoutWidget1 = QWidget(self.ui.scrollAreaWidgetContents_left_6)
        self.ui.horizontalLayoutWidget1.setObjectName(u"horizontalLayoutWidget_" + table_name)
        self.ui.horizontalLayoutWidget1.setGeometry(QRect(0, 31 + self.table_number * 31, 281, 31))

        self.ui.horizontalLayout_1 = QHBoxLayout(self.ui.horizontalLayoutWidget1)
        self.ui.horizontalLayout_1.setObjectName(u"horizontalLayout_" + table_name)
        self.ui.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.ui.checkBox_1 = QCheckBox(self.ui.horizontalLayoutWidget_6)
        self.ui.checkBox_1.setObjectName(u"checkBox_" + table_name)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.checkBox_all_6.sizePolicy().hasHeightForWidth())
        self.ui.checkBox_1.setSizePolicy(sizePolicy)
        self.ui.checkBox_1.setMinimumSize(QSize(0, 0))

        self.ui.horizontalLayout_1.addWidget(self.ui.checkBox_1)

        self.ui.pushButton_1 = QPushButton(self.ui.horizontalLayoutWidget_6)
        self.ui.pushButton_1.setObjectName(u"pushButton_" + table_name)
        self.ui.pushButton_1.setText(table_name)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ui.pushButton_1.sizePolicy().hasHeightForWidth())
        self.ui.pushButton_1.setSizePolicy(sizePolicy1)

        self.ui.horizontalLayout_1.addWidget(self.ui.pushButton_1)

        # 设置scrollAreaWidgetContents大小
        self.ui.scrollAreaWidgetContents_left_6.setMinimumSize(QSize(0, 60 + self.table_number * 31))

        self.table_number += 1

    def checkBox_all_select_clicked(self):
        '''
        全选checkBox点击调用
        :return:
        '''
        if self.ui.centralwidget.findChild(QCheckBox, u"checkBox_all_6").isChecked():
            for checkBox in self.ui.scrollArea_left_6.findChildren(QCheckBox):
                checkBox.setChecked(True)

        else:
            for checkBox in self.ui.scrollArea_left_6.findChildren(QCheckBox):
                checkBox.setChecked(False)

    def table_pushButton_clicked(self, button_text):
        '''
        表配置页按钮点击事件函数
        :param button_text: 按钮的text
        :return:
        '''

        if button_text == '全选':
            self.ui.stackedWidget_right.setCurrentIndex(0)
        else:
            self.ui.stackedWidget_right.setCurrentIndex(1)

            # 保存上个表配置的数据

            # 清空配置框
            self.ui.comboBox_select_table_logicaldeletemark.clear()
            self.ui.comboBox_select_table_businesskeyname.clear()

            # 加载数据到配置框

            for table in self.sql_data['table']:
                if table['table'] == button_text:
                    self.selected_table = table

            self.ui.label_table_name_7.setText(button_text)  # 这里必须调用setText方法，直接对text赋值没用

            self.ui.comboBox_select_table_logicaldeletemark.addItem('选择逻辑删除标识字段')
            self.ui.comboBox_select_table_businesskeyname.addItem('选择业务主键')
            for field in self.selected_table['field']:
                if field['field_type'] == 'int':
                    self.ui.comboBox_select_table_logicaldeletemark.addItem(field['field_name'])
                self.ui.comboBox_select_table_businesskeyname.addItem(field['field_name'])

            self.ui.comboBox_select_table_businesskeyname.currentIndexChanged.connect(partial(self.comboBob_currentIndexChanged))  # 这里的currentIndexChanged.connect会自动传入一个参数index


            # print(self.ui.comboBox_select_table_logicaldeletemark.currentText())

    def comboBob_currentIndexChanged(self, comboBox_index):
        '''
        comboBox的item改变事件，目前为self.ui.comboBox_select_table_businesskeyname专属
        :param comboBox_index: 被选择的item索引
        :return:
        '''

        businesskeyname = self.ui.comboBox_select_table_businesskeyname.currentText()
        for filed in self.selected_table:
            if filed['filed_name'] == businesskeyname:
                pass


def start():

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app/ui/ncepu.jpg'))
    main_window = MainWindow()
    main_window.ui.show()
    sys.exit(app.exec())
