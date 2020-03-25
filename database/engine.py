from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from pathlib import Path

app_folder = Path.home().joinpath('.olx-monitor')
app_folder.mkdir(mode=0o755, exist_ok=True)
db_file = app_folder.joinpath('olx.db')
engine: Engine = create_engine(f'sqlite:///{str(db_file)}', encoding='latin1', echo=False)
