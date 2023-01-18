# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : load_data.py
# @ide    : PyCharm
# @time   : 2023-01-17 21:20:49
'''
this is function description
'''
# import module your need
import time

from PySide6 import QtCore

from PySide6.QtCore import QObject, QThread, Signal

from app import generate
from app.utils.checkSqlLink import SQLHandler


class LoadData(QObject):

    sig_load_table = Signal()
    sig_load_table_comp = Signal(dict)
    sig_load_view = Signal()
    sig_load_view_comp = Signal(dict)
    sig_load_generate = Signal(dict, str)
    sig_load_generate_comp = Signal(dict)

    @QtCore.Slot()
    def load_tables(self):
        table_info = SQLHandler.generate_tables_information()
        self.sig_load_table_comp.emit(table_info)
        return

    @QtCore.Slot()
    def load_views(self):
        view_info = SQLHandler.generate_views_information()
        self.sig_load_view_comp.emit(view_info)

    @QtCore.Slot()
    def load_dbname(self):
        pass

    @QtCore.Slot()
    def load_generate(self, table_config, session_id):
        result = generate.start(table_config, session_id, "127.0.0.1")
        self.sig_load_generate_comp.emit(result)


class LoadThreada(QObject):
    signal = Signal()

class LoadThread(QThread):


    la = LoadThreada()

    def run(self):
        tables_info = SQLHandler.generate_tables_information()
        print(tables_info)
        self.la.signal.emit()

