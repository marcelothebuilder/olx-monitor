import os

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_BOT_CHAT_ID')

from telegram.ext import Updater

PLACEHOLDER_IMG = 'https://via.placeholder.com/640x380'

MAX_DESCRIPTION_SIZE = 500

updater = Updater(token=TOKEN, use_context=True)


def send_notification(photo_url, title, description, price, city, region, url):
    photo_url = photo_url or PLACEHOLDER_IMG

    #truncate
    description = description[:MAX_DESCRIPTION_SIZE] + '...' if len(description) > MAX_DESCRIPTION_SIZE else description

    markdown_message = f"""
<strong>{title}</strong> - R$ {price}

{city} - {region}

{description}

<a href="{url}">{url}</a>
    """
    updater.bot.send_photo(chat_id=CHAT_ID, photo=photo_url, parse_mode='HTML', caption=markdown_message)
