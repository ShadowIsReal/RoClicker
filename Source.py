import keyboard
import os
import pydirectinput
import time
from ctypes import windll, create_unicode_buffer

print("Made by shadowisreal\n")

AutoKeybind = False
ExitKeybind = False

print("Checking for previous config...")

if os.path.exists("C:/Users/"+os.getlogin()+"/.RoClicker/config.txt"):
    print("Config Found!")
    Keybinds = open("C:/Users/"+os.getlogin()+"/.RoClicker/config.txt", "r").read().replace("\n", " ").split(" ")
    AutoKeybind = Keybinds[1]
    ExitKeybind = Keybinds[3]
    print("Config Loaded: \n\nAutoclickerKeybind: "+AutoKeybind+"\nEmergencyExitKeybind: "+ExitKeybind)
else:
    print("No Config Found!\n")

if not AutoKeybind:
    AutoKeybind = input("Please enter a key to press to enable/disable the autoclicker: ")
    ExitKeybind = input("Please enter a key to press to stop the program (shutdown the program incase of emergency): ")

    print("Saving Config!")

    ConfigString = "AutoclickerKeybind: "+AutoKeybind+"\nEmergencyExitKeybind: "+ExitKeybind

    if os.path.exists("C:/Users/"+os.getlogin()+"/.RoClicker"):
        ConfigFile = os.path.join("C:/Users/"+os.getlogin()+"/.RoClicker", "config.txt")
        ConfigFile = open(ConfigFile, "w")
        ConfigFile.write(ConfigString)
        ConfigFile.close()
    else:
        os.system("cd C:/Users/"+os.getlogin()+"/ && mkdir .RoClicker")
        ConfigFile = os.path.join("C:/Users/"+os.getlogin()+"/.RoClicker", "config.txt")
        ConfigFile = open(ConfigFile, "w")
        ConfigFile.write(ConfigString)
        ConfigFile.close()

    print("Config Saved, RoClicker is working!")

keyboard.on_press_key(ExitKeybind, lambda _:os._exit(0))
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

def DisableAuto(self):
    global State
    State = False

keyboard.on_press_key(AutoKeybind, ChangeState)
keyboard.on_press_key("esc", DisableAuto)

while True:
    if not GetWindowTitle() == "Roblox":
        State = False
    if State:
        pydirectinput.click()
    time.sleep(0)
