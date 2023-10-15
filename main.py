# 导入sys
import sys

import pyperclip
# from system_hotkey import SystemHotkey

import core

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtCore import Slot, Signal, QStringListModel, QThread
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
# 导入我们生成的界面
import main_window


# 继承QWidget类，以获取其属性和方法
import listen_keyboard

class ListenThread(QThread):  # 截屏监听线程，监听函数一定要放在后台线程里康康说明那个join了吗（￣︶￣）↗　
    def __init__(self):
        super().__init__()

    def run(self):
        listen_keyboard.listen()

listenThread = ListenThread()


class MainWindow(QMainWindow):
    hotkeySignal = Signal()
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = core.BufferController()
        self.pause_listen = False
        self.pmodel = None
        self.bind()

    @Slot()
    def get_paste(self):
        pdata = pyperclip.paste()
        pMatrix = core.parse_matrix(pdata)
        self.controller.set_buffer_list(core.flat_matrix(pMatrix))
        self.plist = self.controller.buffer_list.copy()
        if self.controller.buffer_list is not None and len(self.controller.buffer_list) > 0:
            print("First item copied: " + self.controller.buffer_list[0])
            pyperclip.copy(self.controller.buffer_list[0])
        self.controller2ui()
        self.ui.textBrowser.setText(pdata)

    def controller2ui(self):
        self.ui.current_label.setText(self.controller.current())
        self.ui.next_label.setText(self.controller.preview_next())
        self.ui.previous_label.setText(self.controller.preview_previous())

        if self.pmodel is None:
            self.pmodel = QStringListModel()
        self.pmodel.setStringList(self.controller.buffer_list[self.controller.current_index+1:])
        self.ui.listView.setModel(self.pmodel)

    def error2ui(self):
        pass
        # if self.controller.error:
        #     self.pause_listen = True
        #     self.ui.pause_btn.setText("Start")
        #     self.errorMsg(self.controller.error_msg, "Information")
        #     self.controller.error = False

    def errorMsg(self, msg, title="Error"):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(msg)
        msgBox.exec()

    @Slot()
    def next(self):
        next_val = self.controller.next()
        if next_val is None:
            self.error2ui()
            return
        print("Put " + next_val + " to clipboard")
        pyperclip.copy(next_val)
        self.controller2ui()

    @Slot()
    def previous(self):
        prev_val = self.controller.previous()
        if prev_val is None:
            self.error2ui()
            return
        pyperclip.copy(prev_val)
        self.controller2ui()

    @Slot()
    def hotKey_activated(self):
        print("call next")
        self.next()

    @Slot()
    def pause_or_start(self):
        if self.pause_listen:
            self.pause_listen = False
            self.ui.pause_btn.setText("Pause")
        else:
            self.pause_listen = True
            self.ui.pause_btn.setText("Start")

    def bind(self):
        global listenThread

        def hotLambda():
            if not self.pause_listen:
                self.hotkeySignal.emit()

        self.ui.pushButton.clicked.connect(self.get_paste)
        self.ui.next_btn.clicked.connect(self.next)
        self.ui.prev_btn.clicked.connect(self.previous)
        self.hotkeySignal.connect(self.hotKey_activated)
        self.ui.pause_btn.clicked.connect(self.pause_or_start)

        self.ui.actionexit.triggered.connect(QApplication.quit)

        listen_keyboard.CTRL_V_CALLBACK = hotLambda


    def closeEvent(self, event):
        global listenThread
        listenThread.terminate()  # 结束此进程


# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
     # 创建监听线程

    listenThread.start()


    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MainWindow()
    window.show()

    # 结束QApplication
    sys.exit(app.exec())