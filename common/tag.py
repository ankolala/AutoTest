#! /usr/bin/env python
# -*- coding: UTF-8 -*-

'''
测试用例标签
'''

from enum import Enum, unique

class NewTag:
    def __init__(self, desc=""):
        self.desc = desc


@unique
class Tag(Enum):
    CORE = NewTag("核心Case") 
    ALL = NewTag("全部Case")

    # 扩展标签
    V1_0_0  = NewTag("V1.0.0版本")