# !/user/bin/env python
# coding=utf-8
# @project : Flask_RESTfulAPI_Codegen_Application
# @author  : ChengKai
# @file   : window_generate.py
# @ide    : PyCharm
# @time   : 2022-10-12 16:15:38
'''
this is function description
'''
# import module your need


from types import MethodType


# 将自己负责的函数复制到此处
def generate_init(self):
    '''
    代码生成页初始化，完善qt designer不能完成的内容，包括组件添加，事件添加，变量定义
    :return:
    '''
    pass

def generate(self):
    '''
    代码生成页主要代码
    :return:
    '''
    pass



# 将函数添加到对象中
def add_func(self):
    '''
    添加该.py文件的方法到对象中
    :param self: 添加函数的对象
    :return:
    '''
    self.generate_init = MethodType(generate_init, self)
    self.generate = MethodType(generate, self)