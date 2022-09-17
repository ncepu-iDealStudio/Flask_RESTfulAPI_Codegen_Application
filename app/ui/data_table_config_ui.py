# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_table_config.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setGeometry(QRect(650, 500, 75, 24))
        self.pushButton_last = QPushButton(self.centralwidget)
        self.pushButton_last.setObjectName(u"pushButton_last")
        self.pushButton_last.setGeometry(QRect(80, 510, 75, 24))
        self.stackedWidget_right = QStackedWidget(self.centralwidget)
        self.stackedWidget_right.setObjectName(u"stackedWidget_right")
        self.stackedWidget_right.setGeometry(QRect(330, 20, 451, 451))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayoutWidget_2 = QWidget(self.page_1)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(30, 10, 351, 91))
        self.verticalLayout_page1 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_page1.setObjectName(u"verticalLayout_page1")
        self.verticalLayout_page1.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_page1.addWidget(self.label_2)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setMouseTracking(False)

        self.verticalLayout_page1.addWidget(self.label)

        self.stackedWidget_right.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayoutWidget_4 = QWidget(self.page_2)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(9, 9, 431, 451))
        self.verticalLayout_page2 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_page2.setObjectName(u"verticalLayout_page2")
        self.verticalLayout_page2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_right = QScrollArea(self.verticalLayoutWidget_4)
        self.scrollArea_right.setObjectName(u"scrollArea_right")
        self.scrollArea_right.setWidgetResizable(True)
        self.scrollAreaWidgetContents_right = QWidget()
        self.scrollAreaWidgetContents_right.setObjectName(u"scrollAreaWidgetContents_right")
        self.scrollAreaWidgetContents_right.setGeometry(QRect(0, -60, 410, 1000))
        self.scrollAreaWidgetContents_right.setMinimumSize(QSize(0, 1000))
        self.label_table_name = QLabel(self.scrollAreaWidgetContents_right)
        self.label_table_name.setObjectName(u"label_table_name")
        self.label_table_name.setGeometry(QRect(20, 10, 54, 16))
        self.label_set_key = QLabel(self.scrollAreaWidgetContents_right)
        self.label_set_key.setObjectName(u"label_set_key")
        self.label_set_key.setGeometry(QRect(20, 140, 151, 16))
        self.label_select_key = QLabel(self.scrollAreaWidgetContents_right)
        self.label_select_key.setObjectName(u"label_select_key")
        self.label_select_key.setGeometry(QRect(20, 170, 161, 16))
        self.comboBox_select_key = QComboBox(self.scrollAreaWidgetContents_right)
        self.comboBox_select_key.setObjectName(u"comboBox_select_key")
        self.comboBox_select_key.setGeometry(QRect(20, 190, 161, 22))
        self.label_set_key_2 = QLabel(self.scrollAreaWidgetContents_right)
        self.label_set_key_2.setObjectName(u"label_set_key_2")
        self.label_set_key_2.setGeometry(QRect(20, 220, 161, 16))
        self.comboBox_set_key = QComboBox(self.scrollAreaWidgetContents_right)
        self.comboBox_set_key.setObjectName(u"comboBox_set_key")
        self.comboBox_set_key.setGeometry(QRect(20, 240, 161, 22))
        self.label_code = QLabel(self.scrollAreaWidgetContents_right)
        self.label_code.setObjectName(u"label_code")
        self.label_code.setGeometry(QRect(20, 310, 161, 16))
        self.verticalLayoutWidget_5 = QWidget(self.scrollAreaWidgetContents_right)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 340, 401, 311))
        self.verticalLayout_code = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_code.setObjectName(u"verticalLayout_code")
        self.verticalLayout_code.setContentsMargins(0, 0, 0, 0)
        self.label_isDelete = QLabel(self.scrollAreaWidgetContents_right)
        self.label_isDelete.setObjectName(u"label_isDelete")
        self.label_isDelete.setGeometry(QRect(20, 50, 158, 16))
        self.comboBox_isDelete = QComboBox(self.scrollAreaWidgetContents_right)
        self.comboBox_isDelete.addItem("")
        self.comboBox_isDelete.setObjectName(u"comboBox_isDelete")
        self.comboBox_isDelete.setGeometry(QRect(20, 80, 158, 21))
        self.scrollArea_right.setWidget(self.scrollAreaWidgetContents_right)

        self.verticalLayout_page2.addWidget(self.scrollArea_right)

        self.stackedWidget_right.addWidget(self.page_2)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 40, 279, 439))
        self.verticalLayout_left = QVBoxLayout(self.widget)
        self.verticalLayout_left.setObjectName(u"verticalLayout_left")
        self.verticalLayout_left.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_left = QScrollArea(self.widget)
        self.scrollArea_left.setObjectName(u"scrollArea_left")
        self.scrollArea_left.setWidgetResizable(True)
        self.scrollAreaWidgetContents_left = QWidget()
        self.scrollAreaWidgetContents_left.setObjectName(u"scrollAreaWidgetContents_left")
        self.scrollAreaWidgetContents_left.setGeometry(QRect(0, 0, 275, 435))
        self.scrollAreaWidgetContents_left.setMinimumSize(QSize(0, 0))
        self.horizontalLayoutWidget = QWidget(self.scrollAreaWidgetContents_left)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 281, 31))
        self.horizontalLayout_all = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_all.setObjectName(u"horizontalLayout_all")
        self.horizontalLayout_all.setContentsMargins(0, 0, 0, 0)
        self.checkBox_all = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_all.setObjectName(u"checkBox_all")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_all.sizePolicy().hasHeightForWidth())
        self.checkBox_all.setSizePolicy(sizePolicy)
        self.checkBox_all.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_all.addWidget(self.checkBox_all)

        self.label_select_all = QLabel(self.horizontalLayoutWidget)
        self.label_select_all.setObjectName(u"label_select_all")

        self.horizontalLayout_all.addWidget(self.label_select_all)

        self.horizontalLayout_all.setStretch(0, 1)
        self.horizontalLayout_all.setStretch(1, 5)
        self.scrollArea_left.setWidget(self.scrollAreaWidgetContents_left)

        self.verticalLayout_left.addWidget(self.scrollArea_left)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 860, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget_right.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
        self.pushButton_last.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u6b65", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u7528\u4e8e\u751f\u6210\u4ee3\u7801\u7684\u6570\u636e\u8868\uff0c\u5e76\u4e3a\u6bcf\u5f20\u8868\u8fdb\u884c\u76f8\u5e94\u7684\u914d\u7f6e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u8868\u51c6\u5907", None))
#if QT_CONFIG(whatsthis)
        self.scrollArea_right.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.scrollArea_right.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_table_name.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u662f\u8868\u540d", None))
        self.label_set_key.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u52a1\u4e3b\u952e\u8bbe\u7f6e", None))
        self.label_select_key.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u52a1\u4e3b\u952e\u5b57\u6bb5\u9009\u62e9", None))
        self.label_set_key_2.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u52a1\u4e3b\u952e\u751f\u6210\u89c4\u5219", None))
        self.label_code.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u9700\u8981\u52a0\u5bc6\u5b58\u50a8\u7684\u5b57\u6bb5", None))
        self.label_isDelete.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u662f\u5426\u903b\u8f91\u5220\u9664", None))
        self.comboBox_isDelete.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u903b\u8f91\u5220\u9664\u6807\u8bc6\u5b57\u6bb5", None))

        self.checkBox_all.setText("")
        self.label_select_all.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
    # retranslateUi

# pyside6-uic data_table_config.ui > data_table_config_ui.py