from dotenv import load_dotenv

from paths.configuration_folder import ConfigurationFolder


def get_path_to_configuration_file():
    return ConfigurationFolder.joinpath('.config')

def load_configuration():

    user_folder_config = get_path_to_configuration_file()
    if user_folder_config.exists():
        load_dotenv(verbose=False, dotenv_path=str(user_folder_config))
    else:
        load_dotenv(verbose=False)
