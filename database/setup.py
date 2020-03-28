from database import Product, Target, engine, session
import logging
import json

from paths.configuration_folder import ConfigurationFolder
from paths.current_folder import CurrentFolder

logging = logging.getLogger(__name__)


def run_keywords_import(import_file, import_file_ok):
    if not import_file.exists():
        return

    import_file_already_imported = import_file_ok.exists()

    if import_file_already_imported:
        return

    with open(str(import_file)) as import_file_fp:
        json_data = json.load(import_file_fp)
        targets = []
        for entry in json_data:
            for keyword in entry['keywords']:
                target = Target(keyword=keyword,
                                state=entry['state'],
                                state_region=entry['state_region'],
                                region_subregion=entry['region_subregion'],
                                city=entry['city'],
                                category=entry['category'],
                                is_new=True)
                targets.append(target)

        try:
            session.add_all(targets)
            session.commit()
            import_file_ok.touch()
        except:
            logging.exception(f'Failure to import {str(import_file)}')


def run_database_setup():
    Product.__table__.create(engine, checkfirst=True)
    Target.__table__.create(engine, checkfirst=True)

    run_keywords_import(ConfigurationFolder.joinpath('keywords-to-import.json'),
                        ConfigurationFolder.joinpath('keywords-to-import.json.imported'))

    run_keywords_import(CurrentFolder.joinpath('keywords-to-import.json'),
                        CurrentFolder.joinpath('keywords-to-import.json.imported'))

