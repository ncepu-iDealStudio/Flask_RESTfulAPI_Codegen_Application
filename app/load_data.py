# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : load_data.py
# @ide    : PyCharm
# @time   : 2023-01-17 21:20:49
'''
数据处理，LoadData类将通过多线程进行复杂的数据处理，避免页面阻塞
'''
# import module your need
import time

import pymysql
from PySide6 import QtCore

from PySide6.QtCore import QObject, QThread, Signal

from app import generate
from app.utils.checkSqlLink import SQLHandler


# 创建该类的实例后，通过moveToThread使得其方法可以通过多线程的方式进行
class LoadData(QObject):

    # 实例化信号
    sig_load_dbname = Signal(str, str, str, str)  # 开始获取数据库名信号
    sig_load_dbname_comp = Signal(dict)  # 获取数据库名完成信号
    sig_load_table = Signal()  # 开始加载表数据信号
    sig_load_table_comp = Signal(dict)  # 表数据加载完成信号
    sig_load_view = Signal()  # 开始加载视图信号
    sig_load_view_comp = Signal(dict)  # 视图加载完成信号
    sig_load_generate = Signal(dict, str)  # 开始生成代码信号
    sig_load_generate_comp = Signal(dict)  # 代码生成完成信号

    @QtCore.Slot()
    def load_tables(self):
        '''
        加载表数据
        :return:
        '''
        table_info = SQLHandler.generate_tables_information()
        self.sig_load_table_comp.emit(table_info)
        return

    @QtCore.Slot()
    def load_views(self):
        '''
        加载视图数据
        :return:
        '''
        view_info = SQLHandler.generate_views_information()
        self.sig_load_view_comp.emit(view_info)

    @QtCore.Slot()
    def load_dbname(self, host, username, password, port):
        result = {}
        try:
            conn = pymysql.connect(
                host=host,
                user=username,
                passwd=password,
                port=int(port),
            )
            cur = conn.cursor()
            cur.execute('SHOW DATABASES')
            dbnames = cur.fetchall()

            result = {'code': 2000, 'data': dbnames}
        except Exception as e:
            result = {'code': 5001, 'data': str(e)}

        finally:
            self.sig_load_dbname_comp.emit(result)

    @QtCore.Slot()
    def load_generate(self, table_config, session_id):
        '''
        生成代码
        :param table_config:
        :param session_id:
        :return:
        '''
        result = generate.start(table_config, session_id, "127.0.0.1")
        self.sig_load_generate_comp.emit(result)


