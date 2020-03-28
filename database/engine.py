from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from paths.configuration_folder import ConfigurationFolder

db_file = ConfigurationFolder.joinpath('olx.db')
engine: Engine = create_engine(f'sqlite:///{str(db_file)}', encoding='latin1', echo=False)
