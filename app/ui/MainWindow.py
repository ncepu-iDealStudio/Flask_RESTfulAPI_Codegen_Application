# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1018, 765)
        MainWindow.setStyleSheet(u"/*\u7070\u8272*/\n"
"QWidget\n"
"{\n"
"    background-color: rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    color: black;  /*\u5b57\u4f53\u989c\u8272*/\n"
"}\n"
"/*\u6309\u94ae\u6b63\u5e38\u72b6\u6001*/\n"
"QPushButton\n"
"{\n"
"    background-color:rgba(198,198,198);/*\u80cc\u666f\u8272*/\n"
"    border-style:solid;/*\u8fb9\u6846\u6837\u5f0f solid\u5b9e\u7ebf none\u65e0\u8fb9\u6846 inset/outset 3D\u8fb9\u6846*/\n"
"    border-width:1px; /*\u8fb9\u6846\u5bbd\u5ea6\u50cf\u7d20*/\n"
"    border-radius:10px;/*\u8fb9\u6846\u5706\u89d2\u534a\u5f84\u50cf\u7d20*/\n"
"    border-color:rgba(205,205,205);/*\u8fb9\u6846\u989c\u8272*/\n"
"    font-size:12pt;/*\u5b57\u4f53 \u5b57\u4f53\u5927\u5c0f*/\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"}\n"
"/*\u9f20\u6807\u6309\u4e0b\u72b6\u6001*/\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgba(198,198,220);/*\u80cc\u666f\u8272*/\n"
"    border-color:rgba(205,205,205);/*\u8fb9\u6846\u989c\u8272*/\n"
"    border-style:solid;/*\u8fb9\u6846\u6837\u5f0f solid\u5b9e"
                        "\u7ebf none\u65e0\u8fb9\u6846 inset/outset 3D\u8fb9\u6846*/\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"}\n"
"/*\u9f20\u6807\u60ac\u505c\u72b6\u6001*/\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgba(198,198,190);/*\u80cc\u666f\u8272*/\n"
"    border-color:rgba(205,205,205);/*\u8fb9\u6846\u989c\u8272*/\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"}\n"
"QLineEdit\n"
"{\n"
"    background-color:rgb(240,240,240);/*\u80cc\u666f\u8272*/\n"
"	height:20px;\n"
"    border-style:solid;/*\u8fb9\u6846\u6837\u5f0f solid\u5b9e\u7ebf none\u65e0\u8fb9\u6846 inset/outset 3D\u8fb9\u6846*/\n"
"    border-width:1px; /*\u8fb9\u6846\u5bbd\u5ea6\u50cf\u7d20*/\n"
"    border-radius:10px;/*\u8fb9\u6846\u5706\u89d2\u534a\u5f84\u50cf\u7d20*/\n"
"    border-color:rgba(205,205,205);/*\u8fb9\u6846\u989c\u8272*/\n"
"    font-size:12pt;/*\u5b57\u4f53 \u5b57\u4f53\u5927\u5c0f*/\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"    padding:6px;/*\u586b\u886c*/\n"
"}\n"
"QCheckBox\n"
"{\n"
"    color:black;/*\u5b57"
                        "\u4f53\u989c\u8272*/\n"
"    background-color:rgb(240,240,240);/*\u80cc\u666f\u8272*/\n"
"}\n"
"QComboBox\n"
"{\n"
"    background-color:rgb(240,240,240);\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"    border-style:solid;/*\u8fb9\u6846\u6837\u5f0f solid\u5b9e\u7ebf none\u65e0\u8fb9\u6846 inset/outset 3D\u8fb9\u6846*/\n"
"    border-width:1px;/*\u8fb9\u6846\u5bbd\u5ea6\u50cf\u7d20*/\n"
"    border-radius:10px;/*\u8fb9\u6846\u5706\u89d2\u534a\u5f84\u50cf\u7d20*/\n"
"    border-color:rgba(205,205,205);/*\u8fb9\u6846\u989c\u8272*/\n"
"    font-size:12pt;\n"
"}\n"
"/*\u5411\u4e0b\u7684\u4e09\u89d2\u5f62\u7bad\u5934\u6837\u5f0f*/\n"
"QComboBox::drop-down\n"
"{\n"
"     width:20px;\n"
"     border:none;\n"
"     background:transparent;\n"
" }\n"
"/*\u5411\u4e0b\u7684\u4e09\u89d2\u5f62\u7bad\u5934*/\n"
"QComboBox::down-arrow\n"
"{\n"
"    image:url(:/image/array_down.png);\n"
"}\n"
"/*\u4e0b\u62c9\u540e\u7684\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53*/\n"
"QComboBox QAbstractItemView\n"
"{\n"
" background-color: "
                        "rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"outline:none;\n"
"}\n"
"/*\u4e0b\u62c9\u6846\u4e0b\u9762\u7684item*/\n"
"QComboBox QAbstractItemView::item\n"
"{\n"
"    height:30px;\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"}\n"
"/*\u4e0b\u62c9\u6846item\u9009\u4e2d*/\n"
"QComboBox QAbstractItemView::item:selected\n"
"{\n"
"    background-color: rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"}\n"
"QLabel\n"
"{\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"font-size:12pt;\n"
"border:none;/*\u8fb9\u6846\u6837\u5f0f*/\n"
"}\n"
"QTabWidget\n"
"{\n"
"    background-color: rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"    background-color: rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"    font-size:12pt;/*\u5b57\u4f53\u5927\u5c0f*/\n"
"    height:30px; /*\u9ad8\u5ea6*/\n"
"    m"
                        "in-width:100px;/*\u5bbd\u5ea6*/\n"
"    border-top-left-radius:4px;/*\u5de6\u4e0a\u8fb9\u6846\u5706\u89d2\u534a\u5f84\u50cf\u7d20*/\n"
"    border-top-right-radius:4px;/*\u53f3\u4e0a\u8fb9\u6846\u5706\u89d2\u534a\u5f84\u50cf\u7d20*/\n"
"    margin-right: 5px;/*\u53f3\u8fb9\u8ddd  \u53f3\u5916\u8fb9\u8ddd*/\n"
"    padding-left:5px;/*\u5de6\u586b\u5145--\u5de6\u5185\u8fb9\u8ddd*/\n"
"    padding-right:5px;/*\u53f3\u586b\u5145--\u53f3\u5185\u8fb9\u8ddd*/\n"
"}\n"
"QTabBar::tab:hover\n"
"{\n"
"    background-color: rgb(198,198,208); /*\u80cc\u666f\u8272*/\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: rgb(198,198,198); /*\u80cc\u666f\u8272*/\n"
"}\n"
"QTableView,QTableWidget{\n"
"    background-color: rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"    selection-background-color:rgba(192,221,244);/*\u80cc\u666f\u8272*/;/*\u70b9\u51fb\u9009\u4e2d\u989c\u8272*/\n"
"    border:1px solid #E0DDDC;/*\u8fb9\u6846\u4e3a1\u50cf\u7d20\uff0c\u7070\u8272*/\n"
" "
                        "   gridline-color:lightgray;/*\u8fd9\u4e2a\u662f\u8868\u683c\u7684\u683c\u5b50\u7ebf\u7684\u989c\u8272\uff0c\u4e3a\u4eae\u7070*/\n"
