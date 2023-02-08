# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : window_table.py
# @ide    : PyCharm
# @time   : 2022-10-12 15:19:00
'''
this is function description
'''
# import module your need

from app.utils.checkSqlLink import SQLHandler

# 表配置页导入的包
from PySide6.QtWidgets import QPushButton, QWidget, QCheckBox, QVBoxLayout, QSizePolicy, QHBoxLayout, QComboBox, QLabel, \
    QListWidgetItem, QListWidget
from PySide6.QtCore import QSize, QRect
from functools import partial

from types import MethodType

def window_init_for_table(self):
    '''
    针对表配置页面，对窗口进行初始化，在程序启动时执行
    :param self:
    :return:
    '''
    # 测试
    self.add_table_list_item('test')


    # 添加表按钮等组件初始化
    self.add_table_button_group_init()
    self.table_number = -1
    self.add_table_button_group('table_select_all')

    # 加密组件初始化
    self.add_field_encrypt_group_init()

    # 初始化多线程信号与槽
    self.loadData.sig_load_view.connect(self.loadData.load_views)
    self.loadData.sig_load_view_comp.connect(self.load_view_comp)


def table_config_init(self):
    '''
    数据库表页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义，在进入当前页面前执行
    :return:
    '''

    # 变量初始化
    self.table_number = 0  # 记录拿到表的序号
    self.selected_table = {}  # 被选中的表缓存数据
    self.selected_field = None  # 被选中的用于主键的字段缓存
    self.businesskeyrule_to_rulename = [
        {
            'businesskeyrule': 'create_uid',
            'rulename': 'uuid生成'
        },
        {
            'businesskeyrule': 'create_hashlib_id',
            'rulename': 'hashlib+时间'
        },
        {
            'businesskeyrule': 'create_random_id',
            'rulename': '时间戳+N位随机数'
        },
        {
            'businesskeyrule': 'create_custom_id',
            'rulename': '用户自定义主键生成规则'
        }
    ]  # 生成方法绑定生成名
    self.typy_to_businesskeyrule = [
        {
            'field_type': 'int',
            'businesskeyrule_to_rulename': [
                {
                    'businesskeyrule': 'create_random_id',
                    'rulename': '时间戳+N位随机数'
                },
                {
                    'businesskeyrule': 'create_custom_id',
                    'rulename': '用户自定义主键生成规则'
                }
            ]
        },
        {
            'field_type': 'others',
            'businesskeyrule_to_rulename': [
                {
                    'businesskeyrule': 'create_uid',
                    'rulename': 'uuid生成'
                },
                {
                    'businesskeyrule': 'create_hashlib_id',
                    'rulename': 'hashlib+时间'
                },
                {
                    'businesskeyrule': 'create_random_id',
                    'rulename': '时间戳+N位随机数'
                },
                {
                    'businesskeyrule': 'create_custom_id',
                    'rulename': '用户自定义主键生成规则'
                }
            ]
        }
    ]  # field_type绑定生成方法
    self.encrypt_group_count = 0  # 字段加密组件总数
    self.encrypt_group_number = 0  # 字段加密组件当前组件编号
    self.field_encryptable = []  # 可加密的字段组成一个列表，目前字段类型为字符允许加密
    self.encrypt_type_list = ['rsa', 'aes']

    # 清空按钮并添加新按钮
    # del_table_button_list = self.ui.verticalLayoutWidget_add_table_button.findChildren(QPushButton)
    # for del_widget in del_table_button_list:
    #     table_name = del_widget.objectName().replace('pushButton_', '')
    #     if table_name != 'table_select_all':
    #         widget_del = self.ui.verticalLayoutWidget_add_table_button.findChild(QWidget, u"horizontalLayoutWidget_" + table_name)
    #         # 如果在没有event loop的thread使用, 那么thread结束后销毁对象。
    #         widget_del.deleteLater()

    self.table_number = 0

    # # 设置scrollAreaWidgetContents大小
    # self.ui.scrollAreaWidgetContents_left_6.setMinimumSize(QSize(0, 45 + self.table_number * 31))
    #
    # # 设置面板大小
    # self.ui.verticalLayoutWidget_add_table_button.setGeometry(QRect(0, 0, 281, 45 + self.table_number * 31))
    #
    # for table in self.sql_data['table']:
    #     self.add_table_button_group(table.get('table'))

    # test  添加list_items
    self.add_table_list()
    self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_table").itemClicked.connect(self.table_list_item_clicked)

    # 初始化全选按钮
    self.ui.centralwidget.findChild(QPushButton, u"pushButton_tsall").setText('全选')

    #  事件初始化
    # 全选CheckBox事件添加
    self.ui.centralwidget.findChild(QCheckBox, u"checkBox_tsall").clicked.connect(self.checkBox_all_select_clicked)

    # 添加字段组件组事件添加
    self.ui.pushButton_add_field_encrypt.clicked.connect(self.add_field_button_clicked)

    # 表对应的pushButton事件添加
    for pushButton in self.ui.listWidget_table.findChildren(QPushButton):
        pushButton.clicked.connect(partial(self.table_pushButton_clicked, pushButton.text()))


