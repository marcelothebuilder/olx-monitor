from twisted.internet.defer import Deferred

from app_logging.logging import configure_app_logging
from database.setup import run_database_setup
from olxscraper.configuration import load_configuration, get_path_to_configuration_file
from paths.configuration_folder import ConfigurationFolder

ConfigurationFolder.create_if_absent()
load_configuration()
configure_app_logging()
run_database_setup()

from olxscraper.spiders.Olx import OlxSpider

import logging

from scrapy.utils.project import get_project_settings

from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor

import signal
import os

runner = CrawlerRunner(settings=get_project_settings())
logger = logging.getLogger(__name__)


def check_mandatory_configuration():
    mandatory_keys = ['TELEGRAM_BOT_TOKEN', 'TELEGRAM_BOT_CHAT_ID']
    missing_keys = list(filter(lambda mandatory_key: os.getenv(mandatory_key) is None, mandatory_keys))

    if len(missing_keys) > 0:
        configuration_file = get_path_to_configuration_file()

        logger.error(f'Required config keys {str(missing_keys)} not set.')
        logger.error(f'You can set these keys through:')
        logger.error(f'* {configuration_file} file')
        logger.error(f'* .env file in the current folder')
        logger.error(f'* Through enviroment variables')

        exit(1)


check_mandatory_configuration()


def handle_sigint(signalnum, handler):
    runner.stop().addBoth(lambda x: reactor.stop())


def schedule_next(seconds_from_now: float):
    logger.info(f'Scheduling next job for {seconds_from_now} seconds from now')
    reactor.callLater(seconds_from_now, lambda: crawl())


def schedule_next_with_user_configuration():
    sec = float(os.getenv('DELAY_BETWEEN_CRAWLS', 15 * 60))
    schedule_next(sec)


def crawl():
    logger.info("Starting job")

    runner.crawl(OlxSpider)

    d: Deferred = runner.join()

    d.addErrback(lambda _: logger.error('Crawling errored'))
    d.addCallback(lambda _: logger.info('Crawling finished without errors'))
    d.addCallback(lambda _: schedule_next_with_user_configuration())

    return d


def run_in_scheduled_mode():
    logger.info('Running in scheduled mode')
    signal.signal(signal.SIGINT, handle_sigint)
    crawl()
    reactor.run()


def run_in_single_run_mode():
    logger.info('Running in single run mode')
    runner.crawl(OlxSpider)
    d: Deferred = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


if __name__ == '__main__':

    import sys

    if '--scheduled' in sys.argv[1:]:
        run_in_scheduled_mode()
    else:
        run_in_single_run_mode()
