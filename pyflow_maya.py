import sys
from PyFlow.App import PyFlow
from PySide2.QtWidgets import QApplication

from PySide2 import QtWidgets
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance


def get_maya_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QMainWindow)


def main():
    # app = QApplication(sys.argv)

    instance = PyFlow.instance(parent=get_maya_window(), software="maya")
    if instance is not None:
        # app.setActiveWindow(instance)
        instance.show()

        # try:
        #     sys.exit(app.exec_())
        # except Exception as e:
        #     print(e)


if __name__ == '__main__':
    main()
