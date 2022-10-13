# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : window_confirm.py
# @ide    : PyCharm
# @time   : 2022-10-12 16:14:53
'''
this is function description
'''
# import module your need
import configparser
import datetime
import os
import sys

import pymysql
from PySide6.QtCore import QFile, Qt
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidgetItem, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon


from types import MethodType


# 将自己负责的函数复制到此处
def confirm_config_init(self):
    '''
    确认配置页初始化初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
    :return:
    '''
    pass

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
             'ischecked': False}, {'view': 'v_student_course_score',
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
            str1 = '/'
        str2 = self.sql_data['table'][i]['logicaldeletemark']
        if self.sql_data['table'][i]['logicaldeletemark'] == '':
            str2 = "/"
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
            str2 = '/'
        item_name_2 = QTableWidgetItem(str2)
        item_name_2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.tableWidget_View.setItem(i, 0, item_name_1)
        self.ui.tableWidget_View.setItem(i, 1, item_name_2)
    self.ui.tableWidget_View.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # 给出一个调试数据，正常情况应该使用self.sql_data数据

    self.ui.stackedWidget.setCurrentIndex(2)



# 将函数添加到对象中
def add_func(self):
    '''
    添加该.py文件的方法到对象中
    :param self: 添加函数的对象
    :return:
    '''
    self.confirm_config_init = MethodType(confirm_config_init, self)
    self.confirm_config = MethodType(confirm_config, self)