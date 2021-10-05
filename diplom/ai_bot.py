import logging
from aiogram import Bot, Dispatcher, executor, types, filters
from decouple import config
from command import command, callback, startpars
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

# START #
@dp.message_handler(filters.CommandStart())
async def command_start_handler(msg: types.message):
    #await msg.answer(f'Привет, чего хотел?')
    await startpars(dp, msg)

# HELP #
@dp.message_handler(filters.CommandHelp())
async def command_start_handler(msg: types.message):
    await msg.answer(f'Привет, чем помочь?')

# PRIVET #
@dp.message_handler(filters.Text(startswith=['hi', 'he'], ignore_case=True))
async def text_contains_all_handler(message: types.message):
    await message.answer("Хеллоу!")

@dp.message_handler(filters.Text(contains='прив', ignore_case=True))
@dp.message_handler(filters.Text(contains='здрав', ignore_case=True))
@dp.message_handler(filters.Text(contains='здоро', ignore_case=True))
@dp.message_handler(filters.Text(contains='добр', ignore_case=True))
async def text_contains_all_handler(message: types.message):
    await message.answer("Привет!")

# Other message #
# фильтра здесь нет! хандлер ловит все что сюда дошло!
@dp.message_handler()
async def user_text(message: types.message):
    await command(dp, message)

# Buttonlink #
@dp.callback_query_handler(lambda c: c.data in ['1', '2', '3', '4'])
async def process_callback(query: types.callback_query):
    await callback(bot, query)


executor.start_polling(dp, skip_updates=True)