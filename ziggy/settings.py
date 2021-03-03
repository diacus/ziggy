import os

HOME = os.environ["HOME"]


class Settings:
    HISTORY_PATH = os.path.join(
        HOME, os.environ.get("ZIGGY_HISTORY", ".ziggy_history")
    )
    HISTORY_LENGTH = 1000
