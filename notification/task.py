from database import Product, session
from notification.telegram_bot import TelegramBot

import app_logging


def send_notifications():
    new_products = Product.get_new()
    telegram = TelegramBot()

    for product in new_products:
        p: Product = product
        try:
            telegram.send_notification(p.image, p.title, p.description, p.price, p.city, p.region, p.url)
            p.is_new = False
            session.commit()
        except:
            app_logging.exception(f"Error while notifying user about product {p.olx_id} - {p.title}")


if __name__ == '__main__':
    send_notifications()
