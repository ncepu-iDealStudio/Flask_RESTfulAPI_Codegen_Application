# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : window_view.py
# @ide    : PyCharm
# @time   : 2022-10-12 16:14:17
'''
this is function description
'''
# import module your need
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QRect, QSize
from PySide6.QtWidgets import QCheckBox, QPushButton, QWidget, QHBoxLayout, QSizePolicy, QVBoxLayout, QListWidgetItem, \
    QListWidget

from functools import partial

from types import MethodType


# 将自己负责的函数复制到此处
def window_init_for_view(self):
    # 添加表按钮等组件初始化
    self.add_view_button_group_init()
    self.view_number = -1
    self.add_view_button_group('select_all')

def view_config_init(self):
    '''
    视图页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
    :return:
    '''

    self.view_number = 0  # 记录视图序号
    self.selected_view = {}  # 被选中的视图的缓存数据
    self.selected_field = {}  # 被选中的视图的字段

    self.view_field_number = 0  # 记录视图字段序号

    # 清空按钮并添加新按钮
    del_view_button_list = self.ui.listWidget_view.findChildren(QPushButton)
    for del_widget in del_view_button_list:
        table_name = del_widget.objectName().replace('pushButton_', '')
        if table_name != 'select_all':
            widget_del = self.ui.listWidget_view.findChild(QWidget,
                                                                                 u"horizontalLayoutWidget_" + table_name)
            # 如果在没有event loop的thread使用, 那么thread结束后销毁对象。
            widget_del.deleteLater()

    self.view_number = 0
    self.ui.listWidget_view.clear()

    # # 设置scrollAreaWidgetContents大小
    # self.ui.scrollAreaWidgetContents_left_2.setMinimumSize(QSize(0, 45 + self.view_number * 31))

    # # 设置面板大小
    # self.ui.verticalLayoutWidget_add_view_button.setGeometry(QRect(0, 0, 281, 45 + self.view_number * 31))
    # 视图选择按钮
    self.add_view_list()
    self.ui.centralwidget.findChild(QListWidget, u"listWidget_view").itemClicked.connect(self.view_list_item_clicked)

    # 初始化全选按钮
    self.ui.centralwidget.findChild(QPushButton, u"pushButton_vsall").setText('全选')
    # 全选CheckBox事件添加
    self.ui.listWidget_view.findChild(QCheckBox, u"checkBox_vsall").clicked.connect(self.view_checkBox_all_select_clicked)

    # 视图页CheckBox事件添加
    for checkbox in self.ui.listWidget_view.findChildren(QCheckBox):
        checkbox.stateChanged.connect(partial(self.view_checkBox_clicked, checkbox))

    # # 表对应的pushButton事件添加
    for pushButton in self.ui.listWidget_view.findChildren(QPushButton):
        pushButton.clicked.connect(partial(self.view_pushButton_clicked, pushButton.text()))

def view_config(self):
    '''
    视图配置页主要代码
    :return:
    '''
    self.next_step()

    # 进入下一步前，完成相关配置并完成对主要数据sql_data的修改

def add_view_button_group_init(self):
    '''
    表格按钮初始化
    :return:
    '''
    # self.ui.verticalLayoutWidget_add_view_button = QWidget(self.ui.scrollAreaWidgetContents_left_2)
    # # self.ui.verticalLayoutWidget_add.setGeometry(QRect(20, 320 + 41 * self.encrypt_group_number, 497, 41))
    #
    # self.ui.verticalLayoutWidget_add_view_button.setGeometry(QRect(0, 0, 281, 31))
    #
    # self.ui.add_view_button_encrypt_group_layout = QVBoxLayout(self.ui.verticalLayoutWidget_add_view_button)
    #
    # # # 初始化滚动面板容量
    # # self.ui.scrollAreaWidgetContents_right_7.setMinimumSize(QSize(0, 400 + 41 * self.encrypt_group_count))
    #
    # # 设置scrollAreaWidgetContents大小
    # self.ui.scrollAreaWidgetContents_left_2.setMinimumSize(QSize(0, 60))