def table_config(self):
    '''
    数据库表配置页主要代码，点击下一步时调用
    :return:
    '''

    # 获取选中的表数据
    checkBox_list = self.ui.listWidget_table.findChildren(QCheckBox)
    for table in self.sql_data['table']:
        table['ischecked'] = False
    for checkBox in checkBox_list:
        table_name = checkBox.objectName().replace('checkBox_', '')
        if table_name != 'table_select_all':
            if checkBox.isChecked() == True:
                for table in self.sql_data['table']:
                    if table['table'] == table_name:
                        table['ischecked'] = True

    # 发送加载视图信号，通过多线程加载数据
    self.loadData.sig_load_view.emit()

    # 显示加载中弹窗
    self.dialog_fault.open()


def add_table_button_group_init(self):
    '''
    表格按钮初始化
    :return:
    '''

    # self.ui.verticalLayoutWidget_add_table_button = QWidget(self.ui.scrollAreaWidgetContents_left_6)
    #
    # self.ui.verticalLayoutWidget_add_table_button.setGeometry(QRect(0, 0, 281, 31))
    #
    # self.ui.add_table_button_encrypt_group_layout = QVBoxLayout(self.ui.verticalLayoutWidget_add_table_button)
    #
    # # 设置scrollAreaWidgetContents大小
    # self.ui.scrollAreaWidgetContents_left_6.setMinimumSize(QSize(0, 60))


def add_table_button_group(self, table_name):
    '''
    添加单个按钮组件组，用于表配置页面
    :param table_name: 表名
    :return:
    '''

    # self.ui.horizontalLayoutWidget1 = QWidget()
    # self.ui.horizontalLayoutWidget1.setObjectName(u"horizontalLayoutWidget_" + table_name)
    # self.ui.horizontalLayoutWidget1.setGeometry(QRect(0, 31 + self.table_number * 31, 281, 31))
    #
    # self.ui.horizontalLayout_1 = QHBoxLayout(self.ui.horizontalLayoutWidget1)
    # self.ui.horizontalLayout_1.setObjectName(u"horizontalLayout_" + table_name)
    # self.ui.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
    # self.ui.checkBox_1 = QCheckBox(self.ui.horizontalLayoutWidget_6)
    # self.ui.checkBox_1.setObjectName(u"checkBox_" + table_name)
    #
    # sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    # sizePolicy.setHorizontalStretch(0)
    # sizePolicy.setVerticalStretch(0)
    # sizePolicy.setHeightForWidth(self.ui.checkBox_1.sizePolicy().hasHeightForWidth())
    # self.ui.checkBox_1.setSizePolicy(sizePolicy)
    # self.ui.checkBox_1.setMinimumSize(QSize(0, 0))
    #
    # self.ui.horizontalLayout_1.addWidget(self.ui.checkBox_1)
    #
    # self.ui.pushButton_1 = QPushButton(self.ui.horizontalLayoutWidget_6)
    # self.ui.pushButton_1.setObjectName(u"pushButton_" + table_name)
    # self.ui.pushButton_1.setText(table_name)
    # sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    # sizePolicy1.setHorizontalStretch(0)
    # sizePolicy1.setVerticalStretch(0)
    # sizePolicy1.setHeightForWidth(self.ui.pushButton_1.sizePolicy().hasHeightForWidth())
    # self.ui.pushButton_1.setSizePolicy(sizePolicy1)
    #
    # self.ui.horizontalLayout_1.addWidget(self.ui.pushButton_1)
    #
    # # 把组件添加到面板
    # self.ui.add_table_button_encrypt_group_layout.addWidget(self.ui.horizontalLayoutWidget1)
    #
    # self.table_number += 1
    #
    # # 设置scrollAreaWidgetContents大小
    # self.ui.scrollAreaWidgetContents_left_6.setMinimumSize(QSize(0, 45 + self.table_number * 31))
    #
    # # 设置面板大小
    # self.ui.verticalLayoutWidget_add_table_button.setGeometry(QRect(0, 0, 281, 45 + self.table_number * 31))


