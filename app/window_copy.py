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
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QPushButton, QDialog, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QMovie, Qt

# 以下为各页面模块
from app import window_database
from app import window_table
from app import window_view
from app import window_confirm
from app import window_generate
from app.ui.MainWindow import Ui_MainWindow

GLOBAL_STATE = False

class MainWindow(QMainWindow):

    def __init__(self):
        # 从文件中加载UI定义
        # qfile_main = QFile('app/ui/main.ui')
        # qfile_main.open(QFile.ReadOnly)
        # qfile_main.close()
        #
        # # 从 UI 定义中动态 创建一个相应的窗口对象
        # # 注意：里面的控件对象也成为窗口对象的属性了
        # # 比如 self.ui.button , self.ui.textEdit
        # self.ui = QUiLoader().load(qfile_main)

        # test

        QMainWindow.__init__(self)

        # # SET AS GLOBAL WIDGETS
        # # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        print('test')
        # STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # MOVE WINDOW / MAXIMIZE / RESTORE
        # def moveWindow(event):
        #     # # IF MAXIMIZED CHANGE TO NORMAL
        #     # if UIFunctions.returStatus(self):
        #     #     UIFunctions.maximize_restore(self)
        #     # MOVE WINDOW
        #     if event.buttons() == Qt.LeftButton:
        #         self.ui.move(self.ui.pos() + event.globalPos() - self.dragPos)
        #         self.dragPos = event.globalPos()
        #         event.accept()
        #
        # self.ui.titleRightInfo.mouseMoveEvent = moveWindow
        #
        # # CUSTOM GRIPS
        # self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        # self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        # self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        # self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        # # RESIZE WINDOW
        # self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        # self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")


        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: self.maximize_restore())

        print(self.ui.titleRightInfo.mouseDoubleClickEvent)
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore
        print(self.ui.titleRightInfo.mouseDoubleClickEvent)



        # MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            print('move')
            if GLOBAL_STATE:
                self.maximize_restore()
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.ui.move(self.ui.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.mouseMoveEvent = moveWindow

        # MINIMIZE
        # 最小化
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.ui.showMinimized())

        # MAXIMIZE/RESTORE
        # 最大化
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: self.maximize_restore())

        # CLOSE APPLICATION
        # 关闭
        self.ui.closeAppBtn.clicked.connect(lambda: self.ui.close())


    #     # 初始化加载中弹窗
    #     self.dialog_fault = QDialog()
    #     self.label_loading = QLabel(self.dialog_fault)  # 弹窗
    #     self.label_loading.setText('')
    #     self.label_loading.setGeometry(110, 10, 230, 230)
    #
    #     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     image_path = os.path.join(base_dir, 'app', 'ui', 'static', 'loading.gif')
    #     label_pic = QLabel(self.label_loading)  # loading动图label
    #     label_pic.setGeometry(55, 10, 120, 120)
    #     pic = QMovie(image_path)  # loading动图
    #     pic.setScaledSize(QSize(label_pic.width(), label_pic.height()))
    #     pic.start()
    #     label_pic.setMovie(pic)
    #
    #     label_text = QLabel(self.dialog_fault)  # 弹窗提示
    #     label_text.setGeometry(175, 130, 220, 50)
    #     label_text.setText("加载中,请稍候...")
    #
    #     # cancel_pbt = QPushButton(self.dialog_fault)  # 取消按钮
    #     # cancel_pbt.setText("取消")
    #     # cancel_pbt.setGeometry(150, 180, 180, 35)
    #
    #     # 初始化数据处理线程
    #
    #     from .load_data import LoadData
    #     self.loadData = LoadData()
    #     self.load_thread = QThread()
    #     self.loadData.moveToThread(self.load_thread)
    #     self.load_thread.start()
    #
    #     # 定义主要数据sql_data
    #     self.sql_data = {
    #         'table': [],
    #         'view': []
    #     }
    #
    #     # 加载各模块的函数
    #     window_database.add_func(self)
    #     window_table.add_func(self)
    #     window_view.add_func(self)
    #     window_confirm.add_func(self)
    #     window_generate.add_func(self)
    #
    #     # 对各个页面进行初始化
    #     self.frame_init()
    #     self.window_init_for_database()
    #     self.window_init_for_table()
    #     self.window_init_for_view()
    #     self.window_init_for_confirm()
    #     self.window_init_for_generate()
    #
    # def frame_init(self):
    #     '''
    #     框架初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
    #     :return:
    #     '''
    #     self.ui.pushButton_next.clicked.connect(self.button_next)
    #     self.ui.pushButton_last.clicked.connect(self.button_last)
    #
    #
    # def button_next(self):
    #     '''
    #     下一步按钮点击函数
    #     :return:
    #     '''
    #
    #     # 对不同页面给出不同的操作分支，各自完善相关方法
    #     if self.ui.stackedWidget.currentIndex() == 0:
    #         self.db_config()
    #         return
    #
    #     if self.ui.stackedWidget.currentIndex() == 1:
    #         self.table_config()
    #         return
    #
    #     if self.ui.stackedWidget.currentIndex() == 2:
    #         self.view_config()
    #         return
    #
    #     if self.ui.stackedWidget.currentIndex() == 3:
    #         self.confirm_config()
    #         self.ui.pushButton_next.setText('生成代码')
    #         return
    #
    #     if self.ui.stackedWidget.currentIndex() == 4:
    #         self.generate()
    #         return
    #
    # def button_last(self):
    #     '''
    #     上一步按钮点击函数
    #     :return:
    #     '''
    #
    #     if self.ui.stackedWidget.currentIndex() == 4:
    #         self.ui.stackedWidget.setCurrentIndex(3)
    #         self.ui.stackedWidget_step.setCurrentIndex(3)
    #         self.ui.pushButton_next.setText('下一步')
    #         return
    #
    #     if self.ui.stackedWidget.currentIndex() == 3:
    #         self.ui.stackedWidget.setCurrentIndex(2)
    #         self.ui.stackedWidget_step.setCurrentIndex(2)
    #         return
    #
    #     if self.ui.stackedWidget.currentIndex() == 2:
    #         self.ui.stackedWidget.setCurrentIndex(1)
    #         self.ui.stackedWidget_step.setCurrentIndex(1)
    #         return
    #
    #     if self.ui.stackedWidget.currentIndex() == 1:
    #         self.ui.stackedWidget.setCurrentIndex(0)
    #         self.ui.stackedWidget_step.setCurrentIndex(0)
    #         return
    #
    # # 当前页面的操作完成后，调用该函数进入下一步
    # def next_step(self):
    #     '''
    #     通过判断当前所在页面，进行相应操作并跳转到对应页面
    #     :return:
    #     '''
    #     if self.ui.stackedWidget.currentIndex() == 0:
    #         self.table_config_init()
    #         self.ui.stackedWidget.setCurrentIndex(1)
    #         self.ui.stackedWidget_step.setCurrentIndex(1)
    #         return
    #
    #     if self.ui.stackedWidget.currentIndex() == 1:
    #         self.view_config_init()
    #         self.ui.stackedWidget.setCurrentIndex(2)
    #         self.ui.stackedWidget_step.setCurrentIndex(2)
    #         return
    #
    #     if self.ui.stackedWidget.currentIndex() == 2:
    #         self.confirm_config_init()
    #         self.ui.stackedWidget.setCurrentIndex(3)
    #         self.ui.stackedWidget_step.setCurrentIndex(3)
    #         return
    #
    #     if self.ui.stackedWidget.currentIndex() == 3:
    #         self.generate_init()
    #         self.ui.pushButton_next.setText('生成代码')
    #         self.ui.stackedWidget.setCurrentIndex(4)
    #         self.ui.stackedWidget_step.setCurrentIndex(4)
    #         return
    #
    #     if self.ui.stackedWidget.currentIndex() == 4:
    #         self.generate()
    #         return
    #
    # def maximize_restore(self):
    #     global GLOBAL_STATE
    #     status = GLOBAL_STATE
    #     if status == False:
    #         self.ui.showMaximized()
    #         GLOBAL_STATE = True
    #         # self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
    #         self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
    #         self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
    #         self.ui.frame_size_grip.hide()
    #         # self.left_grip.hide()
    #         # self.right_grip.hide()
    #         # self.top_grip.hide()
    #         # self.bottom_grip.hide()
    #     else:
    #         GLOBAL_STATE = False
    #         self.ui.showNormal()
    #         self.ui.resize(self.ui.width() + 1, self.ui.height() + 1)
    #         # self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
    #         self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
    #         self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
    #         self.ui.frame_size_grip.show()
    #         # self.left_grip.show()
    #         # self.right_grip.show()
    #         # self.top_grip.show()
    #         # self.bottom_grip.show()


def start():

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app/ui/ncepu.jpg'))
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
