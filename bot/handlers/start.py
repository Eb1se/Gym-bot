from aiogram import Router, types
from aiogram.filters import Command
from sqlalchemy import select

from shared.database.base import get_db
from shared.database.models import User

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обработчик команды /start
    Регистрируем пользователя если он еще не находится в БД
    TODO:
    Сейчас есть баг:
    Ошибка при регистрации: 'User' object has no attribute 'utc_now'
    """

    tg_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name

    async for session in get_db():
        try:
            result = await session.execute(
                select(User).where(User.telegram_id == tg_id)
            )
            user = result.scalar_one_or_none()

            if user is None:
                user = User(
                    telegram_id=tg_id,
                    username=username,
                    first_name=first_name
                )
                session.add(user)

                await session.commit()

                await message.answer(
                    f"👋 Привет, {first_name or "друг"}!\n\n"
                    f"✅ Ты успешно зарегестрирован в боте!\n\n"
                    f"📝 Что умеет этот бот:\n"
                    f"🏋️ Записывать тренировки\n"
                    f"📊 Отслеживать статистику по тренировкам, и не только\n"
                    f"📏 Фиксировать замеры\n"
                    f"Используй /help чтобы узнать все команды!"
                )
            else:
                user.last_activity = user.utc_now()
                user.username = username
                user.first_name = first_name
                await session.commit()

                await message.answer(
                    f"👋 С возвращением, {user.first_name or "друг"}!\n\n"
                    f"Используй /help чтобы увидеть все команды"
                )

        except Exception as e:
            print(f"Ошибка при регистрации: {e}")
            await message.answer(
                "❌ Произошла ошибка при регистрации.\n"
                "Попробуй позже, или сообщи администратору!"
            )
