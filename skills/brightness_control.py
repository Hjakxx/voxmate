# Uses screen_brightness_control (pip install screen_brightness_control)
import screen_brightness_control as sbc

def brightness_up():
    try:
        current = sbc.get_brightness()[0]
        new_level = min(current + 10, 100)
        sbc.set_brightness(new_level)
        return True, f"Brightness increased to {new_level}%"
    except Exception:
        return False, "Failed to increase brightness"

def brightness_down():
    try:
        current = sbc.get_brightness()[0]
        new_level = max(current - 10, 0)
        sbc.set_brightness(new_level)
        return True, f"Brightness decreased to {new_level}%"
    except Exception:
        return False, "Failed to decrease brightness"

def brightness_set(level):
    try:
        level = int(level)
        level = max(0, min(level, 100))
        sbc.set_brightness(level)
        return True, f"Brightness set to {level}%"
    except Exception:
        return False, "Failed to set brightness"
