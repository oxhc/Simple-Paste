from time import sleep

from pynput import keyboard

CTRL_V_CALLBACK = None

def listen():  # 键盘监听函数
    print("listening")

    def ctrl_v():
        print("<ctrl>+v")
        if not CTRL_V_CALLBACK is None:
            sleep(0.1)
            CTRL_V_CALLBACK()


    with keyboard.GlobalHotKeys({'<ctrl>+v': ctrl_v}) as h:
        h.join()
