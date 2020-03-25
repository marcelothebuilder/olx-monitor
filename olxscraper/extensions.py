import logging

from scrapy import signals, Spider
from scrapy.exceptions import CloseSpider

from database import Target
from notification.task import send_notifications
from olxscraper.spiders import Olx

logger = logging.getLogger(__name__)


class Test(object):
    @classmethod
    def from_crawler(cls, crawler):
        # instantiate the extension object
        ext = cls()

        # connect the extension object to signals
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)

        # return the extension object
        return ext

    def spider_closed(self, spider: Olx):
        logger.info("closed spider %s", spider.name)
        # mark first executions as done!
        if spider.requests:
            Target.mark_all_as_not_new()
            send_notifications()
