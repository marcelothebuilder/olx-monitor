# Welcome to Olx-monitor 👋
[![License: GPL--3.0](https://img.shields.io/badge/License-GPL--3.0-yellow.svg)](https://www.gnu.org/licenses/gpl-3.0.pt-br.html)
[![Twitter: marcelopaixaor](https://img.shields.io/twitter/follow/marcelopaixaor.svg?style=social)](https://twitter.com/marcelopaixaor)

> scrapes Olx website, watching for user-defined keywords and notifies the user via Telegram

## Install

Please read first [Creating a Telegram bot with BotFather - telegram.org](https://core.telegram.org/bots#6-botfather)
and
[Telegram Bot - how to get a group chat id? - Stackoverflow](https://stackoverflow.com/a/32572159/11128168)


Create a .env file with the following options:

```
TELEGRAM_BOT_TOKEN="<bot token:string>"
TELEGRAM_BOT_CHAT_ID=<chat id:int>
```

Then:

```sh
pipenv shell
pipenv install
```

## Usage

```sh
pipenv run python create_schema.py # (only once)
pipenv run python runner.py
```

## Schedule

Run:
```
crontab -e
```

Add to the end of the file:
```
*/15 * * * * cd <project directory> && /usr/bin/pipenv run python <project directory>/runner.py
```

`*/15 * * * *` equals every 15 minutes. Check [Crontab Guru](https://crontab.guru/) for a nice crontab editing experiencie.

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