def checkBox_all_select_clicked(self):
    '''
    全选checkBox点击调用
    :return:
    '''

    if self.ui.centralwidget.findChild(QCheckBox, u"checkBox_tsall").isChecked():
        for checkBox in self.ui.listWidget_table.findChildren(QCheckBox):
            checkBox.setChecked(True)

    else:
        for checkBox in self.ui.listWidget_table.findChildren(QCheckBox):
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

        # 清空数据缓存
        self.field_encryptable = []

        # 清除事件
        self.ui.comboBox_select_table_businesskeyname.currentIndexChanged.connect(
            partial(self.comboBob_businesskeyname_currentIndexChanged))
        self.ui.comboBox_select_table_businesskeyname.currentIndexChanged.disconnect()

        self.ui.comboBox_select_table_logicaldeletemark.currentIndexChanged.connect(
            partial(self.comboBob_logicaldeletemark_currentIndexChanged))
        self.ui.comboBox_select_table_logicaldeletemark.currentIndexChanged.disconnect()

        # 清空配置框
        self.ui.comboBox_select_table_logicaldeletemark.clear()
        self.ui.comboBox_select_table_businesskeyname.clear()
        self.ui.comboBox_select_table_logicaldeletemark.addItem('选择逻辑删除标识字段')
        self.ui.comboBox_select_table_businesskeyname.addItem('选择业务主键')

        # 加载数据到配置框

        for table in self.sql_data['table']:
            if table['table'] == button_text:
                self.selected_table = table

        self.ui.label_table_name_7.setText(button_text)  # 这里必须调用setText方法，直接对text赋值没用
        for field in self.selected_table['field']:
            if field['field_type'] == 'int':
                self.ui.comboBox_select_table_logicaldeletemark.addItem(field['field_name'])
            self.ui.comboBox_select_table_businesskeyname.addItem(field['field_name'])

            if field['field_type'] == 'str':
                self.field_encryptable.append(field)

        # 事件添加（逻辑删除字段修改，主键修改）
        self.ui.comboBox_select_table_logicaldeletemark.currentIndexChanged.connect(
            partial(self.comboBob_logicaldeletemark_currentIndexChanged))

        self.ui.comboBox_select_table_businesskeyname.currentIndexChanged.connect(partial(
            self.comboBob_businesskeyname_currentIndexChanged))  # 这里的currentIndexChanged.connect会自动传入一个参数index

        # 初始化主键配置组件内容

        # 初始化逻辑删除字段
        for i in range(self.ui.comboBox_select_table_logicaldeletemark.count()):
            if self.ui.comboBox_select_table_logicaldeletemark.itemText(i) == self.selected_table['logicaldeletemark']:
                self.ui.comboBox_select_table_logicaldeletemark.setCurrentIndex(i)

        # 初始化主键字段
        for i in range(self.ui.comboBox_select_table_businesskeyname.count()):
            if self.ui.comboBox_select_table_businesskeyname.itemText(i) == self.selected_table['businesskeyname']:
                self.ui.comboBox_select_table_businesskeyname.setCurrentIndex(i)
        self.comboBob_businesskeyname_currentIndexChanged()

        # 根据field_type拿到相应的主键生成规则
        if self.selected_field == None:
            self.businesskeyrule_to_rulename = []
        else:
            for businesskeyrule_to_rulename in self.typy_to_businesskeyrule:
                if businesskeyrule_to_rulename['field_type'] == 'others':
                    self.businesskeyrule_to_rulename = businesskeyrule_to_rulename['businesskeyrule_to_rulename']
            for businesskeyrule_to_rulename in self.typy_to_businesskeyrule:
                if businesskeyrule_to_rulename['field_type'] == self.selected_field['field_type']:
                    self.businesskeyrule_to_rulename = businesskeyrule_to_rulename['businesskeyrule_to_rulename']

        # 根据生成规则字典和sql_data设置生成方式
        for i in range(self.ui.comboBox_select_table_businesskeyrule.count()):
            for rule in self.businesskeyrule_to_rulename:
                if rule['rulename'] == self.ui.comboBox_select_table_businesskeyrule.itemText(i):
                    if self.selected_table['businesskeyrule'] == rule['businesskeyrule']:
                        self.ui.comboBox_select_table_businesskeyrule.setCurrentIndex(i)

        # 初始化加密组件

        # 删除加密组件
        del_encrypt_list = self.ui.centralwidget.findChildren(QPushButton)
        del_encrypt_list1 = []
        for del_encrypt in del_encrypt_list:
            if 'pushButton_delete_field_encrypt_add' in del_encrypt.objectName():
                del_encrypt_list1.append(del_encrypt)
        del_encrypt_list = del_encrypt_list1

        for del_encrypt in del_encrypt_list:
            index = del_encrypt.objectName().replace('pushButton_delete_field_encrypt_add', '')
            widget_del = self.ui.centralwidget.findChild(QHBoxLayout, u"horizontalLayout_add" + index)
            # 如果在没有event loop的thread使用, 那么thread结束后销毁对象。
            while widget_del.count():
                item = widget_del.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
            widget_del.deleteLater()

        self.encrypt_group_count = 0
        self.ui.listWidget_encrypt.clear()

        # 按照后台数据添加组件到加密字段组件列表
        for field in self.field_encryptable:
            if field['field_encrypt'] == True:
                self.add_field_button_clicked()
                name_comboBox = self.ui.centralwidget.findChild(QComboBox, u"comboBox_select_table_field_encrypt_add" + str(self.encrypt_group_number - 1))
                name_comboBox.currentIndexChanged.connect(partial(self.comboBox_field_update))
                name_comboBox.currentIndexChanged.disconnect()
                name_comboBox.addItem(field['field_name'])
                for i in range(name_comboBox.count()):
                    if name_comboBox.itemText(i) == field['field_name']:
                        name_comboBox.setCurrentIndex(i)

                encrypt_comboBox = self.ui.centralwidget.findChild(QComboBox,
                                                                           u"comboBox_select_table_encrypt_type_add" + str(
                                                                               self.encrypt_group_number - 1))
                encrypt_comboBox.currentIndexChanged.connect(partial(self.comboBox_field_update))
                encrypt_comboBox.currentIndexChanged.disconnect()
                for i in range(encrypt_comboBox.count()):
                    if encrypt_comboBox.itemText(i) == field['encrypt_type']:
                        encrypt_comboBox.setCurrentIndex(i)

                name_comboBox.currentIndexChanged.connect(partial(self.comboBox_field_update))
                encrypt_comboBox.currentIndexChanged.connect(partial(self.comboBox_field_update))

        self.comboBox_field_update()


