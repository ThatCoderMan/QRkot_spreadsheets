# QRKot Google Sheets
 
![workflows](https://github.com/ThatCoderMan/QRkot_spreadsheets/actions/workflows/deploy.yml/badge.svg)

<details>
<summary>Project stack</summary>

- Python 3.9
- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- Aiogoogle
- GitHub Actions

</details>


Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Запуск проекта
### Установка
Клонируйте репозиторий:
~~~commandline
git clone git@github.com:ThatCoderMan/cat_charity_fund.git
~~~
Перейдите в папку cat_charity_fund/:
~~~commandline
cd cat_charity_fund
~~~
Активируйте виртуальное окружение:
- для MacOS:
    ~~~commandline
    python -m venv venv && source venv/bin/activate
    ~~~
- для Windows:
    ~~~commandline
    pip install -r requirements.txt
    ~~~
создайте `.env` файд
~~~commandline
touch .env
~~~
Заполните .env файл
~~~dotenv
APP_TITLE=Сервис для поддержки котиков!
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=YOURSECRET
FIRST_SUPERUSER_EMAIL=admin@admin.com
FIRST_SUPERUSER_PASSWORD=admin
~~~
Миграции базы данных:
~~~commandline
alembic revision --autogenerate 
alembic upgrade head
~~~
### Запуск программы
~~~commandline
uvicorn app.main:app
~~~
---

Документация доступна после запуска программы по адресу `/docs`

---
## Автор проекта
- [Artemii Berezin](https://github.com/ThatCoderMan)