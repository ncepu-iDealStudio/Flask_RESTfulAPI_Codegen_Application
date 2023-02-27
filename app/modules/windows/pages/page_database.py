# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : page_database.py
# @ide    : PyCharm
# @time   : 2022-10-12 16:13:18
'''
数据库配置页面主要操作
'''
import configparser
import os
from PySide6.QtWidgets import QMessageBox
import config.setting
from utils.checkSqlLink import SQLHandler
from app.modules.windows import MainWindow


class PageDatabase(MainWindow):
    '''
    数据库配置页
    '''
    def __init__(self, mainWindow):
        '''
        页面初始化
        :param mainWindow:
        '''
        MainWindow.__init__(self)
        self.dialog_loading = mainWindow.dialog_loading
        self.ui = mainWindow.ui
        self.dataProcessing = mainWindow.dataProcessing
        self.sql_data = mainWindow.sql_data
        self.next_step = mainWindow.next_step
        self.id = mainWindow.id

    def refresh_db_page(self):
        '''
        刷新页面
        :return:
        '''
        self.ui.button_get_db_names.clicked.connect(self.get_dbname)

        # 初始化多线程信号与槽
        self.dataProcessing.sig_load_table.connect(self.dataProcessing.load_tables)
        self.dataProcessing.sig_load_table_comp.connect(self.load_table_comp)
        self.dataProcessing.sig_load_dbname.connect(self.dataProcessing.load_dbname)
        self.dataProcessing.sig_load_dbname_comp.connect(self.load_dbname_comp)

        # 加载用户上一次使用的配置
        user_configfile = "config/user_config.conf"
        if os.path.isfile(user_configfile):
            user_conf = configparser.ConfigParser()  # 实例类
            user_conf.read(user_configfile, encoding='UTF-8')  # 读取配置文件
            if user_conf.has_section('DATABASE'):
                self.ui.text_host.setText(user_conf['DATABASE']['host'])
                self.ui.text_port.setText(user_conf['DATABASE']['port'])
                self.ui.text_user.setText(user_conf['DATABASE']['username'])
                self.ui.text_password.setText(user_conf['DATABASE']['password'])
                self.ui.checkBox_re.setChecked(1)

    def set_db_config(self):
        """
        配置数据库完成
        """
        base_dir = config.setting.BASE_DIR
        f = open(base_dir + r"/config/config_" + str(self.id) + ".conf", "w")
        f.close()

        # 接收参数
        if len(host := self.ui.text_host.text()) == 0:
            QMessageBox.information(self, '提示', '请填写主机')
            return
        if len(port := self.ui.text_port.text()) == 0:
            QMessageBox.information(self, '提示', '请填写数据库端口')
            return
        if len(username := self.ui.text_user.text()) == 0:
            QMessageBox.information(self, '提示', '请填写账号')
            return
        if len(password := self.ui.text_password.text()) == 0:
            QMessageBox.information(self, '提示', '请填写密码')
            return
        if self.ui.comboBox_database.currentText() == '请先获取数据库名':
            print(self.ui.comboBox_database.currentText())
            QMessageBox.information(self, '提示', '请先获取数据库名')
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
            base_dir = config.setting.BASE_DIR
            configfile = "config/config_" + str(self.id) + ".conf"
            configfile = os.path.join(base_dir, configfile)
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

            self.this_db = database
            self.dataProcessing.sig_load_table.emit()  # 启用多线程加载数据

            self.dialog_loading.open()  # 阻塞当前窗口，避免用户违规操作
            return

        else:
            QMessageBox.critical(self, '错误', '数据库读取失败!')
            return

    def get_dbname(self):
        """
        获取数据库名
        """
        if len(host := self.ui.text_host.text()) == 0:
            QMessageBox.information(self, '提示', '请填写主机')
            return
        if len(port := self.ui.text_port.text()) == 0:
            QMessageBox.information(self, '提示', '请填写数据库端口')
            return
        if len(username := self.ui.text_user.text()) == 0:
            QMessageBox.information(self, '提示', '请填写账号')
            return
        if len(password := self.ui.text_password.text()) == 0:
            QMessageBox.information(self, '提示', '请填写密码')
            return

        # 清空下拉框
        self.ui.comboBox_database.clear()
        self.ui.comboBox_database.addItem('请先获取数据库名')

        self.dataProcessing.sig_load_dbname.emit(host, username, password, port)  # 开始用多线程获取dbname

        self.dialog_loading.open()  # 阻塞当前窗口，避免用户违规操作

    def load_dbname_comp(self, result):
        '''
        加载数据库名完成
        :param result: 加载数据库名返回值
        :return:
        '''
        self.dialog_loading.close()
        if result.get('code') == 2000:
            # 清空下拉框
            self.ui.comboBox_database.clear()

            dbnames = result.get('data')
            # 将数据库名添加到下拉框中
            for dbname in dbnames:
                self.ui.comboBox_database.addItem(dbname[0])
        else:
            QMessageBox.critical(self, '错误', str(result))
            QMessageBox.critical(self, '错误', '数据库连接失败!')

    def load_table_comp(self, tables_info):
        '''
        加载表数据完成
        :param tables_info:表数据
        :return:
        '''
        if tables_info.get('code'):
            self.sql_data['table'] = tables_info['data']['table']
            kwargs = {}
            kwargs['sql_data'] = self.sql_data
            self.next_step(**kwargs)
            self.dialog_loading.close()
        else:
            self.dialog_loading.close()
            QMessageBox.critical(self, '错误', str(tables_info.get('message')))
            QMessageBox.critical(self, '错误', '数据库连接失败!')