def comboBob_logicaldeletemark_currentIndexChanged(self, comboBox_index = -1):
    if self.ui.comboBox_select_table_logicaldeletemark.currentText() == '选择逻辑删除标识字段':
        self.selected_table['logicaldeletemark'] = ''
    else:
        self.selected_table['logicaldeletemark'] = self.ui.comboBox_select_table_logicaldeletemark.currentText()


def comboBob_businesskeyname_currentIndexChanged(self, comboBox_index = -1):
    '''
    comboBox的item改变事件，目前为self.ui.comboBox_select_table_businesskeyname专属
    :param comboBox_index: 被选择的item索引
    :return:
    '''

    # 清空上次操作的缓存数据
    self.selected_field = None

    # 取到别选中的字段，并赋值给sql_data['table'][n]['businesskeyname']
    businesskeyname = self.ui.comboBox_select_table_businesskeyname.currentText()
    if businesskeyname == '选择业务主键':
        businesskeyname = ''
        self.selected_table['businesskeyrule'] = ''
    for field in self.selected_table['field']:
        if field['field_name'] == businesskeyname:
            self.selected_field = field
    self.selected_table['businesskeyname'] = businesskeyname

    # 根据field_type拿到相应的主键生成规则
    if self.selected_field == None:
        self.businesskeyrule_to_rulename = []
    else:
        for businesskeyrule_to_rulename in self.typy_to_businesskeyrule:
            if businesskeyrule_to_rulename['field_type'] == 'others':
                self.businesskeyrule_to_rulename = businesskeyrule_to_rulename['businesskeyrule_to_rulename']
        for businesskeyrule_to_rulename in self.typy_to_businesskeyrule:
            if businesskeyrule_to_rulename['field_type'] == self.selected_field['field_type']:
                self.businesskeyrule_to_rulename = businesskeyrule_to_rulename['businesskeyrule_to_rulename']

    # 更新选择业务主键生成规则comboBox
    self.ui.comboBox_select_table_businesskeyrule.currentIndexChanged.connect(
        partial(self.comboBob_businesskeyrule_currentIndexChanged))
    self.ui.comboBox_select_table_businesskeyrule.currentIndexChanged.disconnect()
    self.ui.comboBox_select_table_businesskeyrule.clear()
    self.ui.comboBox_select_table_businesskeyrule.addItem('选择业务主键生成规则')
    for rule in self.businesskeyrule_to_rulename:
        self.ui.comboBox_select_table_businesskeyrule.addItem(rule['rulename'])

    #  绑定业务主键生成规则comboBox改变事件
    # self.ui.disconnect(self.ui.comboBox_select_table_businesskeyrule)  # 注销事件
    self.ui.comboBox_select_table_businesskeyrule.currentIndexChanged.connect(
        partial(self.comboBob_businesskeyrule_currentIndexChanged))  # 这里的currentIndexChanged.connect会自动传入一个参数index