"    font:bold 12pt;/*\u5b57\u4f53 \u5b57\u4f53\u5927\u5c0f*/\n"
"}\n"
"/*\u8868\u683c\u8868\u5934\u6837\u5f0f*/\n"
"QHeaderView::section{\n"
"    background-color:rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    border:0px solid #E0DDDC;/*\u5148\u628a\u8fb9\u6846\u5bbd\u5ea6\u8bbe\u4e3a0\uff0c\u5373\u9690\u85cf\u6240\u6709\u8868\u5934\u8fb9\u6846*/\n"
"    border-bottom:1px solid #E0DDDC;/*\u7136\u540e\u53ea\u663e\u793a\u4e0b\u8fb9\u6846\uff0c\u56e0\u4e3a\u4e0a\u8fb9\u6846\u548c\u5de6\u53f3\u8fb9\u6846\u662f\u6574\u4e2aTable\u7684\u8fb9\u6846\uff0c\u90fd\u663e\u793a\u4f1a\u67092px\u7684\u8fb9\u6846\u5bbd\u5ea6*/\n"
"    min-height:30px;;/*\u8868\u5934\u9ad8\u5ea6*/\n"
"    font-size:12pt;/*\u5b57\u4f53\u5927\u5c0f*/\n"
"}\n"
"QTreeWidget,QTreeView\n"
"{\n"
"    background-color: rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    color: rgb(79,129,168);/*\u5b57\u4f53\u989c\u8272*/\n"
""
                        "    selection-background-color:rgba(5,23,200);/*\u70b9\u51fb\u9009\u4e2d\u989c\u8272*/\n"
"    font-size:12pt;/*\u5b57\u4f53\u5927\u5c0f*/\n"
"}\n"
"\n"
"#label_table_name_7,#label_set_key_13{font-size:30px;}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/*top*/\n"
"#contentTopBg{\n"
"	background-color: #6272a4;\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid #bd93f9;\n"
"}\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"	background-color: #6272a4;\n"
"}\n"
"#leftBox{\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"#rightButtons{\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #bd93f9; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #ff79c6; border-style: solid; border-radius: 4px; }\n"
"\n"
"/*\u7070\u8272*/\n"
"QWidget\n"
"{\n"
"    background-color: rgb(221, 221, 221); /*\u80cc\u666f\u8272*/\n"
"    color: black;  /*\u5b57\u4f53\u989c\u8272*/\n"
"}\n"
"/*\u6309\u94ae\u6b63\u5e38\u72b6\u6001*/\n"
"QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;\n"
"	background-color: #6272a4;\n"
"    color: #f8f"
                        "8f2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"QCheckBox\n"
"{\n"
"    color:black;/*\u5b57\u4f53\u989c\u8272*/\n"
"    background-color:rgb(240,240,240);/*\u80cc\u666f\u8272*/\n"
"}\n"
"QComboBox{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
""
                        "	subcontrol-position: top right;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);\n"
"	background-color: #6272a4;\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"text-align:justify;\n"
"color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"font-size:12pt;\n"
"border:none;/*\u8fb9\u6846\u6837\u5f0f*/\n"
"}\n"
"QTableWidget {\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
""
                        "	background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #6272a4;\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"	background-color: #6272a4;\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"    background-color: rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"    font-size:12pt;/*\u5b57\u4f53\u5927\u5c0f*/\n"
"    height:30px; /*\u9ad8\u5ea6*/\n"
"    min-width:100px;/*\u5bbd\u5ea6*/\n"
"    border-top-left-radius:4px;/*\u5de6\u4e0a\u8fb9\u6846\u5706\u89d2\u534a\u5f84\u50cf\u7d20*/\n"
"    border-top-right-radius:4px;/*\u53f3\u4e0a\u8fb9\u6846\u5706\u89d2\u534a\u5f84\u50cf\u7d20*/\n"
"    margin-right: 5px;/*\u53f3\u8fb9\u8ddd  \u53f3\u5916\u8fb9\u8ddd*/\n"
"    padding-left:5px;/*\u5de6\u586b\u5145--\u5de6\u5185\u8fb9\u8ddd*/\n"
"    padding-right:5px;/*\u53f3\u586b\u5145--\u53f3\u5185\u8fb9\u8ddd*/\n"
"}\n"
"QTabBar::tab:hover\n"
"{\n"
"    background-c"
                        "olor: rgb(198,198,208); /*\u80cc\u666f\u8272*/\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: rgb(198,198,198); /*\u80cc\u666f\u8272*/\n"
"}\n"
"QTableView,QTableWidget{\n"
"    background-color: rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    color: black;/*\u5b57\u4f53\u989c\u8272*/\n"
"    selection-background-color:rgba(192,221,244);/*\u80cc\u666f\u8272*/;/*\u70b9\u51fb\u9009\u4e2d\u989c\u8272*/\n"
"    border:1px solid #E0DDDC;/*\u8fb9\u6846\u4e3a1\u50cf\u7d20\uff0c\u7070\u8272*/\n"
"    gridline-color:lightgray;/*\u8fd9\u4e2a\u662f\u8868\u683c\u7684\u683c\u5b50\u7ebf\u7684\u989c\u8272\uff0c\u4e3a\u4eae\u7070*/\n"
"    font:bold 12pt;/*\u5b57\u4f53 \u5b57\u4f53\u5927\u5c0f*/\n"
"}\n"
"/*\u8868\u683c\u8868\u5934\u6837\u5f0f*/\n"
"QHeaderView::section{\n"
"    background-color:rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    border:0px solid #E0DDDC;/*\u5148\u628a\u8fb9\u6846\u5bbd\u5ea6\u8bbe\u4e3a0\uff0c\u5373\u9690\u85cf\u6240\u6709\u8868\u5934\u8fb9\u6846*/\n"
"    border-bottom:1px so"
                        "lid #E0DDDC;/*\u7136\u540e\u53ea\u663e\u793a\u4e0b\u8fb9\u6846\uff0c\u56e0\u4e3a\u4e0a\u8fb9\u6846\u548c\u5de6\u53f3\u8fb9\u6846\u662f\u6574\u4e2aTable\u7684\u8fb9\u6846\uff0c\u90fd\u663e\u793a\u4f1a\u67092px\u7684\u8fb9\u6846\u5bbd\u5ea6*/\n"
"    min-height:30px;;/*\u8868\u5934\u9ad8\u5ea6*/\n"
"    font-size:12pt;/*\u5b57\u4f53\u5927\u5c0f*/\n"
"}\n"
"QTreeWidget,QTreeView\n"
"{\n"
"    background-color: rgb(240,240,240); /*\u80cc\u666f\u8272*/\n"
"    color: rgb(79,129,168);/*\u5b57\u4f53\u989c\u8272*/\n"
"    selection-background-color:rgba(5,23,200);/*\u70b9\u51fb\u9009\u4e2d\u989c\u8272*/\n"
"    font-size:12pt;/*\u5b57\u4f53\u5927\u5c0f*/\n"
"}\n"
"\n"
"#label_table_name_7,#label_set_key_13{font-size:30px;}\n"
"\n"
"#pushButton_last{}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QRadioButton"
                        "::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position"
                        ": left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4"
                        "px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: #495474; }\n"
