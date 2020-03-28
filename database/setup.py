from database import Product, Target, engine, session
import logging

logging = logging.getLogger(__name__)


def run_database_setup():

    Product.__table__.create(engine, checkfirst=True)
    Target.__table__.create(engine, checkfirst=True)

    keywords = [
        'switch',
        'psp',
        'metal gear',
        '3ds',
        'pokemon',
        'nintendo',
        'gamecube',
        'vita',
        'ps4',
        'moto snap',
        'resident evil',
        'snes',
        'wii',
        'gameboy',
        'game boy',
        'ps3',
        'dead space'
    ]

    for k in keywords:
        target = Target(keyword=k,
                        state='mg',
                        state_region='regiao-de-uberlandia-e-uberaba',
                        region_subregion='triangulo-mineiro',
                        city='uberlandia',
                        category='videogames',
                        is_new=True)

        is_already_there = session.query(Target).filter_by(keyword=k,
                                                           state='mg',
                                                           state_region='regiao-de-uberlandia-e-uberaba',
                                                           region_subregion='triangulo-mineiro',
                                                           city='uberlandia',
                                                           category='videogames').count() > 0

        if is_already_there:
            continue

        logging.info(f'Adding keyword {target.keyword}')

        session.add(target)
        session.commit()
