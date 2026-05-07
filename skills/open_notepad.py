import subprocess

def run(params=None):
    try:
        subprocess.Popen("notepad.exe")
        return True, "Opening Notepad"
    except Exception:
        return False, "Failed to open Notepad"