"#bottomBar QLabel {\n"
"	background-color: #495474;\n"
"	font-size: 11px; color: #f8f8f2;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	padding-bottom: 2px; }\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.centralwidget)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.topLogo = QFrame(self.leftBox)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"image: url(:/images/images/images/PyDracula.png);\n"
"background-color:transparent;")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.topLogo)

        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy1)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.titleRightInfo)


        self.horizontalLayout_6.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.closeAppBtn)


        self.horizontalLayout_6.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.contentTopBg)

        self.main_step = QFrame(self.centralwidget)
        self.main_step.setObjectName(u"main_step")
        self.horizontalLayout_4 = QHBoxLayout(self.main_step)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackedWidget_step = QStackedWidget(self.main_step)
        self.stackedWidget_step.setObjectName(u"stackedWidget_step")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget_step.sizePolicy().hasHeightForWidth())
        self.stackedWidget_step.setSizePolicy(sizePolicy2)
        self.stackedWidget_step.setMinimumSize(QSize(1000, 35))
        self.stackedWidget_step.setStyleSheet(u"\n"
"\n"
"QLabel {\n"
"	width:100px;\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"QLabel:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}")
        self.page_step_1 = QWidget()
        self.page_step_1.setObjectName(u"page_step_1")
        self.layoutWidget_4 = QWidget(self.page_step_1)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 4, 741, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_step1 = QLabel(self.layoutWidget_4)
        self.label_step1.setObjectName(u"label_step1")
        self.label_step1.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #bd93f9;\n"
"	border-radius: 5px;	\n"
"	background-color: #bd93f9;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_step1)

        self.label_step2 = QLabel(self.layoutWidget_4)
        self.label_step2.setObjectName(u"label_step2")
        self.label_step2.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_step2)

        self.label_step3 = QLabel(self.layoutWidget_4)
        self.label_step3.setObjectName(u"label_step3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_step3.sizePolicy().hasHeightForWidth())
        self.label_step3.setSizePolicy(sizePolicy3)
        self.label_step3.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_step3)

        self.label_step4 = QLabel(self.layoutWidget_4)
        self.label_step4.setObjectName(u"label_step4")
        self.label_step4.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_step4)

        self.label_step5 = QLabel(self.layoutWidget_4)
        self.label_step5.setObjectName(u"label_step5")
        self.label_step5.setMinimumSize(QSize(0, 0))
        self.label_step5.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_step5)

        self.stackedWidget_step.addWidget(self.page_step_1)
        self.page_step_2 = QWidget()
        self.page_step_2.setObjectName(u"page_step_2")
        self.layoutWidget_9 = QWidget(self.page_step_2)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(0, 4, 741, 31))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_step1_3 = QLabel(self.layoutWidget_9)
        self.label_step1_3.setObjectName(u"label_step1_3")
        self.label_step1_3.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step1_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_step1_3)

        self.label_step2_3 = QLabel(self.layoutWidget_9)
        self.label_step2_3.setObjectName(u"label_step2_3")
        self.label_step2_3.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #bd93f9;\n"
"	border-radius: 5px;	\n"
"	background-color: #bd93f9;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step2_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_step2_3)

        self.label_step3_3 = QLabel(self.layoutWidget_9)
        self.label_step3_3.setObjectName(u"label_step3_3")
        sizePolicy3.setHeightForWidth(self.label_step3_3.sizePolicy().hasHeightForWidth())
        self.label_step3_3.setSizePolicy(sizePolicy3)
        self.label_step3_3.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step3_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_step3_3)

        self.label_step4_3 = QLabel(self.layoutWidget_9)
        self.label_step4_3.setObjectName(u"label_step4_3")
        self.label_step4_3.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step4_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_step4_3)

        self.label_step5_3 = QLabel(self.layoutWidget_9)
        self.label_step5_3.setObjectName(u"label_step5_3")
        self.label_step5_3.setMinimumSize(QSize(0, 0))
        self.label_step5_3.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step5_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_step5_3)

        self.stackedWidget_step.addWidget(self.page_step_2)
        self.page_step_3 = QWidget()
        self.page_step_3.setObjectName(u"page_step_3")
        self.layoutWidget_10 = QWidget(self.page_step_3)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(0, 4, 741, 31))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_step1_7 = QLabel(self.layoutWidget_10)
        self.label_step1_7.setObjectName(u"label_step1_7")
        self.label_step1_7.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step1_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_step1_7)

        self.label_step2_7 = QLabel(self.layoutWidget_10)
        self.label_step2_7.setObjectName(u"label_step2_7")
        self.label_step2_7.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step2_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_step2_7)

        self.label_step3_7 = QLabel(self.layoutWidget_10)
        self.label_step3_7.setObjectName(u"label_step3_7")
        sizePolicy3.setHeightForWidth(self.label_step3_7.sizePolicy().hasHeightForWidth())
        self.label_step3_7.setSizePolicy(sizePolicy3)
        self.label_step3_7.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #bd93f9;\n"
"	border-radius: 5px;	\n"
"	background-color: #bd93f9;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step3_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_step3_7)

        self.label_step4_7 = QLabel(self.layoutWidget_10)
        self.label_step4_7.setObjectName(u"label_step4_7")
        self.label_step4_7.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step4_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_step4_7)

        self.label_step5_7 = QLabel(self.layoutWidget_10)
        self.label_step5_7.setObjectName(u"label_step5_7")
        self.label_step5_7.setMinimumSize(QSize(0, 0))
        self.label_step5_7.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step5_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_step5_7)

        self.stackedWidget_step.addWidget(self.page_step_3)
        self.page_step_4 = QWidget()
        self.page_step_4.setObjectName(u"page_step_4")
        self.layoutWidget_11 = QWidget(self.page_step_4)
        self.layoutWidget_11.setObjectName(u"layoutWidget_11")
        self.layoutWidget_11.setGeometry(QRect(0, 4, 741, 31))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_step1_4 = QLabel(self.layoutWidget_11)
        self.label_step1_4.setObjectName(u"label_step1_4")
        self.label_step1_4.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step1_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_step1_4)

        self.label_step2_4 = QLabel(self.layoutWidget_11)
        self.label_step2_4.setObjectName(u"label_step2_4")
        self.label_step2_4.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step2_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_step2_4)

        self.label_step3_4 = QLabel(self.layoutWidget_11)
        self.label_step3_4.setObjectName(u"label_step3_4")
        sizePolicy3.setHeightForWidth(self.label_step3_4.sizePolicy().hasHeightForWidth())
        self.label_step3_4.setSizePolicy(sizePolicy3)
        self.label_step3_4.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step3_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_step3_4)

        self.label_step4_4 = QLabel(self.layoutWidget_11)
        self.label_step4_4.setObjectName(u"label_step4_4")
        self.label_step4_4.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #bd93f9;\n"
