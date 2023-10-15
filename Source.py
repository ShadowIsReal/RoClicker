import keyboard
import os
import pydirectinput
import time
from ctypes import windll, create_unicode_buffer

print("Made by shadowisreal\n")

AutoKeybind = input("Please enter a key to press to enable/disable the autoclicker: ")
ExitKeybund = input("Please enter a key to press to stop the program (shutdown the program incase of emergency): ")

pydirectinput.Pause = False
keyboard.on_press_key(ExitKeybund, lambda _:os._exit(0))
time.sleep(2)

State = False

def GetWindowTitle():
    WindowHandle = windll.user32.GetForegroundWindow()
    WindowTextLength = windll.user32.GetWindowTextLengthW(WindowHandle)
    Buff = create_unicode_buffer(WindowTextLength + 1)
    windll.user32.GetWindowTextW(WindowHandle, Buff, WindowTextLength+1)

    if (Buff.value):
        return Buff.value
    
    return False

def ChangeState(self):
    global State
    State = not State

keyboard.on_press_key(AutoKeybind, ChangeState)

while True:
    if not GetWindowTitle() == "Roblox":
        State = False
    if State:
        pydirectinput.click()
    time.sleep(0)
