# QRKot Google Sheets
 
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

---
## Запуск проекта
### Установка
~~~
git clone git@github.com:ThatCoderMan/cat_charity_fund.git
~~~
~~~
cd cat_charity_fund
~~~
~~~
python -m venv venv && source venv/bin/activate
~~~
~~~
pip install -r requirements.txt
~~~
~~~
touch .env
~~~
### Заполните .env файл

Пример .env файла:
~~~
APP_TITLE=Сервис для поддержки котиков!
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=HelloWorld
FIRST_SUPERUSER_EMAIL=admin@admin.com
FIRST_SUPERUSER_PASSWORD=admin
~~~

###Миграции базы данных
~~~
alembic revision --autogenerate 
alembic upgrade head
~~~
### Запуск программы
~~~
uvicorn app.main:app
~~~
---

Документация доступна после запуска программы по адресу /docs

---
## Автор
- [Artemii](https://github.com/ThatCoderMan)