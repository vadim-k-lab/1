import logging
from aiogram import Bot, Dispatcher, executor, types, filters
from decouple import config
from command import command, callback, startpars, help, cansel
from register import set_commands
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())

#set_commands(dp.bot) # регистрация команд не работает!

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

# START #
@dp.message_handler(filters.CommandStart())
async def command_start_handler(msg: types.message):
    await startpars(dp, msg)

# HELP #
@dp.message_handler(filters.CommandHelp())
async def bot_help(msg: types.message):
    await help(msg)

# CANSEL #
@dp.message_handler(state='*', commands=['cancel'])
async def comand_cansel(msg: types.message, state):
    await cansel(msg, state)

# Other message #
@dp.message_handler()
async def user_text(message: types.message):
    await command(dp, message)

# Buttonlink #
@dp.callback_query_handler(lambda c: c.data in ['1', '2', '3', '4'])
async def process_callback(query: types.callback_query):
    await callback(bot, query)


executor.start_polling(dp, skip_updates=True)