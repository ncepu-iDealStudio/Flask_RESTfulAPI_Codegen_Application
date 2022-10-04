# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : table_ui_perfect.py
# @ide    : PyCharm
# @time   : 2022-09-16 11:08:56
'''
在designer设计ui的基础上完善界面
'''
# import module your need
import sys

from app.ui.data_table_config import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class table_ui(Ui_MainWindow):
    # 对象初始化，传入表信息
    def __init__(self, main_window, table_sql):

        # 初始化ui工具生成的ui
        super().__init__()
        self.setupUi(main_window)
        self.retranslateUi(main_window)
        self.stackedWidget_right.setCurrentIndex(0)

        # 表数据正常，则正常运行
        self.table_number = 0
        if table_sql.get("code") == True:
            self.table_data = table_sql.get('data').get('table')
            self.table_sql = table_sql

            print(self.table_data)

            self.object_perfect()
            self.signal_perfect()

    def add_checkBox_group(self, table_name):
        self.horizontalLayoutWidget1 = QWidget(self.scrollAreaWidgetContents_left)
        self.horizontalLayoutWidget1.setObjectName(u"horizontalLayoutWidget_" + table_name)
        self.horizontalLayoutWidget1.setGeometry(QRect(0, 31 + self.table_number * 31, 281, 31))

        self.horizontalLayout_1 = QHBoxLayout(self.horizontalLayoutWidget1)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_" + table_name)
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.checkBox_1 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_1.setObjectName(u"checkBox_" + table_name)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_all.sizePolicy().hasHeightForWidth())
        self.checkBox_1.setSizePolicy(sizePolicy)
        self.checkBox_1.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_1.addWidget(self.checkBox_1)

        self.pushButton_1 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_" + table_name)
        self.pushButton_1.setText(table_name)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy1)

        self.horizontalLayout_1.addWidget(self.pushButton_1)

        # 设置scrollAreaWidgetContents大小
        self.scrollAreaWidgetContents_left.setMinimumSize(QSize(0, 60 + self.table_number * 31))

        self.table_number += 1

    def object_perfect(self):

        # 给全选按钮命名
        self.pushButton_all.setText('全选')

        # 添加表按钮等组件
        for table in self.table_data:
            self.add_checkBox_group(table.get('table'))

        # 测试用，添加组件
        for x in range(10):
            self.add_checkBox_group(str(x))



    def signal_perfect(self):

        self.centralwidget.findChild(QCheckBox, u"checkBox_all").clicked.connect(self.checkBox_all_select)

        self.centralwidget.findChild(QPushButton, u"pushButton_all").clicked.connect(self.pushButton_clicked)

        for pushButton in self.centralwidget.findChildren(QPushButton):
            print(pushButton.text())
            pushButton.clicked.connect(self.pushButton_clicked(pushButton.text()))
            # pushButton.clicked.connect(lambda text = 1: self.pushButton_clicked(text))

    def checkBox_all_select(self):
        '''
        全选checkBox点击调用
        :return:
        '''
        if self.centralwidget.findChild(QCheckBox, u"checkBox_all").isChecked():
            for checkBox in self.centralwidget.findChildren(QCheckBox):
                checkBox.setChecked(True)

        else:
            for checkBox in self.centralwidget.findChildren(QCheckBox):
                checkBox.setChecked(False)

    @Slot(str)
    def pushButton_clicked(self, text):
        print("绑定")
        self.stackedWidget_right.setCurrentIndex(1)
        print(text)


        print(text)

    def test(self):
        print("yes")



if __name__ == '__main__':

    table_sql = {'code': True, 'message': '成功', 'data': {'table': [{'table': 'course', 'businesskeyname': 'Cno', 'businesskeyrule': '', 'logicaldeletemark': '', 'field': [{'field_name': 'Cname', 'field_type': 'str', 'field_encrypt': False}, {'field_name': 'hours', 'field_type': 'str', 'field_encrypt': False}], 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False}, {'table': 'student', 'businesskeyname': 'Sno', 'businesskeyrule': '', 'logicaldeletemark': '', 'field': [{'field_name': 'Sname', 'field_type': 'str', 'field_encrypt': False}, {'field_name': 'sex', 'field_type': 'str', 'field_encrypt': False}, {'field_name': 'age', 'field_type': 'int', 'field_encrypt': False}, {'field_name': 'dept', 'field_type': 'str', 'field_encrypt': False}], 'businesskeyuneditable': True, 'businesskeytype': 'str', 'issave': False}, {'table': 'sc', 'businesskeyname': '', 'businesskeyrule': '', 'logicaldeletemark': '', 'field': [{'field_name': 'grade', 'field_type': 'int', 'field_encrypt': False}], 'businesskeyuneditable': True, 'businesskeytype': '', 'issave': False}]}, 'invalid': {'primary_key': [], 'keyword': []}}

    app = QApplication([])
    window = QMainWindow()
    config1 = table_ui(main_window=window, table_sql=table_sql)
    window.show()
    app.exec_()
