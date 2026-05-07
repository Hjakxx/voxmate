import platform
import psutil
import os

def get_system_info():
    try:
        info = {}

        # Basic OS + hardware
        info["OS"] = platform.system() + " " + platform.release()
        info["Version"] = platform.version()
        info["Processor"] = platform.processor() or "Unknown CPU"
        info["Machine"] = platform.machine()

        # RAM info
        mem = psutil.virtual_memory()
        info["Total RAM"] = f"{round(mem.total / (1024**3), 2)} GB"
        info["Available RAM"] = f"{round(mem.available / (1024**3), 2)} GB"

        # Disk info (C drive only)
        disk = psutil.disk_usage(os.path.expanduser("~"))
        info["Disk Total"] = f"{round(disk.total / (1024**3), 2)} GB"
        info["Disk Free"] = f"{round(disk.free / (1024**3), 2)} GB"

        # Format response
        output_lines = [
            f"Operating System: {info['OS']}",
            f"OS Version: {info['Version']}",
            f"Processor: {info['Processor']}",
            f"Architecture: {info['Machine']}",
            f"Total RAM: {info['Total RAM']}",
            f"Available RAM: {info['Available RAM']}",
            f"Disk Total: {info['Disk Total']}",
            f"Disk Free: {info['Disk Free']}",
        ]

        formatted = "\n".join(output_lines)

        return True, formatted

    except Exception as e:
        return False, f"Failed to get system info: {e}"
