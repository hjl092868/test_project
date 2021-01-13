# -*- coding: utf-8 -*-

'''
单例模式
'''

class SingleTon():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

a = SingleTon()
b = SingleTon()
print(id(a) == id(b))