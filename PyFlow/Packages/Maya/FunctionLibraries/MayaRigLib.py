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

from binding_system.core.rig_operation import Rig


class MayaRigLib(FunctionLibraryBase):

    def __init__(self, packageName):
        super(MayaRigLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={NodeMeta.CATEGORY: 'Math', NodeMeta.KEYWORDS: []})
    def integer(x=('IntPin', 0)):
        """一个整数"""
        return int(x)

    @staticmethod
    @IMPLEMENT_NODE(returns=('BoolPin', True), meta={NodeMeta.CATEGORY: 'Math', NodeMeta.KEYWORDS: []})
    def Boolean(x=('BoolPin', True)):
        """返回一个布尔值"""
        return bool(x)

    @staticmethod
    @IMPLEMENT_NODE(returns=('BoolPin', False), nodeType=NodeTypes.Callable,
                    meta={'Category': 'Rig', 'Keywords': ['fk', 'rig']})
    def fk(joint_list=("StringPin", ""), group_num=("IntPin", 1)):
        """给骨骼链创建一套fk绑定"""
        from binding_system.core.functional_abstract_class.fk import FkSystem
        jnt_list = Rig.sort_by_parent_first(joint_list, reverse=False)
        FkSystem(jnt_list).create_fk_control(grp_num=group_num)
        print 'create fk --->', joint_list, type(joint_list), group_num, type(group_num)
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('BoolPin', False), nodeType=NodeTypes.Callable,
                    meta={'Category': 'Rig', 'Keywords': ['rotatePlaneIK', 'ik', 'rig']})
    def rotatePlaneIK(joint_list=("StringPin", ""), pv_locator=("StringPin", "")):
        """给骨骼链创建一套旋转平面ik绑定,具有拉伸和极向量lock设置"""
        from binding_system.core.component_rig.arm_bind import ArmBindForTest
        skjnt_list = [pm.PyNode(i) for i in joint_list]
        ArmBindForTest(skjnt_list=skjnt_list, pv_lct=pm.PyNode(pv_locator), sec_bind=False, knot=4,
                       bind_type='ik').main()
        print 'create rotate plane ik --->', joint_list, pv_locator
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=('BoolPin', False), nodeType=NodeTypes.Callable,
                    meta={'Category': 'Rig', 'Keywords': ['fkik', 'fk', 'ik', 'rig']})
    def fkik(joint_list=("StringPin", ""),
             pv_locator=("StringPin", ""),
             secondary_bind=('BoolPin', False),
             secondary_jnt_num=("IntPin", 4),
             seamless=('BoolPin', False)):
        """给骨骼链创建一套fkik绑定，具有拉伸，次级等效果"""
        from binding_system.core.component_rig.arm_bind import ArmBindForTest
        skjnt_list = [pm.PyNode(i) for i in joint_list]
        ArmBindForTest(skjnt_list=skjnt_list, pv_lct=pm.PyNode(pv_locator), sec_bind=secondary_bind, seamless=seamless,
                       knot=secondary_jnt_num, bind_type='fkik').main()
        print 'create fkik --->', joint_list, pv_locator, secondary_bind, secondary_jnt_num, seamless
        return True

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", []), nodeType=NodeTypes.Callable,
                    meta={'Category': 'Rig', 'Keywords': ['getSelectJntList', 'joint', 'rig']})
    def getJntList():
        """获取当前选择的骨骼链（Get the currently selected joint chain）"""
        return [jnt.name() for jnt in pm.selected(type='joint')]

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", 'select locator'), nodeType=NodeTypes.Callable,
                    meta={'Category': 'Rig', 'Keywords': ['locator', 'getLocator', 'rig']})
    def getLocator():
        """获取选择的locator"""
        return pm.selected(type='transform')[0]
