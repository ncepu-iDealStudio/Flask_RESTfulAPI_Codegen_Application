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

from PySide6.QtCore import QFile, QSize, QThread
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QPushButton, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QMovie

# 以下为各页面模块
from app import window_database
from app import window_table
from app import window_view
from app import window_confirm
from app import window_generate

class MainWindow:

    def __init__(self):
        # 从文件中加载UI定义
        qfile_main = QFile('app/ui/MainWindow.ui')
        qfile_main.open(QFile.ReadOnly)
        qfile_main.close()

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile_main)

        # 初始化加载中弹窗
        self.dialog_fault = QDialog()
        self.label_loading = QLabel(self.dialog_fault)  # 弹窗
        self.label_loading.setText('')
        self.label_loading.setGeometry(110, 10, 230, 230)

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(base_dir, 'app', 'ui', 'static', 'loading.gif')
        label_pic = QLabel(self.label_loading)  # loading动图label
        label_pic.setGeometry(55, 10, 120, 120)
        pic = QMovie(image_path)  # loading动图
        pic.setScaledSize(QSize(label_pic.width(), label_pic.height()))
        pic.start()
        label_pic.setMovie(pic)

        label_text = QLabel(self.dialog_fault)  # 弹窗提示
        label_text.setGeometry(175, 130, 220, 50)
        label_text.setText("加载中,请稍候...")

        # cancel_pbt = QPushButton(self.dialog_fault)  # 取消按钮
        # cancel_pbt.setText("取消")
        # cancel_pbt.setGeometry(150, 180, 180, 35)

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


def start():

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app/ui/ncepu.jpg'))
    main_window = MainWindow()
    main_window.ui.show()
    sys.exit(app.exec())
