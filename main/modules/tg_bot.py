from aiogram import Dispatcher, Bot, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from datetime import datetime
import asyncio

MESSAGE = '<i>[' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ''']</i>
<b>Name: {0}</b>
<b>Contacts: {1}</b>

{2}
'''

class SingletonBot:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SingletonBot, cls).__new__(cls)
        return cls.__instance

    def __init__(self, token):
        self._bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self._dp = Dispatcher(storage=MemoryStorage())

        @self._dp.message(Command("start"))
        async def start(message: types.Message):
            await message.reply(
                f'Hello! I will send you notifications from the site.\nYour ID: {message.from_user.id}'
            )

    async def sendMessage(self, chatId, text):
        await self._bot.send_message(chatId, text, parse_mode=ParseMode.HTML)

    async def start(self):
        await self._dp.start_polling(self._bot)