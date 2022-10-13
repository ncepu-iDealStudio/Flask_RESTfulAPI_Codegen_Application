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
import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QFile, QRect, QSize
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QCheckBox, QPushButton, QWidget, QHBoxLayout, QSizePolicy

from functools import partial

class MainWindow:

    def __init__(self):
        # 从文件中加载UI定义
        qfile_main = QFile('app/ui/MainWindow_copy3.ui')
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
                 'filter_field': [{'field_name': 'autoID', 'field_type': 'int', 'ischecked':False},
                                  {'field_name': 'studentID', 'field_type': 'str', 'ischecked': False},
                                  {'field_name': 'classID', 'field_type': 'str', 'ischecked': False}],
                 'ischecked': False},
                {'view': 'v_test', 'filter_field': [
                    {'field_name': 'autoID', 'field_type': 'int', 'ischecked': False},
                    {'field_name': 'testID', 'field_type': 'str', 'ischecked': False},
                    {'field_name': 'testName', 'field_type': 'str', 'ischecked': False}], 'ischecked': False}]
        }
        self.sql_data = sql_data

        self.view_number = 0  #记录视图序号
        self.selected_view = {}  # 被选中的视图的缓存数据
        self.selected_field = {}  # 被选中的视图的字段

        self.view_field_number = 0 # 记录视图字段序号


        self.ui.pushButton_all_2.setText('全选')  #全选按钮命名

        # 视图选择按钮
        for view in self.sql_data['view']:
            self.add_view_button_group(view.get('view'))


        # 全选CheckBox事件添加
        self.ui.centralwidget.findChild(QCheckBox, u"checkBox_all_2").clicked.connect(self.view_checkBox_all_select_clicked)


        # 视图页CheckBox事件添加
        for checkbox in self.ui.scrollArea_left_2.findChildren(QCheckBox):
            checkbox.stateChanged.connect(partial(self.view_checkBox_clicked, checkbox, self.sql_data))


        # # 表对应的pushButton事件添加
        for pushButton in self.ui.scrollArea_left_2.findChildren(QPushButton):
            pushButton.clicked.connect(partial(self.view_pushButton_clicked, pushButton.text(), self.sql_data))

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

    def add_view_button_group(self,view_name):
        '''
        视图页添加按钮
        :param view_name: 视图名
        :return:
        '''
        self.ui.horizontalLayoutWidget1 = QWidget(self.ui.scrollAreaWidgetContents_left_2)
        self.ui.horizontalLayoutWidget1.setObjectName(u"horizontalLayoutWidget_" + view_name)
        self.ui.horizontalLayoutWidget1.setGeometry(QRect(0, 31 + self.view_number * 31, 281, 31))

        self.ui.horizontalLayout_1 = QHBoxLayout(self.ui.horizontalLayoutWidget1)
        self.ui.horizontalLayout_1.setObjectName(u"horizontalLayout_" + view_name)
        self.ui.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.ui.checkBox_1 = QCheckBox(self.ui.horizontalLayoutWidget)
        self.ui.checkBox_1.setObjectName(u"checkBox_" + view_name)
        self.ui.checkBox_1.setText(view_name)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.checkBox_all_2.sizePolicy().hasHeightForWidth())
        self.ui.checkBox_1.setSizePolicy(sizePolicy)
        self.ui.checkBox_1.setMinimumSize(QSize(0, 0))
        self.ui.checkBox_1.setMaximumSize(QSize(13, 13))

        self.ui.horizontalLayout_1.addWidget(self.ui.checkBox_1)

        self.ui.pushButton_1 = QPushButton(self.ui.horizontalLayoutWidget)
        self.ui.pushButton_1.setObjectName(u"pushButton_" + view_name)
        self.ui.pushButton_1.setText(view_name)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ui.pushButton_1.sizePolicy().hasHeightForWidth())
        self.ui.pushButton_1.setSizePolicy(sizePolicy1)

        self.ui.horizontalLayout_1.addWidget(self.ui.pushButton_1)

        # 设置scrollAreaWidgetContents大小
        self.ui.scrollAreaWidgetContents_left_2.setMinimumSize(QSize(0, 60 + self.view_number * 31))

        self.view_number += 1


    def view_checkBox_clicked(self, checkbox, sql_data, index = -1):
        '''
        视图选择框里的checkbox事件注册
        :param checkbox: 复选框
        :return:
        '''
        self.sql_data = sql_data
        if checkbox.isChecked():
            self.sql_data_view_ischecked_update(checkbox, True)

        else:
            self.sql_data_view_ischecked_update(checkbox, False)


    def sql_data_view_ischecked_update(self, checkbox, bool):
        '''
        视图选择框里的checkbox事件注册实现方法
        :return:
        '''
        for view_num in range(len(self.sql_data['view'])):
            if self.sql_data['view'][view_num]['view'] == checkbox.text():
                    self.sql_data['view'][view_num]['ischecked'] = bool



    def view_checkBox_all_select_clicked(self):
        '''
        全选checkBox点击调用
        :return:
        '''
        if self.ui.centralwidget.findChild(QCheckBox, u"checkBox_all_2").isChecked():
            for checkBox in self.ui.scrollArea_left_2.findChildren(QCheckBox):
                checkBox.setChecked(True)

        else:
            for checkBox in self.ui.scrollArea_left_2.findChildren(QCheckBox):
                checkBox.setChecked(False)



    def view_pushButton_clicked(self,button_text,sql_data):
        '''
        视图配置，点击事件
        :param button_text: 视图名
        :return:
        '''
        print(2)
        self.sql_data = sql_data
        self.view_field_number = 0
        if button_text == '全选':
            self.ui.stackedWidget_3.setCurrentIndex(0)
        else:
            self.ui.stackedWidget_3.setCurrentIndex(1)

            # 匹配视图

            for view in self.sql_data['view']:
                if view['view'] == button_text:
                    self.selected_view = view

            # 添加字段按钮
            # for view in self.sql_data['view']:
            #     self.add_view_button_group(view.get('view'))

            # 修改表名
            self.ui.label_view.setText(button_text)

            # 字段表初始化
            self.tableWidget_init()

            # 添加字段按钮
            for filter_field in self.selected_view['filter_field']:
                self.add_field_button_group(filter_field['field_name'],button_text)

            # 添加字段事件
            for checkbox in self.ui.scrollArea_6.findChildren(QCheckBox):
                checkbox.stateChanged.connect(partial(self.field_checkBox_clicked, checkbox, button_text))
                # checkbox.stateChanged.connect(self.field_checkBox_clicked(checkbox,button_text))


    def field_checkBox_clicked(self,field_check,button_text,index = -1):
        '''
        字段点击事件
        :param button_text: 视图名
        :return:
        '''

        if field_check.isChecked():
            self.sql_data_view_field_update(field_check,button_text, True)

        else:
            self.sql_data_view_field_update(field_check, button_text,False)


    def sql_data_view_field_update(self,field_check,button_text, bool):
        '''
        字段点击事件实现方法
        :param button_text: 视图名
        :return:
        '''
        for view_num in range(len(self.sql_data['view'])):
            if self.sql_data['view'][view_num]['view'] == button_text:
                for field_num in range(len(self.sql_data['view'][view_num]['filter_field'])):
                    if self.sql_data['view'][view_num]['filter_field'][field_num]['field_name'] == field_check.text():
                        self.sql_data['view'][view_num]['filter_field'][field_num]['ischecked'] = bool


    def tableWidget_init(self):
        '''
        字段表初始化
        :return:
        '''
        #删除当前表
        self.ui.tableWidget.clearContents()

        row = 4 #行数
        column = 4 # 列数
        self.ui.tableWidget.setRowCount(row)
        self.ui.tableWidget.setColumnCount(column)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.horizontalHeader().setVisible(False)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.ui.tableWidget.setShowGrid(False)



    def add_field_button_group(self,field_name,button_text):
        '''
        添加字段复选框
        :param field_name: 字段名称
        :return:
        '''
        checkBox = QtWidgets.QCheckBox(self.ui.scrollAreaWidgetContents_4)
        for filter_field in self.selected_view['filter_field']:
            if filter_field['field_name'] == field_name:
                if filter_field['ischecked'] == False:
                    checkBox.setCheckState(QtCore.Qt.Unchecked)
                else:
                    checkBox.setChecked(True)
        checkBox.setObjectName('checkBox_'+field_name)
        checkBox.setText(field_name)
        self.ui.tableWidget.setCellWidget(int(self.view_field_number / 4), self.view_field_number % 4, checkBox)

        self.view_field_number += 1

        checkBox.stateChanged.connect(partial(self.field_checkBox_clicked, checkBox, button_text))


def start():

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app/ui/ncepu.jpg'))
    main_window = MainWindow()
    main_window.ui.show()
    sys.exit(app.exec())
