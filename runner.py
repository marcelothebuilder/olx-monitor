from scrapy.utils.log import configure_logging
from twisted.internet.defer import Deferred

from olxscraper.configuration import load_configuration

load_configuration()
configure_logging()

from olxscraper.spiders.Olx import OlxSpider

import logging

from scrapy.utils.project import get_project_settings

from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor

import signal
import os

runner = CrawlerRunner(settings=get_project_settings())

import sys

scheduled = '--scheduled' in sys.argv[1:]

logging = logging.getLogger(__name__)


def handle_sigint(signalnum, handler):
    runner.stop().addBoth(lambda x: reactor.stop())


def schedule_next(seconds_from_now: float):
    logging.info(f'Scheduling next job for {seconds_from_now} seconds from now')
    reactor.callLater(seconds_from_now, lambda: crawl())


def schedule_next_with_user_configuration():
    sec = float(os.getenv('DELAY_BETWEEN_CRAWLS', 60))
    schedule_next(sec)


def crawl():
    logging.getLogger(__name__).info("Starting job")

    runner.crawl(OlxSpider)

    d: Deferred = runner.join()

    d.addErrback(lambda _: logging.error('Crawling errored'))
    d.addCallback(lambda _: logging.info('Crawling finished without errors'))
    d.addCallback(lambda _: schedule_next_with_user_configuration())

    return d


def run_in_scheduled_mode():
    logging.info('Running in scheduled mode')
    signal.signal(signal.SIGINT, handle_sigint)
    schedule_next_with_user_configuration()
    reactor.run()


def run_in_single_run_mode():
    logging.info('Running in single run mode')
    runner.crawl(OlxSpider)
    d: Deferred = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


if __name__ == '__main__':
    if scheduled:
        run_in_scheduled_mode()
    else:
        run_in_single_run_mode()
