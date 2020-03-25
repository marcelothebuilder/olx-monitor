import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from dotenv import load_dotenv
from olxscraper.spiders.Olx import OlxSpider
import logging

logging.getLogger('scrapy_deltafetch.middleware').setLevel(logging.WARN)

# OR, the same with increased verbosity
load_dotenv(verbose=True)

process = CrawlerProcess(settings=get_project_settings())
process.crawl(OlxSpider)
process.start()
