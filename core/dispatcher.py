"""
Routes intents to skill modules.
"""
from skills import open_chrome, close_chrome, open_notepad, create_folder, create_folder_specific, volume_control, brightness_control
from skills import screenshot 
from skills import system_info


def execute(intent: str, params: dict):
    if intent == "open_chrome":
        return open_chrome.run(params)
    if intent == "close_chrome":
        return close_chrome.run(params)
    if intent == "open_notepad":
        return open_notepad.run(params)
    if intent == "create_folder":
        return create_folder.run(params)
    if intent == "create_folder_specific":
        return create_folder_specific.run(params)
   
    if intent == "brightness_up":
        return brightness_control.brightness_up()
    if intent == "brightness_down":
        return brightness_control.brightness_down()
    if intent == "brightness_set":
        return brightness_control.brightness_set(params.get("level"))
    if intent == "volume_up":
        return volume_control.run("volume_up")

    if intent == "volume_down":
        return volume_control.run("volume_down")

    if intent == "volume_mute":
        return volume_control.run("volume_mute")

    if intent == "volume_unmute":
        return volume_control.run("volume_unmute")

    if intent == "volume_set":
        return volume_control.run("volume_set", params.get("level"))
    
    from skills import search_files

    if intent == "search_file_name":
        return search_files.search_by_name(params.get("name"))

    if intent == "search_file_extension":
        return search_files.search_by_extension(params.get("ext"))

    if intent == "take_screenshot":
        return screenshot.take_screenshot()

    if intent == "system_info":
        return system_info.get_system_info()


    return False, "I don't recognize this command."
