import ctypes

MB_OK = 0x0
MB_ICONINFORMATION = 0x40
MB_ICONERROR = 0x10

def success_message(message="Task executed successfully"):
    ctypes.windll.user32.MessageBoxW(
        0,
        message,
        "VoxMate",
        MB_OK | MB_ICONINFORMATION
    )

def error_message(message="Task execution failed"):
    ctypes.windll.user32.MessageBoxW(
        0,
        message,
        "VoxMate",
        MB_OK | MB_ICONERROR
    )
