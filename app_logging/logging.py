import os
import sys
from datetime import datetime

import logging
from paths.configuration_folder import ConfigurationFolder


def configure_app_logging():
    logging_filename = datetime.now().strftime('olx-%Y-%m-%d.log')

    logs_folder = ConfigurationFolder.create_path_if_absent('logs')

    logging_filepath = str(logs_folder.joinpath(logging_filename))

    logging.basicConfig(filename=logging_filepath, level=os.getenv("DEFAULT_LOGGING_LEVEL", logging.DEBUG))
    handler = logging.StreamHandler(sys.stdout)
    logging.root.addHandler(handler)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