"	border-radius: 5px;	\n"
"	background-color: #bd93f9;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step4_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_step4_4)

        self.label_step5_4 = QLabel(self.layoutWidget_11)
        self.label_step5_4.setObjectName(u"label_step5_4")
        self.label_step5_4.setMinimumSize(QSize(0, 0))
        self.label_step5_4.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step5_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_step5_4)

        self.stackedWidget_step.addWidget(self.page_step_4)
        self.page_step_5 = QWidget()
        self.page_step_5.setObjectName(u"page_step_5")
        self.layoutWidget_12 = QWidget(self.page_step_5)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(0, 4, 741, 31))
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_step1_8 = QLabel(self.layoutWidget_12)
        self.label_step1_8.setObjectName(u"label_step1_8")
        self.label_step1_8.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step1_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_step1_8)

        self.label_step2_8 = QLabel(self.layoutWidget_12)
        self.label_step2_8.setObjectName(u"label_step2_8")
        self.label_step2_8.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step2_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_step2_8)

        self.label_step3_8 = QLabel(self.layoutWidget_12)
        self.label_step3_8.setObjectName(u"label_step3_8")
        sizePolicy3.setHeightForWidth(self.label_step3_8.sizePolicy().hasHeightForWidth())
        self.label_step3_8.setSizePolicy(sizePolicy3)
        self.label_step3_8.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step3_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_step3_8)

        self.label_step4_8 = QLabel(self.layoutWidget_12)
        self.label_step4_8.setObjectName(u"label_step4_8")
        self.label_step4_8.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step4_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_step4_8)

        self.label_step5_8 = QLabel(self.layoutWidget_12)
        self.label_step5_8.setObjectName(u"label_step5_8")
        self.label_step5_8.setMinimumSize(QSize(0, 0))
        self.label_step5_8.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid black;\n"
"	color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	border: 2px solid #bd93f9;\n"
"	border-radius: 5px;	\n"
"	background-color: #bd93f9;\n"
"    color: #f8f8f2;\n"
"}\n"
"")
        self.label_step5_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_step5_8)

        self.stackedWidget_step.addWidget(self.page_step_5)

        self.horizontalLayout_4.addWidget(self.stackedWidget_step)


        self.verticalLayout_3.addWidget(self.main_step)

        self.main_line = QFrame(self.centralwidget)
        self.main_line.setObjectName(u"main_line")
        sizePolicy3.setHeightForWidth(self.main_line.sizePolicy().hasHeightForWidth())
        self.main_line.setSizePolicy(sizePolicy3)
        self.main_line.setMinimumSize(QSize(0, 20))
        self.verticalLayout_12 = QVBoxLayout(self.main_line)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.line = QFrame(self.main_line)
        self.line.setObjectName(u"line")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy4)
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line)


        self.verticalLayout_3.addWidget(self.main_line)

        self.main_page = QFrame(self.centralwidget)
        self.main_page.setObjectName(u"main_page")
        self.horizontalLayout_2 = QHBoxLayout(self.main_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setMinimumSize(QSize(1000, 550))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.scrollArea_1 = QScrollArea(self.page_1)
        self.scrollArea_1.setObjectName(u"scrollArea_1")
        self.scrollArea_1.setGeometry(QRect(0, 0, 991, 561))
        self.scrollArea_1.setFrameShape(QFrame.NoFrame)
        self.scrollArea_1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_1 = QWidget()
        self.scrollAreaWidgetContents_1.setObjectName(u"scrollAreaWidgetContents_1")
        self.scrollAreaWidgetContents_1.setGeometry(QRect(0, 0, 991, 561))
        self.label_db_4 = QLabel(self.scrollAreaWidgetContents_1)
        self.label_db_4.setObjectName(u"label_db_4")
        self.label_db_4.setGeometry(QRect(60, -10, 141, 41))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_db_4.setFont(font2)
        self.label_9 = QLabel(self.scrollAreaWidgetContents_1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 20, 931, 51))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei"])
        font3.setBold(True)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"font-size:20px;")
        self.label_9.setFrameShape(QFrame.NoFrame)
        self.label_9.setFrameShadow(QFrame.Plain)
        self.label_9.setLineWidth(2)
        self.label_9.setTextFormat(Qt.AutoText)
        self.layoutWidget = QWidget(self.scrollAreaWidgetContents_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 70, 891, 481))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_db_type_5 = QLabel(self.layoutWidget)
        self.label_db_type_5.setObjectName(u"label_db_type_5")
        sizePolicy3.setHeightForWidth(self.label_db_type_5.sizePolicy().hasHeightForWidth())
        self.label_db_type_5.setSizePolicy(sizePolicy3)
        self.label_db_type_5.setFont(font2)

        self.horizontalLayout_27.addWidget(self.label_db_type_5)

        self.comboBox_db_type = QComboBox(self.layoutWidget)
        self.comboBox_db_type.addItem("")
        self.comboBox_db_type.setObjectName(u"comboBox_db_type")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox_db_type.sizePolicy().hasHeightForWidth())
        self.comboBox_db_type.setSizePolicy(sizePolicy5)

        self.horizontalLayout_27.addWidget(self.comboBox_db_type)

        self.horizontalLayout_27.setStretch(0, 1)
        self.horizontalLayout_27.setStretch(1, 8)

        self.verticalLayout.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_db_host_5 = QLabel(self.layoutWidget)
        self.label_db_host_5.setObjectName(u"label_db_host_5")
        self.label_db_host_5.setFont(font2)
        self.label_db_host_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_db_host_5)

        self.text_host = QLineEdit(self.layoutWidget)
        self.text_host.setObjectName(u"text_host")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.text_host.sizePolicy().hasHeightForWidth())
        self.text_host.setSizePolicy(sizePolicy6)
        self.text_host.setClearButtonEnabled(True)

        self.horizontalLayout_28.addWidget(self.text_host)

        self.horizontalLayout_28.setStretch(0, 1)
        self.horizontalLayout_28.setStretch(1, 8)

        self.verticalLayout.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_db_port_5 = QLabel(self.layoutWidget)
        self.label_db_port_5.setObjectName(u"label_db_port_5")
        self.label_db_port_5.setFont(font2)
        self.label_db_port_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_db_port_5)

        self.text_port = QLineEdit(self.layoutWidget)
        self.text_port.setObjectName(u"text_port")
        self.text_port.setClearButtonEnabled(True)

        self.horizontalLayout_29.addWidget(self.text_port)

        self.horizontalLayout_29.setStretch(0, 1)
        self.horizontalLayout_29.setStretch(1, 8)

        self.verticalLayout.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_db_user_5 = QLabel(self.layoutWidget)
        self.label_db_user_5.setObjectName(u"label_db_user_5")
        self.label_db_user_5.setFont(font2)

        self.horizontalLayout_30.addWidget(self.label_db_user_5)

        self.text_user = QLineEdit(self.layoutWidget)
        self.text_user.setObjectName(u"text_user")
        self.text_user.setClearButtonEnabled(True)

        self.horizontalLayout_30.addWidget(self.text_user)

        self.horizontalLayout_30.setStretch(0, 1)
        self.horizontalLayout_30.setStretch(1, 8)

        self.verticalLayout.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_db_password_5 = QLabel(self.layoutWidget)
        self.label_db_password_5.setObjectName(u"label_db_password_5")
        self.label_db_password_5.setFont(font2)

        self.horizontalLayout_31.addWidget(self.label_db_password_5)

        self.text_password = QLineEdit(self.layoutWidget)
        self.text_password.setObjectName(u"text_password")
        self.text_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.text_password.setClearButtonEnabled(True)

        self.horizontalLayout_31.addWidget(self.text_password)

        self.horizontalLayout_31.setStretch(0, 1)
        self.horizontalLayout_31.setStretch(1, 8)

        self.verticalLayout.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_tables_5 = QLabel(self.layoutWidget)
        self.label_tables_5.setObjectName(u"label_tables_5")
        sizePolicy3.setHeightForWidth(self.label_tables_5.sizePolicy().hasHeightForWidth())
        self.label_tables_5.setSizePolicy(sizePolicy3)
        self.label_tables_5.setFont(font2)

        self.horizontalLayout_32.addWidget(self.label_tables_5)

        self.comboBox_database = QComboBox(self.layoutWidget)
        self.comboBox_database.addItem("")
        self.comboBox_database.setObjectName(u"comboBox_database")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.comboBox_database.sizePolicy().hasHeightForWidth())
        self.comboBox_database.setSizePolicy(sizePolicy7)

        self.horizontalLayout_32.addWidget(self.comboBox_database)

        self.button_get_db_names = QPushButton(self.layoutWidget)
        self.button_get_db_names.setObjectName(u"button_get_db_names")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.button_get_db_names.sizePolicy().hasHeightForWidth())
        self.button_get_db_names.setSizePolicy(sizePolicy8)
        self.button_get_db_names.setStyleSheet(u"height:30px;")

        self.horizontalLayout_32.addWidget(self.button_get_db_names)

        self.horizontalLayout_32.setStretch(0, 1)
        self.horizontalLayout_32.setStretch(1, 7)
        self.horizontalLayout_32.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.checkBox_re = QCheckBox(self.layoutWidget)
        self.checkBox_re.setObjectName(u"checkBox_re")
        self.checkBox_re.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"\n"
