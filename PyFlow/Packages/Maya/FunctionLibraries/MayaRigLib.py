# -*- coding: UTF-8 -*-
"""
@File    : MayaRigLib.py
@Vision  : 1.0.0
@Time    : 2020/8/5 16:12
@Author  : Qing Shuang
@Email   : 2075693226@qq.com
@Software: PyCharm
"""
from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE
import pymel.core as pm


class MayaRigLib(FunctionLibraryBase):

    def __init__(self, packageName):
        super(MayaRigLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={NodeMeta.CATEGORY: 'Math', NodeMeta.KEYWORDS: []})
    def integer(x=('IntPin', 0)):
        """一个整数"""
        return int(x)

    @staticmethod
    @IMPLEMENT_NODE(returns=('BoolPin', False), meta={'Category': 'Rig', 'Keywords': []})
    def rotatePlaneIK(joint_list=("StringPin", ""), pv_locator=("StringPin", "")):
        """给骨骼链创建一套旋转平面ik绑定"""
        print 'create rotate plane ik',joint_list, pv_locator
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('BoolPin', False), nodeType=NodeTypes.Callable,
                    meta={'Category': 'Rig', 'Keywords': []})
    def fk(joint_list=("StringPin", ""), group_num=("StringPin", "")):
        """给骨骼链创建一套fk绑定"""
        print 'create fk', joint_list
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('BoolPin', False), meta={'Category': 'Rig', 'Keywords': []})
    def fkik(joint_list=("StringPin", ""), pv_locator=("StringPin", "")):
        """给骨骼链创建一套fkik绑定，具有拉伸，次级等效果"""
        print 'create fkik', joint_list, pv_locator
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", []), meta={'Category': 'Rig', 'Keywords': []})
    def joint_list():
        return pm.selected(type='joint')

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", 'locator'), meta={'Category': 'Rig', 'Keywords': []})
    def locator():
        """加载一个locator"""
        return pm.ls(type='locator')[0]