def add_view_button_group(self,view_name):
    '''
    视图页添加按钮
    :param view_name: 视图名
    :return:
    '''
    # self.ui.horizontalLayoutWidget1 = QWidget()
    # self.ui.horizontalLayoutWidget1.setObjectName(u"horizontalLayoutWidget_" + view_name)
    # self.ui.horizontalLayoutWidget1.setGeometry(QRect(0, 31 + self.view_number * 31, 281, 31))
    #
    # self.ui.horizontalLayout_1 = QHBoxLayout(self.ui.horizontalLayoutWidget1)
    # self.ui.horizontalLayout_1.setObjectName(u"horizontalLayout_" + view_name)
    # self.ui.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
    # self.ui.checkBox_1 = QCheckBox(self.ui.horizontalLayoutWidget)
    # self.ui.checkBox_1.setObjectName(u"checkBox_" + view_name)
    # self.ui.checkBox_1.setText(view_name)
    #
    # sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    # sizePolicy.setHorizontalStretch(0)
    # sizePolicy.setVerticalStretch(0)
    # sizePolicy.setHeightForWidth(self.ui.checkBox_1.sizePolicy().hasHeightForWidth())
    # self.ui.checkBox_1.setSizePolicy(sizePolicy)
    # self.ui.checkBox_1.setMinimumSize(QSize(0, 0))
    # self.ui.checkBox_1.setMaximumSize(QSize(13, 13))
    #
    # self.ui.horizontalLayout_1.addWidget(self.ui.checkBox_1)
    #
    # self.ui.pushButton_1 = QPushButton(self.ui.horizontalLayoutWidget)
    # self.ui.pushButton_1.setObjectName(u"pushButton_" + view_name)
    # self.ui.pushButton_1.setText(view_name)
    # sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    # sizePolicy1.setHorizontalStretch(0)
    # sizePolicy1.setVerticalStretch(0)
    # sizePolicy1.setHeightForWidth(self.ui.pushButton_1.sizePolicy().hasHeightForWidth())
    # self.ui.pushButton_1.setSizePolicy(sizePolicy1)
    #
    # self.ui.horizontalLayout_1.addWidget(self.ui.pushButton_1)
    #
    # # 把组件添加到面板
    # self.ui.add_view_button_encrypt_group_layout.addWidget(self.ui.horizontalLayoutWidget1)
    #
    # self.view_number += 1
    #
    # # 设置scrollAreaWidgetContents大小
    # self.ui.scrollAreaWidgetContents_left_2.setMinimumSize(QSize(0, 45 + self.view_number * 31))
    #
    # # 设置面板大小
    # self.ui.verticalLayoutWidget_add_view_button.setGeometry(QRect(0, 0, 281, 45 + self.view_number * 31))

def view_checkBox_clicked(self, checkbox, index = -1):
    '''
    视图选择框里的checkbox事件注册
    :param checkbox: 复选框
    :return:
    '''
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
    if self.ui.centralwidget.findChild(QCheckBox, u"checkBox_vsall").isChecked():
        for checkBox in self.ui.listWidget_view.findChildren(QCheckBox):
            checkBox.setChecked(True)

    else:
        for checkBox in self.ui.listWidget_view.findChildren(QCheckBox):
            checkBox.setChecked(False)

def view_pushButton_clicked(self,button_text):
    '''
    视图配置，点击事件
    :param button_text: 视图名
    :return:
    '''
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


