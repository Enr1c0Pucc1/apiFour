# Отправка фотографий в Телеграм
Простой скрипт на Python для отправки фотографий из папки "images" в чаты Телеграм.

## Описание

Этот проект представляет собой скрипт, который автоматически отправляет фотографии из заданной папки "images" в чаты Телеграм.


## Требования

- Python 3.6 или выше
- Учетная запись бота в Телеграм (получите токен бота через @BotFather)

## Установка

1. Клонируйте репозиторий: `git clone https://github.com/Enr1c0Pucc1/apiFour`
2. Перейдите в директорию проекта: `cd apiFour`
3. Зависимости должны установиться автоматически.


## Конфигурация

1. Получите токен бота от @BotFather в Телеграм.
2. В файле `.env` вставьте полученный токен в переменную `TELEGRAM_TOKEN`.

## Использование

1. Поместите фотографии, которые вы хотите отправить, в папку "images".
2. Запустите скрипт: `python telegram_bot.py`. По умолчанию задержка стоит 4 часа, поменять задержку можно через аргумент `--t`.
3. Скрипт автоматически отправит все фотографии из папки "images" в выбранные чаты Телеграм.