"QCheckBox{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(44, 49, 58);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(221, 221, 221);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid #ff79c6;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}")

        self.horizontalLayout_33.addWidget(self.checkBox_re)


        self.verticalLayout.addLayout(self.horizontalLayout_33)

        self.scrollArea_1.setWidget(self.scrollAreaWidgetContents_1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.scrollArea_2 = QScrollArea(self.page_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 991, 641))
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 991, 641))
        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 70, 171, 20))
        self.stackedWidget_right = QStackedWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget_right.setObjectName(u"stackedWidget_right")
        self.stackedWidget_right.setGeometry(QRect(280, 0, 711, 641))
        self.page_23 = QWidget()
        self.page_23.setObjectName(u"page_23")
        self.verticalLayoutWidget_20 = QWidget(self.page_23)
        self.verticalLayoutWidget_20.setObjectName(u"verticalLayoutWidget_20")
        self.verticalLayoutWidget_20.setGeometry(QRect(20, 0, 522, 91))
        self.verticalLayout_page1_7 = QVBoxLayout(self.verticalLayoutWidget_20)
        self.verticalLayout_page1_7.setObjectName(u"verticalLayout_page1_7")
        self.verticalLayout_page1_7.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.verticalLayoutWidget_20)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.verticalLayout_page1_7.addWidget(self.label_15)

        self.label_18 = QLabel(self.verticalLayoutWidget_20)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_page1_7.addWidget(self.label_18)

        self.stackedWidget_right.addWidget(self.page_23)
        self.page_24 = QWidget()
        self.page_24.setObjectName(u"page_24")
        self.verticalLayoutWidget_21 = QWidget(self.page_24)
        self.verticalLayoutWidget_21.setObjectName(u"verticalLayoutWidget_21")
        self.verticalLayoutWidget_21.setGeometry(QRect(0, 0, 711, 551))
        self.verticalLayout_page2_7 = QVBoxLayout(self.verticalLayoutWidget_21)
        self.verticalLayout_page2_7.setObjectName(u"verticalLayout_page2_7")
        self.verticalLayout_page2_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_right_7 = QScrollArea(self.verticalLayoutWidget_21)
        self.scrollArea_right_7.setObjectName(u"scrollArea_right_7")
        self.scrollArea_right_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_right_7 = QWidget()
        self.scrollAreaWidgetContents_right_7.setObjectName(u"scrollAreaWidgetContents_right_7")
        self.scrollAreaWidgetContents_right_7.setGeometry(QRect(0, -239, 699, 1000))
        self.scrollAreaWidgetContents_right_7.setMinimumSize(QSize(0, 1000))
        self.pushButton_add_field_encrypt = QPushButton(self.scrollAreaWidgetContents_right_7)
        self.pushButton_add_field_encrypt.setObjectName(u"pushButton_add_field_encrypt")
        self.pushButton_add_field_encrypt.setGeometry(QRect(530, 440, 100, 36))
        self.label_code_7 = QLabel(self.scrollAreaWidgetContents_right_7)
        self.label_code_7.setObjectName(u"label_code_7")
        self.label_code_7.setGeometry(QRect(20, 370, 660, 51))
        self.layoutWidget1 = QWidget(self.scrollAreaWidgetContents_right_7)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 10, 311, 121))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_table_name_7 = QLabel(self.layoutWidget1)
        self.label_table_name_7.setObjectName(u"label_table_name_7")

        self.verticalLayout_9.addWidget(self.label_table_name_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_isDelete_7 = QLabel(self.layoutWidget1)
        self.label_isDelete_7.setObjectName(u"label_isDelete_7")

        self.verticalLayout_8.addWidget(self.label_isDelete_7)

        self.comboBox_select_table_logicaldeletemark = QComboBox(self.layoutWidget1)
        self.comboBox_select_table_logicaldeletemark.addItem("")
        self.comboBox_select_table_logicaldeletemark.setObjectName(u"comboBox_select_table_logicaldeletemark")

        self.verticalLayout_8.addWidget(self.comboBox_select_table_logicaldeletemark)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.layoutWidget2 = QWidget(self.scrollAreaWidgetContents_right_7)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 160, 481, 121))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_set_key_13 = QLabel(self.layoutWidget2)
        self.label_set_key_13.setObjectName(u"label_set_key_13")

        self.verticalLayout_10.addWidget(self.label_set_key_13)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_select_key_7 = QLabel(self.layoutWidget2)
        self.label_select_key_7.setObjectName(u"label_select_key_7")

        self.verticalLayout_5.addWidget(self.label_select_key_7)

        self.comboBox_select_table_businesskeyname = QComboBox(self.layoutWidget2)
        self.comboBox_select_table_businesskeyname.addItem("")
        self.comboBox_select_table_businesskeyname.setObjectName(u"comboBox_select_table_businesskeyname")

        self.verticalLayout_5.addWidget(self.comboBox_select_table_businesskeyname)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_set_key_14 = QLabel(self.layoutWidget2)
        self.label_set_key_14.setObjectName(u"label_set_key_14")

        self.verticalLayout_7.addWidget(self.label_set_key_14)

        self.comboBox_select_table_businesskeyrule = QComboBox(self.layoutWidget2)
        self.comboBox_select_table_businesskeyrule.addItem("")
        self.comboBox_select_table_businesskeyrule.setObjectName(u"comboBox_select_table_businesskeyrule")

        self.verticalLayout_7.addWidget(self.comboBox_select_table_businesskeyrule)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.verticalLayoutWidget_2 = QWidget(self.scrollAreaWidgetContents_right_7)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(9, 520, 671, 451))
        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.listWidget_encrypt = QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_encrypt.setObjectName(u"listWidget_encrypt")
        self.listWidget_encrypt.setStyleSheet(u"")
        self.listWidget_encrypt.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_13.addWidget(self.listWidget_encrypt)

        self.scrollArea_right_7.setWidget(self.scrollAreaWidgetContents_right_7)

        self.verticalLayout_page2_7.addWidget(self.scrollArea_right_7)

        self.stackedWidget_right.addWidget(self.page_24)
        self.layoutWidget3 = QWidget(self.scrollAreaWidgetContents_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 0, 279, 551))
        self.verticalLayout_left_6 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_left_6.setObjectName(u"verticalLayout_left_6")
        self.verticalLayout_left_6.setContentsMargins(0, 0, 0, 0)
        self.listWidget_table = QListWidget(self.layoutWidget3)
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_table)
        __qlistwidgetitem.setCheckState(Qt.Unchecked);
        QListWidgetItem(self.listWidget_table)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_table)
        __qlistwidgetitem1.setCheckState(Qt.PartiallyChecked);
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        QListWidgetItem(self.listWidget_table)
        self.listWidget_table.setObjectName(u"listWidget_table")
        self.listWidget_table.setStyleSheet(u"\n"
".QWidget{\n"
"background-color: #6272a4;\n"
"}\n"
"\n"
".QWidget {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
".QWidget:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
".QWidget:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"/*\u6309\u94ae\u6b63\u5e38\u72b6\u6001*/\n"
"/*\n"
"QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"*/\n"
"\n"
"QPushButton {\n"
"	border:none;\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"	background: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	backgro"
                        "und-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"	background: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"	background: transparent;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(44, 49, 58);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(221, 221, 221);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid #ff79c6;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}")
        self.listWidget_table.setBatchSize(105)

        self.verticalLayout_left_6.addWidget(self.listWidget_table)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.scrollArea_3 = QScrollArea(self.page_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(0, 0, 991, 641))
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 991, 641))
        self.label_3 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 70, 171, 20))
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 281, 551))
        self.verticalLayout_left_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_left_2.setObjectName(u"verticalLayout_left_2")
        self.verticalLayout_left_2.setContentsMargins(0, 0, 0, 0)
        self.listWidget_view = QListWidget(self.verticalLayoutWidget)
        QListWidgetItem(self.listWidget_view)
        QListWidgetItem(self.listWidget_view)
        self.listWidget_view.setObjectName(u"listWidget_view")
        self.listWidget_view.setStyleSheet(u"\n"
".QWidget{\n"
"background-color: #6272a4;\n"
"}\n"
"\n"
".QWidget {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
".QWidget:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
".QWidget:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"/*\u6309\u94ae\u6b63\u5e38\u72b6\u6001*/\n"
"/*\n"
"QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"*/\n"
"\n"
"QPushButton {\n"
"	border:none;\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"	background: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	backgro"
                        "und-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"	background: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"	background: transparent;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(44, 49, 58);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(221, 221, 221);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid #ff79c6;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}")

        self.verticalLayout_left_2.addWidget(self.listWidget_view)

        self.stackedWidget_3 = QStackedWidget(self.scrollAreaWidgetContents_6)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setGeometry(QRect(280, 0, 711, 641))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayoutWidget_22 = QWidget(self.page)
        self.verticalLayoutWidget_22.setObjectName(u"verticalLayoutWidget_22")
        self.verticalLayoutWidget_22.setGeometry(QRect(20, 0, 522, 91))
        self.verticalLayout_page1_8 = QVBoxLayout(self.verticalLayoutWidget_22)
        self.verticalLayout_page1_8.setObjectName(u"verticalLayout_page1_8")
        self.verticalLayout_page1_8.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.verticalLayoutWidget_22)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.verticalLayout_page1_8.addWidget(self.label_12)

        self.label_13 = QLabel(self.verticalLayoutWidget_22)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_page1_8.addWidget(self.label_13)

        self.stackedWidget_3.addWidget(self.page)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayoutWidget_3 = QWidget(self.page_6)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 711, 551))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6 = QScrollArea(self.verticalLayoutWidget_3)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 707, 547))
        self.label_view = QLabel(self.scrollAreaWidgetContents_4)
        self.label_view.setObjectName(u"label_view")
        self.label_view.setGeometry(QRect(30, 20, 221, 61))
        self.label_view.setFont(font2)
        self.label_14 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 90, 191, 31))
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents_4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 150, 651, 271))
        self.tableWidget.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(44, 49, 58);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(221, 221, 221);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid #ff79c6;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_6.addWidget(self.scrollArea_6)

        self.stackedWidget_3.addWidget(self.page_6)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_6)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.scrollArea_4 = QScrollArea(self.page_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(0, 0, 991, 641))
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 991, 641))
        self.layoutWidget_3 = QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(70, 0, 842, 554))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget = QTabWidget(self.layoutWidget_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setIconSize(QSize(50, 20))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(0, 400))
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget_DB = QTableWidget(self.tab)
        if (self.tableWidget_DB.columnCount() < 5):
            self.tableWidget_DB.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_DB.setObjectName(u"tableWidget_DB")
        self.tableWidget_DB.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #6272a4;\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #6272a4;\n"