def comboBob_businesskeyrule_currentIndexChanged(self, comboBox_index):
    '''
    comboBox的item改变事件，目前为self.ui.comboBox_select_table_businesskeyrule专属
    :param comboBox_index:
    :return:
    '''

    rulename = self.ui.comboBox_select_table_businesskeyrule.currentText()
    if rulename == '选择业务主键生成规则':
        rulename = ''
        self.selected_table['businesskeyrule'] = ''

    for rule in self.businesskeyrule_to_rulename:
        if rule['rulename'] == rulename:
            self.selected_table['businesskeyrule'] = rule['businesskeyrule']


def add_field_button_clicked(self):
    '''
    添加加密字段按钮点击事件
    :return:
    '''

    # 添加一个选择加密字段组
    self.add_field_encrypt_group()


    # 绑定事件,初始化数据
    button_delete = self.ui.listWidget_encrypt.findChild(QWidget, u"pushButton_delete_field_encrypt_add" + str(self.encrypt_group_number - 1))
    button_delete.clicked.connect(partial(self.del_field_encrypt_group, button_delete))

    comboBox_field = self.ui.listWidget_encrypt.findChild(QComboBox,
                                                                u"comboBox_select_table_field_encrypt_add" + str(
                                                                    self.encrypt_group_number - 1))
    for field in self.field_encryptable:
        if field['field_encrypt'] == False:
            comboBox_field.addItem(field['field_name'])
    comboBox_field.currentIndexChanged.connect(partial(self.comboBox_field_update))

    comboBox_encrypt_type = self.ui.listWidget_encrypt.findChild(QComboBox,
                                                                u"comboBox_select_table_encrypt_type_add" + str(
                                                                    self.encrypt_group_number - 1))
    for encrypt_type in self.encrypt_type_list:
        comboBox_encrypt_type.addItem(encrypt_type)
    comboBox_encrypt_type.currentIndexChanged.connect(partial(self.comboBox_field_update))

    # 更新加密组件，这里可以不更新
    # self.comboBox_field_update()


