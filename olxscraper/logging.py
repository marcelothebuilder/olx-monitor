import logging
import os
from datetime import datetime
from pathlib import Path


def configure_logging():
    app_folder = Path.home().joinpath('.olx-monitor')
    app_folder.mkdir(mode=0o755, exist_ok=True)
    logs_folder = app_folder.joinpath('logs')
    logs_folder.mkdir(mode=0o755, exist_ok=True)

    logging_filename = datetime.now().strftime('olx-%Y-%m-%d.log')

    logging_filepath = str(logs_folder.joinpath(logging_filename))

    logging.basicConfig(filename=logging_filepath, level=os.getenv("DEFAULT_LOGGING_LEVEL", logging.INFO))
    logging.getLogger('scrapy_deltafetch.middleware').setLevel(logging.WARN)
