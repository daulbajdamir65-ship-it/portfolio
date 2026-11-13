# Портфолио Дамира — Flask

Готовый адаптивный сайт-портфолио на Python Flask.

## 1. Что понадобится
- Python 3.10 или новее
- Интернет для загрузки Flask при первой установке и для подключения Google Fonts (сайт также работает без шрифта из Google Fonts)

## 2. Запуск на Windows

Откройте папку проекта в терминале и выполните:

```bash
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
py app.py
```

## 3. Запуск на macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```

После запуска откройте в браузере:

http://127.0.0.1:5000

Остановить сервер: `Ctrl + C`.

## 4. Где менять информацию

Основные данные находятся в словаре `PROFILE` в файле `app.py`.
Тексты и разметка сайта находятся в `templates/index.html`.
Оформление — `static/css/style.css`, небольшое поведение меню — `static/js/main.js`.

## 5. Перед публикацией в интернете

Сейчас приложение запускается в режиме разработки (`debug=True`) для локальной работы.
Для публичного размещения выключите debug и используйте production-сервер, например Waitress или Gunicorn.
