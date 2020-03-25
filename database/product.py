from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import Query

from database import session
from database.base import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    keyword = Column(String)
    olx_id = Column(Integer, index=True, nullable=False, unique=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    city = Column(String)
    zip = Column(String)
    region = Column(String)
    image = Column(String)
    url = Column(String)
    date_time = Column(DateTime)
    is_new = Column(Boolean, index=True)

    @staticmethod
    def get_new():
        return session.query(Product).filter(Product.is_new == True)

    @staticmethod
    def get_by_olx_id(id):
        query: Query = session.query(Product).filter(Product.olx_id == id)
        return query.first()

    def __repr__(self):
        return "<Product(id='%s', title='%s')>" % (
            self.id, self.title)

    def __str__(self):
        return self.__repr__()
