## Copyright 2015-2019 Ilgar Lunin, Pedro Cabrera

## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at

##     http://www.apache.org/licenses/LICENSE-2.0

## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.


from PyFlow.Packages.Base.Nodes.switchOnString import switchOnString
from PyFlow.Packages.Base.Nodes.getVar import getVar
from PyFlow.Packages.Base.Nodes.setVar import setVar
from PyFlow.Packages.Base.Nodes.sequence import sequence
from PyFlow.Packages.Base.Nodes.pythonNode import pythonNode
from PyFlow.Packages.Base.Nodes.commentNode import commentNode
from PyFlow.Packages.Base.Nodes.stickyNote import stickyNote
from PyFlow.Packages.Base.Nodes.reroute import reroute
from PyFlow.Packages.Base.Nodes.rerouteExecs import rerouteExecs
from PyFlow.Packages.Base.Nodes.graphNodes import (
    graphInputs,
    graphOutputs
)
from PyFlow.Packages.Base.Nodes.floatRamp import floatRamp
from PyFlow.Packages.Base.Nodes.colorRamp import colorRamp

from PyFlow.Packages.Base.Nodes.compound import compound
from PyFlow.Packages.Base.Nodes.constant import constant
from PyFlow.Packages.Base.Nodes.convertTo import convertTo
from PyFlow.Packages.Base.Nodes.makeDict import makeDict
from PyFlow.Packages.Base.Nodes.makeAnyDict import makeAnyDict

from PyFlow.Packages.Base.Nodes.forLoopBegin import forLoopBegin
from PyFlow.Packages.Base.Nodes.whileLoopBegin import whileLoopBegin

from PyFlow.Packages.Base.Nodes.imageDisplay import imageDisplay
from PyFlow.Packages.Base.UI.UIImageDisplayNode import UIImageDisplayNode

from PyFlow.Packages.Base.UI.UISwitchOnStringNode import UISwitchOnString
from PyFlow.Packages.Base.UI.UIGetVarNode import UIGetVarNode
from PyFlow.Packages.Base.UI.UISetVarNode import UISetVarNode
from PyFlow.Packages.Base.UI.UISequenceNode import UISequenceNode
from PyFlow.Packages.Base.UI.UICommentNode import UICommentNode
from PyFlow.Packages.Base.UI.UIStickyNote import UIStickyNote
from PyFlow.Packages.Base.UI.UIRerouteNodeSmall import UIRerouteNodeSmall
from PyFlow.Packages.Base.UI.UIPythonNode import UIPythonNode
from PyFlow.Packages.Base.UI.UIGraphNodes import (
    UIGraphInputs,
    UIGraphOutputs
)
from PyFlow.Packages.Base.UI.UIFloatRamp import UIFloatRamp
from PyFlow.Packages.Base.UI.UIColorRamp import UIColorRamp

from PyFlow.Packages.Base.UI.UICompoundNode import UICompoundNode
from PyFlow.Packages.Base.UI.UIConstantNode import UIConstantNode
from PyFlow.Packages.Base.UI.UIConvertToNode import UIConvertToNode
from PyFlow.Packages.Base.UI.UIMakeDictNode import UIMakeDictNode
from PyFlow.Packages.Base.UI.UIForLoopBeginNode import UIForLoopBeginNode
from PyFlow.Packages.Base.UI.UIWhileLoopBeginNode import UIWhileLoopBeginNode

from PyFlow.UI.Canvas.UINodeBase import UINodeBase


def createUINode(raw_instance):
    if isinstance(raw_instance, getVar):
        return UIGetVarNode(raw_instance)
    if isinstance(raw_instance, setVar):
        return UISetVarNode(raw_instance)
    if isinstance(raw_instance, switchOnString):
        return UISwitchOnString(raw_instance)
    if isinstance(raw_instance, sequence):
        return UISequenceNode(raw_instance)
    if isinstance(raw_instance, commentNode):
        return UICommentNode(raw_instance)
    if isinstance(raw_instance, stickyNote):
        return UIStickyNote(raw_instance)
    if isinstance(raw_instance, reroute) or isinstance(raw_instance, rerouteExecs):
        return UIRerouteNodeSmall(raw_instance)
    if isinstance(raw_instance, graphInputs):
        return UIGraphInputs(raw_instance)
    if isinstance(raw_instance, graphOutputs):
        return UIGraphOutputs(raw_instance)
    if isinstance(raw_instance, compound):
        return UICompoundNode(raw_instance)
    if isinstance(raw_instance, pythonNode):
        return UIPythonNode(raw_instance)
    if isinstance(raw_instance, constant):
        return UIConstantNode(raw_instance)
    if isinstance(raw_instance, convertTo):
        return UIConvertToNode(raw_instance)
    if isinstance(raw_instance, makeDict):
        return UIMakeDictNode(raw_instance)
    if isinstance(raw_instance, makeAnyDict):
        return UIMakeDictNode(raw_instance)
    if isinstance(raw_instance, floatRamp):
        return UIFloatRamp(raw_instance)
    if isinstance(raw_instance, colorRamp):
        return UIColorRamp(raw_instance)
    if isinstance(raw_instance, imageDisplay):
        return UIImageDisplayNode(raw_instance)
    if isinstance(raw_instance,forLoopBegin):
        return UIForLoopBeginNode(raw_instance)
    if isinstance(raw_instance,whileLoopBegin):
        return UIWhileLoopBeginNode(raw_instance)
    return UINodeBase(raw_instance)