def add_field_encrypt_group(self):
    '''
    添加加密字段配置组件
    :param
    :return:
    '''

    table_item = QListWidgetItem()
    table_item.setText("encrypt_itme_" + str(self.encrypt_group_number))
    self.ui.listWidget_encrypt.addItem(table_item)
    # self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_table").setItemWidget(table_item, table_checkBox)

    self.ui.encrypt_widget = QWidget()
    self.ui.encrypt_widget.setObjectName(u"horizontalLayoutWidget_" + str(self.encrypt_group_number))


    # 更新verticalLayoutWidget_add大小
    # self.ui.verticalLayoutWidget_add.setGeometry(QRect(20, 320, 497, 41 * (self.encrypt_group_count + 1)))
    #
    # self.ui.scrollAreaWidgetContents_right_7.setMinimumSize(QSize(0, 400 + 41 * self.encrypt_group_count))

    self.ui.horizontalLayout_add = QHBoxLayout(self.ui.encrypt_widget)
    self.ui.horizontalLayout_add.setObjectName(u"horizontalLayout_add" + str(self.encrypt_group_number))
    self.ui.horizontalLayout_add.setContentsMargins(0, 0, 0, 0)

    self.ui.label_add = QLabel(self.ui.verticalLayoutWidget_add)
    self.ui.label_add.setObjectName(u"label_field_add" + str(self.encrypt_group_number))
    self.ui.label_add.setText('字段选择')

    self.ui.horizontalLayout_add.addWidget(self.ui.label_add)

    self.ui.comboBox_select_table_field_encrypt_add = QComboBox(self.ui.verticalLayoutWidget_add)
    self.ui.comboBox_select_table_field_encrypt_add.addItem("选择需要加密的字段")
    self.ui.comboBox_select_table_field_encrypt_add.setObjectName(u"comboBox_select_table_field_encrypt_add" + str(self.encrypt_group_number))
    self.ui.comboBox_select_table_field_encrypt_add.setMinimumSize(QSize(150, 0))

    self.ui.horizontalLayout_add.addWidget(self.ui.comboBox_select_table_field_encrypt_add)

    self.ui.label_add = QLabel(self.ui.verticalLayoutWidget_add)
    self.ui.label_add.setObjectName(u"label_encrypt_add" + str(self.encrypt_group_number))
    self.ui.label_add.setText('加密方式')

    self.ui.horizontalLayout_add.addWidget(self.ui.label_add)

    self.ui.comboBox_select_table_encrypt_type_add = QComboBox(self.ui.verticalLayoutWidget_add)
    # self.ui.comboBox_select_table_encrypt_type_add.addItem("选择加密方式")
    self.ui.comboBox_select_table_encrypt_type_add.setObjectName(u"comboBox_select_table_encrypt_type_add" + str(self.encrypt_group_number))
    self.ui.comboBox_select_table_encrypt_type_add.setMinimumSize(QSize(150, 0))

    self.ui.horizontalLayout_add.addWidget(self.ui.comboBox_select_table_encrypt_type_add)

    self.ui.pushButton_delete_field_encrypt_add = QPushButton(self.ui.verticalLayoutWidget_add)
    self.ui.pushButton_delete_field_encrypt_add.setObjectName(u"pushButton_delete_field_encrypt_add" + str(self.encrypt_group_number))
    self.ui.pushButton_delete_field_encrypt_add.setText('删除')

    self.ui.horizontalLayout_add.addWidget(self.ui.pushButton_delete_field_encrypt_add)

    self.encrypt_group_count += 1
    self.encrypt_group_number += 1

    # self.ui.add_encrypt_group_layout.addLayout(self.ui.horizontalLayout_add)
    self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_encrypt").setItemWidget(table_item,
                                                                                   self.ui.encrypt_widget)



def add_field_encrypt_group_init(self):
    '''
    加密字段组件面板初始化，（这里是由于添加组件时遇到无法显示bug不得已而使用）
    :return:
    '''

    self.ui.verticalLayoutWidget_add = QWidget(self.ui.scrollAreaWidgetContents_right_7)
    # self.ui.verticalLayoutWidget_add.setGeometry(QRect(20, 320 + 41 * self.encrypt_group_number, 497, 41))

    # self.ui.verticalLayoutWidget_add.setGeometry(QRect(20, 320, 497, 41))

    self.ui.add_encrypt_group_layout = QVBoxLayout(self.ui.verticalLayoutWidget_add)


