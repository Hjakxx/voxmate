import subprocess
import os

def run(params=None):
    # Try default install path, fallback to chrome in PATH
    paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "chrome.exe"
    ]
    for p in paths:
        try:
            if os.path.exists(p):
                subprocess.Popen(p)
            else:
                subprocess.Popen(p, shell=True)
            return True, "Opening Chrome"
        except Exception:
            continue
    return False, "Failed to open Chrome"
