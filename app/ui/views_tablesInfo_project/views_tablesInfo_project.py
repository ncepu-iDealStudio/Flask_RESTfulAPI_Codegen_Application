# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'views_tablesInfo_project.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QTabWidget, QWidget)
import app.ui.views_tablesInfo_project.res.images_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(838, 493)
        Form.setStyleSheet(u"font-faimly:\u5fae\u8f6f\u96c5\u9ed1;")
        self.tabWidget_first = QTabWidget(Form)
        self.tabWidget_first.setObjectName(u"tabWidget_first")
        self.tabWidget_first.setGeometry(QRect(100, 50, 661, 381))
        self.tabWidget_first.setStyleSheet(u"QTabWidget::pane{\n"
                                           "min-width:70px;\n"
                                           "min-height:25px;\n"
                                           "border-top: 2px solid;\n"
                                           "\n"
                                           "}\n"
                                           "\n"
                                           "QTabBar::tab {\n"
                                           "\n"
                                           "min-width:70px;\n"
                                           "\n"
                                           "min-height:25px;\n"
                                           "\n"
                                           "color: white;\n"
                                           "\n"
                                           "font:12px \"Microsoft YaHei\";\n"
                                           "\n"
                                           "border: 0px solid;\n"
                                           "\n"
                                           "\n"
                                           "\n"
                                           "}\n"
                                           "\n"
                                           "QTabBar::tab:selected{\n"
                                           "\n"
                                           "min-width:70px;\n"
                                           "\n"
                                           "min-height:25px;\n"
                                           "color: white;\n"
                                           "\n"
                                           "font:13px \"Microsoft YaHei\";\n"
                                           "\n"
                                           "border: 0px solid;\n"
                                           "\n"
                                           "border-bottom: 2px solid;\n"
                                           "\n"
                                           "border-color: #4796f0;\n"
                                           "\n"
                                           "}")
        self.tab_view = QWidget()
        self.tab_view.setObjectName(u"tab_view")
        self.checkBox_isCheckAll = QCheckBox(self.tab_view)
        self.checkBox_isCheckAll.setObjectName(u"checkBox_isCheckAll")
        self.checkBox_isCheckAll.setGeometry(QRect(20, 0, 79, 20))
        self.checkBox_isCheckAll.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_text = QLabel(self.tab_view)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setGeometry(QRect(170, 0, 361, 81))
        self.label_text.setStyleSheet(u"")
        self.pushButton_lastStep = QPushButton(self.tab_view)
        self.pushButton_lastStep.setObjectName(u"pushButton_lastStep")
        self.pushButton_lastStep.setGeometry(QRect(70, 300, 75, 24))
        self.pushButton_lastStep.setStyleSheet(u"QPushButton {\n"
                                               "	background-color: rgb(107, 146, 255);\n"
                                               "	color: rgb(255, 255, 255);\n"
                                               "	border-radius: 5px;\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "	background-color: qlineargradient(spread:pad, x1:0.238636, y1:0.239, x2:1, y2:1, stop:0 rgba(107, 146, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                               "}\n"
                                               "QPushButton:pressed {\n"
                                               "	padding-top:1px;\n"
                                               "	padding-left:1px;\n"
                                               "}\n"
                                               "")
        self.pushButton_nextStep = QPushButton(self.tab_view)
        self.pushButton_nextStep.setObjectName(u"pushButton_nextStep")
        self.pushButton_nextStep.setGeometry(QRect(500, 300, 75, 24))
        self.pushButton_nextStep.setStyleSheet(u"QPushButton {\n"
                                               "	background-color: rgb(107, 146, 255);\n"
                                               "	color: rgb(255, 255, 255);\n"
                                               "	border-radius: 5px;\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "	background-color: qlineargradient(spread:pad, x1:0.238636, y1:0.239, x2:1, y2:1, stop:0 rgba(107, 146, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                               "}\n"
                                               "QPushButton:pressed {\n"
                                               "	padding-top:1px;\n"
                                               "	padding-left:1px;\n"
                                               "}")
        self.label_2 = QLabel(self.tab_view)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 0, 1, 100))
        self.label_2.setStyleSheet(u"background-color: rgb(75,84,102);")
        self.tabWidget_first.addTab(self.tab_view, "")
        self.tab_tables_info = QWidget()
        self.tab_tables_info.setObjectName(u"tab_tables_info")
        self.tabWidget_table_info = QTabWidget(self.tab_tables_info)
        self.tabWidget_table_info.setObjectName(u"tabWidget_table_info")
        self.tabWidget_table_info.setGeometry(QRect(0, 70, 611, 111))
        self.tabWidget_table_info.setStyleSheet(u"\n"
                                                "QTabWidget::pane{\n"
                                                "min-width:70px;\n"
                                                "min-height:25px;\n"
                                                "border-top: 2px solid;\n"
                                                "\n"
                                                "}\n"
                                                "\n"
                                                "QTabBar::tab {\n"
                                                "font-size:10px;\n"
                                                "min-width:70px;\n"
                                                "\n"
                                                "min-height:25px;\n"
                                                "\n"
                                                "color: white;\n"
                                                "\n"
                                                "font:12px \"Microsoft YaHei\";\n"
                                                "\n"
                                                "border: -1px solid;\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "}\n"
                                                "\n"
                                                "QTabBar::tab:selected{\n"
                                                "\n"
                                                "min-width:70px;\n"
                                                "\n"
                                                "min-height:25px;\n"
                                                "color: white;\n"
                                                "\n"
                                                "font:11px \"Microsoft YaHei\";\n"
                                                "\n"
                                                "border: 0px solid;\n"
                                                "\n"
                                                "border-bottom: 2px solid;\n"
                                                "\n"
                                                "border-color: #4796f0;\n"
                                                "\n"
                                                "}")
        self.tab_table = QWidget()
        self.tab_table.setObjectName(u"tab_table")
        self.tabWidget_table_info.addTab(self.tab_table, "")
        self.tab_view_2 = QWidget()
        self.tab_view_2.setObjectName(u"tab_view_2")
        self.tabWidget_table_info.addTab(self.tab_view_2, "")
        self.label_text_2 = QLabel(self.tab_tables_info)
        self.label_text_2.setObjectName(u"label_text_2")
        self.label_text_2.setGeometry(QRect(10, 0, 591, 61))
        self.label_text_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_lastStep_2 = QPushButton(self.tab_tables_info)
        self.pushButton_lastStep_2.setObjectName(u"pushButton_lastStep_2")
        self.pushButton_lastStep_2.setGeometry(QRect(70, 300, 75, 24))
        self.pushButton_lastStep_2.setStyleSheet(u"QPushButton {\n"
                                                 "	background-color: rgb(107, 146, 255);\n"
                                                 "	color: rgb(255, 255, 255);\n"
                                                 "	border-radius: 5px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-color: qlineargradient(spread:pad, x1:0.238636, y1:0.239, x2:1, y2:1, stop:0 rgba(107, 146, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                 "}\n"
                                                 "QPushButton:pressed {\n"
                                                 "	padding-top:1px;\n"
                                                 "	padding-left:1px;\n"
                                                 "}")
        self.pushButton_nextStep_2 = QPushButton(self.tab_tables_info)
        self.pushButton_nextStep_2.setObjectName(u"pushButton_nextStep_2")
        self.pushButton_nextStep_2.setGeometry(QRect(500, 300, 75, 24))
        self.pushButton_nextStep_2.setStyleSheet(u"QPushButton {\n"
                                                 "	background-color: rgb(107, 146, 255);\n"
                                                 "	color: rgb(255, 255, 255);\n"
                                                 "	border-radius: 5px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-color: qlineargradient(spread:pad, x1:0.238636, y1:0.239, x2:1, y2:1, stop:0 rgba(107, 146, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                 "}\n"
                                                 "QPushButton:pressed {\n"
                                                 "	padding-top:1px;\n"
                                                 "	padding-left:1px;\n"
                                                 "}")
        self.tabWidget_first.addTab(self.tab_tables_info, "")
        self.tab_project = QWidget()
        self.tab_project.setObjectName(u"tab_project")
        self.pushButton_lastStep_3 = QPushButton(self.tab_project)
        self.pushButton_lastStep_3.setObjectName(u"pushButton_lastStep_3")
        self.pushButton_lastStep_3.setGeometry(QRect(70, 300, 75, 24))
        self.pushButton_lastStep_3.setStyleSheet(u"QPushButton {\n"
                                                 "	background-color: rgb(107, 146, 255);\n"
                                                 "	color: rgb(255, 255, 255);\n"
                                                 "	border-radius: 5px;\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-color: qlineargradient(spread:pad, x1:0.238636, y1:0.239, x2:1, y2:1, stop:0 rgba(107, 146, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                 "}\n"
                                                 "QPushButton:pressed {\n"
                                                 "	padding-top:1px;\n"
                                                 "	padding-left:1px;\n"
                                                 "}")
        self.pushButton_toStart = QPushButton(self.tab_project)
        self.pushButton_toStart.setObjectName(u"pushButton_toStart")
        self.pushButton_toStart.setGeometry(QRect(500, 300, 75, 24))
        self.pushButton_toStart.setStyleSheet(u"QPushButton {\n"
                                              "	background-color: rgb(107, 146, 255);\n"
                                              "	color: rgb(255, 255, 255);\n"
                                              "	border-radius: 5px;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "	background-color: qlineargradient(spread:pad, x1:0.238636, y1:0.239, x2:1, y2:1, stop:0 rgba(107, 146, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                              "}\n"
                                              "QPushButton:pressed {\n"
                                              "	padding-top:1px;\n"
                                              "	padding-left:1px;\n"
                                              "}")
        self.label = QLabel(self.tab_project)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 5, 221, 21))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_path = QLineEdit(self.tab_project)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setGeometry(QRect(180, 50, 400, 19))
        self.lineEdit_path.setStyleSheet(u"background-color: transparent;\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 1px solid;\n"
                                         "border-color: rgb(75,84,102);")
        self.lineEdit_name = QLineEdit(self.tab_project)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(180, 119, 400, 20))
        self.lineEdit_name.setStyleSheet(u"background-color: transparent;\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 1px solid;\n"
                                         "border-color: rgb(75,84,102);")
        self.lineEdit_version = QLineEdit(self.tab_project)
        self.lineEdit_version.setObjectName(u"lineEdit_version")
        self.lineEdit_version.setGeometry(QRect(180, 187, 400, 20))
        self.lineEdit_version.setStyleSheet(u"background-color: transparent;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border: 1px solid;\n"
                                            "border-color: rgb(75,84,102);")
        self.label_path = QLabel(self.tab_project)
        self.label_path.setObjectName(u"label_path")
        self.label_path.setGeometry(QRect(50, 50, 72, 16))
        self.label_path.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_name = QLabel(self.tab_project)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(57, 110, 81, 31))
        self.label_name.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_version = QLabel(self.tab_project)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setGeometry(QRect(57, 187, 91, 21))
        self.label_version.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tabWidget_first.addTab(self.tab_project, "")
        self.label_main = QLabel(Form)
        self.label_main.setObjectName(u"label_main")
        self.label_main.setGeometry(QRect(0, 0, 821, 481))
        self.label_main.setPixmap(QPixmap(u":/background/background.png"))
        self.label_main.setScaledContents(True)
        self.pushButton_minimize = QPushButton(Form)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        self.pushButton_minimize.setGeometry(QRect(710, 40, 31, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_minimize.sizePolicy().hasHeightForWidth())
        self.pushButton_minimize.setSizePolicy(sizePolicy)
        self.pushButton_minimize.setMinimumSize(QSize(20, 0))
        self.pushButton_minimize.setMaximumSize(QSize(40, 16777215))
        self.pushButton_minimize.setStyleSheet(u"QPushButton {	\n"
                                               "	border: none;\n"
                                               "	border-radius: 6px;\n"
                                               "	background-color: transparent;\n"
                                               "}\n"
                                               "QPushButton:pressed {\n"
                                               "	padding-top:1px;\n"
                                               "	padding-left:1px;\n"
                                               "}")
        icon = QIcon()
        icon.addFile(u":/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_minimize.setIcon(icon)
        self.pushButton_close = QPushButton(Form)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(740, 40, 31, 31))
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        self.pushButton_close.setMinimumSize(QSize(20, 0))
        self.pushButton_close.setMaximumSize(QSize(40, 16777215))
        self.pushButton_close.setStyleSheet(u"QPushButton {	\n"
                                            "	border: none;\n"
                                            "	border-radius: 6px;\n"
                                            "	background-color: transparent;\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "	padding-top:1px;\n"
                                            "	padding-left:1px;\n"
                                            "}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon1)
        self.pushButton_ncepu = QPushButton(Form)
        self.pushButton_ncepu.setObjectName(u"pushButton_ncepu")
        self.pushButton_ncepu.setGeometry(QRect(40, 30, 61, 51))
        self.pushButton_ncepu.setStyleSheet(u"QPushButton {	\n"
                                            "	border-image: url(:/icons/ncepu.png);\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "	padding-top:7px;\n"
                                            "	padding-left:7px;\n"
                                            "}")
        self.label_main.raise_()
        self.tabWidget_first.raise_()
        self.pushButton_minimize.raise_()
        self.pushButton_close.raise_()
        self.pushButton_ncepu.raise_()

        self.retranslateUi(Form)

        self.tabWidget_first.setCurrentIndex(0)
        self.tabWidget_table_info.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBox_isCheckAll.setText(QCoreApplication.translate("Form", u"\u5168\u9009", None))
        self.label_text.setText(QCoreApplication.translate("Form",
                                                           u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">\u89c6\u56fe\u51c6\u5907</span></p><p><span style=\" color:#ffffff;\">\u8bf7\u9009\u62e9\u7528\u4e8e\u751f\u6210\u4ee3\u7801\u7684\u89c6\u56fe\uff0c\u5e76\u4e3a\u6bcf\u5f20\u8868\u8fdb\u884c\u76f8\u5e94\u7684\u914d\u7f6e</span></p></body></html>",
                                                           None))
        self.pushButton_lastStep.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u6b65", None))
        self.pushButton_nextStep.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u6b65", None))
        self.label_2.setText("")
        self.tabWidget_first.setTabText(self.tabWidget_first.indexOf(self.tab_view),
                                        QCoreApplication.translate("Form", u"\u89c6\u56fe\u51c6\u5907", None))
        self.tabWidget_table_info.setTabText(self.tabWidget_table_info.indexOf(self.tab_table),
                                             QCoreApplication.translate("Form", u"\u6570\u636e\u5e93", None))
        self.tabWidget_table_info.setTabText(self.tabWidget_table_info.indexOf(self.tab_view_2),
                                             QCoreApplication.translate("Form", u"\u89c6\u56fe", None))
        self.label_text_2.setText(QCoreApplication.translate("Form",
                                                             u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\"> \u6570\u636e\u5e93\u914d\u7f6e</span></p><p><span style=\" font-size:10pt;\"> \u8bf7\u68c0\u67e5\u8981\u751f\u6210\u63a5\u53e3\u9879\u76ee\u4ee3\u7801\u7684\u76ee\u6807\u6570\u636e\u5e93\uff0c\u751f\u6210\u5668\u5c06\u9488\u5bf9\u6b64\u6570\u636e\u5e93\u751f\u6210\u4e00\u4e2a\u5206\u5c42\u8bbe\u8ba1\u7684\u63a5\u53e3\u9879\u76ee</span></p></body></html>",
                                                             None))
        self.pushButton_lastStep_2.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u6b65", None))
        self.pushButton_nextStep_2.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u6b65", None))
        self.tabWidget_first.setTabText(self.tabWidget_first.indexOf(self.tab_tables_info),
                                        QCoreApplication.translate("Form", u"\u6570\u636e\u5e93\u914d\u7f6e", None))
        self.pushButton_lastStep_3.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u6b65", None))
        self.pushButton_toStart.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u751f\u6210", None))
        self.label.setText(QCoreApplication.translate("Form",
                                                      u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">\u8981\u751f\u6210\u7684\u76ee\u6807\u63a5\u53e3\u9879\u76ee\u57fa\u672c\u914d\u7f6e</span></p></body></html>",
                                                      None))
        self.lineEdit_path.setInputMask("")
        self.label_path.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u4ee3\u7801\u8def\u5f84", None))
        self.label_name.setText(QCoreApplication.translate("Form",
                                                           u"<html><head/><body><p><img src=\":/icons/asterisk.png\">\u9879\u76ee\u540d\u79f0</p></body></html>",
                                                           None))
        self.label_version.setText(QCoreApplication.translate("Form",
                                                              u"<html><head/><body><p><img src=\":/icons/asterisk.png\"/>\u63a5\u53e3\u7248\u672c</p></body></html>",
                                                              None))
        self.tabWidget_first.setTabText(self.tabWidget_first.indexOf(self.tab_project),
                                        QCoreApplication.translate("Form", u"\u57fa\u672c\u914d\u7f6e", None))
        self.label_main.setText("")
        # if QT_CONFIG(tooltip)
        self.pushButton_minimize.setToolTip(QCoreApplication.translate("Form", u"Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.pushButton_minimize.setText("")
        # if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(QCoreApplication.translate("Form", u"Close", None))
        # endif // QT_CONFIG(tooltip)
        self.pushButton_close.setText("")
        self.pushButton_ncepu.setText("")
    # retranslateUi
