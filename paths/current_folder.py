from pathlib import Path


class CurrentFolder:
    @staticmethod
    def get_path():
        return Path.cwd()

    @staticmethod
    def create_if_absent():
        path = CurrentFolder.get_path()
        path.mkdir(mode=0o755, exist_ok=True)
        return path

    @staticmethod
    def create_path_if_absent(*args):
        path = CurrentFolder.joinpath(*args)
        path.mkdir(mode=0o755, exist_ok=True)
        return path

    @staticmethod
    def joinpath(*args):
        return CurrentFolder.get_path().joinpath(*args)
