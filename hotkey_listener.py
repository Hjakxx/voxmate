import keyboard
from main import run_once

HOTKEY = "ctrl+shift+v"

print(f"[VoxMate] Hotkey mode active. Press {HOTKEY} to speak.")

keyboard.add_hotkey(HOTKEY, run_once)

keyboard.wait()  # keeps script running
