import os

from toapi.settings import Settings


class MySettings(Settings):
    """
    Create custom configuration
    """
    storage = {
        "PATH": os.getcwd(),
        "DB_URL": None
    }
