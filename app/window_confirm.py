# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : window_confirm.py
# @ide    : PyCharm
# @time   : 2022-10-12 16:14:53
'''

'''

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem, QAbstractItemView


from types import MethodType


def window_init_for_confirm(self):
    pass


def confirm_config_init(self):
    '''
    确认配置页初始化初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
    :return:
    '''
    new_table = []
    for x in self.sql_data['table']:
        if x['ischecked'] == True:
            new_table.append(x)
    self.ui.tableWidget_DB.setRowCount(len(new_table))
    self.ui.tableWidget_DB.setColumnCount(5)
    for i in range(len(new_table)):
        item_name_1 = QTableWidgetItem(new_table[i]['table'])
        item_name_1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        str1 = ''
        for x in new_table[i]['field']:
            if x["field_encrypt"] == True:
                str1 = str1 + x["field_name"] + ","
        if str1 == '':
            str1 = '/'
        str2 = new_table[i]['logicaldeletemark']
        if new_table[i]['logicaldeletemark'] == '':
            str2 = "/"
        str3 = self.sql_data['table'][i]['businesskeyname']
        if new_table[i]['businesskeyname'] == '':
            str3 = "/"
        str4 = new_table[i]['businesskeyrule']
        if new_table[i]['businesskeyrule'] == '':
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
    new_view = []
    for x in self.sql_data['view']:
        if x["ischecked"] == True:
            new_view.append(x)
    self.ui.tableWidget_View.setRowCount(len(new_view))
    self.ui.tableWidget_View.setColumnCount(2)
    for i in range(len(new_view)):
        item_name_1 = QTableWidgetItem(new_view[i]['view'])
        item_name_1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        str2 = ' '
        for x in new_view[i]['filter_field']:
            if x["ischecked"] == True:
                str2 = str2 + x["field_name"] + ","
        if str2 == '':
            str2 = '/'
        item_name_2 = QTableWidgetItem(str2)
        item_name_2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.tableWidget_View.setItem(i, 0, item_name_1)
        self.ui.tableWidget_View.setItem(i, 1, item_name_2)
    self.ui.tableWidget_View.setEditTriggers(QAbstractItemView.NoEditTriggers)


def confirm_config(self):
    '''
    确认配置页主要代码
    :return:
    '''

    self.next_step()


# 将函数添加到对象中
def add_func(self):
    '''
    添加该.py文件的方法到对象中
    :param self: 添加函数的对象
    :return:
    '''
    self.confirm_config_init = MethodType(confirm_config_init, self)
    self.confirm_config = MethodType(confirm_config, self)
    self.window_init_for_confirm = MethodType(window_init_for_confirm, self)