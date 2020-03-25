# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
##
from scrapy.exceptions import DropItem
from sqlalchemy import func

from database import session, Product
from olxscraper.items import Product as OlxProduct


class OlxscraperPipeline(object):
    def process_item(self, item: OlxProduct, spider):
        product = Product(
            title=item.get('title'),
            olx_id=item.get('id'),
            keyword=item.get('keyword'),
            description=item.get('description'),
            price=item.get('price'),
            city=item.get('city'),
            zip=item.get('zip'),
            region=item.get('region'),
            image=item.get('image'),
            url=item.get('url'),
            date_time=item.get('date_time'),
            is_new=not item.get('is_new')
        )

        is_already_registered = session\
            .query(func.count(Product.id))\
            .filter(Product.olx_id == product.olx_id)\
            .scalar() != 0

        if is_already_registered:
            print("Skipping product, already inserted")
            raise DropItem()

        session.add(product)
        session.commit()

        return item