def del_field_encrypt_group(self, Qobject):
    '''
    删除一个加密组
    :param Qobject: 加密组件
    :return:
    '''

    index = int(Qobject.objectName().replace('pushButton_delete_field_encrypt_add', ''))

    # 删除加密组
    widget_del = self.ui.listWidget_encrypt.findChild(QHBoxLayout, u"horizontalLayout_add" + str(index))

    # ”deleteLater()“依赖于Qt的event loop机制。
    # 如果在event loop启用前被调用, 那么event loop启用后对象才会被销毁;
    # 如果在event loop结束后被调用, 那么对象不会被销毁;
    # 如果在没有event loop的thread使用, 那么thread结束后销毁对象。
    while widget_del.count():
        item = widget_del.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.deleteLater()
    widget_del.deleteLater()

    # 更新verticalLayoutWidget_add大小
    # self.ui.verticalLayoutWidget_add.setGeometry(QRect(20, 320, 497, 41 * (self.encrypt_group_count + 1)))
    #
    # self.ui.scrollAreaWidgetContents_right_7.setMinimumSize(QSize(0, 400 + 41 * self.encrypt_group_count))

    # 删除item
    d_item = self.ui.listWidget_encrypt.item(index)
    for i in range(self.encrypt_group_count):
        if self.ui.listWidget_encrypt.item(i).text() == "encrypt_itme_" + str(index):
            d_item = self.ui.listWidget_encrypt.takeItem(i)
            break

    self.ui.listWidget_encrypt.removeItemWidget(d_item)
    del d_item

    # 更新加密组件
    self.comboBox_field_update(layout_index=int(index))

    # 更新总组件数量
    self.encrypt_group_count -= 1


def comboBox_field_update(self, comboBox_item_index = 0, layout_index = -1):
    '''
    更新已有comboBox组件,同步组件数据与后台数据
    :return:
    '''

    # 重置加密字段
    for field in self.field_encryptable:
        field['field_encrypt'] = False

    QComboBox_list = self.ui.centralwidget.findChildren(QComboBox)
    QComboBox_list1 = []
    for combobox in QComboBox_list:
        if 'comboBox_select_table_field_encrypt_add' in combobox.objectName():
            QComboBox_list1.append(combobox)
    QComboBox_list = QComboBox_list1


    # 更新加密字段
    comboBox_index = 0
    for comboBox in QComboBox_list:
        comboBox_index += 1
        # if comboBox_index % 2 != 0:
        if True:

            # 排除待删除的组件造成的影响
            if layout_index != -1 and layout_index == int(
                    comboBox.objectName().replace('comboBox_select_table_field_encrypt_add', '')):
                continue
            if comboBox.currentText() != '选择需要加密的字段':
                for field in self.field_encryptable:
                    if comboBox.currentText() == field['field_name']:
                        field['field_encrypt'] = True
                        field['encrypt_type'] = comboBox.currentText()

    comboBox_index = 0
    for comboBox in QComboBox_list:
        comboBox_index += 1
        if comboBox_index % 2 != 0:

            # 清除事件，避免循环
            comboBox.currentIndexChanged.disconnect()

            text = comboBox.currentText()

            # 更新comboBox
            comboBox.clear()
            if text != '选择需要加密的字段':
                comboBox.addItem('选择需要加密的字段')
            comboBox.addItem(text)
            for field in self.field_encryptable:
                if field['field_encrypt'] == False:
                    comboBox.addItem(field['field_name'])
            if comboBox.itemText(1) == text:
                comboBox.setCurrentIndex(1)

            # 重新绑定事件
            comboBox.currentIndexChanged.connect(partial(self.comboBox_field_update))


