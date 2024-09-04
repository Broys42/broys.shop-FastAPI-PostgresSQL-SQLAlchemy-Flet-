# broys.shop

# Магазин наушников (FastAPI, FastAPIUsers, PostgreSQL, SQLAlchemy, Flet, Flet-FastAPI)

## О проекте
- Данные передаются через ORM-запросы к базе данных PostgreSQL
- ORM-запросы реализованы через SQLAlchemy
- Атомарный дизайн реализованный на Flet
- Добавлены роутеры на регистрацию, логин и выход (FastAPIUsers)
- Добавлены роутеры на проверку авторизации (Через статус внутри FastAPIusers current_user())
- Добавлены роутеры для работы с моделью данных наушников

## Что на данный момент в разработке
- Добавление информации на страницу наушников через их id (сейчас в карточках наушников их id)
- Добавление наушников в корзину пользователя с заданными количеством
- Переход на страницу оплаты
- Docker-compose файл

## В планах
- На этом проекте в сентябре я хочу разобраться с процессом деплоя, чтобы приложение работало на домене broys.shop

## Скриншоты
[![Screenshot-1.jpg](https://i.postimg.cc/mkmkSg4B/Screenshot-1.jpg)](https://postimg.cc/dZTJsvDx)
[![Screenshot-2.jpg](https://i.postimg.cc/KzFYSMvm/Screenshot-2.jpg)](https://postimg.cc/Z97m60dQ)
[![Screenshot-3.jpg](https://i.postimg.cc/kGgXDPbZ/Screenshot-3.jpg)](https://postimg.cc/hzNq3wMb)
[![Screenshot-4.jpg](https://i.postimg.cc/X7XYb33B/Screenshot-4.jpg)](https://postimg.cc/Mv2S7Cnz)
[![Screenshot-5.jpg](https://i.postimg.cc/9fPWpQPK/Screenshot-5.jpg)](https://postimg.cc/PLxsfhRQ)
