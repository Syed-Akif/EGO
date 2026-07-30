import ctypes
import os


def lock_computer() -> bool:
    """
    Locks the current Windows session.
    """

    try:
        return bool(ctypes.windll.user32.LockWorkStation())

    except Exception:
        return False


def shutdown_computer() -> bool:
    """
    Shuts down the computer.
    """

    try:
        os.system("shutdown /s /t 0")
        return True

    except Exception:
        return False


def restart_computer() -> bool:
    """
    Restarts the computer.
    """

    try:
        os.system("shutdown /r /t 0")
        return True

    except Exception:
        return False


def sleep_computer() -> bool:
    """
    Puts the computer to sleep.
    """

    try:
        ctypes.windll.powrprof.SetSuspendState(False, True, False)
        return True

    except Exception:
        return False