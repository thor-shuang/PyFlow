import os
RESOURCES_DIR = os.path.dirname(os.path.realpath(__file__)) + "/res/"

from PyFlow.UI.Tool import REGISTER_TOOL
from PyFlow.Packages.PyflowBase import PACKAGE_NAME
from PyFlow.Packages.PyflowBase.Tools.TestTool import TestTool


REGISTER_TOOL(PACKAGE_NAME, TestTool())