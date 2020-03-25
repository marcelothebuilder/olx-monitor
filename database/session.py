from sqlalchemy.orm import sessionmaker, Session

from database.engine import engine

ConfiguredSession: Session = sessionmaker(bind=engine)
session: Session = ConfiguredSession()
