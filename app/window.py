# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : window.py
# @ide    : PyCharm
# @time   : 2022-10-06 09:17:22
'''
窗口主文件，负责对窗口进行初始化以及对各个子页面的整体调度
'''
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
        # # 从文件中加载UI定义
        # qfile_main = QFile('app/ui/MainWindow.ui')
        # qfile_main.open(QFile.ReadOnly)
        # qfile_main.close()
        #
        # # 从 UI 定义中动态 创建一个相应的窗口对象
        # # 注意：里面的控件对象也成为窗口对象的属性了
        # # 比如 self.ui.button , self.ui.textEdit
        # self.ui = QUiLoader().load(qfile_main)

        QMainWindow.__init__(self)

        # # SET AS GLOBAL WIDGETS
        # # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 加载主窗口样式
        self.setStyleSheet('')  # 这里不设计样式就会出现bug,因为主窗口已经在qtDesigner中设计过样式了

        # 加载样式
        file = "app/themes/style.qss"
        str = open(file, 'r', encoding='UTF-8').read()
        self.ui.centralwidget.setStyleSheet(str)


        # STANDARD TITLE BAR 去除窗口标题栏
        # self.setWindowFlags(Qt.FramelessWindowHint)    # 去除标题栏后不可改变大小
        self.setWindowFlags(Qt.CustomizeWindowHint)      # 去除标题栏后可以改变大小


        # 鼠标双击事件
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: self.maximize_restore())

        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore



        # MOVE WINDOW / MAXIMIZE / RESTORE
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

        # 使用 self.setWindowFlags(Qt.CustomizeWindowHint) 这里可以不用单独添加窗口伸缩的代码
        # 窗口可伸缩
        # # CUSTOM GRIPS
        # self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        # self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        # self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        # self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        # # DROP SHADOW
        # self.shadow = QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(17)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QColor(0, 0, 0, 150))
        # self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # # RESIZE WINDOW
        # self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        # self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        # 最小化
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        # 最大化
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: self.maximize_restore())

        # CLOSE APPLICATION
        # 关闭
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

        # 去除标题栏
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

    def frame_init(self):
        '''
        框架初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
        :return:
        '''
        self.ui.pushButton_next.clicked.connect(self.button_next)
        self.ui.pushButton_last.clicked.connect(self.button_last)


    def button_next(self):
        '''
        下一步按钮点击函数
        :return:
        '''

        # 对不同页面给出不同的操作分支，各自完善相关方法
        if self.ui.stackedWidget.currentIndex() == 0:
            self.db_config()
            return

        if self.ui.stackedWidget.currentIndex() == 1:
            self.table_config()
            return

        if self.ui.stackedWidget.currentIndex() == 2:
            self.view_config()
            return

        if self.ui.stackedWidget.currentIndex() == 3:
            self.confirm_config()
            self.ui.pushButton_next.setText('生成代码')
            return

        if self.ui.stackedWidget.currentIndex() == 4:
            self.generate()
            return

    def button_last(self):
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

    # 当前页面的操作完成后，调用该函数进入下一步
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
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def close_window(self):
        self.dialog_fault.close()
        self.close()

    # def resize_grips(self):
    #     self.left_grip.setGeometry(0, 10, 10, self.height())
    #     self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
    #     self.top_grip.setGeometry(0, 0, self.width(), 10)
    #     self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    # def resizeEvent(self, event):
    #     # Update Size Grips
    #     self.resize_grips()


def start():

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app/ui/ncepu.jpg'))
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
