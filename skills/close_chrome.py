# skills/close_chrome.py
import psutil

def run(params):
    """
    Close ALL chrome.exe processes safely.
    Dispatcher expects return (success: bool, message: str)
    """
    closed_any = False

    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and proc.info['name'].lower() == "chrome.exe":
                proc.kill()
                closed_any = True
        except Exception as e:
            pass

    if closed_any:
        return True, "Chrome closed successfully."
    else:
        return False, "Chrome is not running."
