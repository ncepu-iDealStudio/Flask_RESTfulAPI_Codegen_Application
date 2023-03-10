# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : page_table.py
# @ide    : PyCharm
# @time   : 2022-10-12 15:19:00
'''
表配置页面主要操作
'''
from PySide6.QtWidgets import QPushButton, QWidget, QCheckBox, QSizePolicy, QHBoxLayout, QComboBox, QLabel, \
    QListWidgetItem, QListWidget
from PySide6.QtCore import QSize
from functools import partial
from app.modules.windows import MainWindow


class PageTable(MainWindow):

    def __init__(self, mainWindow):
        MainWindow.__init__(self)
        # 加载主窗口mainWindow的部分成员
        self.dialog_loading = mainWindow.dialog_loading
        self.ui = mainWindow.ui
        self.dataProcessing = mainWindow.dataProcessing
        self.sql_data = mainWindow.sql_data
        self.next_step = mainWindow.next_step
        self.db_changed = mainWindow.db_changed

        # 初始化多线程信号与槽
        self.dataProcessing.sig_load_view.connect(self.dataProcessing.load_views)
        self.dataProcessing.sig_load_view_comp.connect(self.load_view_comp)

    def refresh_table_page(self):
        '''
        表配置页面刷新
        :return:
        '''
        # 如果数据库没有改变，不刷新页面
        if self.db_changed.get('table_is_config'):
            return
        self.db_changed['table_is_config'] = True

        # 进页面前调整控件初始状态
        self.ui.stackedWidget_right.setCurrentIndex(0)

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
        self.encrypt_type_list = ['rsa', 'aes']  # 加密方式
        self.table_selected_itme = None  # 数据库表被选中的item

        # 此处存在第二次加载时上一个组件没有销毁，同时存在多个同名组件的问题，最终会导致多选按钮的点击事件无效
        # 先通过改变组件名解决问题
        if self.ui.centralwidget.findChild(QCheckBox, u"checkBox_tsall"):
            self.ui.centralwidget.findChild(QCheckBox, u"checkBox_tsall").setObjectName(u"checkBox_tsall1")

        # 添加list_items
        self.refresh_table_list()
        self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_table").itemClicked.connect(
            self.table_list_item_clicked)

        # 全选CheckBox事件添加
        self.ui.centralwidget.findChild(QCheckBox, u"checkBox_tsall").clicked.connect(self.checkBox_all_select_clicked)

        # 其他CheckBox事件添加
        for checkbox in self.ui.listWidget_table.findChildren(QCheckBox):
            checkbox.stateChanged.connect(partial(self.table_checkBox_clicked, checkbox))

        # 添加字段组件组事件添加
        self.ui.pushButton_add_field_encrypt.clicked.connect(self.add_field_button_clicked)
        self.ui.pushButton_add_field_encrypt.clicked.disconnect()
        self.ui.pushButton_add_field_encrypt.clicked.connect(self.add_field_button_clicked)

        # 表对应的pushButton事件添加
        for pushButton in self.ui.listWidget_table.findChildren(QPushButton):
            pushButton.clicked.connect(partial(self.table_pushButton_clicked, pushButton.text()))
            pushButton.clicked.disconnect()
            pushButton.clicked.connect(partial(self.table_pushButton_clicked, pushButton.text()))

    def set_table_config(self):
        '''
        配置数据库表完成
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

        if not self.db_changed.get('view_is_config'):
            # 发送加载视图信号，通过多线程加载数据
            self.dataProcessing.sig_load_view.emit()

            # 显示加载中弹窗
            self.dialog_loading.open()
        else:
            self.next_step()

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

    def table_checkBox_clicked(self, checkbox, index=-1):
        '''
        视图选择框里的checkbox事件注册
        :param checkbox: 复选框
        :return:
        '''

        # # 点击checkbox时同时调用点击PushButton事件
        # self.table_pushButton_clicked(checkbox.objectName().replace('checkBox_', ''))

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

            # 设置数据库表列表选中样式
            if self.table_selected_itme:
                self.table_selected_itme.setStyleSheet(
                    'background-color: rgb(255, 255, 255); border: 0px solid rgb(255, 255, 255);')
            self.table_selected_itme = self.ui.centralwidget.findChild(QWidget,
                                                                       u"horizontalLayoutWidget_" + button_text)
            self.table_selected_itme.setStyleSheet('')

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
                if self.ui.comboBox_select_table_logicaldeletemark.itemText(i) == self.selected_table[
                    'logicaldeletemark']:
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
                    name_comboBox = self.ui.centralwidget.findChild(QComboBox,
                                                                    u"comboBox_select_table_field_encrypt_add" + str(
                                                                        self.encrypt_group_number - 1))
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

    def comboBob_logicaldeletemark_currentIndexChanged(self, comboBox_index=-1):
        if self.ui.comboBox_select_table_logicaldeletemark.currentText() == '选择逻辑删除标识字段':
            self.selected_table['logicaldeletemark'] = ''
        else:
            self.selected_table['logicaldeletemark'] = self.ui.comboBox_select_table_logicaldeletemark.currentText()

    def comboBob_businesskeyname_currentIndexChanged(self, comboBox_index=-1):
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

        # 添加一个空白的选择加密字段组
        encrypy_widget = self.add_field_encrypt_group()

        # 绑定事件
        button_delete = encrypy_widget.findChildren(QPushButton)[0]
        button_delete.clicked.connect(partial(self.del_field_encrypt_group, button_delete))

        # 根据field_encryptable添加没有设置加密的字段到comboBox
        comboBox_field = encrypy_widget.findChildren(QComboBox)[0]
        for field in self.field_encryptable:
            if field['field_encrypt'] == False:
                comboBox_field.addItem(field['field_name'])
        comboBox_field.currentIndexChanged.connect(partial(self.comboBox_field_update))

        # 根据encrypt_type_list添加加密方法到comboBox
        comboBox_encrypt_type = encrypy_widget.findChildren(QComboBox)[1]
        for encrypt_type in self.encrypt_type_list:
            comboBox_encrypt_type.addItem(encrypt_type)
        comboBox_encrypt_type.currentIndexChanged.connect(partial(self.comboBox_field_update))

    def add_field_encrypt_group(self):
        '''
        添加加密字段配置组件,在QListWidgetItem中添加一个item然后使用自定义的加密组替换
        :param
        :return:
        '''

        table_item = QListWidgetItem()
        table_item.setSizeHint(QSize(0, 40))
        table_item.setText("encrypt_itme_" + str(self.encrypt_group_number))
        self.ui.listWidget_encrypt.addItem(table_item)

        self.ui.encrypt_widget = QWidget()
        self.ui.encrypt_widget.setObjectName(u"horizontalLayoutWidget_" + str(self.encrypt_group_number))

        self.ui.horizontalLayout_add = QHBoxLayout(self.ui.encrypt_widget)
        self.ui.horizontalLayout_add.setObjectName(u"horizontalLayout_add" + str(self.encrypt_group_number))
        self.ui.horizontalLayout_add.setContentsMargins(0, 0, 0, 0)

        self.ui.label_add = QLabel(self.ui.listWidget_encrypt)
        self.ui.label_add.setObjectName(u"label_field_add" + str(self.encrypt_group_number))
        self.ui.label_add.setText('字段选择')

        self.ui.horizontalLayout_add.addWidget(self.ui.label_add)

        self.ui.comboBox_select_table_field_encrypt_add = QComboBox(self.ui.listWidget_encrypt)
        self.ui.comboBox_select_table_field_encrypt_add.addItem("选择需要加密的字段")
        self.ui.comboBox_select_table_field_encrypt_add.setObjectName(
            u"comboBox_select_table_field_encrypt_add" + str(self.encrypt_group_number))
        self.ui.comboBox_select_table_field_encrypt_add.setMinimumSize(QSize(150, 0))

        self.ui.horizontalLayout_add.addWidget(self.ui.comboBox_select_table_field_encrypt_add)

        self.ui.label_add = QLabel(self.ui.listWidget_encrypt)
        self.ui.label_add.setObjectName(u"label_encrypt_add" + str(self.encrypt_group_number))
        self.ui.label_add.setText('加密方式')

        self.ui.horizontalLayout_add.addWidget(self.ui.label_add)

        self.ui.comboBox_select_table_encrypt_type_add = QComboBox(self.ui.listWidget_encrypt)
        # self.ui.comboBox_select_table_encrypt_type_add.addItem("选择加密方式")
        self.ui.comboBox_select_table_encrypt_type_add.setObjectName(
            u"comboBox_select_table_encrypt_type_add" + str(self.encrypt_group_number))
        self.ui.comboBox_select_table_encrypt_type_add.setMinimumSize(QSize(150, 0))

        self.ui.horizontalLayout_add.addWidget(self.ui.comboBox_select_table_encrypt_type_add)

        self.ui.pushButton_delete_field_encrypt_add = QPushButton(self.ui.listWidget_encrypt)
        self.ui.pushButton_delete_field_encrypt_add.setObjectName(
            u"pushButton_delete_field_encrypt_add" + str(self.encrypt_group_number))
        self.ui.pushButton_delete_field_encrypt_add.setText('删除')

        self.ui.horizontalLayout_add.addWidget(self.ui.pushButton_delete_field_encrypt_add)

        self.encrypt_group_count += 1
        self.encrypt_group_number += 1

        # 将整个按钮组添加到listWidget_encrypt
        self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_encrypt").setItemWidget(table_item,
                                                                                         self.ui.encrypt_widget)
        return self.ui.encrypt_widget

    def del_field_encrypt_group(self, Qobject):
        '''
        删除一个加密组
        :param Qobject: 加密组件
        :return:
        '''

        index = int(Qobject.objectName().replace('pushButton_delete_field_encrypt_add', ''))

        # 删除加密组
        widget_del = self.ui.listWidget_encrypt.findChild(QHBoxLayout, u"horizontalLayout_add" + str(index))
        while widget_del.count():
            item = widget_del.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        widget_del.deleteLater()

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

    def comboBox_field_update(self, comboBox_item_index=0, layout_index=-1):
        '''
        更新已有comboBox组件,同步组件数据与后台数据,避免选中相同的字段进行加密
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

        # comboBox数据同步到后台数据
        comboBox_index = 0
        for comboBox in QComboBox_list:
            comboBox_index += 1

            # 排除待删除的组件造成的影响
            if layout_index != -1 and layout_index == int(
                    comboBox.objectName().replace('comboBox_select_table_field_encrypt_add', '')):
                continue
            if comboBox.currentText() != '选择需要加密的字段':
                for field in self.field_encryptable:
                    if comboBox.currentText() == field['field_name']:
                        field['field_encrypt'] = True
                        field['encrypt_type'] = comboBox.currentText()

        # 根据后台数据加载加密数据
        comboBox_index = 0
        for comboBox in QComboBox_list:
            comboBox_index += 1

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

    def add_table_list_item(self, table_name):
        '''
        添加table_list的一个item,在QListWidgetItem中添加一个item然后使用自定义的加密组替换
        :param table_name:
        :return:
        '''
        table_item = QListWidgetItem()
        table_item.setSizeHint(QSize(0, 40))

        table_item.setText(table_name)
        table_checkBox = QCheckBox()
        table_checkBox.setText(table_name)
        self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_table").addItem(table_item)

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
        if table_name == 'tsall':
            self.ui.pushButton_1.setText('全选')

        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ui.pushButton_1.sizePolicy().hasHeightForWidth())
        self.ui.pushButton_1.setSizePolicy(sizePolicy1)

        self.ui.horizontalLayout_1.addWidget(self.ui.pushButton_1)

        # 设置间距
        self.ui.horizontalLayout_1.setContentsMargins(10, 0, 0, 0)
        self.ui.horizontalLayout_1.setSpacing(15)

        # 把item替换为自定义的组件组
        self.ui.scrollArea_2.findChild(QListWidget, u"listWidget_table").setItemWidget(table_item,
                                                                                       self.ui.horizontalLayoutWidget1)

    def refresh_table_list(self):
        '''
        刷新数据库表列表
        :param self:
        :return:
        '''
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
        text = self.ui.centralwidget.findChild(QPushButton, 'pushButton_' + item.text()).text()
        self.table_pushButton_clicked(text)

    def load_view_comp(self, view_info):
        '''
        加载视图数据完成
        :param self:
        :param view_info:
        :return:
        '''
        self.sql_data['view'] = view_info['data']['view']
        self.next_step()
        self.dialog_loading.close()
