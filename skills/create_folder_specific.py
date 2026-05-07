import os

def resolve_location(loc: str):
    loc = loc.lower()
    user_home = os.path.expanduser("~")
    common_paths = {
        "desktop": os.path.join(user_home, "Desktop"),
        "downloads": os.path.join(user_home, "Downloads"),
        "documents": os.path.join(user_home, "Documents"),
        "pictures": os.path.join(user_home, "Pictures"),
        "music": os.path.join(user_home, "Music"),
        "videos": os.path.join(user_home, "Videos"),
    }
    if loc in common_paths:
        return common_paths[loc]
    if "drive" in loc:
        letter = loc[0].upper()
        return f"{letter}:/"
    return common_paths["desktop"]

def run(params):
    name = params.get("name") or "NewFolder"
    location = params.get("location") or "desktop"
    base_path = resolve_location(location)
    target_path = os.path.join(base_path, name)
    try:
        os.makedirs(target_path, exist_ok=True)
        return True, f"Created folder '{name}' in {location}"
    except Exception:
        return False, "Failed to create folder in the specified location"
