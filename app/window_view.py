# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : window_view.py
# @ide    : PyCharm
# @time   : 2022-10-12 16:14:17
'''
this is function description
'''
# import module your need


from types import MethodType


# 将自己负责的函数复制到此处
def view_config_init(self):
    '''
    视图页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
    :return:
    '''
    pass

def view_config(self):
    '''
    视图配置页主要代码
    :return:
    '''

    # 进入下一步前，完成相关配置并完成对主要数据sql_data的修改
    self.ui.stackedWidget.setCurrentIndex(1)



# 将函数添加到对象中
def add_func(self):
    '''
    添加该.py文件的方法到对象中
    :param self: 添加函数的对象
    :return:
    '''
    self.view_config_init = MethodType(view_config_init, self)
    self.view_config = MethodType(view_config, self)