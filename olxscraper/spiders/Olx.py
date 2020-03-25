# -*- coding: utf-8 -*-

import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.http import Request, HtmlResponse

from database import Target, Product
from olxscraper.items import Product as OlxProduct
from olxscraper.loaders import ProductLoader


def _check_pending_products():
    query = Product.get_new().count()
    if query != 0:
        raise CloseSpider(reason="Pending products found, aborting")


class OlxSpider(scrapy.Spider):
    name = 'Olx'
    allowed_domains = ['olx.com.br']
    requests = 0

    _check_pending_products()

    def start_requests(self):

        for target in Target.all():
            self.requests = self.requests + 1
            yield Request(
                f'https://{target.state}.olx.com.br/{target.state_region}/{target.region_subregion}/{target.city}/{target.category}?q={target.keyword}&sf=1',
                meta={
                    'keyword': target.keyword,
                    'state': target.state,
                    'state_region': target.state_region,
                    'region_subregion': target.region_subregion,
                    'city': target.city,
                    'category': target.category,
                    'is_new': target.is_new
                })

    def parse_item(self, response: HtmlResponse):

        loader = ProductLoader(item=OlxProduct(), response=response)

        olx_ad_id: str = response.css('link[rel="alternate"]::attr(href)') \
            .get() \
            .replace("olxapp://adpage/?id=", "")

        assert olx_ad_id != ''
        assert olx_ad_id is not None

        loader.add_value('id', olx_ad_id)
        loader.add_css('title', 'h1[tag="h1"]::text')
        # this seems unsafe:
        loader.add_css('description', 'span[tag="span"][color="dark"][weight=""][font-weight="400"]::text')
        loader.add_css('price', 'h2[tag="h2"]::text')
        loader.add_xpath('zip', '//dt[contains(.//text(), "CEP")]/../dd/text()')
        loader.add_xpath('city', '//dt[contains(.//text(), "Município")]/../dd/text()')
        loader.add_xpath('region', '//dt[contains(.//text(), "Bairro")]/../dd/text()')
        loader.add_css('image', 'img.image::attr(src)')
        loader.add_value('url', response.request.url)
        loader.add_value('keyword', response.meta['keyword'])
        loader.add_value('is_new', response.meta['is_new'])

        date_time: str = response.css('span[color="grayscale.darker"][tag="span"]') \
            .xpath('.//node()') \
            .re_first(r'.*às.*')

        loader.add_value('date_time', date_time)

        yield loader.load_item()

    def parse(self, response: HtmlResponse):

        items = response.css('#main-ad-list').css('.item:not(.list_native):not(.yap-loaded)')

        new_item_count = 0

        for item in items:
            attrib = item.attrib
            id = attrib['data-list_id']

            product = Product.get_by_olx_id(int(id))

            if product is not None:
                continue

            new_item_count = new_item_count + 1

            url: str = item.css('.OLXad-list-link::attr(href)').get()
            if url is None:
                url = item.css('.OLXad-list-link-featured::attr(href)').get()

            yield response.follow(url, callback=self.parse_item, meta=response.meta.copy())

        if new_item_count > 0:
            for next_link in response.css('a.link[rel="next"]'):
                yield response.follow(next_link, callback=self.parse, meta=response.meta)
