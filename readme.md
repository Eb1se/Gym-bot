# 🏋️ Gym Bot — Фитнес-трекер в Telegram

Telegram бот для отслеживания тренировок, питания, замеров и прогресса с собственным REST API.

## 🏗️ Архитектура

```
┌─────────────────┐     ┌─────────────────┐
│  Telegram Bot   │     │  FastAPI        │
│  (aiogram)      │────▶│  (REST API)     │
└────────┬────────┘     └────────┬────────┘
         │                       │
         ▼                       ▼
    ┌─────────────────────────────────┐
    │      База данных (SQLite)       │
    │      SQLAlchemy ORM             │
    └─────────────────────────────────┘
```

## 📦 Стек технологий

| Компонент | Технология |
|-----------|------------|
| Telegram Bot | aiogram 3.x |
| API | FastAPI |
| ORM | SQLAlchemy 2.0 |
| База данных | SQLite |
| HTTP-клиент | httpx |
| Тесты | pytest, pytest-asyncio |

## 🚀 Запуск проекта

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Eb1se/gym-bot.git
cd gym-bot
```

### 2. Создать и активировать виртуальное окружение

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

### 3. Установить зависимости

```bash
pip install -r requirements-dev.txt #зависимости для разработки
```

### 4. Настроить переменные окружения

Создай файл `.env` в корне:

```env
BOT_TOKEN=твой_токен_от_BotFather
DATABASE_URL=sqlite+aiosqlite:///./gym_bot.db
```

### 5. Запустить API и бота

**Терминал 1 — API:**

```bash
python main_api.py
```

**Терминал 2 — Бот:**

```bash
python main.py
```

### 6. Документация API

Открой в браузере: http://localhost:8000/docs

## 📁 Структура проекта

```
app/
├── api/                 # FastAPI
│   ├── routes/          # Эндпоинты
│   ├── schemas/         # Pydantic модели
│   └── dependencies.py  # Зависимости
├── bot/                 # Telegram бот
│   ├── core/            # Конфиг
│   ├── database/        # SQLAlchemy модели
│   ├── handlers/        # Хендлеры aiogram
│   └── messages/        # Тексты сообщений
├── services/            # Бизнес-логика
└── clients/             # HTTP-клиенты
```

## 🧪 Тестирование

```bash
pytest tests/ -v
```

## 📝 Доступные команды

| Команда | Описание |
|---------|----------|
| `/start` | Регистрация и приветствие |
| `/help` | Список команд |

## 🎯 Планы

- [x] Регистрация пользователя
- [x] FastAPI + SQLAlchemy
- [ ] Запись тренировок, и прочих данных
- [ ] Статистика
- [ ] PostgreSQL
- [ ] Docker

## 👤 Автор

[Eb1se](https://github.com/Eb1se)

## Телеграм канал где я рассказываю о разработке
[Дневник разработчика](https://t.me/Eb1seDev)