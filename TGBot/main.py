import os
import time
import aiogram
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


class TGBot:
    def __init__(self, core):
        self.core = core
        storage = MemoryStorage()
        try:
            self.bot = aiogram.Bot(self.core.config["telegramBotToken"])
            self.dp = aiogram.Dispatcher(self.bot, storage = storage)
            self.rulesApply()
        except Exception as e:
            exit(f"[!] Can not start TGBot: {e}")

    def rulesApply(self):
        @self.dp.message_handler(content_types=[types.ContentType.VOICE])
        async def userInputHandler(message: types.Message):
            voice = await message.voice.get_file()
            fileName = voice.file_id
            await self.bot.download_file(file_path=voice.file_path, destination=f"{fileName}.ogg")
            answer = self.core.recognizer.recognize(f"{fileName}.ogg")
            if answer:
                self.core.modulesParser.handleModule(answer)
                await message.answer(f"[*] Распознано: {answer}")


    def run(self):
        try:
            aiogram.executor.start_polling(self.dp, skip_updates=True)
        except Exception as e:
            exit(f"[!] Can not start TGBot: {e}")