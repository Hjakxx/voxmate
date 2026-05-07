import os
from datetime import datetime

def run(params=None):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = "VoxFolder_" + datetime.now().strftime("%H%M%S")
    path = os.path.join(desktop, folder_name)
    try:
        os.makedirs(path, exist_ok=True)
        return True, f"Created folder: {folder_name}"
    except Exception:
        return False, "Failed to create folder"
