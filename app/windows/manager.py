from app.windows.power import (
    lock_computer,
    shutdown_computer,
    restart_computer,
    sleep_computer,
)


class WindowsManager:
    """
    Service layer for Windows system operations.
    """

    def lock(self) -> bool:
        return lock_computer()

    def shutdown(self) -> bool:
        return shutdown_computer()

    def restart(self) -> bool:
        return restart_computer()

    def sleep(self) -> bool:
        return sleep_computer()