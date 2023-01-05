# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_copy2.ui'
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
        MainWindow.resize(1320, 768)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget_2 = QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.stackedWidget_2.addWidget(self.page_13)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.stackedWidget_2.addWidget(self.page_14)

        self.verticalLayout.addWidget(self.stackedWidget_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(1000, 650))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.scrollArea_1 = QScrollArea(self.page_1)
        self.scrollArea_1.setObjectName(u"scrollArea_1")
        self.scrollArea_1.setGeometry(QRect(0, 0, 991, 641))
        self.scrollArea_1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_1 = QWidget()
        self.scrollAreaWidgetContents_1.setObjectName(u"scrollAreaWidgetContents_1")
        self.scrollAreaWidgetContents_1.setGeometry(QRect(0, 0, 989, 639))
        self.label = QLabel(self.scrollAreaWidgetContents_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(353, 50, 171, 20))
        self.scrollArea_1.setWidget(self.scrollAreaWidgetContents_1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.scrollArea_4 = QScrollArea(self.page_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(0, 0, 991, 641))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 989, 639))
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 80, 171, 20))
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.scrollArea_5 = QScrollArea(self.page_5)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setGeometry(QRect(0, 0, 991, 641))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 989, 639))
        self.label_5 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(380, 160, 171, 20))
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_9)
        self.stackedWidget.addWidget(self.page_5)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.scrollArea_3 = QScrollArea(self.page_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(0, 0, 991, 641))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 989, 639))
        self.label_3 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 70, 171, 20))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_6)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.scrollArea_2 = QScrollArea(self.page_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 991, 641))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 989, 639))
        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 70, 171, 20))
        self.layoutWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 279, 641))
        self.verticalLayout_left_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_left_6.setObjectName(u"verticalLayout_left_6")
        self.verticalLayout_left_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_left_6 = QScrollArea(self.layoutWidget)
        self.scrollArea_left_6.setObjectName(u"scrollArea_left_6")
        self.scrollArea_left_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_left_6 = QWidget()
        self.scrollAreaWidgetContents_left_6.setObjectName(u"scrollAreaWidgetContents_left_6")
        self.scrollAreaWidgetContents_left_6.setGeometry(QRect(0, 0, 275, 637))
        self.scrollAreaWidgetContents_left_6.setMinimumSize(QSize(0, 0))
        self.horizontalLayoutWidget_6 = QWidget(self.scrollAreaWidgetContents_left_6)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(0, 0, 281, 34))
        self.horizontalLayout_all_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_all_6.setObjectName(u"horizontalLayout_all_6")
        self.horizontalLayout_all_6.setContentsMargins(0, 0, 0, 0)
        self.checkBox_all_6 = QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_all_6.setObjectName(u"checkBox_all_6")
        sizePolicy.setHeightForWidth(self.checkBox_all_6.sizePolicy().hasHeightForWidth())
        self.checkBox_all_6.setSizePolicy(sizePolicy)
        self.checkBox_all_6.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_all_6.addWidget(self.checkBox_all_6)

        self.pushButton_all_6 = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_all_6.setObjectName(u"pushButton_all_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_all_6.sizePolicy().hasHeightForWidth())
        self.pushButton_all_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_all_6.addWidget(self.pushButton_all_6)

        self.scrollArea_left_6.setWidget(self.scrollAreaWidgetContents_left_6)

        self.verticalLayout_left_6.addWidget(self.scrollArea_left_6)

        self.stackedWidget_right = QStackedWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget_right.setObjectName(u"stackedWidget_right")
        self.stackedWidget_right.setGeometry(QRect(280, 0, 711, 641))
        self.page_23 = QWidget()
        self.page_23.setObjectName(u"page_23")
        self.verticalLayoutWidget_20 = QWidget(self.page_23)
        self.verticalLayoutWidget_20.setObjectName(u"verticalLayoutWidget_20")
        self.verticalLayoutWidget_20.setGeometry(QRect(30, 10, 351, 91))
        self.verticalLayout_page1_7 = QVBoxLayout(self.verticalLayoutWidget_20)
        self.verticalLayout_page1_7.setObjectName(u"verticalLayout_page1_7")
        self.verticalLayout_page1_7.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.verticalLayoutWidget_20)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_page1_7.addWidget(self.label_18)

        self.label_19 = QLabel(self.verticalLayoutWidget_20)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMouseTracking(False)

        self.verticalLayout_page1_7.addWidget(self.label_19)

        self.stackedWidget_right.addWidget(self.page_23)
        self.page_24 = QWidget()
        self.page_24.setObjectName(u"page_24")
        self.verticalLayoutWidget_21 = QWidget(self.page_24)
        self.verticalLayoutWidget_21.setObjectName(u"verticalLayoutWidget_21")
        self.verticalLayoutWidget_21.setGeometry(QRect(-1, -1, 711, 641))
        self.verticalLayout_page2_7 = QVBoxLayout(self.verticalLayoutWidget_21)
        self.verticalLayout_page2_7.setObjectName(u"verticalLayout_page2_7")
        self.verticalLayout_page2_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_right_7 = QScrollArea(self.verticalLayoutWidget_21)
        self.scrollArea_right_7.setObjectName(u"scrollArea_right_7")
        self.scrollArea_right_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_right_7 = QWidget()
        self.scrollAreaWidgetContents_right_7.setObjectName(u"scrollAreaWidgetContents_right_7")
        self.scrollAreaWidgetContents_right_7.setGeometry(QRect(0, -17, 690, 1000))
        self.scrollAreaWidgetContents_right_7.setMinimumSize(QSize(0, 1000))
        self.label_table_name_7 = QLabel(self.scrollAreaWidgetContents_right_7)
        self.label_table_name_7.setObjectName(u"label_table_name_7")
        self.label_table_name_7.setGeometry(QRect(20, 10, 54, 16))
        self.label_set_key_13 = QLabel(self.scrollAreaWidgetContents_right_7)
        self.label_set_key_13.setObjectName(u"label_set_key_13")
        self.label_set_key_13.setGeometry(QRect(20, 140, 151, 16))
        self.label_select_key_7 = QLabel(self.scrollAreaWidgetContents_right_7)
        self.label_select_key_7.setObjectName(u"label_select_key_7")
        self.label_select_key_7.setGeometry(QRect(20, 170, 161, 16))
        self.comboBox_select_table_businesskeyname = QComboBox(self.scrollAreaWidgetContents_right_7)
        self.comboBox_select_table_businesskeyname.addItem("")
        self.comboBox_select_table_businesskeyname.setObjectName(u"comboBox_select_table_businesskeyname")
        self.comboBox_select_table_businesskeyname.setGeometry(QRect(20, 190, 161, 22))
        self.label_set_key_14 = QLabel(self.scrollAreaWidgetContents_right_7)
        self.label_set_key_14.setObjectName(u"label_set_key_14")
        self.label_set_key_14.setGeometry(QRect(210, 170, 161, 16))
        self.comboBox_select_table_businesskeyrule = QComboBox(self.scrollAreaWidgetContents_right_7)
        self.comboBox_select_table_businesskeyrule.addItem("")
        self.comboBox_select_table_businesskeyrule.setObjectName(u"comboBox_select_table_businesskeyrule")
        self.comboBox_select_table_businesskeyrule.setGeometry(QRect(210, 190, 161, 22))
        self.label_code_7 = QLabel(self.scrollAreaWidgetContents_right_7)
        self.label_code_7.setObjectName(u"label_code_7")
        self.label_code_7.setGeometry(QRect(20, 250, 651, 16))
        self.verticalLayoutWidget_22 = QWidget(self.scrollAreaWidgetContents_right_7)
        self.verticalLayoutWidget_22.setObjectName(u"verticalLayoutWidget_22")
        self.verticalLayoutWidget_22.setGeometry(QRect(20, 320, 497, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.verticalLayoutWidget_22)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.verticalLayoutWidget_22)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_4.addWidget(self.label_20)

        self.comboBox_select_table_field_encrypt = QComboBox(self.verticalLayoutWidget_22)
        self.comboBox_select_table_field_encrypt.addItem("")
        self.comboBox_select_table_field_encrypt.setObjectName(u"comboBox_select_table_field_encrypt")
        self.comboBox_select_table_field_encrypt.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.comboBox_select_table_field_encrypt)

        self.label_21 = QLabel(self.verticalLayoutWidget_22)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_4.addWidget(self.label_21)

        self.comboBox_select_table_encrypt_type = QComboBox(self.verticalLayoutWidget_22)
        self.comboBox_select_table_encrypt_type.addItem("")
        self.comboBox_select_table_encrypt_type.setObjectName(u"comboBox_select_table_encrypt_type")
        self.comboBox_select_table_encrypt_type.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.comboBox_select_table_encrypt_type)

        self.pushButton_delete_field_encrypt = QPushButton(self.verticalLayoutWidget_22)
        self.pushButton_delete_field_encrypt.setObjectName(u"pushButton_delete_field_encrypt")

        self.horizontalLayout_4.addWidget(self.pushButton_delete_field_encrypt)

        self.label_isDelete_7 = QLabel(self.scrollAreaWidgetContents_right_7)
        self.label_isDelete_7.setObjectName(u"label_isDelete_7")
        self.label_isDelete_7.setGeometry(QRect(20, 50, 158, 16))
        self.comboBox_select_table_logicaldeletemark = QComboBox(self.scrollAreaWidgetContents_right_7)
        self.comboBox_select_table_logicaldeletemark.addItem("")
        self.comboBox_select_table_logicaldeletemark.setObjectName(u"comboBox_select_table_logicaldeletemark")
        self.comboBox_select_table_logicaldeletemark.setGeometry(QRect(20, 80, 158, 21))
        self.pushButton_add_field_encrypt = QPushButton(self.scrollAreaWidgetContents_right_7)
        self.pushButton_add_field_encrypt.setObjectName(u"pushButton_add_field_encrypt")
        self.pushButton_add_field_encrypt.setGeometry(QRect(540, 280, 75, 24))
        self.scrollArea_right_7.setWidget(self.scrollAreaWidgetContents_right_7)

        self.verticalLayout_page2_7.addWidget(self.scrollArea_right_7)

        self.stackedWidget_right.addWidget(self.page_24)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_last = QPushButton(self.centralwidget)
        self.pushButton_last.setObjectName(u"pushButton_last")
        sizePolicy.setHeightForWidth(self.pushButton_last.sizePolicy().hasHeightForWidth())
        self.pushButton_last.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_last)

        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")
        sizePolicy.setHeightForWidth(self.pushButton_next.sizePolicy().hasHeightForWidth())
        self.pushButton_next.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_next)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1320, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget_right.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4ee3\u7801\u751f\u6210\u5668", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u662f\u6570\u636e\u5e93\u914d\u7f6e\u9875\u9762", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u662f\u914d\u7f6e\u786e\u8ba4\u914d\u7f6e\u9875\u9762", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u662f\u4ee3\u7801\u751f\u6210\u9875\u9762", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u662f\u89c6\u56fe\u8868\u914d\u7f6e\u9875\u9762", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u662f\u6570\u636e\u5e93\u8868\u914d\u7f6e\u9875\u9762", None))
        self.checkBox_all_6.setText("")
        self.pushButton_all_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u7528\u4e8e\u751f\u6210\u4ee3\u7801\u7684\u6570\u636e\u8868\uff0c\u5e76\u4e3a\u6bcf\u5f20\u8868\u8fdb\u884c\u76f8\u5e94\u7684\u914d\u7f6e", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u8868\u51c6\u5907", None))
