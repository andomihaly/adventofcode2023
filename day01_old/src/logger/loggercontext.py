import sys
import logging


class LoggerContext(object):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = logging.getLogger()
            cls._instance.setLevel(logging.INFO)
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            cls._instance.addHandler(handler)
            cls._instance.info("New logger is created.")
        cls._instance.info("Ask logger")
        return cls._instance


