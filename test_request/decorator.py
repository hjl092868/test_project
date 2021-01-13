# -*- coding:utf-8 -*-

'''
装饰器
'''

# 装饰器格式
import datetime


def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


#普通装饰器
def decorator_test(func):
    def wrapper(*args, **kwargs):
        print('程序开始')
        func(*args, **kwargs)
        print('程序结束')
    return wrapper

@decorator_test
def dec_test():
    print('bbb')

# dec_test()
'''
打印出来是
程序开始
bbb
程序结束
'''


#能带入参数的装饰器
def decorator_param(s):
    def wrapper2(func):
        def wrapper(*args, **kwargs):
            if s:
                print('程序开始并打印时间',datetime.datetime.now())
            else:
                print('程序开始')
            func(*args, **kwargs)
        return wrapper
    return wrapper2

@decorator_param(111)
def dec_param_test():
    print('ccc')

# dec_param_test()
'''
打印出来是
程序开始并打印时间 2020-12-23 14:20:47.596423
ccc
'''


#不带参数的类装饰器
class Decorator():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('程序开始')
        self.func( *args, **kwargs)
        print('程序结束')

@Decorator
def class_decorator_test():
    print('bbb')

# class_decorator_test()


#带参数的类装饰器
class DecoratorParam():
    def __init__(self, s=0):
        self.s = s

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.s:
                print('程序开始并打印时间')
            else:
                print('程序开始但不打印时间')
            func(*args, **kwargs)
        return wrapper

@DecoratorParam()
def class_decorator_param_test():
    print('bbb')

class_decorator_param_test()