#if QT_CONFIG(whatsthis)
        self.scrollArea_right_7.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.scrollArea_right_7.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_table_name_7.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u662f\u8868\u540d", None))
        self.label_set_key_13.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u52a1\u4e3b\u952e\u8bbe\u7f6e", None))
        self.label_select_key_7.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u52a1\u4e3b\u952e\u5b57\u6bb5\u9009\u62e9", None))
        self.comboBox_select_table_businesskeyname.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e1a\u52a1\u4e3b\u952e", None))

        self.label_set_key_14.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u52a1\u4e3b\u952e\u751f\u6210\u89c4\u5219", None))
        self.comboBox_select_table_businesskeyrule.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u52a0\u5bc6\u65b9\u5f0f", None))

        self.label_code_7.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u5b58\u50a8\u5b57\u6bb5\u8bbe\u7f6e(\u4e3a\u6ee1\u8db3\u5b89\u5168\u5ba1\u8ba1\u9700\u8981,\u4e00\u4e9b\u654f\u611f\u5b57\u6bb5\u53ef\u80fd\u9700\u8981\u5728\u6570\u636e\u5e93\u4e2d\u52a0\u5bc6\u5b58\u50a8\uff0c\u5982\u7528\u6237\u8eab\u4efd\u8bc1\u53f7\uff0c\u624b\u673a\u53f7\u7b49)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u6bb5\u9009\u62e9", None))
        self.comboBox_select_table_field_encrypt.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u9700\u8981\u52a0\u5bc6\u7684\u5b57\u6bb5", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u65b9\u5f0f", None))
        self.comboBox_select_table_encrypt_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u52a0\u5bc6\u65b9\u5f0f", None))

        self.pushButton_delete_field_encrypt.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.label_isDelete_7.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u662f\u5426\u903b\u8f91\u5220\u9664", None))
        self.comboBox_select_table_logicaldeletemark.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u903b\u8f91\u5220\u9664\u6807\u8bc6\u5b57\u6bb5", None))

        self.pushButton_add_field_encrypt.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5b57\u6bb5", None))
        self.pushButton_last.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u6b65", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
    # retranslateUi

# pyside6-uic MainWindow_copy2.ui > MainWindow_copy2_ui.py