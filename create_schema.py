from database import Product, engine, Target
from database.session import session


def recreate_schema():
    Product.__table__.drop(engine, checkfirst=True)
    Product.__table__.create(engine, checkfirst=True)
    Target.__table__.drop(engine, checkfirst=True)
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

        session.add(target)
        session.commit()


if __name__ == '__main__':
    recreate_schema()
