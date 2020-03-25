from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from olxscraper.configuration import load_configuration
from olxscraper.logging import configure_logging
from olxscraper.spiders.Olx import OlxSpider

load_configuration()
configure_logging()

process = CrawlerProcess(settings=get_project_settings())
process.crawl(OlxSpider)
process.start()
