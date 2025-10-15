# test_blog_api

REST API для блога на Python (Django + DRF)  
Проект реализует базовый функционал: создание, чтение, обновление и удаление записей (CRUD), а также простую аутентификацию/авторизацию.
Приложение Flask выполняет запрос на получение всех постов блога и заполняет ими базу данных.
---

## 📂 Структура проекта

├── simple_blog/ # приложение на Django + Django Rest Framework

├── flask_prj/ # приложение на Flask для проверки API

├── requirements.txt # зависимости проекта

└── README.md


---

## Запуск проекта

### Предварительные шаги

1. Клонировать репозиторий:  
   ```bash
   git clone https://github.com/MaminAmetist/test_blog_api.git
   cd test_blog_api

2. Создать виртуальное окружение и активировать его:
    ```bash
    python3 -m venv venv
    source venv/bin/activate ```     # для Linux / macOS
    # либо
    venv\Scripts\activate         # для Windows


3. Установить зависимости:
    ```bash
    pip install -r requirements.txt

4. Запуск Django / DRF версии
   Перейти в папку simple_blog:

       ```bash
       cd simple_blog

   Применить миграции:

        ```bash
        python manage.py migrate

   Запустить сервер:

    ```bash
    python manage.py runserver


API будет доступен по адресу http://localhost:8000/

Текущая версия доступна по адресу https://test-blog-api-m71h.onrender.com

5. Запуск Flask версии

    Перейти в папку flask_prj:

        ```bash
        cd flask_prj

    Запустить приложение:

        ```bash
        flask run

API будет доступен по адресу http://localhost:5000/

Текущая версия доступна по адресу https://test-blog-api-flask.onrender.com

✅ Требования / зависимости

Python 3.10

Django, djangorestframework (для версии simple_blog)

Flask и сопутствующие библиотеки (для версии flask_prj)

Другие зависимости перечислены в requirements.txt
