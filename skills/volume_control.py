import subprocess

NIRCMD = r"C:\nircmd\nircmd.exe"

def volume_up():
    try:
        subprocess.call([NIRCMD, "changesysvolume", "5000"])
        return True, "Volume increased"
    except Exception:
        return False, "Failed to increase volume"

def volume_down():
    try:
        subprocess.call([NIRCMD, "changesysvolume", "-5000"])
        return True, "Volume decreased"
    except Exception:
        return False, "Failed to decrease volume"

def volume_mute():
    try:
        subprocess.call([NIRCMD, "mutesysvolume", "1"])
        return True, "Volume muted"
    except Exception:
        return False, "Failed to mute volume"

def volume_unmute():
    try:
        subprocess.call([NIRCMD, "mutesysvolume", "0"])
        return True, "Volume unmuted"
    except Exception:
        return False, "Failed to unmute volume"

def volume_set(level):
    try:
        level = int(level)
        level = max(0, min(level, 100))

        sys_val = int((level / 100) * 65535)

        result = subprocess.call([NIRCMD, "setsysvolume", str(sys_val)])

        if result == 0:
            return True, f"Volume set to {level}%"
        else:
            return False, "Could not set system volume (NirCmd error)"

    except Exception:
        return False, "Failed to set volume"

def run(intent, level=None):
    if intent == "volume_up":
        return volume_up()
    if intent == "volume_down":
        return volume_down()
    if intent == "volume_mute":
        return volume_mute()
    if intent == "volume_unmute":
        return volume_unmute()
    if intent == "volume_set":
        return volume_set(level)
    return False, "Unknown volume command"
