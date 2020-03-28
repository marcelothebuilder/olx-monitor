import logging

from database.engine import engine
from database.session import session
from database.product import Product
from database.target import Target

logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)
