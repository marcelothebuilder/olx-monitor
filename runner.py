from dotenv import load_dotenv
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from olxscraper.logging import configure_logging
from olxscraper.spiders.Olx import OlxSpider

configure_logging()

load_dotenv(verbose=False)

process = CrawlerProcess(settings=get_project_settings())
process.crawl(OlxSpider)
process.start()
