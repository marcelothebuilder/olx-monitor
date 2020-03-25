from sqlalchemy import Column, Integer, String, Boolean

from database.base import Base
from database.session import session

from sqlalchemy import update


class Target(Base):
    __tablename__ = 'target'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    keyword = Column(String)
    state = Column(String)
    state_region = Column(String)
    region_subregion = Column(String)
    city = Column(String)
    category = Column(String)
    is_new = Column(Boolean)

    @staticmethod
    def all():
        return session.query(Target).order_by(Target.id)

    @staticmethod
    def mark_all_as_not_new():
        stmt = update(Target).values(is_new = False)
        session.execute(stmt)
        session.commit()

    def __repr__(self):
        return "<Target(id='%s', title='%s')>" % (
            self.id, self.keyword)

    def __str__(self):
        return self.__repr__()

