import os
from datetime import datetime
from PIL import ImageGrab

def take_screenshot():
    try:
        # Save folder inside Pictures
        base_dir = os.path.join(os.path.expanduser("~"), "Pictures", "VoxMate_Screenshots")
        os.makedirs(base_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.png"
        path = os.path.join(base_dir, filename)

        # Capture
        img = ImageGrab.grab()
        img.save(path, "PNG")

        return True, f"Screenshot saved: {path}"
    except Exception as e:
        return False, f"Failed to capture screenshot: {e}"
