from database import Product, session
from notification.telegram_bot import send_notification


def send_notifications():
    new_products = Product.get_new()

    for product in new_products:
        p: Product = product
        send_notification(p.image, p.title, p.description, p.price, p.city, p.region, p.url)
        p.is_new = False
        session.commit()

if __name__ == '__main__':
    send_notifications()
