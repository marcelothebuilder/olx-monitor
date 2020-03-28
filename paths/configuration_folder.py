from pathlib import Path


class ConfigurationFolder:
    @staticmethod
    def get_path():
        return Path.home().joinpath('.olx-monitor')

    @staticmethod
    def create_if_absent():
        path = ConfigurationFolder.get_path()
        path.mkdir(mode=0o755, exist_ok=True)
        return path

    @staticmethod
    def create_path_if_absent(*args):
        path = ConfigurationFolder.joinpath(*args)
        path.mkdir(mode=0o755, exist_ok=True)
        return path

    @staticmethod
    def joinpath(*args):
        return ConfigurationFolder.get_path().joinpath(*args)
