import ctypes

def is_admin():
    """Checks if the script is running with admin privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except AttributeError:
        # This might happen on non-Windows systems
        return False