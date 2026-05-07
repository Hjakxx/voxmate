import os


# Common folders to search

def get_common_dirs():
    user = os.path.expanduser("~")
    return [
        os.path.join(user, "Desktop"),
        os.path.join(user, "Documents"),
        os.path.join(user, "Downloads"),
        os.path.join(user, "Pictures"),
        os.path.join(user, "Music"),
        os.path.join(user, "Videos")
    ]



# Search by filename
# 
def search_by_name(filename):
    if not filename:
        return False, "No filename provided"

    filename = filename.lower()
    matches = []

    for directory in get_common_dirs():
        if not os.path.exists(directory):
            continue
        for root, dirs, files in os.walk(directory):
            for f in files:
                if filename in f.lower():
                    matches.append(os.path.join(root, f))

    if matches:
        formatted = "\n".join(matches)
        return True, f"Found {len(matches)} file(s):\n{formatted}"
    else:
        return False, "No matching files found"


# 
# Search by file extension
# 
def search_by_extension(ext):
    if not ext:
        return False, "No extension provided"

    ext = ext.lower().strip().replace(".", "")  # normalize
    matches = []

    for directory in get_common_dirs():
        if not os.path.exists(directory):
            continue
        for root, dirs, files in os.walk(directory):
            for f in files:
                if f.lower().endswith("." + ext):
                    matches.append(os.path.join(root, f))

    if matches:
        formatted = "\n".join(matches)
        return True, f"Found {len(matches)} file(s):\n{formatted}"
    else:
        return False, f"No .{ext} files found"
