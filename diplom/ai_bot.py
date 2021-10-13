import logging
import os
from aiogram import Bot, Dispatcher, executor, filters, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config
from aiogram.utils.executor import start_webhook
from command import callback, cansel, command, help, startpars
from register import set_commands

WEBHOOK_HOST = 'https://depbot1.herokuapp.com'  # name your app
WEBHOOK_PATH = '/webhook/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.environ.get('PORT')
#TOKEN = os.environ['TOKEN']

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


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    # insert code here to run it before shutdown
    pass

if __name__ == '__main__':
    start_webhook(dispatcher=dp, webhook_path=WEBHOOK_PATH,
                  on_startup=on_startup, on_shutdown=on_shutdown,
                  host=WEBAPP_HOST, port=WEBAPP_PORT)



#executor.start_polling(dp, skip_updates=True)