def add_view_list_item(self,view_name):
    view_item = QListWidgetItem()
    view_item.setSizeHint(QSize(0, 22))
    view_item.setText(view_name)
    view_checkBox = QCheckBox()
    view_checkBox.setText(view_name)
    self.ui.centralwidget.findChild(QListWidget, u"listWidget_view").addItem(view_item)
    # self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_table").setItemWidget(table_item, table_checkBox)

    self.ui.horizontalLayoutWidget1 = QWidget()
    self.ui.horizontalLayoutWidget1.setObjectName(u"horizontalLayoutWidget_" + view_name)
    self.ui.horizontalLayoutWidget1.setGeometry(QRect(0, 31 + self.view_number * 31, 281, 31))

    self.ui.horizontalLayout_1 = QHBoxLayout(self.ui.horizontalLayoutWidget1)
    self.ui.horizontalLayout_1.setObjectName(u"horizontalLayout_" + view_name)
    self.ui.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
    self.ui.checkBox_1 = QCheckBox(self.ui.horizontalLayoutWidget1)
    self.ui.checkBox_1.setObjectName(u"checkBox_" + view_name)
    self.ui.checkBox_1.setText(view_name)

    sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.ui.checkBox_1.sizePolicy().hasHeightForWidth())
    self.ui.checkBox_1.setSizePolicy(sizePolicy)
    self.ui.checkBox_1.setMinimumSize(QSize(0, 0))
    self.ui.checkBox_1.setMaximumSize(QSize(13, 13))

    self.ui.horizontalLayout_1.addWidget(self.ui.checkBox_1)

    self.ui.pushButton_1 = QPushButton(self.ui.horizontalLayoutWidget1)
    self.ui.pushButton_1.setObjectName(u"pushButton_" + view_name)
    self.ui.pushButton_1.setText(view_name)
    sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    sizePolicy1.setHorizontalStretch(0)
    sizePolicy1.setVerticalStretch(0)
    sizePolicy1.setHeightForWidth(self.ui.pushButton_1.sizePolicy().hasHeightForWidth())
    self.ui.pushButton_1.setSizePolicy(sizePolicy1)

    self.ui.horizontalLayout_1.addWidget(self.ui.pushButton_1)

    self.view_number += 1

    # 把组件添加到面板

    self.ui.centralwidget.findChild(QListWidget, u"listWidget_view").setItemWidget(view_item, self.ui.horizontalLayoutWidget1)


def add_view_list(self):
    self.ui.centralwidget.findChild(QListWidget, u"listWidget_view").clear()
    self.add_view_list_item("vsall")
    for view in self.sql_data['view']:
        self.add_view_list_item(view.get('view'))


def view_list_item_clicked(self, item):
    '''
    视图配置页listWidgetItem点击事件函数
    :param item: 被点击的listWidgetItem
    :return:
    '''

    # 调用按钮点击方法，使得点击不同的位置效果相同
    self.view_pushButton_clicked(self.ui.listWidget_view.findChild(QPushButton, 'pushButton_' + item.text()).text())


# 将函数添加到对象中
def add_func(self):
    '''
    添加该.py文件的方法到对象中
    :param self: 添加函数的对象
    :return:
    '''
    self.window_init_for_view = MethodType(window_init_for_view, self)
    self.view_config_init = MethodType(view_config_init, self)
    self.view_config = MethodType(view_config, self)
    self.add_view_button_group_init = MethodType(add_view_button_group_init, self)
    self.add_view_button_group = MethodType(add_view_button_group, self)
    self.view_checkBox_clicked = MethodType(view_checkBox_clicked, self)
    self.sql_data_view_ischecked_update = MethodType(sql_data_view_ischecked_update, self)
    self.view_checkBox_all_select_clicked = MethodType(view_checkBox_all_select_clicked, self)
    self.view_pushButton_clicked = MethodType(view_pushButton_clicked, self)
    self.field_checkBox_clicked = MethodType(field_checkBox_clicked, self)
    self.sql_data_view_field_update = MethodType(sql_data_view_field_update, self)
    self.tableWidget_init = MethodType(tableWidget_init, self)
    self.add_field_button_group = MethodType(add_field_button_group, self)

    self.add_view_list = MethodType(add_view_list, self)
    self.add_view_list_item = MethodType(add_view_list_item, self)
    self.view_list_item_clicked = MethodType(view_list_item_clicked, self)