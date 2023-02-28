# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : window_main.py
# @ide    : PyCharm
# @time   : 2022-10-06 09:17:22
'''
窗口主文件，负责对窗口进行初始化以及对各个子页面的整体调度
'''
import configparser
import datetime
import os
from PySide6.QtCore import QThread, QEvent, QTimer
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import Qt
from app.ui.MainWindow import Ui_MainWindow
GLOBAL_STATE = False


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # 从.py文件加载UI定义

        # # SET AS GLOBAL WIDGETS
        # # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 加载样式
        # file = "app/themes/style.qss"
        # style = open(file, 'r', encoding='UTF-8').read()
        # self.ui.centralwidget.setStyleSheet(style)


        # STANDARD TITLE BAR 去除窗口标题栏
        self.setWindowFlags(Qt.FramelessWindowHint)    # 去除标题栏后不可改变大小
        # self.setWindowFlags(Qt.CustomizeWindowHint)      # 去除标题栏后可以改变大小

        # 加载软件版权信息配置
        app_configfile = "app/config/app_config.conf"
        if os.path.isfile(app_configfile):
            app_conf = configparser.ConfigParser()  # 实例类
            app_conf.read(app_configfile, encoding='UTF-8')  # 读取配置文件
            author = app_conf['PARAMETER']['author']
            version = app_conf['PARAMETER']['version']
            app_name = app_conf['PARAMETER']['app_name']

            title = app_name
            description = app_name
            # APPLY TEXTS
            self.setWindowTitle(title)
            self.ui.titleRightInfo.setText(description)
            self.ui.creditsLabel.setText('By:' + author)
            self.ui.version.setText('v' + version)


        # 鼠标双击事件
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: self.maximize_restore())

        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore


        # MOVE WINDOW / MAXIMIZE / RESTORE
        # 移动窗口
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if GLOBAL_STATE:
                self.maximize_restore()
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.titleRightInfo.mouseMoveEvent = moveWindow

        # MINIMIZE
        # 最小化窗口
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # CLOSE APPLICATION
        # 关闭窗口
        self.ui.closeAppBtn.clicked.connect(lambda: self.close_window())

        # 初始化数据处理线程
        from app.modules.dataProcessing.data_processing import DataProcessing
        self.dataProcessing = DataProcessing()
        self.data_thread = QThread()
        self.dataProcessing.moveToThread(self.data_thread)
        self.data_thread.start()

        # 设置初始页面为第一页
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_step.setCurrentIndex(0)

        # 定义主要数据sql_data
        self.sql_data = {
            'table': [],
            'view': []
        }
        self.id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 初始化self.id

        # 全局变量the_db和last_db用于判断数据库是否已经完成配置，
        self.the_db = {
            'host': '',
            'database': ''
        }
        self.last_db = {
            'host': '',
            'database': ''
        }
        self.db_changed = {
            'db_is_changed': True,
            'view_is_config': False,
            'table_is_config': False
        }  # 记录数据库是否改变

    def window_init(self):
        '''
        框架初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
        :return:
        '''
        # 初始化各个子页面
        from app.modules.windows.pages import PageDatabase, PageTable, PageView, PageConfirm, PageGenerate
        self.page_database = PageDatabase(self)
        self.page_database.refresh_db_page()
        self.page_table = PageTable(self)
        self.page_view = PageView(self)
        self.page_confirm = PageConfirm(self)
        self.page_generate = PageGenerate(self)

        self.ui.pushButton_next.clicked.connect(self.button_next_clicked)
        self.ui.pushButton_last.clicked.connect(self.button_last_clicked)

    def button_next_clicked(self):
        '''
        下一步按钮点击函数
        :return:
        '''

        # 对不同页面给出不同的操作分支，各自完善相关方法
        if self.ui.stackedWidget.currentIndex() == 0:

            self.page_database.set_db_config()
            return

        if self.ui.stackedWidget.currentIndex() == 1:
            self.page_table.set_table_config()
            return

        if self.ui.stackedWidget.currentIndex() == 2:
            self.page_view.set_view_config()
            return

        if self.ui.stackedWidget.currentIndex() == 3:
            self.page_confirm.set_confirm_config()
            self.ui.pushButton_next.setText('生成代码')
            return

        if self.ui.stackedWidget.currentIndex() == 4:
            self.page_generate.code_generate()
            return

    def button_last_clicked(self):
        '''
        上一步按钮点击函数
        :return:
        '''

        if self.ui.stackedWidget.currentIndex() == 4:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.stackedWidget_step.setCurrentIndex(3)
            self.ui.pushButton_next.setText('下一步')
            return

        if self.ui.stackedWidget.currentIndex() == 3:
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.stackedWidget_step.setCurrentIndex(2)
            return

        if self.ui.stackedWidget.currentIndex() == 2:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.stackedWidget_step.setCurrentIndex(1)
            return

        if self.ui.stackedWidget.currentIndex() == 1:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.stackedWidget_step.setCurrentIndex(0)
            return

    def next_step(self):
        '''
        通过判断当前所在页面，进行相应操作并跳转到对应页面
        :return:
        '''
        if self.ui.stackedWidget.currentIndex() == 0:
            self.page_table.refresh_table_page()
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.stackedWidget_step.setCurrentIndex(1)
            return

        if self.ui.stackedWidget.currentIndex() == 1:
            self.page_view.refresh_view_page()
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.stackedWidget_step.setCurrentIndex(2)
            return

        if self.ui.stackedWidget.currentIndex() == 2:
            self.page_confirm.refresh_confirm_page()
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.stackedWidget_step.setCurrentIndex(3)
            return

        if self.ui.stackedWidget.currentIndex() == 3:
            self.page_generate.refresh_generate_page()
            self.ui.pushButton_next.setText('生成代码')
            self.ui.stackedWidget.setCurrentIndex(4)
            self.ui.stackedWidget_step.setCurrentIndex(4)
            return

    def mousePressEvent(self, event):
        '''
        鼠标点击事件
        :param event:
        :return:
        '''
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        # if event.buttons() == Qt.LeftButton:
        #     print('Mouse click: LEFT CLICK')
        # if event.buttons() == Qt.RightButton:
        #     print('Mouse click: RIGHT CLICK')

    def close_window(self):
        '''
        关闭窗口
        :return:
        '''
        # 关闭弹窗
        self.dialog_loading.close()

        # 关闭线程
        self.data_thread.quit()
        self.data_thread.wait()
        del self.data_thread

        # 关闭主窗口
        self.close()