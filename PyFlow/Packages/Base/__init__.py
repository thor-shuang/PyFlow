"""Base package
"""
PACKAGE_NAME = 'Base'
from collections import OrderedDict

from PyFlow.UI.UIInterfaces import IPackage

# Pins
from PyFlow.Packages.Base.Pins.AnyPin import AnyPin
from PyFlow.Packages.Base.Pins.BoolPin import BoolPin
from PyFlow.Packages.Base.Pins.ExecPin import ExecPin
from PyFlow.Packages.Base.Pins.FloatPin import FloatPin
from PyFlow.Packages.Base.Pins.IntPin import IntPin
from PyFlow.Packages.Base.Pins.StringPin import StringPin

# Function based nodes
from PyFlow.Packages.Base.FunctionLibraries.ArrayLib import ArrayLib
from PyFlow.Packages.Base.FunctionLibraries.BoolLib import BoolLib
from PyFlow.Packages.Base.FunctionLibraries.DefaultLib import DefaultLib
from PyFlow.Packages.Base.FunctionLibraries.FloatLib import FloatLib
from PyFlow.Packages.Base.FunctionLibraries.IntLib import IntLib
from PyFlow.Packages.Base.FunctionLibraries.MathLib import MathLib
from PyFlow.Packages.Base.FunctionLibraries.MathAbstractLib import MathAbstractLib
from PyFlow.Packages.Base.FunctionLibraries.RandomLib import RandomLib
from PyFlow.Packages.Base.FunctionLibraries.PathLib import PathLib

# Class based nodes
from PyFlow.Packages.Base.Nodes.branch import branch
from PyFlow.Packages.Base.Nodes.tick import tick
from PyFlow.Packages.Base.Nodes.charge import charge
from PyFlow.Packages.Base.Nodes.delay import delay
from PyFlow.Packages.Base.Nodes.deltaTime import deltaTime
from PyFlow.Packages.Base.Nodes.doN import doN
from PyFlow.Packages.Base.Nodes.doOnce import doOnce
from PyFlow.Packages.Base.Nodes.flipFlop import flipFlop
from PyFlow.Packages.Base.Nodes.forLoop import forLoop
from PyFlow.Packages.Base.Nodes.forLoopBegin import forLoopBegin
from PyFlow.Packages.Base.Nodes.loopEnd import loopEnd
from PyFlow.Packages.Base.Nodes.whileLoopBegin import whileLoopBegin
from PyFlow.Packages.Base.Nodes.forEachLoop import forEachLoop
from PyFlow.Packages.Base.Nodes.forLoopWithBreak import forLoopWithBreak
from PyFlow.Packages.Base.Nodes.retriggerableDelay import retriggerableDelay
from PyFlow.Packages.Base.Nodes.sequence import sequence
from PyFlow.Packages.Base.Nodes.switchOnString import switchOnString
from PyFlow.Packages.Base.Nodes.timer import timer
from PyFlow.Packages.Base.Nodes.whileLoop import whileLoop
from PyFlow.Packages.Base.Nodes.getVar import getVar
from PyFlow.Packages.Base.Nodes.setVar import setVar
from PyFlow.Packages.Base.Nodes.reroute import reroute
from PyFlow.Packages.Base.Nodes.rerouteExecs import rerouteExecs
from PyFlow.Packages.Base.Nodes.makeArray import makeArray
from PyFlow.Packages.Base.Nodes.makeList import makeList
from PyFlow.Packages.Base.Nodes.makeDict import makeDict
from PyFlow.Packages.Base.Nodes.makeAnyDict import makeAnyDict
from PyFlow.Packages.Base.Nodes.makeDictElement import makeDictElement
from PyFlow.Packages.Base.Nodes.dictKeys import dictKeys
from PyFlow.Packages.Base.Nodes.floatRamp import floatRamp
from PyFlow.Packages.Base.Nodes.colorRamp import colorRamp
from PyFlow.Packages.Base.Nodes.stringToArray import stringToArray
from PyFlow.Packages.Base.Nodes.cliexit import cliexit


from PyFlow.Packages.Base.Nodes.consoleOutput import consoleOutput
from PyFlow.Packages.Base.Nodes.address import address
from PyFlow.Packages.Base.Nodes.graphNodes import graphInputs, graphOutputs
from PyFlow.Packages.Base.Nodes.pythonNode import pythonNode
from PyFlow.Packages.Base.Nodes.compound import compound
from PyFlow.Packages.Base.Nodes.constant import constant
from PyFlow.Packages.Base.Nodes.convertTo import convertTo
from PyFlow.Packages.Base.Nodes.imageDisplay import imageDisplay


from PyFlow.Packages.Base.Nodes.commentNode import commentNode
from PyFlow.Packages.Base.Nodes.stickyNote import stickyNote

from PyFlow.Packages.Base.Tools.ScreenshotTool import ScreenshotTool
from PyFlow.Packages.Base.Tools.NodeBoxTool import NodeBoxTool
from PyFlow.Packages.Base.Tools.SearchResultsTool import SearchResultsTool
from PyFlow.Packages.Base.Tools.AlignLeftTool import AlignLeftTool
from PyFlow.Packages.Base.Tools.AlignRightTool import AlignRightTool
from PyFlow.Packages.Base.Tools.AlignTopTool import AlignTopTool
from PyFlow.Packages.Base.Tools.AlignBottomTool import AlignBottomTool
from PyFlow.Packages.Base.Tools.HistoryTool import HistoryTool
from PyFlow.Packages.Base.Tools.PropertiesTool import PropertiesTool
from PyFlow.Packages.Base.Tools.VariablesTool import VariablesTool
from PyFlow.Packages.Base.Tools.CompileTool import CompileTool
from PyFlow.Packages.Base.Tools.LoggerTool import LoggerTool

