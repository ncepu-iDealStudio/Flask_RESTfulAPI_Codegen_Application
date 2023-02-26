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
import os
import sys

from PySide6.QtCore import QFile, QSize, QThread, QEvent, QTimer
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QPushButton, QDialog, QMainWindow, QSizeGrip, \
    QGraphicsDropShadowEffect
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QMovie, Qt, QColor

# 以下为各页面模块
from app import window_database
from app import window_table
from app import window_view
from app import window_confirm
from app import window_generate
from app.ui.MainWindow import Ui_MainWindow
from app.widgets import CustomGrip

GLOBAL_STATE = False


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # 从.py文件加载UI定义

        # # SET AS GLOBAL WIDGETS
        # # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # # 加载主窗口样式
        # self.setStyleSheet('')  # 这里不设计样式就会出现bug,因为主窗口已经在qtDesigner中设计过样式了

        # 加载样式
        # file = "app/themes/style.qss"
        # str = open(file, 'r', encoding='UTF-8').read()
        # self.ui.centralwidget.setStyleSheet(str)


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

        # 初始化加载中弹窗
        self.dialog_fault = QDialog()
        self.label_loading = QLabel(self.dialog_fault)  # 弹窗
        self.label_loading.setText('')
        self.label_loading.setGeometry(0, 0, 330, 230)

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(base_dir, 'app', 'ui', 'static', 'loading.gif')
        label_pic = QLabel(self.label_loading)  # loading动图label
        label_pic.setStyleSheet("background-color:transparent")
        label_pic.setGeometry(0, 0, 330, 230)
        pic = QMovie(image_path)  # loading动图
        pic.setScaledSize(QSize(label_pic.width(), label_pic.height()))
        pic.start()
        label_pic.setMovie(pic)
        # 去除弹窗标题栏
        self.dialog_fault.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # 初始化数据处理线程
        from .load_data import LoadData
        self.loadData = LoadData()
        self.load_thread = QThread()
        self.loadData.moveToThread(self.load_thread)
        self.load_thread.start()

        # 定义主要数据sql_data
        self.sql_data = {
            'table': [],
            'view': []
        }

        # 加载各模块的函数
        window_database.add_func(self)
        window_table.add_func(self)
        window_view.add_func(self)
        window_confirm.add_func(self)
        window_generate.add_func(self)

        # 对各个页面进行初始化
        self.frame_init()
        self.window_init_for_database()
        self.window_init_for_table()
        self.window_init_for_view()
        self.window_init_for_confirm()
        self.window_init_for_generate()

        # 设置初始页面为第一页
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_step.setCurrentIndex(0)

        # 定义所有页面公有变量
        self.last_db = ''  # 上一次使用的数据库名
        self.this_db = ''  # 本次使用的数据库名

    def frame_init(self):
        '''
        框架初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
        :return:
        '''
        self.ui.pushButton_next.clicked.connect(self.button_next_clicked)
        self.ui.pushButton_last.clicked.connect(self.button_last_clicked)

    def button_next_clicked(self):
        '''
        下一步按钮点击函数
        :return:
        '''

        # 对不同页面给出不同的操作分支，各自完善相关方法
        if self.ui.stackedWidget.currentIndex() == 0:
            self.db_config()
            return

        if self.ui.stackedWidget.currentIndex() == 1:
            self.set_table_config()
            return

        if self.ui.stackedWidget.currentIndex() == 2:
            self.set_view_config()
            return

        if self.ui.stackedWidget.currentIndex() == 3:
            self.confirm_config()
            self.ui.pushButton_next.setText('生成代码')
            return

        if self.ui.stackedWidget.currentIndex() == 4:
            self.generate()
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
            self.last_db = self.this_db
            self.view_is_config = False
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.stackedWidget_step.setCurrentIndex(0)
            return

    def next_step(self):
        '''
        通过判断当前所在页面，进行相应操作并跳转到对应页面
        :return:
        '''
        if self.ui.stackedWidget.currentIndex() == 0:
            self.table_config_init()
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.stackedWidget_step.setCurrentIndex(1)
            return

        if self.ui.stackedWidget.currentIndex() == 1:
            self.view_config_init()
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.stackedWidget_step.setCurrentIndex(2)
            return

        if self.ui.stackedWidget.currentIndex() == 2:
            self.confirm_config_init()
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.stackedWidget_step.setCurrentIndex(3)
            return

        if self.ui.stackedWidget.currentIndex() == 3:
            self.generate_init()
            self.ui.pushButton_next.setText('生成代码')
            self.ui.stackedWidget.setCurrentIndex(4)
            self.ui.stackedWidget_step.setCurrentIndex(4)
            return

        if self.ui.stackedWidget.currentIndex() == 4:
            self.generate()
            return

    def maximize_restore(self):
        '''
        最大化按钮点击函数
        :return:
        '''
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            # self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            # self.left_grip.hide()
            # self.right_grip.hide()
            # self.top_grip.hide()
            # self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            # self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            # self.left_grip.show()
            # self.right_grip.show()
            # self.top_grip.show()
            # self.bottom_grip.show()

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
        self.dialog_fault.close()

        # 关闭线程
        self.load_thread.quit()
        self.load_thread.wait()
        del self.load_thread

        # 关闭主窗口
        self.close()


def start():

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app/ui/ncepu.jpg'))
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