"}")
        self.tableWidget_DB.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_DB.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_DB.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_3.addWidget(self.tableWidget_DB)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setMinimumSize(QSize(725, 400))
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableWidget_View = QTableWidget(self.tab_2)
        if (self.tableWidget_View.columnCount() < 2):
            self.tableWidget_View.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_View.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_View.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.tableWidget_View.setObjectName(u"tableWidget_View")
        self.tableWidget_View.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #6272a4;\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #6272a4;\n"
"}")
        self.tableWidget_View.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_View.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_View.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.tableWidget_View)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.scrollArea_5 = QScrollArea(self.page_5)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setGeometry(QRect(0, 10, 991, 641))
        self.scrollArea_5.setFrameShape(QFrame.NoFrame)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 991, 641))
        self.label_11 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(70, 0, 431, 71))
        self.label_11.setFont(font2)
        self.verticalLayoutWidget_4 = QWidget(self.scrollAreaWidgetContents_9)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(120, 110, 751, 321))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_5 = QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_34.addWidget(self.label_5)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: #6272a4;")

        self.horizontalLayout_34.addWidget(self.lineEdit)

        self.toolButton_file = QPushButton(self.verticalLayoutWidget_4)
        self.toolButton_file.setObjectName(u"toolButton_file")
        self.toolButton_file.setMinimumSize(QSize(150, 30))
        self.toolButton_file.setFont(font)
        self.toolButton_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_file.setStyleSheet(u"background-color: #6272a4;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_file.setIcon(icon4)

        self.horizontalLayout_34.addWidget(self.toolButton_file)

        self.horizontalLayout_34.setStretch(0, 1)
        self.horizontalLayout_34.setStretch(1, 9)
        self.horizontalLayout_34.setStretch(2, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_8 = QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_35.addWidget(self.label_8)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet(u"background-color: #6272a4;")

        self.horizontalLayout_35.addWidget(self.lineEdit_2)

        self.horizontalLayout_35.setStretch(0, 1)
        self.horizontalLayout_35.setStretch(1, 7)

        self.verticalLayout_11.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_10 = QLabel(self.verticalLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.horizontalLayout_36.addWidget(self.label_10)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setStyleSheet(u"background-color: #6272a4;")

        self.horizontalLayout_36.addWidget(self.lineEdit_3)

        self.horizontalLayout_36.setStretch(0, 1)
        self.horizontalLayout_36.setStretch(1, 7)

        self.verticalLayout_11.addLayout(self.horizontalLayout_36)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_9)
        self.stackedWidget.addWidget(self.page_5)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.main_page)

        self.main_step_button = QFrame(self.centralwidget)
        self.main_step_button.setObjectName(u"main_step_button")
        self.horizontalLayout = QHBoxLayout(self.main_step_button)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_last = QPushButton(self.main_step_button)
        self.pushButton_last.setObjectName(u"pushButton_last")
        sizePolicy2.setHeightForWidth(self.pushButton_last.sizePolicy().hasHeightForWidth())
        self.pushButton_last.setSizePolicy(sizePolicy2)
        self.pushButton_last.setStyleSheet(u"width:100px;\n"
"height:30px;")

        self.horizontalLayout.addWidget(self.pushButton_last)

        self.pushButton_next = QPushButton(self.main_step_button)
        self.pushButton_next.setObjectName(u"pushButton_next")
        sizePolicy2.setHeightForWidth(self.pushButton_next.sizePolicy().hasHeightForWidth())
        self.pushButton_next.setSizePolicy(sizePolicy2)
        self.pushButton_next.setStyleSheet(u"width:100px;\n"
"height:30px;")

        self.horizontalLayout.addWidget(self.pushButton_next)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.main_step_button)

        self.bottomBar = QFrame(self.centralwidget)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"background-color:transparent;")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_size_grip)


        self.verticalLayout_3.addWidget(self.bottomBar)

        self.verticalLayout_3.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_step.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_right.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4ee3\u7801\u751f\u6210\u5668", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PyDracula APP - Theme with colors based on Dracula for Python.", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_step1.setText(QCoreApplication.translate("MainWindow", u"\u2460\u6570\u636e\u5e93\u914d\u7f6e", None))
        self.label_step2.setText(QCoreApplication.translate("MainWindow", u"\u2461\u8868\u914d\u7f6e", None))
        self.label_step3.setText(QCoreApplication.translate("MainWindow", u"\u2462\u89c6\u56fe\u914d\u7f6e", None))
        self.label_step4.setText(QCoreApplication.translate("MainWindow", u"\u2463\u914d\u7f6e\u786e\u8ba4", None))
        self.label_step5.setText(QCoreApplication.translate("MainWindow", u"\u2464\u4ee3\u7801\u751f\u6210", None))
        self.label_step1_3.setText(QCoreApplication.translate("MainWindow", u"\u2460\u6570\u636e\u5e93\u914d\u7f6e", None))
        self.label_step2_3.setText(QCoreApplication.translate("MainWindow", u"\u2461\u8868\u914d\u7f6e", None))
        self.label_step3_3.setText(QCoreApplication.translate("MainWindow", u"\u2462\u89c6\u56fe\u914d\u7f6e", None))
        self.label_step4_3.setText(QCoreApplication.translate("MainWindow", u"\u2463\u914d\u7f6e\u786e\u8ba4", None))
        self.label_step5_3.setText(QCoreApplication.translate("MainWindow", u"\u2464\u4ee3\u7801\u751f\u6210", None))
        self.label_step1_7.setText(QCoreApplication.translate("MainWindow", u"\u2460\u6570\u636e\u5e93\u914d\u7f6e", None))
        self.label_step2_7.setText(QCoreApplication.translate("MainWindow", u"\u2461\u8868\u914d\u7f6e", None))
        self.label_step3_7.setText(QCoreApplication.translate("MainWindow", u"\u2462\u89c6\u56fe\u914d\u7f6e", None))
        self.label_step4_7.setText(QCoreApplication.translate("MainWindow", u"\u2463\u914d\u7f6e\u786e\u8ba4", None))
        self.label_step5_7.setText(QCoreApplication.translate("MainWindow", u"\u2464\u4ee3\u7801\u751f\u6210", None))
        self.label_step1_4.setText(QCoreApplication.translate("MainWindow", u"\u2460\u6570\u636e\u5e93\u914d\u7f6e", None))
        self.label_step2_4.setText(QCoreApplication.translate("MainWindow", u"\u2461\u8868\u914d\u7f6e", None))
        self.label_step3_4.setText(QCoreApplication.translate("MainWindow", u"\u2462\u89c6\u56fe\u914d\u7f6e", None))
        self.label_step4_4.setText(QCoreApplication.translate("MainWindow", u"\u2463\u914d\u7f6e\u786e\u8ba4", None))
        self.label_step5_4.setText(QCoreApplication.translate("MainWindow", u"\u2464\u4ee3\u7801\u751f\u6210", None))
        self.label_step1_8.setText(QCoreApplication.translate("MainWindow", u"\u2460\u6570\u636e\u5e93\u914d\u7f6e", None))
        self.label_step2_8.setText(QCoreApplication.translate("MainWindow", u"\u2461\u8868\u914d\u7f6e", None))
        self.label_step3_8.setText(QCoreApplication.translate("MainWindow", u"\u2462\u89c6\u56fe\u914d\u7f6e", None))
        self.label_step4_8.setText(QCoreApplication.translate("MainWindow", u"\u2463\u914d\u7f6e\u786e\u8ba4", None))
        self.label_step5_8.setText(QCoreApplication.translate("MainWindow", u"\u2464\u4ee3\u7801\u751f\u6210", None))
        self.label_db_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u6570\u636e\u5e93\u914d\u7f6e</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">\u8bf7\u9009\u62e9\u8981\u751f\u6210\u63a5\u53e3\u9879\u76ee\u4ee3\u7801\u7684\u76ee\u6807\u6570\u636e\u5e93\uff0c\u751f\u6210\u5668\u5c06\u9488\u5bf9\u6b64\u6570\u636e\u5e93\uff0c\u751f\u6210\u4e00\u4e2a\u5206\u5c42\u8bbe\u8ba1\u57fa\u4e8eRestful\u98ce\u683c\u7684Web\u63a5\u53e3\u9879\u76ee</span></p></body></html>", None))
        self.label_db_type_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">\u6570\u636e\u5e93\u7c7b\u578b</p></body></html>", None))
        self.comboBox_db_type.setItemText(0, QCoreApplication.translate("MainWindow", u"mysql", None))

        self.label_db_host_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">\u4e3b\u673a </p></body></html>", None))
        self.label_db_port_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">\u7aef\u53e3</p></body></html>", None))
        self.label_db_user_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">\u8d26\u53f7</p></body></html>", None))
        self.label_db_password_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">\u5bc6\u7801</p></body></html>", None))
        self.text_password.setInputMask("")
        self.label_tables_5.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93", None))
        self.comboBox_database.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bf7\u5148\u83b7\u53d6\u6570\u636e\u5e93\u540d", None))

        self.button_get_db_names.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u6570\u636e\u5e93\u540d", None))
        self.checkBox_re.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u4f4f\u6211", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u662f\u6570\u636e\u5e93\u8868\u914d\u7f6e\u9875\u9762", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u8868\u51c6\u5907</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u7528\u4e8e\u751f\u6210\u4ee3\u7801\u7684\u6570\u636e\u8868\uff0c\u5e76\u4e3a\u6bcf\u5f20\u8868\u8fdb\u884c\u76f8\u5e94\u7684\u914d\u7f6e", None))