from PyFlow.Packages.Base.Exporters.PythonScriptExporter import PythonScriptExporter

# Factories
from PyFlow.Packages.Base.Factories.UIPinFactory import createUIPin
from PyFlow.Packages.Base.Factories.PinInputWidgetFactory import getInputWidget
from PyFlow.Packages.Base.Factories.UINodeFactory import createUINode

# Prefs widgets
from PyFlow.Packages.Base.PrefsWidgets.General import GeneralPreferences
from PyFlow.Packages.Base.PrefsWidgets.InputPrefs import InputPreferences
from PyFlow.Packages.Base.PrefsWidgets.ThemePrefs import ThemePreferences


_FOO_LIBS = {
    ArrayLib.__name__: ArrayLib(PACKAGE_NAME),
    BoolLib.__name__: BoolLib(PACKAGE_NAME),
    DefaultLib.__name__: DefaultLib(PACKAGE_NAME),
    FloatLib.__name__: FloatLib(PACKAGE_NAME),
    IntLib.__name__: IntLib(PACKAGE_NAME),
    MathLib.__name__: MathLib(PACKAGE_NAME),
    MathAbstractLib.__name__: MathAbstractLib(PACKAGE_NAME),
    RandomLib.__name__: RandomLib(PACKAGE_NAME),
    PathLib.__name__: PathLib(PACKAGE_NAME),
}


_NODES = {
    branch.__name__: branch,
    charge.__name__: charge,
    delay.__name__: delay,
    deltaTime.__name__: deltaTime,
    doN.__name__: doN,
    doOnce.__name__: doOnce,
    flipFlop.__name__: flipFlop,
    forLoop.__name__: forLoop,
    forLoopBegin.__name__: forLoopBegin,
    loopEnd.__name__: loopEnd,
    forLoopWithBreak.__name__: forLoopWithBreak,
    retriggerableDelay.__name__: retriggerableDelay,
    sequence.__name__: sequence,
    switchOnString.__name__: switchOnString,
    timer.__name__: timer,
    whileLoop.__name__: whileLoop,
    whileLoopBegin.__name__: whileLoopBegin,
    commentNode.__name__: commentNode,
    stickyNote.__name__: stickyNote,
    getVar.__name__: getVar,
    setVar.__name__: setVar,
    reroute.__name__: reroute,
    rerouteExecs.__name__: rerouteExecs,
    graphInputs.__name__: graphInputs,
    graphOutputs.__name__: graphOutputs,
    compound.__name__: compound,
    pythonNode.__name__: pythonNode,
    makeArray.__name__: makeArray,
    makeList.__name__: makeList,
    makeDict.__name__: makeDict,
    makeAnyDict.__name__: makeAnyDict,
    makeDictElement.__name__: makeDictElement,
    consoleOutput.__name__: consoleOutput,
    forEachLoop.__name__: forEachLoop,
    address.__name__: address,
    constant.__name__: constant,
    tick.__name__: tick,
    convertTo.__name__: convertTo,
    dictKeys.__name__: dictKeys,
    floatRamp.__name__: floatRamp,
    colorRamp.__name__: colorRamp,
    stringToArray.__name__: stringToArray,
    imageDisplay.__name__: imageDisplay,
    cliexit.__name__: cliexit
}

_PINS = {
    AnyPin.__name__: AnyPin,
    BoolPin.__name__: BoolPin,
    ExecPin.__name__: ExecPin,
    FloatPin.__name__: FloatPin,
    IntPin.__name__: IntPin,
    StringPin.__name__: StringPin,
}

# Toolbar will be created in following order
_TOOLS = OrderedDict()
_TOOLS[CompileTool.__name__] = CompileTool
_TOOLS[ScreenshotTool.__name__] = ScreenshotTool
_TOOLS[AlignLeftTool.__name__] = AlignLeftTool
_TOOLS[AlignRightTool.__name__] = AlignRightTool
_TOOLS[AlignTopTool.__name__] = AlignTopTool
_TOOLS[AlignBottomTool.__name__] = AlignBottomTool
_TOOLS[HistoryTool.__name__] = HistoryTool
_TOOLS[PropertiesTool.__name__] = PropertiesTool
_TOOLS[VariablesTool.__name__] = VariablesTool
_TOOLS[NodeBoxTool.__name__] = NodeBoxTool
_TOOLS[SearchResultsTool.__name__] = SearchResultsTool
_TOOLS[LoggerTool.__name__] = LoggerTool

_EXPORTERS = OrderedDict()
_EXPORTERS[PythonScriptExporter.__name__] = PythonScriptExporter


_PREFS_WIDGETS = OrderedDict()
_PREFS_WIDGETS["General"] = GeneralPreferences
_PREFS_WIDGETS["Input"] = InputPreferences
_PREFS_WIDGETS["Theme"] = ThemePreferences


class Base(IPackage):
    """Base pyflow package
    """
    def __init__(self):
        super(Base, self).__init__()

    @staticmethod
    def GetExporters():
        return _EXPORTERS

    @staticmethod
    def GetFunctionLibraries():
        # return _FOO_LIBS
        return {}

    @staticmethod
    def GetNodeClasses():
        # return _NODES
        return {}

    @staticmethod
    def GetPinClasses():
        return _PINS

    @staticmethod
    def GetToolClasses():
        return _TOOLS

    @staticmethod
    def UIPinsFactory():
        return createUIPin

    @staticmethod
    def UINodesFactory():
        return createUINode

    @staticmethod
    def PinsInputWidgetFactory():
        return getInputWidget

    @staticmethod
    def PrefsWidgets():
        return _PREFS_WIDGETS
