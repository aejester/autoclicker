import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key

class Executor(threading.Thread):
    def __init__(self, delay, steps):
        super(Executor, self).__init__()
        self.delay = delay
        self.steps = steps
        self.running = False
        self.program_running = True

    def start_run(self):
        self.running = True
    
    def stop_running(self):
        self.running = False

    def exit(self):
        self.stop_running()
        self.program_running = False
    
    def run(self, keyboard, mouse):
        if self.program_running:
            if self.running:
                if "r" in self.steps[0]:
                    n = step.split(" ")[1]
                    is_inf = False
                    if n == "n":
                        is_inf = True
                        self.loop(keyboard, mouse, int(0), is_inf)
                    else:
                        self.loop(keyboard, mouse, int(n), is_inf)
                    break
                else:
                    for step in self.steps:
                        self.run_step(step)
                    

    def loop(self, keyboard, mouse, count, infinity):
        ct = 0

        while self.running:

            if not is_inf and ct == count:
                break

            for step in self.steps:
                self.run_step(step)
            
            ct += 1

    def run_step(self, step):
        if not ("r" in step) and not ("#" in step):
            key = KeyCode.from_vk(int(step.split(" ")[1]))

            if "p" in step:
                keyboard.press(key)
            elif "r" in step:
                keyboard.release(key)
            elif "t" in step:
                keyboard.tap(key)
            else:
                if "m" in step:
                    mouse.click()
                else:
                    print("unknown instruction in step '"+step+"'")
