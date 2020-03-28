# Welcome to Olx-monitor 👋
[![License: GPL--3.0](https://img.shields.io/badge/License-GPL--3.0-yellow.svg)](https://www.gnu.org/licenses/gpl-3.0.pt-br.html)
[![Twitter: marcelopaixaor](https://img.shields.io/twitter/follow/marcelopaixaor.svg?style=social)](https://twitter.com/marcelopaixaor)

> scrapes Olx website, watching for user-defined keywords and notifies the user via Telegram

## Install

Please read first [Creating a Telegram bot with BotFather - telegram.org](https://core.telegram.org/bots#6-botfather)
and
[Telegram Bot - how to get a group chat id? - Stackoverflow](https://stackoverflow.com/a/32572159/11128168)


Create a .env file with the following options:

```dotenv
TELEGRAM_BOT_TOKEN="<bot token:string>"
TELEGRAM_BOT_CHAT_ID=<chat id:int>
```

Then:

```shell script
pipenv shell
pipenv install
```

## Initial data

This app needs keywords to be registered in order to know what to look for.

You can save a file in the format below at `<current working directory>/keywords-to-import.json` or `<home>/.olx-monitor/keywords-to-import.json`:

```json
[
	{
	    "keywords": [ "<any keyword>" ],
	    "state": "<olx brazilian state id>",
	    "state_region": "<olx brazilian state region>",
	    "region_subregion": "<olx brazilian subregion>",
	    "city": "<olx brazilian city",
	    "category": "<olx category>"
	}
]
```

This is a working example:

```json
[
	{
	    "keywords": [ "switch", "psp", "metal gear" ],
	    "state": "mg",
	    "state_region": "regiao-de-uberlandia-e-uberaba",
	    "region_subregion": "triangulo-mineiro",
	    "city": "uberlandia",
	    "category": "videogames"
	}
]
```

## Usage

```shell script
pipenv run python runner.py
```

## Schedule

### Using the app continuous run mechanism

Start the app with:
```shell script
pipenv run python runner.py --scheduled
```

The config key `DELAY_BETWEEN_CRAWLS` can be set in seconds to tune the delay between crawl runs. Set it in the config
file or pass through environment variables.


### Using crontab

Run:
```shell script
crontab -e
```

Add to the end of the file:
```text
*/15 * * * * cd <project directory> && /usr/bin/pipenv run python <project directory>/runner.py
```

`*/15 * * * *` equals every 15 minutes. Check [Crontab Guru](https://crontab.guru/) for a nice crontab editing experience.

## Author

👤 **Marcelo Paixão Resende**

* Website: https://br.linkedin.com/in/marcelopaixaoresende
* Twitter: [@marcelopaixaor](https://twitter.com/marcelopaixaor)
* Github: [@marcelothebuilder](https://github.com/marcelothebuilder)
* LinkedIn: [@marcelopaixaoresende](https://linkedin.com/in/marcelopaixaoresende)

## Show your support

Give a ⭐️ if this project helped you!


## 📝License

Copyright © 2020 [Marcelo Paixão Resende](https://github.com/marcelothebuilder).

This project is [GPL--3.0](https://www.gnu.org/licenses/gpl-3.0.pt-br.html) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_