def add_table_list_item(self,table_name):
    table_item = QListWidgetItem()
    table_item.setSizeHint(QSize(0, 40))
    table_item.setText(table_name)
    table_checkBox = QCheckBox()
    table_checkBox.setText(table_name)
    self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_table").addItem(table_item)
    # self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_table").setItemWidget(table_item, table_checkBox)

    self.ui.horizontalLayoutWidget1 = QWidget()
    self.ui.horizontalLayoutWidget1.setObjectName(u"horizontalLayoutWidget_" + table_name)

    self.ui.horizontalLayout_1 = QHBoxLayout(self.ui.horizontalLayoutWidget1)
    self.ui.horizontalLayout_1.setObjectName(u"horizontalLayout_" + table_name)
    self.ui.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
    self.ui.checkBox_1 = QCheckBox()
    self.ui.checkBox_1.setObjectName(u"checkBox_" + table_name)

    sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.ui.checkBox_1.sizePolicy().hasHeightForWidth())
    self.ui.checkBox_1.setSizePolicy(sizePolicy)
    self.ui.checkBox_1.setMinimumSize(QSize(0, 0))

    self.ui.horizontalLayout_1.addWidget(self.ui.checkBox_1)

    self.ui.pushButton_1 = QPushButton()
    self.ui.pushButton_1.setObjectName(u"pushButton_" + table_name)
    self.ui.pushButton_1.setText(table_name)
    sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    sizePolicy1.setHorizontalStretch(0)
    sizePolicy1.setVerticalStretch(0)
    sizePolicy1.setHeightForWidth(self.ui.pushButton_1.sizePolicy().hasHeightForWidth())
    self.ui.pushButton_1.setSizePolicy(sizePolicy1)

    self.ui.horizontalLayout_1.addWidget(self.ui.pushButton_1)

    # 把组件添加到面板

    self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_table").setItemWidget(table_item, self.ui.horizontalLayoutWidget1)


def add_table_list(self):
    self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_table").clear()
    self.add_table_list_item("tsall")
    for table in self.sql_data['table']:
        self.add_table_list_item(table.get('table'))


def table_list_item_clicked(self, item):
    '''
    表配置页listWidgetItem点击事件函数
    :param item: 被点击的listWidgetItem
    :return:
    '''

    # 调用按钮点击方法，使得点击不同的位置效果相同
    table_pushButton_clicked(self, self.ui.centralwidget.findChild(QPushButton, 'pushButton_' + item.text()).text())



# 数据处理结束
def load_view_comp(self, view_info):
    self.sql_data['view'] = view_info['data']['view']
    self.next_step()
    self.dialog_fault.close()


# 将函数添加到对象中
def add_func(self):
    '''
    添加该.py文件的方法到对象中
    :param self: 添加函数的对象
    :return:
    '''
    self.window_init_for_table = MethodType(window_init_for_table, self)
    self.table_config_init = MethodType(table_config_init, self)
    self.table_config = MethodType(table_config, self)
    self.add_table_button_group_init = MethodType(add_table_button_group_init, self)
    self.add_table_button_group = MethodType(add_table_button_group, self)
    self.checkBox_all_select_clicked = MethodType(checkBox_all_select_clicked, self)
    self.table_pushButton_clicked = MethodType(table_pushButton_clicked, self)
    self.comboBob_logicaldeletemark_currentIndexChanged = MethodType(comboBob_logicaldeletemark_currentIndexChanged, self)
    self.comboBob_businesskeyname_currentIndexChanged = MethodType(comboBob_businesskeyname_currentIndexChanged, self)
    self.comboBob_businesskeyrule_currentIndexChanged = MethodType(comboBob_businesskeyrule_currentIndexChanged, self)
    self.add_field_button_clicked = MethodType(add_field_button_clicked, self)
    self.add_field_encrypt_group = MethodType(add_field_encrypt_group, self)
    self.add_field_encrypt_group_init = MethodType(add_field_encrypt_group_init, self)
    self.del_field_encrypt_group = MethodType(del_field_encrypt_group, self)
    self.comboBox_field_update = MethodType(comboBox_field_update, self)
    self.load_view_comp = MethodType(load_view_comp, self)

    # test
    self.add_table_list_item = MethodType(add_table_list_item, self)
    self.add_table_list = MethodType(add_table_list, self)
    self.table_list_item_clicked = MethodType(table_list_item_clicked, self)