# core/nlp.py
import re

def classify(text: str):
    if not text:
        return {"intent": "unknown", "params": {}}

    text = text.lower().strip()
    text = re.sub(r"[^\w\s\.\-]", " ", text)
    text = re.sub(r"\s+", " ", text)

    
    # 1. OPEN APPLICATIONS
   
    if "open chrome" in text or "launch chrome" in text or "start chrome" in text:
        return {"intent": "open_chrome", "params": {}}

    if "open notepad" in text or "launch notepad" in text or "start notepad" in text:
        return {"intent": "open_notepad", "params": {}}

    # 2. CLOSE APPLICATIONS (specific first)
   
    if "close chrome" in text or "exit chrome" in text or "shutdown chrome" in text:
        return {"intent": "close_chrome", "params": {}}

    if "close notepad" in text or "exit notepad" in text or "shutdown notepad" in text:
        return {"intent": "close_notepad", "params": {}}

   
    # 3. VOLUME CONTROL
    # 

    # Unmute FIRST so it doesn't get detected as "mute"
    if "unmute" in text or "on" in text:
        return {"intent": "volume_unmute", "params": {}}

    # Mute (word-boundary to avoid catching "unmute")
    if re.search(r"\bmute\b", text) or "mute the volume" in text:
        return {"intent": "volume_mute", "params": {}}

    # Set volume → "set volume to 40"
    m = re.search(r"set volume to (\d{1,3})", text)
    if m:
        return {"intent": "volume_set", "params": {"level": int(m.group(1))}}

    # Increase / decrease
    if "increase volume" in text or "volume up" in text or "raise volume" in text:
        return {"intent": "volume_up", "params": {}}

    if "decrease volume" in text or "volume down" in text or "lower volume" in text:
        return {"intent": "volume_down", "params": {}}

    # 
    # 4. BRIGHTNESS CONTROL
    # 
    m = re.search(r"set brightness to (\d{1,3})", text)
    if m:
        return {"intent": "brightness_set", "params": {"level": int(m.group(1))}}

    if "increase brightness" in text or "brightness up" in text or "make it brighter" in text:
        return {"intent": "brightness_up", "params": {}}

    if "decrease brightness" in text or "brightness down" in text or "make it dimmer" in text:
        return {"intent": "brightness_down", "params": {}}

    # 
    # 5. FOLDER CREATION
    # 

    # Specific folder in location
    m = re.search(r"create a folder named ([\w\-\s]+) in ([\w\-\s]+)", text)
    if m:
        name = m.group(1).strip()
        loc = m.group(2).strip()
        return {"intent": "create_folder_specific", "params": {"name": name, "location": loc}}

    # Generic → desktop
    if "create a folder" in text or "make a folder" in text:
        return {"intent": "create_folder", "params": {}}

    # 
    # 6. FILE SEARCH
    # 

    # File by name
    m = re.search(r"(?:find|search for) file named ([\w\-\s\.]+)", text)
    if m:
        return {"intent": "search_file_name", "params": {"name": m.group(1).strip()}}

    # Simple: "find file iot"
    m = re.search(r"(?:find|search for) file ([\w\-\s\.]+)", text)
    if m:
        return {"intent": "search_file_name", "params": {"name": m.group(1).strip()}}

    # File extension: jpg, pdf, png, docx, etc.
    m = re.search(r"(?:find|search for) ([a-z0-9]+) files", text)
    if m:
        return {"intent": "search_file_extension", "params": {"extension": m.group(1).strip()}}

    # 
    # 7. SCREENSHOT
    # 
    if "take screenshot" in text or "screenshot" in text or "capture screen" in text:
        return {"intent": "take_screenshot", "params": {}}

    
    # 8. SYSTEM INFO
    
    if "system info" in text or "device info" in text or "system information" in text:
        return {"intent": "system_info", "params": {}}

    
    # FALLBACK
    
    return {"intent": "unknown", "params": {}}
