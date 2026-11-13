from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "name": "Даулбай Дамир Нуриденулы",
    "city": "Алматы, Казахстан",
    "college": "Алматинский Инновационно-Технический колледж",
    "specialty": "Техник информационных систем",
    "course": "4 курс",
    "telegram": "https://t.me/bellkaTrader",
    "telegram_handle": "@bellkaTrader",
    "github": "https://github.com/softwareOrex",
    "interests": [
        {
            "number": "01",
            "title": "Python-разработка",
            "description": "Изучаю Python и применяю его для создания полезных программ и автоматизации задач.",
            "icon": "⌘",
        },
        {
            "number": "02",
            "title": "Telegram-боты",
            "description": "Интересуюсь разработкой ботов и сервисов, которые упрощают повседневные процессы.",
            "icon": "✳",
        },
        {
            "number": "03",
            "title": "Предпринимательство",
            "description": "Изучаю бизнес-мышление, идеи проектов и способы превращать задумки в продукты.",
            "icon": "↗",
        },
        {
            "number": "04",
            "title": "Искусственный интеллект",
            "description": "Следую за развитием ИИ и изучаю, как использовать новые технологии на практике.",
            "icon": "◎",
        },
    ],
}

@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE)

if __name__ == "__main__":
    app.run(debug=True)
