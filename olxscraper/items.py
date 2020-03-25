# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Product(scrapy.Item):
    keyword = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    city = scrapy.Field()
    zip = scrapy.Field()
    region = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()
    date_time = scrapy.Field()
    is_new = scrapy.Field()