#if QT_CONFIG(whatsthis)
        self.scrollArea_right_7.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.scrollArea_right_7.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_add_field_encrypt.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5b57\u6bb5", None))
        self.label_code_7.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u5b58\u50a8\u5b57\u6bb5\u8bbe\u7f6e(\u4e3a\u6ee1\u8db3\u5b89\u5168\u5ba1\u8ba1\u9700\u8981,\u4e00\u4e9b\u654f\u611f\u5b57\u6bb5\u53ef\u80fd\u9700\u8981\u5728\u6570\u636e\u5e93\u4e2d\u52a0\u5bc6\u5b58\u50a8\uff0c\u5982\u7528\u6237\u8eab\u4efd\u8bc1\u53f7\uff0c\u624b\u673a\u53f7\u7b49)", None))
        self.label_table_name_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">\u8fd9\u662f\u8868\u540d</span></p></body></html>", None))
        self.label_isDelete_7.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u662f\u5426\u903b\u8f91\u5220\u9664", None))
        self.comboBox_select_table_logicaldeletemark.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u903b\u8f91\u5220\u9664\u6807\u8bc6\u5b57\u6bb5", None))

        self.label_set_key_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">\u4e1a\u52a1\u4e3b\u952e\u8bbe\u7f6e</span></p></body></html>", None))
        self.label_select_key_7.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u52a1\u4e3b\u952e\u5b57\u6bb5\u9009\u62e9", None))
        self.comboBox_select_table_businesskeyname.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e1a\u52a1\u4e3b\u952e", None))

        self.label_set_key_14.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u52a1\u4e3b\u952e\u751f\u6210\u89c4\u5219", None))
        self.comboBox_select_table_businesskeyrule.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e1a\u52a1\u4e3b\u952e\u751f\u6210\u89c4\u5219", None))


        __sortingEnabled = self.listWidget_table.isSortingEnabled()
        self.listWidget_table.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_table.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem1 = self.listWidget_table.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem2 = self.listWidget_table.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem3 = self.listWidget_table.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem4 = self.listWidget_table.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem5 = self.listWidget_table.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem6 = self.listWidget_table.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem7 = self.listWidget_table.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem8 = self.listWidget_table.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem9 = self.listWidget_table.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem10 = self.listWidget_table.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem11 = self.listWidget_table.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem12 = self.listWidget_table.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem13 = self.listWidget_table.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem14 = self.listWidget_table.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem15 = self.listWidget_table.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem16 = self.listWidget_table.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        self.listWidget_table.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u662f\u89c6\u56fe\u8868\u914d\u7f6e\u9875\u9762", None))

        __sortingEnabled1 = self.listWidget_view.isSortingEnabled()
        self.listWidget_view.setSortingEnabled(False)
        ___qlistwidgetitem17 = self.listWidget_view.item(0)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem18 = self.listWidget_view.item(1)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        self.listWidget_view.setSortingEnabled(__sortingEnabled1)

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u89c6\u56fe\u51c6\u5907</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u7528\u4e8e\u751f\u6210\u4ee3\u7801\u7684\u89c6\u56fe\uff0c\u5e76\u4e3a\u6bcf\u5f20\u8868\u8fdb\u884c\u76f8\u5e94\u914d\u7f6e\u3002", None))
        self.label_view.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:400;\">TextLabel</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u63a5\u53e3\u67e5\u8be2\u5b57\u6bb5\u9009\u62e9</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">\u6570\u636e\u5e93\u914d\u7f6e</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u68c0\u67e5\u8981\u751f\u6210\u63a5\u53e3\u9879\u76ee\u4ee3\u7801\u7684\u76ee\u6807\u6570\u636e\u5e93\uff0c\u751f\u6210\u5668\u5c06\u9488\u5bf9\u6b64\u6570\u636e\u5e93\u751f\u6210\u4e00\u4e2a\u5206\u5c42\u8bbe\u8ba1\u7684\u63a5\u53e3\u9879\u76ee", None))
        ___qtablewidgetitem = self.tableWidget_DB.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u8868\u540d", None));
        ___qtablewidgetitem1 = self.tableWidget_DB.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u5b57\u6bb5", None));
        ___qtablewidgetitem2 = self.tableWidget_DB.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u903b\u8f91\u5220\u9664\u5b57\u6bb5", None));
        ___qtablewidgetitem3 = self.tableWidget_DB.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u52a1\u4e3b\u952e", None));
        ___qtablewidgetitem4 = self.tableWidget_DB.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u52a1\u4e3b\u952e\u751f\u6210\u89c4\u5219", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u6570\u636e\u8868", None))
        ___qtablewidgetitem5 = self.tableWidget_View.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u8868\u540d", None));
        ___qtablewidgetitem6 = self.tableWidget_View.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u53e3\u67e5\u8be2\u5b57\u6bb5", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u8981\u751f\u6210\u7684\u76ee\u6807\u63a5\u53e3\u9879\u76ee\u57fa\u672c\u914d\u7f6e</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u4ee3\u7801\u8def\u5f84", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.toolButton_file.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9879 \u76ee \u540d \u79f0", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u63a5 \u53e3 \u7248 \u672c", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_last.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u6b65", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: NCEPU-bj-iDeal", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi
