import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.5
lB = Button.left
rB = Button.right
l_pos = [(189, 433), (285, 527), (372, 529)]
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay, lB, rB):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.l_button = lB
        self.r_button = rB
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.position = l_pos[0]
                mouse.click(self.r_button)
                mouse.position = l_pos[1]
                time.sleep(self.delay)
                mouse.position = l_pos[2]
                mouse.click(self.l_button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, lB, rB)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
    elif key == KeyCode(char='y'):
        print(mouse.position)


with Listener(on_press=on_press) as listener:
    listener.join()
