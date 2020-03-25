from pathlib import Path

from dotenv import load_dotenv


def load_configuration():
    app_folder = Path.home().joinpath('.olx-monitor')
    user_folder_config = app_folder.joinpath('.config')
    if user_folder_config.exists():
        load_dotenv(verbose=False, dotenv_path=str(user_folder_config))
    else:
        load_dotenv(verbose=False)
