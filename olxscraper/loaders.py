import re
from typing import List

from datetime import datetime
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Compose


def _fix_strings(stringsx: List[str]):
    for stringx in stringsx:
        yield _fix_string(stringx)


def _fix_string(string: str):
    if string is None:
        return string

    if not isinstance(string, str):
        return string

    without_tab = re.sub(r"\t+", "", string)
    return re.sub(r"\n+", "", without_tab)


def _filter_price(value):
    if not value:
        return None
    without_symbol = value.replace('R$ ', '')
    return float(without_symbol)


def _filter_date_time(value):
    values = value.split(' às ')
    date = values[0]
    time = values[1]

    if len(date.split('/')) == 2:
        current_year = datetime.now().year
        date = f'{date}/{current_year}'

    dt = datetime.strptime(f'{date} {time} -0300', '%d/%m/%Y %H:%M %z')
    return dt


class ProductLoader(ItemLoader):
    default_output_processor = TakeFirst()
    price_out = Compose(TakeFirst(), _filter_price)
    date_time_in = Compose(TakeFirst(), _filter_date_time)

