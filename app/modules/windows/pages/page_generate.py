# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : page_generate.py
# @ide    : PyCharm
# @time   : 2022-10-12 16:15:38
'''
代码生成页面主要操作
'''
import configparser
import os
from PySide6 import QtWidgets
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QMessageBox, QFileDialog
import config.setting
from app.modules.windows import MainWindow
from utils.checkChinese import is_chinese


class PageGenerate(MainWindow):
    def __init__(self, mainWindow):
        MainWindow.__init__(self)
        self.dialog_loading = mainWindow.dialog_loading
        self.ui = mainWindow.ui
        self.dataProcessing = mainWindow.dataProcessing
        self.sql_data = mainWindow.sql_data
        self.next_step = mainWindow.next_step
        self.id = mainWindow.id
        self.close_window = mainWindow.close_window

        # 初始化多线程信号与槽
        self.dataProcessing.sig_load_generate.connect(self.dataProcessing.load_generate)
        self.dataProcessing.sig_load_generate_comp.connect(self.load_generate_comp)

    def refresh_generate_page(self):
        '''
        代码生成页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
        :return:
        '''
        self.ui.dig = QFileDialog()
        self.ui.dig.setFileMode(QFileDialog.AnyFile)
        self.ui.dig.setFilter(QDir.Files)
        self.ui.toolButton_file.clicked.connect(self.button_show_file)

        # 添加默认配置
        session_id = self.id
        configfile = "config/config_" + str(session_id) + ".conf"  # 配置文件路径
        base_dir = config.setting.BASE_DIR
        configfile = os.path.join(base_dir, configfile)
        conf = configparser.ConfigParser()  # 实例类
        conf.read(configfile, encoding='UTF-8')  # 读取配置文件

        base_dir = config.setting.BASE_DIR
        target_dir = os.path.join(base_dir, 'dist')  # 默认目标目录
        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)

        self.ui.lineEdit.setText(target_dir)
        self.ui.lineEdit_2.setText(conf['DATABASE']['database'])
        self.ui.lineEdit_3.setText('1.0')

        # 加载用户上一次使用的配置
        user_configfile = "config/user_config.conf"

        # 如果能够加载用户配置器
        if os.path.isfile(user_configfile):
            user_conf = configparser.ConfigParser()  # 实例类
            user_conf.read(user_configfile, encoding='UTF-8')  # 读取配置文件
            if user_conf.has_section('PARAMETER'):
                self.ui.lineEdit.setText(user_conf['PARAMETER']['target_dir'])
                self.ui.lineEdit_2.setText(user_conf['PARAMETER']['project_name'])
                self.ui.lineEdit_3.setText(user_conf['PARAMETER']['api_version'])

    def code_generate(self):
        """
        代码生成页主要代码
        :return:
        """

        session_id = self.id

        # 获取用户填写的数据，并将其赋值给变量
        path = self.ui.lineEdit.text()
        name = self.ui.lineEdit_2.text()
        version = self.ui.lineEdit_3.text()

        # 检查用户填写的数据是否正确
        if len(path) == 0:
            QMessageBox.information(self, '提示', '生成路径不能为空')
            return
        if not os.path.isdir(path):
            QMessageBox.information(self, '提示', '生成路径有误,该路径不是一个文件夹')
            return
        if is_chinese(path):
            QMessageBox.information(self, '提示', '生成路径不能包含中文字符')
            return
        if len(name) == 0:
            QMessageBox.information(self, '提示', '项目名不能为空')
            return
        if len(version) == 0:
            QMessageBox.information(self, '提示', '版本号不能为空')
            return

        project_path = path
        project_name = name
        interface_version = version

        base_dir = config.setting.BASE_DIR
        configfile = "config/config_" + str(session_id) + ".conf"  # 配置文件路径
        configfile = os.path.join(base_dir, configfile)
        user_configfile = "config/user_config.conf"  # 用户配置文件路径
        user_configfile = os.path.join(base_dir, user_configfile)
        conf = configparser.ConfigParser()  # 实例类
        conf.read(configfile, encoding='UTF-8')  # 读取配置文件

        if not conf.has_section('PARAMETER'):
            conf.add_section('PARAMETER')

        conf.set("PARAMETER", "target_dir", project_path)  # 第一个参数为组名，第二个参数为属性名，第三个参数为属性的值
        conf.set("PARAMETER", "project_name", project_name)
        conf.set("PARAMETER", "api_version", interface_version)
        with open(configfile, "w") as f:
            conf.write(f)

        # 是否保存用户配置
        if self.ui.checkBox_re.isChecked():
            with open(user_configfile, "w") as f:
                conf.write(f)
        else:
            with open(user_configfile, "w") as f:
                f.truncate()

        # 过滤掉未勾选的表和视图
        table_config = {
            'table': [],
            'view': []
        }
        for table in self.sql_data.get('table'):
            if table.get('ischecked'):
                table_config['table'].append(table)

        for view in self.sql_data.get('view'):
            if view.get('ischecked'):
                table_config['view'].append(view)

        # 开始生成代码
        self.dataProcessing.sig_load_generate.emit(table_config, session_id)

        self.dialog_loading.open()

    def button_show_file(self):
        '''
        选择生成地址
        :param self:
        :return:
        '''
        dialog = QtWidgets.QFileDialog
        fileName = dialog.getExistingDirectory(self, "选取文件", os.getcwd())

        self.ui.lineEdit.setText(fileName)

    def load_generate_comp(self, result):
        '''
        代码生成完成
        :param self:
        :param result:
        :return:
        '''

        self.dialog_loading.close()
        if result.get('code') == '2000':
            QMessageBox.information(self, '提示', '代码生成成功!\n即将退出')
        else:
            QMessageBox.critical(self, '错误', '代码生成失败\n即将退出!')
        self.close_window()
