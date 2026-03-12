from aiogram import Dispatcher
from bot.handlers import register_routers

def setup_dispatcher() -> Dispatcher:
    dp = Dispatcher()

    register_routers(dp)

    return dp

dp = setup_dispatcher()