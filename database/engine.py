from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

engine: Engine = create_engine('sqlite:///olx.sqlite', encoding='latin1', echo=False)
